"""Refreshes every live visual from the GitHub and Dev.to APIs (run by the Action every 6 hours).
Writes assets/{signature,live,feed,spotlight}-{dark,light}.svg.
Usage: GITHUB_TOKEN=... python3 scripts/live_stats.py sailwalpranjal | python3 scripts/live_stats.py --placeholder | --test"""
import json, math, os, sys, urllib.request, datetime, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import typo
from typo import path as P, width as W_, wrap

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"
PINS = [p[0] for p in json.loads((ROOT / "ledger.json").read_text())["pins"]]
DEVTO = "sailwalpranjal"
PALETTES = [("vermilion", "#ff5b2e", "#e0400d"), ("cobalt", "#4f7cff", "#2a56e0"), ("acid", "#c6ff3d", "#6d9100"), ("emerald", "#1fd18a", "#0e8a58"),
            ("magenta", "#ff4fa3", "#d11d7c"), ("amber", "#ffb020", "#b36b00"), ("cyan", "#27d9f0", "#0b8aa0"), ("violet", "#9a7bff", "#6b45e0")]
BASE = {"dark": dict(bg="#0b0b0c", ink="#f1eee6", mute="#8c897f", dim="#4a4944", rule="#242427"),
        "light": dict(bg="#f3f0e8", ink="#111110", mute="#6c695f", dim="#b3afa3", rule="#d6d2c5")}


def api(url, token=None, body=None):
    h = {"User-Agent": "profile-live", "Accept": "application/vnd.github+json"}
    if token: h["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None, headers=h)
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.load(r)


def clean(s): return "".join(c if 32 <= ord(c) < 383 else "?" for c in (s or "")).strip()
def fit(s, font, size, maxw, ls=0):
    s = clean(s)
    if W_(s, font, size, ls) <= maxw: return s
    while s and W_(s + "…", font, size, ls) > maxw: s = s[:-1]
    return s.rstrip() + "…"
def ago(iso, today):
    d = (datetime.date.fromisoformat(today) - datetime.date.fromisoformat(iso[:10])).days
    return "today" if d <= 0 else "1 day ago" if d == 1 else f"{d} days ago" if d < 60 else f"{d//30} months ago"


def fetch(user, token):
    today = datetime.date.today()
    since = (datetime.datetime.utcnow() - datetime.timedelta(days=364)).strftime("%Y-%m-%dT00:00:00Z")
    q = {"query": 'query($u:String!,$f:DateTime!){user(login:$u){repositories(ownerAffiliation:OWNER,isFork:false,privacy:PUBLIC){totalCount}'
                  ' contributionsCollection(from:$f){contributionCalendar{totalContributions weeks{contributionDays{contributionCount date}}}}}}',
         "variables": {"u": user, "f": since}}
    g = api("https://api.github.com/graphql", token, q)["data"]["user"]
    cal = g["contributionsCollection"]["contributionCalendar"]
    d = dict(today=today.isoformat(), total=cal["totalContributions"], repos=g["repositories"]["totalCount"],
             days=[(c["date"], c["contributionCount"]) for w in cal["weeks"] for c in w["contributionDays"]])
    langs, repos, page = {}, [], 1
    while True:
        chunk = api(f"https://api.github.com/users/{user}/repos?per_page=100&type=owner&page={page}", token)
        repos += chunk
        if len(chunk) < 100: break
        page += 1
    for r in [r for r in repos if not r["fork"]][:40]:
        try:
            for k, v in api(r["languages_url"], token).items(): langs[k] = langs.get(k, 0) + v
        except Exception: pass
    d["langs"] = sorted(langs.items(), key=lambda x: -x[1])[:6]
    d["ci"], d["shipped"], d["meta"] = [], [], {}
    for r in PINS:
        try:
            runs = api(f"https://api.github.com/repos/{user}/{r}/actions/runs?per_page=1&status=completed", token)["workflow_runs"]
            d["ci"].append((r, runs[0]["conclusion"] if runs else "none"))
        except Exception: d["ci"].append((r, "unknown"))
        try:
            c = api(f"https://api.github.com/repos/{user}/{r}/commits?per_page=1", token)[0]
            d["shipped"].append((r, c["commit"]["message"].split("\n")[0], c["commit"]["author"]["date"]))
        except Exception: pass
        try:
            m = api(f"https://api.github.com/repos/{user}/{r}", token)
            d["meta"][r] = dict(desc=m.get("description") or "", lang=m.get("language") or "", stars=m["stargazers_count"], pushed=m["pushed_at"])
        except Exception: pass
    d["shipped"].sort(key=lambda x: x[2], reverse=True)
    try:
        d["posts"] = [(a["title"], a.get("reading_time_minutes", 0), a.get("positive_reactions_count", 0), a["published_at"])
                      for a in api(f"https://dev.to/api/articles?username={DEVTO}&per_page=4")]
    except Exception: d["posts"] = []
    return d


def streaks(days):
    best = run = 0
    for _, n in days:
        run = run + 1 if n > 0 else 0
        best = max(best, run)
    cur = 0
    for i, (_, n) in enumerate(reversed(days)):
        if n > 0: cur += 1
        elif i == 0: continue
        else: break
    return cur, best


def pack(cx, cy, items, step, gap=0.7):
    placed, grid, cell = [], {}, 12
    def ok(x, y, r):
        for gx in range(int((x - r) // cell) - 2, int((x + r) // cell) + 3):
            for gy in range(int((y - r) // cell) - 2, int((y + r) // cell) + 3):
                for px, py, pr in grid.get((gx, gy), []):
                    if (px - x) ** 2 + (py - y) ** 2 < (pr + r + gap) ** 2: return False
        return True
    for r, meta in items:
        a, rad = 0.0, 0.0
        while True:
            x, y = cx + rad * math.cos(a), cy + rad * math.sin(a) * 0.9
            if ok(x, y, r): break
            a += 0.5; rad += step
        placed.append((x, y, r, meta)); grid.setdefault((int(x // cell), int(y // cell)), []).append((x, y, r))
    return placed


def ctx(d, tn):
    t = dict(BASE[tn]); wk = datetime.date.fromisoformat(d["today"]).isocalendar()[1]
    name, dk, lt = PALETTES[wk % len(PALETTES)]; t["acc"] = dk if tn == "dark" else lt
    return t, wk, name


def lab(x, y, s, t, c=None, size=11, anchor="start", ls=2.0): return P(s.upper(), x, y, "mono", size, c or t["mute"], ls, anchor)
def frame(W, H, body, t, label): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{label}"><title>{label}</title><rect width="{W}" height="{H}" fill="{t["bg"]}"/>{body}</svg>'


def signature(d, tn):
    t, wk, pname = ctx(d, tn); W, H = 1280, 440; b = []
    active = [(dt, n) for dt, n in d.get("days", []) if n > 0]; sub = "waiting for the first run"
    if active:
        nf = list(reversed(active)); items = [(1.7 + 2.3 * math.sqrt(min(n, 16)), i) for i, (dt, n) in enumerate(nf)]
        for x, y, r, i in pack(850, 222, items, 0.09 + (wk % 4) * 0.025):
            op = max(0.28, 1 - i / len(nf) * 0.72)
            an = f'<animate attributeName="r" values="{r:.1f};{r*1.5:.1f};{r:.1f}" dur="3s" begin="{(i%7)*.4:.1f}s" repeatCount="indefinite"/>' if i < 7 else ""
            b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{t["acc"]}" fill-opacity="{op:.2f}">{an}</circle>')
        sub = ago(nf[0][0] + "T00:00:00", d["today"])
    b += [lab(64, 76, f"Live signature · week {wk} · {pname}", t, t["acc"], 12, ls=3.5),
          P("One dot for every day", 64, 150, "display", 46, t["ink"], -1.4), P("I shipped something.", 64, 202, "display", 46, t["ink"], -1.4),
          P(str(d.get("total", "–")), 64, 296, "display", 38, t["ink"], -1.1), lab(64, 322, "contributions in the last 12 months", t, size=10.5, ls=1.8),
          P(sub, 64, 376, "display", 38, t["ink"], -1.1), lab(64, 402, "since my last commit", t, size=10.5, ls=1.8),
          lab(1216, 410, "newest at the core · size = contributions · redrawn every 6 hours", t, t["dim"], 9.5, "end", 1.4)]
    return frame(W, H, "".join(b), t, "Live signature: one dot per active day in the last year")


def dashboard(d, tn):
    t, wk, pname = ctx(d, tn); W, H = 1280, 560; acc = t["acc"]
    def mix(f): return "#" + "".join(f"{int(int(acc[i:i+2], 16) * f + int(t['bg'][i:i+2], 16) * (1 - f)):02x}" for i in (1, 3, 5))
    lv = [t["rule"], mix(.3), mix(.55), mix(.8), acc]
    days = d.get("days", []); cur, best = streaks(days) if days else ("–", "–")
    b = [f'<line x1="64" y1="40" x2="1216" y2="40" stroke="{t["ink"]}" stroke-width="1.5"/>']
    for i, (big, cap) in enumerate([(d.get("total", "–"), "contributions · 12 mo"), (cur, "current streak · days"), (best, "longest streak · days"), (d.get("repos", "–"), "public repositories")]):
        b += [P(str(big), 64 + i * 288, 112, "display", 46, t["ink"], -1.5), lab(64 + i * 288, 138, cap, t, size=10.5, ls=1.8)]
    weeks = [days[i:i + 7] for i in range(0, len(days), 7)]; mx = max((n for _, n in days), default=1) or 1
    for wi, w in enumerate(weeks):
        for di, (_, n) in enumerate(w):
            b.append(f'<rect x="{64+wi*14}" y="{184+di*17}" width="11" height="13" rx="1" fill="{lv[0 if n == 0 else min(4, 1 + int(3 * n / mx))]}"/>')
    if not days: b.append(lab(64, 240, "the heatmap appears after the first run", t))
    wt = [sum(n for _, n in w) for w in weeks]
    if wt:
        sx, sy, sw, sh = 64, 340, 728, 80; top = max(wt) or 1
        pts = [(sx + i * sw / max(len(wt) - 1, 1), sy + sh - v / top * sh) for i, v in enumerate(wt)]
        b.append(f'<path d="M{sx},{sy+sh} ' + " ".join(f"L{x:.1f},{y:.1f}" for x, y in pts) + f' L{sx+sw},{sy+sh} Z" fill="{acc}" fill-opacity=".14"/>')
        b.append(f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{acc}" stroke-width="2"/>')
        b.append(lab(sx, sy - 12, "weekly contributions · 52 weeks", t, size=10, ls=1.8))
    b.append(lab(64, 468, "languages · by bytes, all public repos", t, size=10, ls=1.8))
    langs = d.get("langs", []); tot = sum(v for _, v in langs) or 1; x = 64; shades = [acc, t["ink"], t["mute"], t["dim"], t["rule"], t["rule"]]
    for i, (k, v) in enumerate(langs):
        w = 728 * v / tot; b.append(f'<rect x="{x:.1f}" y="480" width="{max(w-2,1):.1f}" height="10" fill="{shades[i]}"/>')
        if w > 80: b.append(P(f"{k} {100*v/tot:.0f}%", x, 514, "mono", 11.5, t["ink"]))
        x += w
    b.append(lab(880, 174, "latest CI run · pinned repos", t, size=10, ls=1.8))
    L = {"success": ("passing", t["ink"]), "failure": ("failing", acc), "none": ("no CI", t["mute"]), "unknown": ("n/a", t["mute"])}
    for i, (r, c) in enumerate(d.get("ci") or [(r, "unknown") for r in PINS]):
        y = 206 + i * 34; txt, col = L.get(c, (c, t["mute"]))
        b.append(f'<circle cx="886" cy="{y-5}" r="4.5" fill="{col if c in ("success", "failure") else "none"}" stroke="{col}"/>')
        b.append(P(fit(r, "mono", 13, 250), 902, y, "mono", 13, t["ink"])); b.append(P(txt.upper(), 1216, y, "monob" if "monob" in typo.FONTS else "mono", 11.5, col, 1.5, "end"))
    b.append(lab(880, H - 34, f"updated {d['today']}", t, t["dim"], 9.5, ls=1.4))
    return frame(W, H, "".join(b), t, "Live GitHub activity")


def feed(d, tn):
    t, wk, pname = ctx(d, tn); W, H = 1280, 470; b = [f'<line x1="64" y1="40" x2="1216" y2="40" stroke="{t["ink"]}" stroke-width="1.5"/>']
    b += [lab(64, 80, "last shipped", t, t["acc"], 11.5, ls=3), lab(700, 80, "last written · dev.to", t, t["acc"], 11.5, ls=3)]
    sh = d.get("shipped", [])[:5]
    if not sh: b.append(lab(64, 130, "waiting for the first run", t))
    for i, (r, msg, dt) in enumerate(sh):
        y = 130 + i * 62
        b += [f'<line x1="64" y1="{y-30}" x2="640" y2="{y-30}" stroke="{t["rule"]}"/>', P(fit(r, "head", 16.5, 380), 64, y, "head", 16.5, t["ink"], -.2),
              P(ago(dt, d["today"]), 640, y, "mono", 11.5, t["mute"], 0, "end"), P(fit(msg, "body", 14, 576), 64, y + 22, "body", 14, t["mute"])]
    ps = d.get("posts", [])
    if not ps: b.append(lab(700, 130, "no posts loaded yet", t))
    for i, (title, mins, rx, dt) in enumerate(ps):
        y = 130 + i * 62
        b += [f'<line x1="700" y1="{y-30}" x2="1216" y2="{y-30}" stroke="{t["rule"]}"/>', P(fit(title, "head", 16.5, 516), 700, y, "head", 16.5, t["ink"], -.2),
              P(f"{mins} min read · {rx} reactions · {dt[:10]}", 700, y + 22, "mono", 11.5, t["mute"])]
    return frame(W, H, "".join(b), t, "Latest commits and posts")


def spotlight(d, tn):
    t, wk, pname = ctx(d, tn); W, H = 1280, 300; repo = PINS[wk % len(PINS)]; m = d.get("meta", {}).get(repo, {})
    b = [f'<line x1="64" y1="40" x2="1216" y2="40" stroke="{t["ink"]}" stroke-width="1.5"/>', lab(64, 80, f"this week's spotlight · week {wk} of the year", t, t["acc"], 11.5, ls=3),
         P(fit(repo, "display", 60, 760, -2), 64, 160, "display", 60, t["ink"], -2)]
    for i, line in enumerate(wrap(clean(m.get("desc", "")) or "refreshing on the next run", "body", 17.5, 700)[:3]): b.append(P(line, 66, 204 + i * 27, "body", 17.5, t["mute"]))
    cols = [(m.get("lang") or "–", "language"), (str(m.get("stars", "–")), "stars"), (ago(m["pushed"], d["today"]) if m.get("pushed") else "–", "last push")]
    for i, (big, cap) in enumerate(cols):
        x = 900 + i * 110 if False else 880
        y = 110 + i * 62
        b += [P(big, 880, y + 28, "display", 34, t["ink"], -1), lab(880 + 0, y + 50, cap, t, size=10, ls=1.8)] if False else []
    for i, (big, cap) in enumerate(cols):
        x = 880 + (i % 2) * 170; y = 130 + (i // 2) * 90
        b += [P(fit(big, "display", 30, 160, -1), x, y + 28, "display", 30, t["ink"], -1), lab(x, y + 52, cap, t, size=10, ls=1.8)]
    return frame(W, H, "".join(b), t, f"Weekly spotlight: {repo}")


def write(d):
    for tn in BASE:
        for n, fn in (("signature", signature), ("live", dashboard), ("feed", feed), ("spotlight", spotlight)):
            (OUT / f"{n}-{tn}.svg").write_text(fn(d, tn), encoding="utf-8")


if __name__ == "__main__":
    if sys.argv[1] == "--placeholder":
        write(dict(today=datetime.date.today().isoformat()))
    elif sys.argv[1] == "--test":
        import random; random.seed(3); OUT = pathlib.Path("/tmp/livetest"); OUT.mkdir(exist_ok=True)
        t0 = datetime.date.today() - datetime.timedelta(days=363); td = datetime.date.today().isoformat()
        days = [((t0 + datetime.timedelta(days=i)).isoformat(), random.choice([0, 0, 0, 1, 2, 4, 7, 12])) for i in range(364)]
        write(dict(today=td, days=days, total=sum(n for _, n in days), repos=14,
                   langs=[("Python", 52000), ("TypeScript", 31000), ("Go", 24000), ("Java", 15000), ("C++", 6000)],
                   ci=[(p, c) for p, c in zip(PINS, ["success", "success", "none", "failure", "unknown"])],
                   shipped=[(p, "fix the tests that fail on windows paths and add a regression test", td + "T10:00:00Z") for p in PINS],
                   meta={p: dict(desc="LSM-tree storage engine in Java: WAL, SSTables, MVCC snapshots, leveled compaction. Tested with JUnit and JCStress.", lang="Java", stars=3, pushed=td + "T09:00:00Z") for p in PINS},
                   posts=[("How I traced a 4x cost gap to the post-click step", 7, 12, "2026-10-02T00:00:00Z"), ("Writing tests for a CLI that has to say what it cannot catch", 6, 9, "2026-09-20T00:00:00Z")]))
    else:
        write(fetch(sys.argv[1], os.environ["GITHUB_TOKEN"]))
