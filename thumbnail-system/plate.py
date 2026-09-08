# Shared studio plate + subject stand-in for the Pinnacle thumbnail system.

def shelves():
    """Two warm-wood floating shelves dressed with books, vases, plant, frame."""
    def books(x, y, specs):
        out = []
        cx = x
        for w, h, c in specs:
            out.append(f'<div class="bk" style="left:{cx}px;bottom:{y+15}px;width:{w}px;height:{h}px;background:{c}"></div>')
            cx += w + 2
        return "".join(out)

    p = []
    # upper shelf
    p.append('<div class="shelf" style="left:60px;top:196px;width:560px;"></div>')
    p.append(f'<div style="position:absolute;left:60px;top:196px;width:560px;height:0">{books(18,0,[(15,74,"#7C6A55"),(12,66,"#B9AC97"),(17,80,"#5E5346"),(11,60,"#8E7F68"),(14,70,"#CFC4AE")])}</div>')
    p.append('<div class="vase" style="left:250px;top:196px;bottom:auto;transform:translateY(-72px);width:52px;height:72px;"></div>')
    p.append('<div class="bowl" style="left:340px;top:196px;bottom:auto;transform:translateY(-34px);width:62px;height:34px;"></div>')
    p.append('<div class="frm" style="left:440px;top:196px;bottom:auto;transform:translateY(-86px);width:66px;height:86px;"></div>')

    # lower shelf
    p.append('<div class="shelf" style="left:60px;top:392px;width:560px;"></div>')
    p.append(f'<div style="position:absolute;left:60px;top:392px;width:560px;height:0">{books(300,0,[(16,78,"#6B5C49"),(12,64,"#C3B69F"),(15,72,"#554B3E"),(13,68,"#9C8B72")])}</div>')
    p.append('<div class="vase" style="left:110px;top:392px;bottom:auto;transform:translateY(-88px);width:60px;height:88px;"></div>')
    p.append('<div class="frm" style="left:196px;top:392px;bottom:auto;transform:translateY(-74px);width:58px;height:74px;"></div>')

    # trailing plant off the lower shelf
    leaves = "".join(
        f'<div class="leaf" style="left:{22+i*9}px;bottom:0;transform:rotate({-46+i*19}deg) scaleY({0.80+0.11*(i%3)})"></div>'
        for i in range(7))
    p.append(f'<div class="plant" style="left:470px;top:392px;bottom:auto;transform:translateY(-46px);width:86px;height:46px;">{leaves}</div>')
    return "".join(p)


def subject(left=96, h=520, tone="#4A3F36"):
    """Aaron composited from a frame of a published episode. Mockup stand-in
    only — the shipping thumbnail should use a frame from THIS episode."""
    import os
    if os.path.exists("aaron-cutout.png"):
        w = int(h * 321 / 437)
        return (f'<div class="subj" style="left:{left}px;">'
                f'<img src="aaron-cutout.png" width="{w}" height="{h}"></div>')
    # Fallback: flat bust silhouette if no cutout is available.
    w = int(h * 380 / 520)
    svg = f'''<svg width="{w}" height="{h}" viewBox="0 0 380 520">
  <circle cx="190" cy="128" r="82" fill="{tone}"/>
  <path d="M190 224 C92 224 26 302 18 404 L18 520 L362 520 L362 404 C354 302 288 224 190 224 Z" fill="{tone}"/>
</svg>'''
    return f'<div class="subj" style="left:{left}px;">{svg}</div>'


def page(body, extra_css=""):
    return f'''<html><head><meta charset="utf-8">
<link rel="stylesheet" href="base.css"><style>{extra_css}</style></head>
<body><div class="frame"><div class="wall"></div>{shelves()}{body}</div></body></html>'''


def photo_page(body, extra_css=""):
    """Compose over a graded frame from the episode instead of the CSS plate."""
    return f'''<html><head><meta charset="utf-8">
<link rel="stylesheet" href="base.css"><style>
.frame{{background:#CFC3B2;}}
.plate{{position:absolute;inset:0;width:1280px;height:720px;}}
.head{{text-shadow:0 12px 34px rgba(0,0,0,.62),0 4px 12px rgba(0,0,0,.5);}}
{extra_css}</style></head>
<body><div class="frame"><img class="plate" src="plate-photo.png">{body}</div></body></html>'''
