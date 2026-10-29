"""Text to outlined SVG paths (HarfBuzz shaping + kerning), so typography is identical on every device and needs no webfont."""
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

import os, pathlib
_FD = pathlib.Path(__file__).resolve().parent.parent / "fonts"
FONTS = {
    "display": "/usr/share/fonts/opentype/inter/InterDisplay-ExtraBold.otf",
    "black": "/usr/share/fonts/opentype/inter/InterDisplay-Black.otf",
    "head": "/usr/share/fonts/opentype/inter/InterDisplay-SemiBold.otf",
    "body": "/usr/share/fonts/opentype/inter/Inter-Regular.otf",
    "medium": "/usr/share/fonts/opentype/inter/Inter-Medium.otf",
    "serif": "/usr/share/fonts/truetype/crosextra/Caladea-Italic.ttf",
    "mono": "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "monob": "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
}
FONTS = {k: (str(_FD / os.path.basename(v)) if (_FD / os.path.basename(v)).exists() else v) for k, v in FONTS.items()}
_c = {}


def _load(k):
    if k not in _c:
        tt = TTFont(FONTS[k])
        blob = hb.Blob.from_file_path(FONTS[k])
        face = hb.Face(blob)
        _c[k] = (tt, tt.getGlyphSet(), hb.Font(face), tt["head"].unitsPerEm, tt.getGlyphOrder())
    return _c[k]


def shape(text, font, size, ls=0.0):
    tt, gs, hf, upm, order = _load(font)
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
    hb.shape(hf, buf, {"kern": True, "liga": True})
    sc = size / upm
    out, x = [], 0.0
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        out.append((order[info.codepoint], x + pos.x_offset * sc, pos.y_offset * sc))
        x += pos.x_advance * sc + ls
    return out, x - ls if out else 0.0


def width(text, font, size, ls=0.0):
    return shape(text, font, size, ls)[1]


def path(text, x, y, font, size, fill, ls=0.0, anchor="start", opacity=1.0, extra=""):
    tt, gs, hf, upm, order = _load(font)
    glyphs, w = shape(text, font, size, ls)
    if anchor == "middle": x -= w / 2
    elif anchor == "end": x -= w
    sc = size / upm
    pen = SVGPathPen(gs, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
    for name, gx, gy in glyphs:
        tp = TransformPen(pen, (sc, 0, 0, -sc, x + gx, y - gy))
        gs[name].draw(tp)
    d = pen.getCommands()
    op = f' fill-opacity="{opacity}"' if opacity != 1 else ""
    return f'<path d="{d}" fill="{fill}"{op}{extra}/>'


def wrap(text, font, size, maxw, ls=0.0):
    rows, cur = [], ""
    for w_ in text.split():
        t = (cur + " " + w_).strip()
        if width(t, font, size, ls) > maxw and cur:
            rows.append(cur); cur = w_
        else:
            cur = t
    rows.append(cur)
    return rows
