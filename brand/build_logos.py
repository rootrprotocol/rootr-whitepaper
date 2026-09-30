"""Builds the Rooter logo SVGs in site/assets/logo.

Colours are written straight into each file (no CSS variables), so the
logos render the same in browsers, design tools, PDFs and image exports.

Needs: pip install fonttools, and Bricolage Grotesque (opsz 96, wght 800)
as brand/fonts/BricolageGrotesque-800.ttf.
"""
import math, os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "site", "assets", "logo")
FONT = os.path.join(HERE, "fonts", "BricolageGrotesque-800.ttf")

VOID, PANEL, RALLY, BONE, LINE = "#0A0B0D", "#15171B", "#FF4D00", "#F4F1EA", "#26292F"


def rootbot(fg, bg, accent, glow=True, mouth=True, stroke=7, eyes="awake", ident="rb"):
    """The Rootbot drawn on a 200x200 grid. bg is the visor colour."""
    s = f'stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round" fill="none"'
    if eyes == "awake":
        eye = 'M59 106 L77 87 L95 106 M105 106 L123 87 L141 106'
    else:
        eye = 'M62 97 H94 M106 97 H138'
    parts = []
    if glow:
        parts.append(f'<defs><filter id="{ident}-glow" x="-60%" y="-60%" width="220%" height="220%">'
                     f'<feGaussianBlur stdDeviation="5"/></filter></defs>')
    parts += [
        f'<path d="M100 48V24" stroke="{fg}" {s}/>',
        f'<circle cx="100" cy="16" r="10" fill="{accent}"/>',
        f'<rect x="22" y="86" width="12" height="30" rx="5" fill="{fg}"/>',
        f'<rect x="166" y="86" width="12" height="30" rx="5" fill="{fg}"/>',
        f'<rect x="34" y="48" width="132" height="106" rx="30" fill="{fg}"/>',
        f'<rect x="50" y="66" width="100" height="56" rx="18" fill="{bg}"/>',
    ]
    ew = 'stroke-width="9" stroke-linecap="round" stroke-linejoin="round" fill="none"'
    if glow:
        parts.append(f'<path d="{eye}" stroke="{accent}" {ew} opacity="0.85" filter="url(#{ident}-glow)"/>')
    parts.append(f'<path d="{eye}" stroke="{accent}" {ew}/>')
    if mouth:
        parts.append(f'<path d="M80 136Q100 148 120 136" stroke="{bg}" stroke-width="6" stroke-linecap="round" fill="none"/>')
    parts += [
        f'<path d="M68 154Q60 172 72 192M100 154V194M132 154Q140 172 128 192" stroke="{fg}" {s}/>',
        f'<circle cx="72" cy="192" r="5" fill="{accent}"/>',
        f'<circle cx="100" cy="194" r="5" fill="{accent}"/>',
        f'<circle cx="128" cy="192" r="5" fill="{accent}"/>',
    ]
    return "".join(parts)


def svg(w, h, body, vb=None, title="Rooter"):
    vb = vb or f"0 0 {w} {h}"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{w}" height="{h}" '
            f'role="img" aria-label="{title}"><title>{title}</title>{body}</svg>\n')


def wordmark_path(text="ROOTER", tracking=-45, skew_deg=6):
    """Outlines the wordmark: Bricolage Grotesque 800, -0.045em, skewed 6deg forward."""
    f = TTFont(FONT)
    gs, cmap, hm = f.getGlyphSet(), f.getBestCmap(), f["hmtx"]
    k = math.tan(math.radians(skew_deg))
    cap = 660
    pen = SVGPathPen(gs)
    x = 0
    for ch in text:
        g = cmap[ord(ch)]
        # font units are y-up; flip to y-down with the cap height at y=0
        gs[g].draw(TransformPen(pen, (1, 0, k, -1, x, cap)))
        x += hm[g][0] + tracking
    x -= tracking
    return pen.getCommands(), x + k * cap, cap


def write(name, content):
    with open(os.path.join(OUT, name), "w") as fh:
        fh.write(content)


def main():
    os.makedirs(OUT, exist_ok=True)
    # The mark on its own, transparent ground. The visor is cut in the ground colour it sits on.
    write("rootbot-on-dark.svg", svg(200, 200, rootbot(BONE, VOID, RALLY, ident="d"), vb="0 0 200 200", title="Rootbot"))
    write("rootbot-on-light.svg", svg(200, 200, rootbot(VOID, BONE, RALLY, ident="l"), vb="0 0 200 200", title="Rootbot"))
    write("rootbot-asleep.svg", svg(200, 200, rootbot(BONE, VOID, "#5C616B", glow=False, eyes="asleep"), vb="0 0 200 200", title="Rootbot, unclaimed"))

    # App icon: rally tile, ink bot. Padded so the antenna and roots clear the corners.
    tile = lambda bg, inner: (f'<rect width="256" height="256" rx="60" fill="{bg}"/>'
                              f'<g transform="translate(36 30) scale(0.92)">{inner}</g>')
    write("app-icon-rally.svg", svg(256, 256, tile(RALLY, rootbot(VOID, RALLY, VOID, glow=False, ident="a")), title="Rooter"))
    write("app-icon-void.svg", svg(256, 256, tile(VOID, rootbot(BONE, VOID, RALLY, ident="v")), title="Rooter"))
    write("app-icon-bone.svg", svg(256, 256, tile(BONE, rootbot(VOID, BONE, RALLY, glow=False, ident="b")), title="Rooter"))
    # Round avatar for X / Telegram: void disc, rally ring.
    write("avatar.svg", svg(256, 256,
        f'<circle cx="128" cy="128" r="128" fill="{RALLY}"/><circle cx="128" cy="128" r="116" fill="{PANEL}"/>'
        f'<g transform="translate(48 44) scale(0.8)">{rootbot(BONE, PANEL, RALLY, ident="av")}</g>', title="Rooter"))
    # Favicon: fewer details and heavier strokes so it holds at 16px.
    write("favicon.svg", svg(64, 64,
        f'<rect width="64" height="64" rx="14" fill="{VOID}"/>'
        f'<g transform="translate(5 3) scale(0.27)">{rootbot(BONE, VOID, RALLY, glow=False, mouth=False, stroke=12)}</g>', title="Rooter"))

    d, ww, wh = wordmark_path()
    for name, col in (("wordmark-bone.svg", BONE), ("wordmark-ink.svg", VOID)):
        write(name, svg(round(ww), wh, f'<path d="{d}" fill="{col}"/>', vb=f"0 0 {ww:.1f} {wh}", title="Rooter"))

    # Horizontal lockup: mark height = 1.5x cap height, gap = 0.35x cap height.
    scale = wh * 1.5 / 200
    gap = wh * 0.35
    mark_w = 200 * scale
    total_w = mark_w + gap + ww
    total_h = 200 * scale
    y = (total_h - wh) / 2 + wh * 0.06
    for name, fg, bg in (("lockup-on-dark.svg", BONE, VOID), ("lockup-on-light.svg", VOID, BONE)):
        body = (f'<g transform="scale({scale:.4f})">{rootbot(fg, bg, RALLY, ident=name[7:11])}</g>'
                f'<path transform="translate({mark_w + gap:.1f} {y:.1f})" d="{d}" fill="{fg}"/>')
        write(name, svg(round(total_w), round(total_h), body, vb=f"0 0 {total_w:.1f} {total_h:.1f}", title="Rooter"))
    print("wrote", sorted(os.listdir(OUT)))


if __name__ == "__main__":
    main()
