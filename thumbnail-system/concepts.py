from plate import page, subject

MARK_W = 84

def check(x, y, color="#FFFFFF", s=MARK_W):
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;z-index:4" width="{s}" height="{s}" viewBox="0 0 100 100">'
            f'<path d="M18 54 L40 76 L84 24" fill="none" stroke="{color}" stroke-width="17" '
            f'stroke-linecap="round" stroke-linejoin="round"/></svg>')

def cross(x, y, color="#E16E69", s=MARK_W):
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;z-index:4" width="{s}" height="{s}" viewBox="0 0 100 100">'
            f'<path d="M24 24 L76 76 M76 24 L24 76" fill="none" stroke="{color}" stroke-width="17" '
            f'stroke-linecap="round"/></svg>')

SHADOW = 'filter:drop-shadow(0 8px 18px rgba(0,0,0,.45));'


# 1 — RECOMMENDED. Audit / checklist archetype: not live on the channel.
# Title names the number, so the frame shows the verdict, never "5 SIGNS".
def c1():
    marks = "".join(
        (check if i < 2 else cross)(636 + i * (MARK_W + 22), 462) for i in range(5))
    body = (subject(left=44, h=610)
            + '<div class="badge" style="left:636px;top:108px;">Retirement</div>'
            + '<div class="head" style="left:632px;top:196px;font-size:118px;">ARE YOU<br>READY?</div>'
            + f'<div style="{SHADOW}">{marks}</div>')
    return page(body)


# 2 — Alt. Ratio / segmented-meter archetype: also new to the channel.
def c2():
    segs = "".join(
        f'<div style="position:absolute;left:{636 + i*118}px;top:450px;width:100px;height:30px;'
        f'border-radius:5px;background:{"#E16E69" if i < 2 else "#FFFFFF"};'
        f'box-shadow:0 7px 16px rgba(0,0,0,.28)"></div>' for i in range(5))
    labels = ('<div style="position:absolute;left:636px;top:494px;width:218px;text-align:center;'
              'font-family:Inter9,sans-serif;font-weight:900;font-size:25px;letter-spacing:.15em;'
              'color:#E16E69;text-shadow:0 4px 12px rgba(0,0,0,.4)">MONEY</div>'
              '<div style="position:absolute;left:872px;top:494px;width:336px;text-align:center;'
              'font-family:Inter9,sans-serif;font-weight:900;font-size:25px;letter-spacing:.15em;'
              'color:#FFFFFF;text-shadow:0 4px 12px rgba(0,0,0,.4)">LIFE</div>')
    body = (subject(left=44, h=610)
            + '<div class="head" style="left:632px;top:168px;font-size:84px;">ONLY 2<br>ARE ABOUT<br>MONEY</div>'
            + segs + labels)
    return page(body)


# 3 — Alt. Underline-bar treatment, title case. Judgment-adjacent.
def c3():
    body = (subject(left=52, h=620)
            + '<div class="bar" style="left:610px;top:366px;width:520px;height:34px;"></div>'
            + '<div class="head title-case" style="left:616px;top:252px;font-size:100px;'
              'letter-spacing:-.022em;">Still<br>not ready</div>')
    return page(body)


# 4 — Alt. Curiosity / omission: leans on the three non-money signs.
def c4():
    body = (subject(left=44, h=600)
            + '<div class="badge" style="left:640px;top:120px;">Before You Retire</div>'
            + '<div class="head" style="left:636px;top:200px;font-size:126px;">THE 3<br>NOBODY<br>PLANS FOR</div>')
    return page(body)


for i, fn in enumerate([c1, c2, c3, c4], 1):
    open(f"thumb-{i}.html", "w").write(fn())
print("wrote thumb-1..4.html")
