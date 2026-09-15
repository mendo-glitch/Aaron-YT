"""Thumbnail concepts for the episode.

Each concept's elements are defined once, then composed two ways:
  thumb-N.html  — over the graded frame, for review
  gfx-N.html    — graphics only on transparent, for compositing in an NLE
"""
from plate import photo_page, graphics_page

MARK = 74
SHADOW = 'filter:drop-shadow(0 10px 22px rgba(0,0,0,.6));'
X = 656                                   # type column: clear of Aaron's shoulder


def check(x, y, color="#FFFFFF", s=MARK):
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;z-index:4" width="{s}" height="{s}" viewBox="0 0 100 100">'
            f'<path d="M18 54 L40 76 L84 24" fill="none" stroke="{color}" stroke-width="18" '
            f'stroke-linecap="round" stroke-linejoin="round"/></svg>')


def cross(x, y, color="#E16E69", s=MARK):
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;z-index:4" width="{s}" height="{s}" viewBox="0 0 100 100">'
            f'<path d="M24 24 L76 76 M76 24 L24 76" fill="none" stroke="{color}" stroke-width="18" '
            f'stroke-linecap="round"/></svg>')


# --- Concept 1 (RECOMMENDED): audit / checklist, an archetype not live on the
# channel. The title names the number, so the frame delivers the verdict. ---
BADGE_1 = f'<div class="badge" style="left:{X}px;top:92px;">Retirement</div>'
HEAD_1 = f'<div class="head" style="left:{X-4}px;top:158px;font-size:92px;">ARE YOU<br>READY?</div>'
MARKS_1 = ('<div style="' + SHADOW + '">'
           + "".join((check if i < 2 else cross)(X + i * (MARK + 20), 398) for i in range(5))
           + '</div>')


def b1():
    return BADGE_1 + HEAD_1 + MARKS_1


def b2():
    segs = "".join(
        f'<div style="position:absolute;left:{X + i*112}px;top:412px;width:94px;height:28px;'
        f'border-radius:5px;background:{"#E16E69" if i < 2 else "#FFFFFF"};'
        f'box-shadow:0 8px 20px rgba(0,0,0,.45)"></div>' for i in range(5))
    lab = ('<div style="position:absolute;left:{l}px;top:456px;width:{w}px;text-align:center;'
           'font-family:Inter9,sans-serif;font-weight:900;font-size:24px;letter-spacing:.15em;'
           'color:{c};text-shadow:0 5px 14px rgba(0,0,0,.6)">{t}</div>')
    return (f'<div class="head" style="left:{X-4}px;top:132px;font-size:78px;">ONLY 2<br>ARE ABOUT<br>MONEY</div>'
            + segs + lab.format(l=X, w=206, c="#E16E69", t="MONEY")
            + lab.format(l=X + 224, w=318, c="#FFFFFF", t="LIFE"))


def b3():
    return (f'<div class="bar" style="left:{X-6}px;top:338px;width:414px;height:30px;"></div>'
            f'<div class="head title-case" style="left:{X}px;top:236px;font-size:80px;'
            'letter-spacing:-.02em;">Still<br>not ready</div>')


def b4():
    return (f'<div class="badge" style="left:{X}px;top:104px;">Before You Retire</div>'
            f'<div class="head" style="left:{X-4}px;top:176px;font-size:78px;">THE 3<br>NOBODY<br>PLANS FOR</div>')


BODIES = [b1, b2, b3, b4]

for i, fn in enumerate(BODIES, 1):
    open(f"thumb-{i}.html", "w").write(photo_page(fn()))
    open(f"gfx-{i}.html", "w").write(graphics_page(fn()))

# Concept 1 also ships as separated elements so the pick can be repositioned
# independently during the re-edit.
for name, part in [("badge", BADGE_1), ("headline", HEAD_1), ("marks", MARKS_1)]:
    open(f"gfx-1-{name}.html", "w").write(graphics_page(part))

# Shadow-free variants: the re-edit may want its own shadow or none at all.
# !important in the stylesheet beats these elements' inline box-shadows.
FLAT = ("*{text-shadow:none!important;box-shadow:none!important;"
        "filter:none!important;}")
for i, fn in enumerate(BODIES, 1):
    open(f"gfx-{i}-flat.html", "w").write(graphics_page(fn(), extra_css=FLAT))

print("wrote thumb-1..4, gfx-1..4, gfx-1-{badge,headline,marks}, gfx-1..4-flat")
