from plate import photo_page

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


# 1 — RECOMMENDED. Audit / checklist frame, an archetype not live on the
# channel. The title names the number, so this shows the verdict instead.
def c1():
    marks = "".join((check if i < 2 else cross)(X + i * (MARK + 20), 398) for i in range(5))
    return photo_page(
        f'<div class="badge" style="left:{X}px;top:92px;">Retirement</div>'
        f'<div class="head" style="left:{X-4}px;top:158px;font-size:92px;">ARE YOU<br>READY?</div>'
        f'<div style="{SHADOW}">{marks}</div>')


# 2 — Alt. Ratio / segmented meter: the script's sharpest hook, also new here.
def c2():
    segs = "".join(
        f'<div style="position:absolute;left:{X + i*112}px;top:412px;width:94px;height:28px;'
        f'border-radius:5px;background:{"#E16E69" if i < 2 else "#FFFFFF"};'
        f'box-shadow:0 8px 20px rgba(0,0,0,.45)"></div>' for i in range(5))
    lab = ('<div style="position:absolute;left:{l}px;top:456px;width:{w}px;text-align:center;'
           'font-family:Inter9,sans-serif;font-weight:900;font-size:24px;letter-spacing:.15em;'
           'color:{c};text-shadow:0 5px 14px rgba(0,0,0,.6)">{t}</div>')
    return photo_page(
        f'<div class="head" style="left:{X-4}px;top:132px;font-size:78px;">ONLY 2<br>ARE ABOUT<br>MONEY</div>'
        + segs
        + lab.format(l=X, w=206, c="#E16E69", t="MONEY")
        + lab.format(l=X + 224, w=318, c="#FFFFFF", t="LIFE"))


# 3 — Alt. Underline-bar treatment in title case, per "Should you tithe?".
def c3():
    return photo_page(
        f'<div class="bar" style="left:{X-6}px;top:338px;width:414px;height:30px;"></div>'
        f'<div class="head title-case" style="left:{X}px;top:236px;font-size:80px;'
        'letter-spacing:-.02em;">Still<br>not ready</div>')


# 4 — Alt. Curiosity / omission: leans on the three non-money signs.
def c4():
    return photo_page(
        f'<div class="badge" style="left:{X}px;top:104px;">Before You Retire</div>'
        f'<div class="head" style="left:{X-4}px;top:176px;font-size:78px;">THE 3<br>NOBODY<br>PLANS FOR</div>')


for i, fn in enumerate([c1, c2, c3, c4], 1):
    open(f"thumb-{i}.html", "w").write(fn())
print("wrote thumb-1..4.html")
