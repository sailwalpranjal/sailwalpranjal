"""Design system + generator for every profile visual. Editorial, one accent colour, outlined type, real-data art.
Run: python3 scripts/design.py      (reads ledger.json and data/adsets.csv)"""
import csv, json, math, os, pathlib, hashlib
import typo
from typo import path as P, width as W_

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"; OUT.mkdir(exist_ok=True)
L = json.loads((ROOT / "ledger.json").read_text(encoding="utf-8"))

TH = {
    "dark": dict(bg="#0b0b0c", panel="#111113", ink="#f1eee6", mute="#8c897f", dim="#4a4944", rule="#242427", acc="#ff5b2e"),
    "light": dict(bg="#f3f0e8", panel="#ebe7dc", ink="#111110", mute="#6c695f", dim="#b3afa3", rule="#d6d2c5", acc="#e0400d"),
}
import datetime
PALETTES = [("vermilion", "#ff5b2e", "#e0400d"), ("cobalt", "#4f7cff", "#2a56e0"), ("acid", "#c6ff3d", "#6d9100"), ("emerald", "#1fd18a", "#0e8a58"),
            ("magenta", "#ff4fa3", "#d11d7c"), ("amber", "#ffb020", "#b36b00"), ("cyan", "#27d9f0", "#0b8aa0"), ("violet", "#9a7bff", "#6b45e0")]
WEEK = datetime.date.today().isocalendar()[1]
PNAME, _dk, _lt = PALETTES[WEEK % len(PALETTES)]
TH["dark"]["acc"], TH["light"]["acc"] = _dk, _lt   # the whole profile re-colours every Monday
ADS = [(int(r["xyz_campaign_id"]), float(r["Spent"]), int(r["Approved_Conversion"])) for r in csv.DictReader(open(ROOT / "data/adsets.csv", encoding="utf-8", newline=""))]


def svg(w, h, body, t, label, bg=True, radius=0):
    r = f'<rect width="{w}" height="{h}" rx="{radius}" fill="{t["bg"]}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{label}">'
            f'<title>{label}</title>{r}{body}</svg>')


def hl(x1, x2, y, t, c=None, sw=1): return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{c or t["rule"]}" stroke-width="{sw}"/>'
def label(x, y, s, t, c=None, size=11.5, anchor="start", ls=2.2, op=1): return P(s.upper(), x, y, "mono", size, c or t["mute"], ls, anchor, op)


# ------------------------------------------------------------ real-data dot field
def pack(cx, cy, items, gap=0.6):
    placed, grid, cell = [], {}, 12
    def ok(x, y, r):
        for gx in range(int((x - r) // cell) - 2, int((x + r) // cell) + 3):
            for gy in range(int((y - r) // cell) - 2, int((y + r) // cell) + 3):
                for (px, py, pr) in grid.get((gx, gy), []):
                    if (px - x) ** 2 + (py - y) ** 2 < (pr + r + gap) ** 2: return False
        return True
    for (r, tag) in sorted(items, key=lambda i: -i[0]):
        a, rad = 0.0, 0.0
        while True:
            x, y = cx + rad * math.cos(a), cy + rad * math.sin(a) * 0.92
            if ok(x, y, r): break
            a += 0.45; rad += 0.11
        placed.append((x, y, r, tag)); grid.setdefault((int(x // cell), int(y // cell)), []).append((x, y, r))
    return placed


def dotfield(t, centers, k, delay=0.0, animate=True, dim_all=False):
    """centers: {campaign: (cx, cy)}; dot area proportional to spend; filled = ad set produced >=1 approved conversion."""
    out = []
    for ci, (camp, (cx, cy)) in enumerate(centers.items()):
        items = [(max(0.9, k * math.sqrt(s)), a > 0) for c, s, a in ADS if c == camp]
        g = []
        for (x, y, r, filled) in pack(cx, cy, items):
            col = t["acc"] if camp == 1178 else (t["ink"] if camp == 936 else t["mute"])
            if dim_all: col = t["dim"] if camp != 1178 else t["acc"]
            if filled: g.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{col}"/>')
            else: g.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{max(r-0.5,0.5):.1f}" fill="none" stroke="{col}" stroke-width="1" stroke-opacity=".75"/>')
        anim = (f'<animate attributeName="opacity" from="0" to="1" begin="{delay+ci*0.35:.2f}s" dur="1.1s" fill="freeze"/>' if animate else "")
        out.append(f'<g opacity="{0 if animate else 1}">{anim}{"".join(g)}</g>')
    return "".join(out)


# ------------------------------------------------------------ hero
def hero(t):
    Wd, H = 1280, 580
    b = [label(64, 70, "Pranjal Sailwal", t, t["ink"], 12.5, ls=3.5), label(1216, 70, "Dehradun · remote-first · UTC+5:30", t, anchor="end"), hl(64, 1216, 92, t)]
    b.append(P("Messy data into", 64, 210, "display", 86, t["ink"], -2.4))
    b.append(P("decisions,", 64, 312, "serif", 112, t["acc"], -1))
    b.append(P("then shipped.", 64, 400, "display", 86, t["ink"], -2.4))
    for i, s in enumerate(["Product-minded engineer. Funnels, migrations and data platforms,", "built, tested and written down, including what they cannot do."]):
        b.append(P(s, 66, 452 + i * 26, "body", 17.5, t["mute"]))
    cols = L["hero_stats"]
    cw = (1216 - 64) / 4
    b.append(hl(64, 1216, 492, t))
    for i, (big, cap, tag) in enumerate(cols):
        x = 64 + i * cw
        if i: b.append(f'<line x1="{x-18}" y1="508" x2="{x-18}" y2="566" stroke="{t["rule"]}"/>')
        b.append(P(big, x, 548, "display", 40, t["ink"], -1.2))
        b.append(label(x + W_(big, "display", 40, -1.2) + 14, 534, tag, t, t["acc"], 10.5, ls=1.8))
        b.append(P(cap, x, 566 - 0, "body", 12.5, t["mute"]) if False else "")
    for i, (big, cap, tag) in enumerate(cols):
        x = 64 + i * cw
        b.append(P(cap, x, 574 - 0, "body", 12.5, t["mute"]))
    # dot field (real data)
    b.append(dotfield(t, {1178: (1030, 262), 936: (830, 168), 916: (820, 322)}, 0.21))
    b.append(label(1216, 404, "1,143 real ad sets · area = spend", t, anchor="end", size=10.5, ls=1.8))
    for i, (cc, txt, col) in enumerate([("1178", "$63.83 per approved conversion", t["acc"]), ("936", "$15.81", t["ink"]), ("916", "$6.24 · only 54 ad sets", t["mute"])]):
        y = 424 + i * 20
        b.append(f'<circle cx="760" cy="{y-4}" r="4" fill="{col}"/>')
        b.append(label(774, y, f"campaign {cc}", t, col, 10.5, ls=1.6)); b.append(label(1216, y, txt, t, col, 10.5, "end", 1.6))
    b.append(label(760, 484, "Filled = produced approved conversions · hollow = none", t, size=9.5, ls=1.4))
    return svg(Wd, H + 8, "".join(b), t, "Pranjal Sailwal: messy data into decisions, then shipped.", radius=0)


# ------------------------------------------------------------ banner / social
def banner(t):
    Wd, H = 1584, 396
    b = [dotfield(t, {1178: (1390, 205), 936: (1240, 95), 916: (1235, 310)}, 0.25, animate=False, dim_all=False)]
    b.append(f'<rect width="{Wd}" height="{H}" fill="{t["bg"]}" opacity=".0"/>')
    b.append(f'<rect x="0" y="0" width="1010" height="{H}" fill="{t["bg"]}"/>')
    b.append(f'<linearGradient id="fd" x1="0" x2="1"><stop offset="0" stop-color="{t["bg"]}"/><stop offset="1" stop-color="{t["bg"]}" stop-opacity="0"/></linearGradient><rect x="1010" y="0" width="160" height="{H}" fill="url(#fd)"/>')
    b.append(label(560, 96, "Product-minded engineer", t, t["acc"], 13, ls=4))
    b.append(P("Messy data into", 560, 176, "display", 60, t["ink"], -1.8))
    b.append(P("decisions,", 560, 250, "serif", 76, t["acc"], -.5))
    b.append(P("then shipped.", 560 + W_("decisions,", "serif", 76, -.5) + 22, 250, "display", 60, t["ink"], -1.8))
    b.append(hl(560, 1010, 288, t))
    b.append(label(560, 318, "Funnels · migrations · data platforms", t, t["mute"], 12, ls=2.6))
    b.append(label(560, 344, "Python · Go · SQL · TypeScript", t, t["mute"], 12, ls=2.6))
    return svg(Wd, H, "".join(b), t, "LinkedIn banner")


def social(t, name, line, metrics):
    Wd, H = 1280, 640
    seed = int(hashlib.sha256(name.encode()).hexdigest()[:8], 16)
    import random; rnd = random.Random(seed)
    items = [(rnd.uniform(2, 15), rnd.random() > 0.35) for _ in range(150)]
    dots = "".join((f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{t["acc"]}"/>' if f else f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r-.5:.1f}" fill="none" stroke="{t["mute"]}"/>') for x, y, r, f in pack(1020, 330, items))
    b = [dots, label(80, 96, "sailwalpranjal / repository", t, t["acc"], 13, ls=4), hl(80, 700, 120, t)]
    size = 92 if len(name) < 14 else 64 if len(name) < 26 else 50
    rows = typo.wrap(name.replace("-", "-​"), "display", size, 640, -2) if False else [name]
    b.append(P(name, 80, 250, "display", size, t["ink"], -2.2))
    for i, r in enumerate(typo.wrap(line, "body", 26, 600)[:3]): b.append(P(r, 82, 318 + i * 38, "body", 26, t["mute"]))
    b.append(hl(80, 700, 470, t))
    for i, (big, cap) in enumerate(metrics):
        x = 80 + i * 210
        b.append(P(big, x, 540, "display", 52, t["ink"], -1.5)); b.append(label(x, 570, cap, t, size=11))
    return svg(Wd, H, "".join(b), t, name)


# ------------------------------------------------------------ principles
def principles(t):
    Wd, H = 1280, 260
    b, cw = [], (1216 - 64 - 3 * 28) / 4
    for i, p in enumerate(L["principles"]):
        x = 64 + i * (cw + 28)
        b += [hl(x, x + cw, 30, t, t["ink"], 1.5), label(x, 64, f"0{i+1}", t, t["acc"], 12, ls=2.5),
              P(p["title"], x, 112, "display", 27, t["ink"], -.6)]
        for j, line in enumerate(p["lines"]): b.append(P(line, x, 146 + j * 23, "body", 15, t["mute"]))
        b.append(label(x, 226, p["proof"], t, t["mute"], 9.5, ls=1.2))
    return svg(Wd, H, "".join(b), t, "How I work: four principles")


# ------------------------------------------------------------ cases
def case_text(t, c, idx, H):
    b = [hl(64, 1216, 24, t, t["ink"], 1.5), P(f"0{idx}", 64, 126, "display", 86, t["dim"], -3, opacity=.9), label(176, 66, c["kicker"], t, t["acc"], 11.5, ls=3),
         P(c["title"], 176, 118, "display", 44 if W_(c["title"], "display", 44, -1.3) < 490 else 38, t["ink"], -1.3)]
    y = 166
    for line in typo.wrap(" ".join(c["lines"]), "body", 16.5, 470):
        b.append(P(line, 176, y, "body", 16.5, t["mute"])); y += 27
    for i, (big, cap) in enumerate(c["metrics"]):
        x = 176 + i * 172
        b.append(P(big, x, H - 62, "display", 40, t["ink"], -1.2)); b.append(label(x, H - 36, cap, t, size=10.5, ls=1.8))
    return b


def case_funnel(t):
    H = 430; c = L["cases"][0]; b = case_text(t, c, 1, H)
    x0, y0, w, h = 700, 120, 500, 220
    steps = [("start", 15.81, "n"), ("CPM", -3.74, "n"), ("CTR", 4.66, "n"), ("post-click", 47.10, "a"), ("end", 63.83, "t")]
    b.append(label(x0, 62, "Where the $48.02 gap came from", t, size=11, ls=2.2))
    sc, base, run = h / 70.0, y0 + h, 0
    b.append(hl(x0, x0 + w, base, t, t["mute"]))
    bw = 64; pitch = (w - bw) / 4
    prev_top = None
    for i, (lab, v, kind) in enumerate(steps):
        x = x0 + i * pitch
        if i in (0, 4): top, hh, run = base - v * sc, v * sc, (v if i == 0 else run)
        else:
            a_, b_ = run, run + v; top = base - max(a_, b_) * sc; hh = abs(v) * sc; run = b_
        col = t["acc"] if kind == "a" else (t["ink"] if kind == "t" else t["mute"])
        fill = f'fill="{col}"' if kind != "n" else f'fill="none" stroke="{col}" stroke-width="1.5"'
        b.append(f'<rect x="{x:.0f}" y="{top:.1f}" width="{bw}" height="{max(hh,1.5):.1f}" {fill}/>')
        val = f"${v:.2f}" if i in (0, 4) else f"{v:+.2f}"
        b.append(P(val, x + bw / 2, top - 12, "mono", 13, t["ink"], 0, "middle"))
        b.append(label(x + bw / 2, base + 24, lab, t, size=10.5, anchor="middle", ls=1.4))
        if i < 4:
            ly = base - run * sc
            b.append(f'<line x1="{x+bw:.0f}" y1="{ly:.1f}" x2="{x+pitch:.0f}" y2="{ly:.1f}" stroke="{t["dim"]}" stroke-dasharray="3 4"/>')
    b.append(label(x0, H - 40, "Sequential bridge · observational · public ad data", t, size=10, ls=1.6))
    return svg(1280, H, "".join(b), t, "Funnel Intelligence Lab")


def case_guard(t):
    H = 430; c = L["cases"][1]; b = case_text(t, c, 2, H)
    x0 = 700
    b.append(label(x0, 62, "Eight commands · one verdict", t, size=11))
    cmds = ["doctor", "inventory", "snapshot", "compare", "verify", "preflight", "report", "version"]
    for i, cm in enumerate(cmds):
        y = 100 + i * 28; hot = cm in ("snapshot", "compare", "verify")
        b.append(hl(x0, x0 + 230, y + 8, t))
        b.append(P(cm, x0, y, "mono", 14.5, t["ink"] if hot else t["mute"]))
        if hot: b.append(f'<circle cx="{x0+220}" cy="{y-5}" r="3.5" fill="{t["acc"]}"/>')
    for i, (lab, style) in enumerate([("PASS", "ink"), ("WARN", "dash"), ("BLOCK", "acc")]):
        x, y, w, h = 1000, 100 + i * 78, 216, 62
        if style == "acc": b.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{t["acc"]}"/>'); col = t["bg"]
        elif style == "dash": b.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{t["ink"]}" stroke-dasharray="5 4"/>'); col = t["ink"]
        else: b.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{t["ink"]}" stroke-width="1.5"/>'); col = t["ink"]
        b.append(P(lab, x + 24, y + 40, "display", 26, col, 1))
        b.append(label(x + w - 20, y + 38, "+ reason", t, col, 10, "end", 1.8))
    b.append(label(x0, H - 40, "Read-only · local-first · no numeric score, by design", t, size=10, ls=1.6))
    return svg(1280, H, "".join(b), t, "Appwrite Migration Guard")


def case_aether(t):
    H = 430; c = L["cases"][2]; b = case_text(t, c, 3, H)
    cx, cy, R = 880, 215, 118
    b.append(label(700, 62, "Eleven sources · one registry", t, size=11))
    for i in range(11):
        a = -math.pi / 2 + i * 2 * math.pi / 11
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        b.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{cx}" y2="{cy}" stroke="{t["dim"]}"/>')
        b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{t["bg"]}" stroke="{t["ink"]}" stroke-width="1.5"/>')
        b.append(f'<circle r="2.6" fill="{t["acc"]}"><animateMotion dur="{2.6+(i%4)*.6}s" begin="{i*.25:.2f}s" repeatCount="indefinite" path="M{x:.1f},{y:.1f} L{cx},{cy}"/></circle>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="34" fill="{t["acc"]}"/>')
    b.append(P("registry", cx, cy + 5, "monob", 13, t["bg"], 0, "middle"))
    b.append(f'<line x1="{cx+40}" y1="{cy}" x2="1060" y2="{cy}" stroke="{t["ink"]}"/>')
    b.append(P("53", 1130, cy + 18, "display", 70, t["ink"], -2, "middle")); b.append(label(1130, cy + 46, "route handlers", t, size=10.5, anchor="middle", ls=1.8))
    b.append(label(700, H - 40, "Licence · rate limit · provenance recorded per source", t, size=10, ls=1.6))
    return svg(1280, H, "".join(b), t, "AetherScan")


def case_nitro(t):
    H = 430; c = L["cases"][3]; b = case_text(t, c, 4, H)
    x0 = 700
    b.append(label(x0, 62, "Write path · leveled compaction", t, size=11))
    for i, s in enumerate(["WAL", "memtable", "flush"]):
        x = x0 + i * 150
        b.append(f'<rect x="{x}" y="92" width="130" height="40" fill="none" stroke="{t["ink"]}" stroke-width="1.5"/>' + P(s, x + 65, 118, "mono", 14, t["ink"], 0, "middle"))
        if i < 2: b.append(f'<line x1="{x+130}" y1="112" x2="{x+150}" y2="112" stroke="{t["acc"]}" stroke-width="2"/>')
    for i in range(4):
        w = 100 + i * 100; y = 176 + i * 42
        b.append(f'<rect x="{x0}" y="{y}" width="{w}" height="28" fill="{t["acc"] if i==3 else "none"}" stroke="{t["acc"] if i==3 else t["mute"]}"/>')
        b.append(P(f"L{i}", x0 + 14, y + 19, "monob", 12.5, t["bg"] if i == 3 else t["ink"]))
        b.append(label(x0 + w + 14, y + 19, "sstables" if i < 3 else "compacted", t, size=10, ls=1.6))
    b.append(label(x0, H - 40, "wal · memtable · sstable · bloom · index · mvcc · compaction · cache", t, size=10, ls=1.2))
    return svg(1280, H, "".join(b), t, "NitroDB")


# ------------------------------------------------------------ ledger, closing, dividers
def ledger(t):
    rows = L["ledger"]; Wd = 1280; H = 150 + 50 * len(rows)
    b = [hl(64, 1216, 28, t, t["ink"], 1.5), P("Receipts", 64, 84, "display", 40, t["ink"], -1.2),
         label(64, 116, "Every number here, and how I know it", t, size=11, ls=2.4)]
    b.append(label(1216, 116, "RAN = executed · READ = checked in source · DOC = document held", t, size=10.5, anchor="end", ls=1.6))
    for i, r in enumerate(rows):
        y = 168 + 50 * i
        b += [hl(64, 1216, y - 30, t), P(r["claim"], 64, y, "head", 17.5, t["ink"], -.2), P(r["how"], 790, y, "mono", 12.5, t["mute"]),
              (f'<circle cx="1150" cy="{y-6}" r="4.5" fill="{t["acc"]}"/>' if r["tier"] == "RAN" else f'<circle cx="1150" cy="{y-6}" r="4.5" fill="none" stroke="{t["ink"]}" stroke-width="1.5"/>' if r["tier"] == "READ" else f'<rect x="1146" y="{y-10}" width="8" height="8" fill="none" stroke="{t["mute"]}" stroke-width="1.5"/>'),
              label(1216, y - 1, r["tier"], t, t["acc"] if r["tier"] == "RAN" else t["ink"], 11, "end", 2)]
    b.append(hl(64, 1216, 168 + 50 * len(rows) - 30, t))
    return svg(Wd, H, "".join(b), t, "Receipts")


def closing(t):
    Wd, H = 1280, 300
    b = [hl(64, 1216, 30, t, t["ink"], 1.5), label(64, 70, "Get in touch", t, t["acc"], 12, ls=3.5),
         P("A messy funnel, a risky migration,", 64, 150, "display", 52, t["ink"], -1.6),
         P("a data problem?", 64, 212, "serif", 64, t["acc"], -.5),
         P("Tell me what you are trying to decide.", 64 + W_("a data problem?", "serif", 64, -.5) + 28, 212, "display", 36, t["ink"], -1.0),
         label(64, 266, "pranjalsailwal09@gmail.com   ·   linkedin.com/in/pranjal-sailwal   ·   pranjalsailwal.com", t, t["mute"], 12, ls=1.8)]
    return svg(Wd, H, "".join(b), t, "Contact")


def divider(t, num, name):
    b = [P(num, 64, 44, "mono", 14, t["acc"], 1), label(110, 44, name, t, t["mute"], 11.5, ls=4), hl(64, 1216, 62, t)]
    return svg(1280, 76, "".join(b), t, name, bg=False)


def build():
    for tn, t in TH.items():
        files = {"hero": hero(t), "case-funnel": case_funnel(t), "case-guard": case_guard(t), "case-aether": case_aether(t),
                 "case-nitro": case_nitro(t), "ledger": ledger(t), "closing": closing(t)}
        if not os.environ.get("PROFILE_ONLY"):
            files.update({"principles": principles(t), "linkedin-banner": banner(t)})
        for i, n in enumerate(["selected work", "live", "receipts"]):
            files[f"div{i}"] = divider(t, f"0{i+1}", n)
        for k, v in files.items(): (OUT / f"{k}-{tn}.svg").write_text(v, encoding="utf-8")
        (OUT / "social").mkdir(exist_ok=True)
        for pn in ([] if os.environ.get("PROFILE_ONLY") else L["pins"]):
            m = L["social"][pn[0]]; (OUT / "social" / f"{pn[0]}-{tn}.svg").write_text(social(t, pn[0], m["line"], m["metrics"]), encoding="utf-8")
    print("built")


if __name__ == "__main__":
    build()
