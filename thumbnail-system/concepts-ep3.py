"""Thumbnail concepts — "Do You Actually Need a Financial Advisor?".

Each concept's elements are defined once, then composed two ways:
  ep3-thumb-N.html  — over the graded frame, for review
  ep3-gfx-N.html    — graphics only on transparent, for compositing

No frame from this shoot was supplied, so the review plate is episode 2's.
The shipping thumbnail should be built on a frame from THIS episode.
"""
from plate import photo_page, graphics_page

X = 690                        # type column: clear of Aaron's shoulder in this crop
PLATE = "plate-ep2.png"


def badge(text, top):
    return f'<div class="badge" style="left:{X}px;top:{top}px;">{text}</div>'


def head(html, top, size, cls="", left=None):
    return (f'<div class="head {cls}" style="left:{(X-4) if left is None else left}px;top:{top}px;'
            f'font-size:{size}px;">{html}</div>')


# --- 1 (RECOMMENDED) — the confession. The title asks the question; the frame
# gives the answer nobody expects from an advisor. Not an archetype live on the
# channel (judgment, warning, clean-brand, comparison, checklist, subtraction). ---
def b1():
    return badge("Honest Answer", 112) + head("MAYBE<br>NOT.", 184, 122)


# --- 2 — value / judgment on the fee. Judgment is in rotation, so alternate. ---
def b2():
    return badge("Paying An Advisor", 118) + head("WORTH<br>IT?", 194, 118)


# --- 3 — framework: the five jobs. Oversized numeral is the accent move. ---
def b3():
    return (f'<div class="mega" style="left:{X+262}px;top:112px;font-size:440px;">5</div>'
            + head("WHAT<br>YOU'RE<br>PAYING<br>FOR", 118, 88))


# --- 4 — the self-test. Underline bar is the accent move, title case. ---
def b4():
    return (f'<div class="bar" style="left:{X-6}px;top:372px;width:500px;height:30px;"></div>'
            + head("Ask these<br>5 first", 184, 100, cls="title-case"))


BODIES = [b1, b2, b3, b4]
FLAT = "*{text-shadow:none!important;box-shadow:none!important;filter:none!important;}"

for i, fn in enumerate(BODIES, 1):
    open(f"ep3-thumb-{i}.html", "w").write(photo_page(fn()).replace("plate-photo.png", PLATE))
    open(f"ep3-gfx-{i}.html", "w").write(graphics_page(fn()))
    open(f"ep3-gfx-{i}-flat.html", "w").write(graphics_page(fn(), extra_css=FLAT))

print("wrote ep3-thumb-1..4, ep3-gfx-1..4, ep3-gfx-1..4-flat")
