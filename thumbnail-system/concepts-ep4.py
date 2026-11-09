"""Thumbnail concepts — "5 Questions to Answer Before You Retire".

Each concept's elements are defined once, then composed two ways:
  ep4-thumb-N.html  — over the graded frame, for review
  ep4-gfx-N.html    — graphics only on transparent, for compositing

No frame from this shoot was supplied, so the review plate is episode 2's.
The shipping thumbnail should be built on a frame from THIS episode.

Episode 1 ("5 Signs You're Not Ready to Retire") already owns the checklist
frame and the "ARE YOU READY?" headline, so nothing here asks that question.
"""
from plate import photo_page, graphics_page

X = 690                        # type column: clear of Aaron's shoulder in this crop
PLATE = "plate-ep2.png"


def badge(text, top):
    return f'<div class="badge" style="left:{X}px;top:{top}px;">{text}</div>'


def head(html, top, size, cls=""):
    return (f'<div class="head {cls}" style="left:{X-4}px;top:{top}px;'
            f'font-size:{size}px;">{html}</div>')


# --- 1 (RECOMMENDED) — permission frame. The script opens on people who could
# retire today and don't know it. Positive possibility, where the channel's live
# frames are warnings and verdicts. ---
def b1():
    return badge("Before You Decide", 112) + head("RETIRE<br>TODAY?", 184, 122)


# --- 2 — the closing line, set as a quote. Anton title case + underline bar. ---
def b2():
    return (f'<div class="bar" style="left:{X-6}px;top:418px;width:480px;height:30px;"></div>'
            + head("You can't<br>make<br>more time", 150, 96, cls="anton title-case"))


# --- 3 — the health-insurance blocker from question three. ---
def b3():
    return badge("Health Insurance", 112) + head("DON'T<br>WAIT<br>FOR 65", 184, 104)


# --- 4 — question four, the one with nothing to do with money. ---
def b4():
    return badge("Nobody Asks This", 112) + head("RETIRING<br>TO WHAT?", 184, 94)


BODIES = [b1, b2, b3, b4]
FLAT = "*{text-shadow:none!important;box-shadow:none!important;filter:none!important;}"

for i, fn in enumerate(BODIES, 1):
    open(f"ep4-thumb-{i}.html", "w").write(photo_page(fn()).replace("plate-photo.png", PLATE))
    open(f"ep4-gfx-{i}.html", "w").write(graphics_page(fn()))
    open(f"ep4-gfx-{i}-flat.html", "w").write(graphics_page(fn(), extra_css=FLAT))

print("wrote ep4-thumb-1..4, ep4-gfx-1..4, ep4-gfx-1..4-flat")
