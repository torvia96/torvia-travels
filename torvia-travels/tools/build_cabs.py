"""Generates flat side-view cab illustrations as local SVG files."""

BODY = "#F4F5F1"
BODY_SHADE = "#DCE1D9"
LINE = "#C3CBC1"
GLASS = "#2C4A38"
GLASS_HI = "#4A6A54"
TYRE = "#1F2C25"
RIM = "#E9EBE4"
HUB = "#B17D43"
HEAD = "#F6CE86"
TAIL = "#B8402F"
SHADOW = "#294635"


def wheel(cx, cy, r=46):
    return f"""
  <circle cx="{cx}" cy="{cy}" r="{r}" fill="{TYRE}"/>
  <circle cx="{cx}" cy="{cy}" r="{r*0.58:.0f}" fill="{RIM}"/>
  <circle cx="{cx}" cy="{cy}" r="{r*0.22:.0f}" fill="{HUB}"/>"""


def frame(inner, label):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="800" height="460" role="img" aria-label="{label}">
  <ellipse cx="400" cy="424" rx="300" ry="20" fill="{SHADOW}" opacity="0.13"/>
{inner}
</svg>
"""


# ---------------------------------------------------------------- 4 seater hatchback
hatch = f"""
  <path d="M168 372 C162 336 168 314 194 308 L246 300 C264 262 288 238 322 230 C364 220 424 220 462 230 C492 238 518 264 542 296 L570 302 C594 308 604 322 604 348 L604 366 C604 378 598 384 584 384 L182 384 C172 384 168 380 168 372 Z" fill="{BODY}"/>
  <path d="M168 366 C200 372 340 376 604 366 C604 378 598 384 584 384 L182 384 C172 384 167 380 168 366 Z" fill="{BODY_SHADE}"/>
  <path d="M266 298 C282 266 302 246 328 240 C348 236 376 235 396 236 L396 298 Z" fill="{GLASS}"/>
  <path d="M412 236 C436 238 456 244 470 252 C490 264 508 278 522 296 L412 296 Z" fill="{GLASS}"/>
  <path d="M278 292 C292 268 308 252 328 247 L328 292 Z" fill="{GLASS_HI}" opacity="0.5"/>
  <path d="M404 234 L404 300" stroke="{BODY}" stroke-width="9"/>
  <path d="M402 300 L402 384" stroke="{LINE}" stroke-width="3"/>
  <path d="M262 300 L262 320" stroke="{LINE}" stroke-width="3"/>
  <path d="M259 306 L248 302 C240 300 238 310 246 313 Z" fill="{BODY_SHADE}"/>
  <path d="M172 330 L204 326 C214 325 216 342 206 343 L172 344 Z" fill="{HEAD}"/>
  <path d="M598 326 L574 324 L574 346 L598 346 Z" fill="{TAIL}"/>
  <path d="M330 350 L520 350" stroke="{LINE}" stroke-width="3"/>
{wheel(262, 372, 46)}
{wheel(526, 372, 46)}
"""

# ---------------------------------------------------------------- 5 seater sedan
sedan = f"""
  <path d="M104 372 C98 336 104 314 130 308 L188 300 C206 264 232 240 268 232 C316 222 388 222 430 232 C462 240 492 266 516 298 L664 312 C692 318 700 338 698 366 C697 378 690 384 676 384 L118 384 C108 384 104 380 104 372 Z" fill="{BODY}"/>
  <path d="M104 366 C140 372 320 376 698 366 C699 378 690 384 676 384 L118 384 C108 384 103 380 104 366 Z" fill="{BODY_SHADE}"/>
  <path d="M208 298 C224 266 246 246 274 240 C296 236 328 236 350 237 L350 298 Z" fill="{GLASS}"/>
  <path d="M366 238 C392 240 414 244 430 252 C452 264 474 280 490 298 L366 298 Z" fill="{GLASS}"/>
  <path d="M220 292 C234 268 250 252 272 247 L272 292 Z" fill="{GLASS_HI}" opacity="0.5"/>
  <path d="M358 236 L358 300" stroke="{BODY}" stroke-width="9"/>
  <path d="M356 300 L356 384" stroke="{LINE}" stroke-width="3"/>
  <path d="M204 300 L204 320" stroke="{LINE}" stroke-width="3"/>
  <path d="M201 306 L190 302 C182 300 180 310 188 313 Z" fill="{BODY_SHADE}"/>
  <path d="M108 330 L140 326 C150 325 152 342 142 343 L108 344 Z" fill="{HEAD}"/>
  <path d="M692 328 L668 326 L668 346 L692 346 Z" fill="{TAIL}"/>
  <path d="M280 350 L520 350" stroke="{LINE}" stroke-width="3"/>
  <path d="M520 306 L648 314" stroke="{LINE}" stroke-width="3"/>
{wheel(208, 372, 46)}
{wheel(580, 372, 46)}
"""

# ---------------------------------------------------------------- Innova style MPV
innova = f"""
  <path d="M96 366 C90 326 96 300 122 294 L156 288 C176 244 200 214 236 206 C300 194 468 194 540 208 C566 213 580 232 586 262 L664 282 C692 290 702 312 700 356 C699 374 692 380 676 380 L112 380 C100 380 96 376 96 366 Z" fill="{BODY}"/>
  <path d="M96 360 C150 368 340 374 700 356 C701 372 692 380 676 380 L112 380 C100 380 95 374 96 360 Z" fill="{BODY_SHADE}"/>
  <path d="M176 284 C192 244 214 222 244 216 C264 212 292 211 314 212 L314 284 Z" fill="{GLASS}"/>
  <path d="M330 212 L444 214 L444 284 L330 284 Z" fill="{GLASS}"/>
  <path d="M460 215 L536 220 C556 224 566 240 572 262 L460 262 Z" fill="{GLASS}"/>
  <path d="M188 278 C202 246 218 228 242 222 L242 278 Z" fill="{GLASS_HI}" opacity="0.5"/>
  <path d="M322 210 L322 288" stroke="{BODY}" stroke-width="9"/>
  <path d="M452 212 L452 288" stroke="{BODY}" stroke-width="9"/>
  <path d="M320 288 L320 380" stroke="{LINE}" stroke-width="3"/>
  <path d="M450 288 L450 380" stroke="{LINE}" stroke-width="3"/>
  <path d="M172 288 L172 310" stroke="{LINE}" stroke-width="3"/>
  <path d="M169 294 L156 290 C148 288 146 298 155 301 Z" fill="{BODY_SHADE}"/>
  <path d="M242 200 L470 200" stroke="{BODY_SHADE}" stroke-width="8" stroke-linecap="round"/>
  <path d="M100 318 L134 314 C146 313 148 332 136 333 L100 334 Z" fill="{HEAD}"/>
  <path d="M694 318 L668 316 L668 338 L694 338 Z" fill="{TAIL}"/>
  <path d="M260 344 L560 344" stroke="{LINE}" stroke-width="3"/>
{wheel(200, 366, 48)}
{wheel(586, 366, 48)}
"""

# ---------------------------------------------------------------- Tempo Traveller
tempo = f"""
  <path d="M72 356 C66 312 72 286 96 278 L124 272 C132 214 152 176 186 168 C268 150 592 150 664 168 C696 176 708 206 710 262 L710 344 C710 366 702 372 686 372 L88 372 C76 372 72 368 72 356 Z" fill="{BODY}"/>
  <path d="M72 350 C140 360 380 366 710 344 L710 350 C710 366 702 372 686 372 L88 372 C76 372 71 366 72 350 Z" fill="{BODY_SHADE}"/>
  <path d="M136 268 C146 214 164 186 192 180 C208 176 232 175 252 176 L252 268 Z" fill="{GLASS}"/>
  <path d="M280 178 L376 178 L376 258 L280 258 Z" fill="{GLASS}"/>
  <path d="M396 178 L492 178 L492 258 L396 258 Z" fill="{GLASS}"/>
  <path d="M512 178 L608 178 L608 258 L512 258 Z" fill="{GLASS}"/>
  <path d="M628 178 L668 180 C692 186 700 214 702 258 L628 258 Z" fill="{GLASS}"/>
  <path d="M148 262 C158 216 172 192 196 186 L196 262 Z" fill="{GLASS_HI}" opacity="0.5"/>
  <path d="M264 172 L264 276" stroke="{BODY}" stroke-width="10"/>
  <path d="M262 276 L262 372" stroke="{LINE}" stroke-width="3"/>
  <path d="M132 276 L132 300" stroke="{LINE}" stroke-width="3"/>
  <path d="M129 282 L116 278 C108 276 106 286 115 289 Z" fill="{BODY_SHADE}"/>
  <path d="M76 308 L112 304 C124 303 126 324 114 325 L76 326 Z" fill="{HEAD}"/>
  <path d="M704 306 L676 304 L676 328 L704 328 Z" fill="{TAIL}"/>
  <path d="M300 300 L660 300" stroke="{LINE}" stroke-width="3"/>
  <path d="M190 158 L660 158" stroke="{BODY_SHADE}" stroke-width="8" stroke-linecap="round"/>
{wheel(196, 356, 50)}
{wheel(600, 356, 50)}
"""

files = {
    "img/cab-4-seater.svg": (hatch, "Four seater hatchback cab, side view"),
    "img/cab-5-seater.svg": (sedan, "Five seater sedan cab, side view"),
    "img/cab-innova.svg": (innova, "Seven seater Innova style MPV, side view"),
    "img/cab-tempo-traveller.svg": (tempo, "Twelve seater Tempo Traveller, side view"),
}

for path, (inner, label) in files.items():
    with open(path, "w") as f:
        f.write(frame(inner, label))
    print("wrote", path)
