# Pinnacle thumbnail system

Reverse-engineered from three live thumbnails on the **Aaron Christopherson, CFP®**
channel: *Will It Last?*, *#1 Retirement Threat*, and *Should You Tithe?*

Purpose: render 1280×720 concept mockups that match what already ships, so
thumbnail review is a decision about **idea and layout**, not about art direction.

## The system

**Plate** — warm cream brick wall, two wood floating shelves dressed with books,
vases, a frame and a trailing plant. Soft key from upper-left, vignette bottom-right.

**Talent** — Aaron mid-shot, left third, gesturing. In mockups he is a flat bust
silhouette: it marks blocking only and is deliberately not a likeness.

**Type** — heavy grotesque in white, tight leading (0.86), heavy drop shadow for
separation against the warm wall. The channel mixes ALL CAPS (`WILL IT LAST?`)
and title case (`Should you tithe?`) — both are in-system.

**Accent** — a single salmon red, sampled at `#E16E69`, used exactly one way per
frame: a badge pill, an underline bar, or an oversized background numeral. Never
two at once.

**Depth** — headline sits both behind and in front of the talent. That overlap is
the channel's signature; a frame with type fully clear of the subject reads as
off-brand.

## Palette

| Token | Hex | Use |
|---|---|---|
| Accent red | `#E16E69` | badge, bar, mega numeral |
| Wall light | `#E4DACA` | upper-left falloff |
| Wall mid | `#D5C8B4` | body of wall |
| Wall shadow | `#BFB09A` | lower-right vignette |
| Wood | `#9A6F41` | shelves |
| White | `#FFFFFF` | headline |
| Silhouette | `#4A3F36` | talent stand-in |

> Note: this supersedes the navy `#0E2A47` / gold `#F5C518` palette written into
> the `pinnacle-episode-packaging` skill. Nothing on the channel uses navy — the
> skill's palette is stale and should be updated to match this file.

## Usage

```bash
./fetch-fonts.sh          # Archivo Black, Anton, Archivo 900, Inter 900 (OFL)
python3 proof.py          # emit HTML for the concepts
./render.sh proof.html    # -> proof.png at exactly 1280x720
```

`render.sh` oversizes the Chromium window to 1280×900 and crops to 720. Headless
Chromium returns a viewport short of the requested height, which otherwise leaves
a white band across the bottom of every frame.

`plate.py` exposes `page(body)`, `shelves()` and `subject()`; a concept is just a
set of absolutely-positioned `.badge` / `.head` / `.bar` / `.mega` elements
composed over the plate.
