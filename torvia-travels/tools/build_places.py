"""Generates local SVG illustrations for Coorg destinations and the estate strip."""

W, H = 800, 560


def smooth(pts):
    """Catmull-Rom through pts -> cubic bezier path data."""
    p = [pts[0]] + list(pts) + [pts[-1]]
    d = f"M{pts[0][0]} {pts[0][1]}"
    for i in range(1, len(p) - 2):
        p0, p1, p2, p3 = p[i - 1], p[i], p[i + 1], p[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}"
    return d


def ridge(pts, fill, base=H, opacity=1):
    d = smooth(pts) + f" L{pts[-1][0]} {base} L{pts[0][0]} {base} Z"
    return f'  <path d="{d}" fill="{fill}" opacity="{opacity}"/>\n'


def mist(cx, cy, rx, ry=12, o=0.55):
    return f'  <ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#FFFFFF" opacity="{o}" filter="url(#blur)"/>\n'


def tree(x, y, s=1.0, fill="#26402C"):
    return (f'  <g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0 0 L0 -52" stroke="{fill}" stroke-width="4"/>'
            f'<ellipse cx="0" cy="-58" rx="11" ry="8" fill="{fill}"/>'
            f'<ellipse cx="-10" cy="-46" rx="9" ry="6" fill="{fill}"/>'
            f'<ellipse cx="10" cy="-42" rx="8" ry="6" fill="{fill}"/></g>\n')


def palm(x, y, s=1.0, fill="#274A31"):
    fronds = "".join(
        f'<path d="M0 -70 C{18*d} -78 {40*d} -70 {52*d} -52 C{34*d} -60 {16*d} -62 0 -60 Z" fill="{fill}"/>'
        for d in (1, -1))
    return (f'  <g transform="translate({x} {y}) scale({s})">'
            f'<path d="M0 0 C-4 -30 2 -50 0 -70" stroke="{fill}" stroke-width="5" fill="none"/>{fronds}'
            f'<path d="M0 -70 C10 -86 26 -92 40 -88 C26 -84 12 -78 0 -66 Z" fill="{fill}"/>'
            f'<path d="M0 -70 C-10 -86 -26 -92 -40 -88 C-26 -84 -12 -78 0 -66 Z" fill="{fill}"/></g>\n')


def canopy(y=H, fill="#1E3324", o=1.0):
    """Dense leafy border along the bottom."""
    out = f'  <g opacity="{o}">'
    x = -20
    i = 0
    while x < W + 40:
        r = 42 + (i % 3) * 14
        out += f'<ellipse cx="{x}" cy="{y - 6 + (i % 2) * 10}" rx="{r}" ry="{r*0.72:.0f}" fill="{fill}"/>'
        x += 54
        i += 1
    return out + "</g>\n"


def head(title, sky_stops, extra_defs=""):
    stops = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in sky_stops)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
            f'role="img" aria-label="{title}">\n'
            f'  <defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">{stops}</linearGradient>'
            f'<filter id="blur" x="-30%" y="-400%" width="160%" height="900%">'
            f'<feGaussianBlur stdDeviation="14"/></filter>{extra_defs}</defs>\n'
            f'  <rect width="{W}" height="{H}" fill="url(#sky)"/>\n')


svgs = {}

# ------------------------------------------------------------------ Abbey Falls
s = head("Abbey Falls, a waterfall dropping through Coorg rainforest",
         [("0", "#DCE7D6"), ("1", "#B9CFBC")],
         '<linearGradient id="water" x1="0" y1="0" x2="0" y2="1">'
         '<stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#DCEAE6"/></linearGradient>')
s += ridge([(0, 250), (140, 200), (300, 236), (500, 190), (660, 226), (800, 196)], "#8FAE95")
s += mist(400, 258, 460, 16, 0.5)
s += ridge([(0, 330), (180, 290), (380, 320), (600, 276), (800, 306)], "#5F8168")
# gorge walls
s += ('  <path d="M0 300 C120 320 250 340 300 420 C330 470 320 520 340 560 L0 560 Z" fill="#33513B"/>\n'
      '  <path d="M800 296 C680 318 560 336 508 414 C476 466 486 520 470 560 L800 560 Z" fill="#2C4634"/>\n'
      '  <path d="M300 330 C260 356 236 400 232 460 L300 460 Z" fill="#3E5F45" opacity="0.7"/>\n')
# falls
s += ('  <path d="M348 300 C336 360 330 410 336 470 L474 470 C480 410 474 356 462 300 Z" fill="url(#water)"/>\n'
      '  <path d="M372 302 C364 356 360 412 364 466" stroke="#F4FAF7" stroke-width="9" opacity="0.9"/>\n'
      '  <path d="M408 300 C404 356 402 412 406 466" stroke="#FFFFFF" stroke-width="12" opacity="0.85"/>\n'
      '  <path d="M440 302 C438 356 438 412 442 466" stroke="#F0F7F4" stroke-width="8" opacity="0.85"/>\n'
      '  <ellipse cx="405" cy="490" rx="120" ry="26" fill="#CFE2DE"/>\n'
      '  <ellipse cx="405" cy="486" rx="86" ry="16" fill="#FFFFFF" opacity="0.85" filter="url(#blur)"/>\n'
      '  <path d="M300 500 C360 486 460 486 520 502 C560 512 600 530 640 560 L180 560 C220 530 262 512 300 500 Z" fill="#4A6B52"/>\n')
s += mist(405, 470, 150, 22, 0.6)
s += tree(120, 330, 1.0) + tree(700, 320, 0.9) + palm(214, 470, 1.1) + palm(596, 480, 1.0)
s += canopy(H + 8, "#1C2F21")
svgs["img/place-abbey-falls.svg"] = s + "</svg>\n"

# ------------------------------------------------------------------ Mandalpatti
s = head("Mandalpatti peaks rising above a sea of clouds at sunrise",
         [("0", "#F7D9A5"), ("0.45", "#F3E3C6"), ("1", "#E2E8D5")])
s += '  <circle cx="600" cy="150" r="46" fill="#FBE2AE"/>\n'
s += '  <circle cx="600" cy="150" r="110" fill="#FBD68F" opacity="0.35" filter="url(#blur)"/>\n'
s += ridge([(0, 250), (120, 196), (260, 240), (420, 178), (580, 232), (720, 190), (800, 216)], "#A9BEAE")
s += mist(380, 262, 500, 26, 0.9)
s += ridge([(0, 320), (160, 268), (340, 314), (520, 258), (700, 300), (800, 276)], "#7A9880")
s += mist(560, 330, 420, 28, 0.92) + mist(150, 346, 340, 24, 0.85)
s += ridge([(0, 400), (180, 356), (400, 396), (620, 344), (800, 384)], "#4F7159")
s += mist(400, 412, 540, 30, 0.8) + mist(620, 392, 260, 18, 0.7)
s += ridge([(0, 470), (200, 442), (440, 476), (660, 434), (800, 462)], "#31513B")
# jeep track and a 4x4 on the ridge
s += ('  <path d="M170 560 C250 528 300 502 380 490 C450 486 540 484 610 478" stroke="#8A5A38" stroke-width="15" fill="none" opacity="0.8"/>\n'
      '  <g transform="translate(432 492) scale(0.34)">'
      '<path d="M-76 0 C-80 -26 -72 -40 -48 -44 L-38 -46 C-30 -76 -14 -90 12 -92 L58 -92 C80 -90 92 -72 98 -46 L110 -42 C126 -34 130 -20 128 0 Z" fill="#F1F3EE"/>'
      '<path d="M-30 -50 C-24 -74 -12 -82 10 -84 L30 -84 L30 -50 Z" fill="#2C4A38"/>'
      '<path d="M46 -84 L58 -84 C76 -82 86 -68 92 -50 L46 -50 Z" fill="#2C4A38"/>'
      '<path d="M-20 -96 L86 -96" stroke="#DCE1D9" stroke-width="8" stroke-linecap="round"/>'
      '<circle cx="-40" cy="4" r="24" fill="#1F2C25"/><circle cx="-40" cy="4" r="10" fill="#E9EBE4"/>'
      '<circle cx="90" cy="4" r="24" fill="#1F2C25"/><circle cx="90" cy="4" r="10" fill="#E9EBE4"/></g>\n')
s += ridge([(0, 540), (240, 520), (520, 546), (800, 522)], "#213A29")
s += tree(60, 546, 0.7, "#1B2F23") + tree(740, 540, 0.7, "#1B2F23")
svgs["img/place-mandalpatti.svg"] = s + "</svg>\n"

# ------------------------------------------------------------------ Raja's Seat
s = head("Raja's Seat garden pavilion overlooking the hills at sunset",
         [("0", "#F6CE96"), ("0.5", "#F3DEC0"), ("1", "#E7E9D6")])
s += '  <circle cx="250" cy="200" r="54" fill="#F7B96F" opacity="0.85"/>\n'
s += '  <circle cx="250" cy="200" r="130" fill="#F6C177" opacity="0.3" filter="url(#blur)"/>\n'
s += ridge([(0, 300), (160, 258), (340, 296), (520, 250), (700, 292), (800, 268)], "#A8B9A6")
s += mist(400, 310, 460, 16, 0.6)
s += ridge([(0, 366), (200, 326), (420, 366), (640, 320), (800, 354)], "#6F8D74")
s += ridge([(0, 420), (220, 396), (480, 428), (800, 400)], "#4C6C54")
# terrace
s += ('  <path d="M0 452 L800 434 L800 560 L0 560 Z" fill="#3C5A44"/>\n'
      '  <path d="M0 452 L800 434 L800 462 L0 480 Z" fill="#C6B693"/>\n')
# pavilion
s += ('  <g transform="translate(400 452)">'
      '<rect x="-96" y="-96" width="192" height="96" fill="#F5EFE0"/>'
      '<path d="M-118 -96 L118 -96 L96 -128 L-96 -128 Z" fill="#8C4A3A"/>'
      '<path d="M-96 -128 L96 -128 L60 -156 L-60 -156 Z" fill="#A45A44"/>'
      '<path d="M0 -156 L0 -180" stroke="#B17D43" stroke-width="6"/><circle cx="0" cy="-186" r="8" fill="#B17D43"/>'
      '<path d="M-72 -18 L-72 -78 C-72 -96 -40 -96 -40 -78 L-40 -18 Z" fill="#2F4A38"/>'
      '<path d="M-16 -18 L-16 -78 C-16 -96 16 -96 16 -78 L16 -18 Z" fill="#2F4A38"/>'
      '<path d="M40 -18 L40 -78 C40 -96 72 -96 72 -78 L72 -18 Z" fill="#2F4A38"/>'
      '<rect x="-100" y="-4" width="200" height="10" fill="#D8CBAC"/></g>\n')
# flower beds
beds = ""
for i, x in enumerate(range(40, 800, 84)):
    col = ["#C8443A", "#E2A03F", "#D9635A", "#EFC05C"][i % 4]
    beds += (f'<ellipse cx="{x}" cy="{510 + (i % 2) * 14}" rx="38" ry="14" fill="#3F6048"/>'
             f'<circle cx="{x-14}" cy="{505 + (i % 2) * 14}" r="6" fill="{col}"/>'
             f'<circle cx="{x+4}" cy="{510 + (i % 2) * 14}" r="7" fill="{col}"/>'
             f'<circle cx="{x+20}" cy="{503 + (i % 2) * 14}" r="5" fill="{col}"/>')
s += f'  <g>{beds}</g>\n'
s += tree(90, 460, 0.8, "#2C4834") + tree(716, 452, 0.8, "#2C4834")
svgs["img/place-rajas-seat.svg"] = s + "</svg>\n"

# ------------------------------------------------------------------ Dubare
s = head("Dubare elephant camp on the banks of the Cauvery river",
         [("0", "#DCE8D8"), ("1", "#C3D8C6")])
s += ridge([(0, 220), (200, 176), (420, 214), (640, 170), (800, 202)], "#93AE97")
s += mist(400, 232, 470, 16, 0.55)
s += ridge([(0, 300), (200, 262), (440, 300), (660, 258), (800, 288)], "#5D7F64")
s += f'  <rect y="326" width="{W}" height="20" fill="#2E4A36"/>\n'
s += canopy(340, "#25402C")
# river
s += ('  <path d="M0 400 L800 380 L800 560 L0 560 Z" fill="#9FC3C4"/>\n'
      '  <path d="M0 400 L800 380 L800 404 L0 424 Z" fill="#C9DFDA" opacity="0.8"/>\n'
      '  <path d="M60 460 L300 456" stroke="#E4F0EC" stroke-width="6" opacity="0.7"/>\n'
      '  <path d="M420 500 L700 492" stroke="#E4F0EC" stroke-width="6" opacity="0.7"/>\n'
      '  <path d="M120 520 L360 514" stroke="#E4F0EC" stroke-width="5" opacity="0.55"/>\n')
# sand bank
s += '  <path d="M0 392 C160 372 320 380 470 392 C360 402 160 404 0 400 Z" fill="#D8C9A6"/>\n'
# elephant
s += ('  <g transform="translate(468 470) scale(1.02)">'
      '<ellipse cx="10" cy="-56" rx="80" ry="44" fill="#6E7173"/>'
      '<path d="M-58 -104 C-92 -104 -108 -80 -104 -50 C-100 -20 -78 -8 -56 -14 C-38 -20 -32 -44 -36 -70 C-40 -92 -46 -104 -58 -104 Z" fill="#787B7D"/>'
      '<ellipse cx="-72" cy="-62" rx="30" ry="38" fill="#63676A"/>'
      '<path d="M-52 -22 C-62 4 -60 28 -46 44 C-36 56 -50 66 -60 54 C-78 32 -82 2 -74 -26 Z" fill="#7D8082"/>'
      '<path d="M-32 -22 L-8 -6 C0 -1 -6 10 -14 5 L-36 -10 Z" fill="#F1EFE6"/>'
      '<circle cx="-40" cy="-70" r="5.5" fill="#33383A"/>'
      '<rect x="-24" y="-16" width="26" height="42" rx="11" fill="#63676A"/>'
      '<rect x="12" y="-12" width="26" height="38" rx="11" fill="#6E7173"/>'
      '<rect x="52" y="-16" width="26" height="42" rx="11" fill="#63676A"/>'
      '<rect x="80" y="-12" width="22" height="38" rx="10" fill="#6E7173"/>'
      '<path d="M88 -72 C110 -76 114 -50 100 -42" stroke="#63676A" stroke-width="7" fill="none"/></g>\n')
s += '  <ellipse cx="474" cy="500" rx="118" ry="13" fill="#6E8E8C" opacity="0.5"/>\n'
s += palm(76, 400, 1.15, "#22402C") + palm(736, 392, 1.05, "#22402C")
svgs["img/place-dubare.svg"] = s + "</svg>\n"

# ------------------------------------------------------------------ Golden Temple, Bylakuppe
s = head("Namdroling monastery, the golden temple near Kushalnagar",
         [("0", "#EFE3C8"), ("0.5", "#E6E6D2"), ("1", "#D9E3D2")],
         '<linearGradient id="gold" x1="0" y1="0" x2="0" y2="1">'
         '<stop offset="0" stop-color="#E8B95F"/><stop offset="1" stop-color="#C08C36"/></linearGradient>')
s += ridge([(0, 250), (200, 212), (420, 250), (640, 208), (800, 240)], "#9DB59E")
s += mist(400, 262, 460, 14, 0.5)
s += ridge([(0, 320), (240, 288), (520, 322), (800, 292)], "#6C8A72")
# prayer flags
s += ('  <path d="M20 250 C220 300 580 300 780 244" stroke="#7C8F80" stroke-width="3" fill="none"/>\n')
flags = ""
cols = ["#C8443A", "#E2A03F", "#F2E6CE", "#3F7A5A", "#3C6E9A"]
for i in range(16):
    x = 40 + i * 46
    y = 258 + (0 if i in (0, 15) else int(38 * (1 - abs(i - 7.5) / 7.5)))
    flags += f'<path d="M{x} {y} L{x+22} {y+4} L{x+22} {y+30} L{x} {y+26} Z" fill="{cols[i % 5]}" opacity="0.95"/>'
s += f'  <g>{flags}</g>\n'
# temple
s += ('  <g transform="translate(400 470)">'
      '<rect x="-190" y="-10" width="380" height="14" fill="#D9CBA9"/>'
      '<rect x="-150" y="-120" width="300" height="112" fill="#F3EBD8"/>'
      '<rect x="-150" y="-120" width="300" height="12" fill="#B03A32"/>'
      '<path d="M-176 -120 L176 -120 L146 -158 L-146 -158 Z" fill="url(#gold)"/>'
      '<rect x="-112" y="-206" width="224" height="50" fill="#F3EBD8"/>'
      '<path d="M-134 -206 L134 -206 L108 -240 L-108 -240 Z" fill="url(#gold)"/>'
      '<rect x="-64" y="-278" width="128" height="40" fill="#F3EBD8"/>'
      '<path d="M-84 -278 L84 -278 L60 -306 L-60 -306 Z" fill="url(#gold)"/>'
      '<path d="M0 -306 L0 -334" stroke="#C08C36" stroke-width="6"/><circle cx="0" cy="-340" r="10" fill="#E8B95F"/>'
      '<path d="M-40 -96 L40 -96 L40 -8 L-40 -8 Z" fill="#8C3B32"/>'
      '<path d="M-32 -88 L32 -88 L32 -8 L-32 -8 Z" fill="#C08C36"/>'
      '<rect x="-124" y="-96" width="34" height="56" fill="#2F4A38"/>'
      '<rect x="-72" y="-96" width="24" height="56" fill="#2F4A38"/>'
      '<rect x="48" y="-96" width="24" height="56" fill="#2F4A38"/>'
      '<rect x="90" y="-96" width="34" height="56" fill="#2F4A38"/>'
      '<rect x="-92" y="-196" width="30" height="40" fill="#2F4A38"/>'
      '<rect x="-16" y="-196" width="32" height="40" fill="#2F4A38"/>'
      '<rect x="62" y="-196" width="30" height="40" fill="#2F4A38"/></g>\n')
s += '  <path d="M0 474 L800 460 L800 560 L0 560 Z" fill="#3F5F47"/>\n'
s += '  <path d="M340 560 L360 474 L440 474 L460 560 Z" fill="#C6B693"/>\n'
s += tree(80, 476, 0.9, "#2A4632") + tree(722, 468, 0.9, "#2A4632")
svgs["img/place-golden-temple.svg"] = s + "</svg>\n"

# ------------------------------------------------------------------ Talacauvery
s = head("Talacauvery temple on the misty Brahmagiri slopes",
         [("0", "#DFE7DA"), ("0.6", "#CBDBCB"), ("1", "#B7CDBB")])
s += ridge([(0, 210), (180, 160), (400, 206), (620, 156), (800, 196)], "#A5BAA6")
s += mist(400, 224, 470, 18, 0.7)
s += ridge([(0, 292), (220, 246), (460, 292), (700, 244), (800, 274)], "#7C9A82")
s += mist(240, 306, 380, 16, 0.65) + mist(660, 296, 300, 14, 0.6)
s += ridge([(0, 372), (240, 336), (520, 380), (800, 340)], "#557A5F")
# temple compound on the slope
s += ('  <path d="M0 440 C180 410 420 418 800 396 L800 560 L0 560 Z" fill="#3E5F49"/>\n'
      '  <g transform="translate(430 434)">'
      '<rect x="-150" y="-16" width="300" height="16" fill="#CFC3A4"/>'
      '<rect x="-120" y="-86" width="240" height="70" fill="#EFE7D4"/>'
      '<path d="M-140 -86 L140 -86 L120 -108 L-120 -108 Z" fill="#9A4E3C"/>'
      '<rect x="-44" y="-170" width="88" height="64" fill="#EFE7D4"/>'
      '<path d="M-56 -170 L56 -170 L44 -196 L-44 -196 Z" fill="#9A4E3C"/>'
      '<path d="M-30 -196 C-30 -226 30 -226 30 -196 Z" fill="#B17D43"/>'
      '<path d="M0 -226 L0 -246" stroke="#B17D43" stroke-width="5"/><circle cx="0" cy="-252" r="8" fill="#D6A45E"/>'
      '<rect x="-22" y="-70" width="44" height="54" fill="#7C3E33"/>'
      '<rect x="-96" y="-70" width="26" height="40" fill="#33503C"/>'
      '<rect x="70" y="-70" width="26" height="40" fill="#33503C"/></g>\n')
# steps down to the tank
s += ('  <path d="M300 452 L560 446 L580 560 L280 560 Z" fill="#D6CBAC"/>\n'
      '  <path d="M296 480 L566 474" stroke="#BEB292" stroke-width="5"/>\n'
      '  <path d="M290 508 L572 502" stroke="#BEB292" stroke-width="5"/>\n'
      '  <path d="M284 536 L578 530" stroke="#BEB292" stroke-width="5"/>\n'
      '  <rect x="352" y="486" width="150" height="48" rx="6" fill="#9FC3C4"/>\n'
      '  <rect x="352" y="486" width="150" height="12" rx="6" fill="#C6DEDA" opacity="0.8"/>\n')
s += mist(400, 430, 520, 20, 0.5)
s += tree(96, 452, 0.9, "#2C4834") + tree(700, 440, 0.85, "#2C4834") + tree(180, 462, 0.7, "#2C4834")
svgs["img/place-talacauvery.svg"] = s + "</svg>\n"

for path, data in svgs.items():
    with open(path, "w") as f:
        f.write(data)
    print("wrote", path)
