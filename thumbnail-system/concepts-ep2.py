"""Thumbnail concepts — "How to Maximize Your Social Security Benefit".

Each concept's elements are defined once, then composed two ways:
  ep2-thumb-N.html  — over the graded frame, for review
  ep2-gfx-N.html    — graphics only on transparent, for compositing
"""
from plate import photo_page, graphics_page

X = 690                        # type column: clear of Aaron's shoulder in this crop
PLATE = "plate-ep2.png"


def badge(text, top):
    return f'<div class="badge" style="left:{X}px;top:{top}px;">{text}</div>'


def head(html, top, size, cls=""):
    return (f'<div class="head {cls}" style="left:{X-4}px;top:{top}px;'
            f'font-size:{size}px;">{html}</div>')


# --- 1 (RECOMMENDED) — survivor benefit. A subtraction frame: two incomes
# collapsing to one. Not an archetype live on the channel, and deliberately not
# the "$X MISTAKE" treatment locked to the earlier Social Security episode. ---
def b1():
    return badge("Survivor Benefit", 96) + head("2 CHECKS<br>BECOME 1", 166, 80)


# --- 2 — the three claiming ages. Decision/comparison, already in rotation on
# the channel, so it stays an alternate. ---
def b2():
    return badge("When To Claim", 104) + head("62, 67<br>OR 70?", 176, 92)


# --- 3 — authority / framework. ---
def b3():
    return badge("Before You Claim", 104) + head("THE 4<br>RULES", 176, 96)


# --- 4 — curiosity: the zeros dragging down a 35-year record. ---
def b4():
    return head("THE ZEROS<br>ON YOUR<br>RECORD", 150, 72)


BODIES = [b1, b2, b3, b4]
FLAT = "*{text-shadow:none!important;box-shadow:none!important;filter:none!important;}"

for i, fn in enumerate(BODIES, 1):
    open(f"ep2-thumb-{i}.html", "w").write(photo_page(fn()).replace("plate-photo.png", PLATE))
    open(f"ep2-gfx-{i}.html", "w").write(graphics_page(fn()))
    open(f"ep2-gfx-{i}-flat.html", "w").write(graphics_page(fn(), extra_css=FLAT))

print("wrote ep2-thumb-1..4, ep2-gfx-1..4, ep2-gfx-1..4-flat")
