---
name: pinnacle-episode-packaging
description: "Use this skill to package a YouTube episode for Pinnacle Wealth Advisors (channel: Aaron Christopherson, CFP®, handle: @pinnaclewealthadvisors). Trigger whenever Mendo provides a cleaned episode script — typically a .docx — and asks for packaging, titles, thumbnails, description, tags, or any combination thereof, even if he doesn't name all four pieces. Also trigger for related asks like 'package this episode', 'I have a new script ready', 'let's do titles and thumbs for X', or 'write the description for the new video'. The skill produces a single 2-page .docx packaging deliverable containing ranked title options, a 2x2 grid of generated thumbnail mockups, the video description with the mandatory compliance disclaimer appended verbatim, and a tags list packed to 480-500 characters."
---

# Pinnacle Episode Packaging

## What this skill is for

You're packaging a new YouTube episode for the **Aaron Christopherson, CFP®** channel (handle: `@pinnaclewealthadvisors`, site: thinkpinnacle.com). The channel positions around "Simplifying Smart Investing" with a retirement-planning focus and publishes biweekly on Tuesdays. Mendo is the producer/creative director and has dyslexia — that's why this skill enforces tight, visual-first layout choices over dense text.

The deliverable is **one 2-page `.docx` file**. Page 1: titles + thumbnails. Page 2: description + tags. Anything that doesn't fit in those two pages doesn't belong in the deliverable.

## What you'll need to start

You'll almost always receive a **cleaned script as a `.docx`** in the uploads. Read it before doing anything else — the angle, hook, frameworks, and case examples in the script drive every other piece of the packaging. Use `extract-text <path>` for a fast read.

If Mendo gave you just a topic (no script), ask once for the angle and the main takeaway before drafting titles.

## Deliverable layout — strict

```
PAGE 1
├── Centered title: "[Episode Topic] — YouTube Packaging"
├── Title Options
│   ├── Scoring table (3 rows, 5 columns: # / Title / Search / Len / Pattern)
│   └── Legend line above the table explaining Search and Len
└── Thumbnail Concepts
    └── 2x2 grid of embedded PNG mockups (1 recommended + 3 alternates)

PAGE 2 (forced page break)
├── Video Description
│   ├── Body (~500 chars: hook + bullets + soft CTA)
│   └── Disclaimer (verbatim, no header above it, no "Compliance:" label)
└── Tags
    ├── Count + char meter (e.g. "17 tags · 492 / 500 chars")
    └── Comma-separated tag list
```

What's NOT in the deliverable (deliberately cut to keep it 2 pages and low-friction):
- No subtitle / channel name / handle under the main title
- No rationale paragraphs under titles (the scoring table does the work)
- No text descriptions of thumbnails (the images do the work)
- No "Compliance disclaimer (mandatory)" header — the disclaimer is included raw, ready to copy-paste
- No Packaging Strategy section at the end

## The workflow

### Step 1 — Title options (3 titles, scored)

Generate **3 titles in 3 different patterns** so Mendo has real strategic choice. Patterns that have worked on this channel: warning/loss, judgment/question, decision/comparison, authority/framework, contrarian pushback. Don't write three variations of the same pattern.

**Scoring is two columns, both objective:**

- **Search** (1–10): how well does the title match the phrase a retirement-planning viewer would actually type into YouTube? `social security at 62 vs 67 vs 70` scores high; `the smart move you're missing` scores low. This is judgment, but anchored in real search behavior.
- **Len**: actual character count. Color it green if ≤60 chars (stays visible in mobile / sidebar truncation), red if >60. No vague "tension" or "expectation" scores — they aren't measurable and feel arbitrary when shown as numbers.

The fifth column is **Pattern** (e.g. "Authority / framework", "Contrarian pushback") — a label, not a score.

The frameworks behind title selection are Paddy Galloway (packaging-led growth) and Kallaway (curiosity that pays off). Apply them silently — don't cite them in the deliverable.

**Title-to-thumbnail relationship:** the top title and the recommended thumbnail should reinforce each other, not duplicate. If the title names the number, the thumbnail visualizes the stakes — not the same number again.

### Step 2 — Thumbnail concepts (1 recommended + 3 alternates, all as images)

Generate **four 16:9 thumbnail mockups** as 1280x720 PNGs, embedded in the .docx as a 2x2 grid. Each cell has a short italic caption underneath identifying which is the recommended pick (e.g. `Recommended — "ASK THESE 4"` / `Alt — "WHEN DO YOU CLAIM?"`).

Mendo is strongest visually — he wants to see the concepts, not read about them. No archetype labels, no four-field specs, no rationale text in the deliverable. The captions are just so he knows which is the recommended one.

**You still apply the archetype rule when designing the concepts.** Check `references/thumbnail-archetypes.md` before generating — concepts that match archetypes already live on the channel shouldn't be the recommended pick. The rule lives in your design choices, not in visible text on the page.

**How to render the thumbnails:**

Build each thumbnail as an inline HTML page with embedded CSS (1280x720 frame, bold typography, warm studio plate, channel palette), then render to PNG with headless Chromium:

```bash
# Render at 1280x900 and crop to 720: headless Chromium returns a viewport
# short of the requested height, which leaves a white band across the bottom.
chromium --headless --disable-gpu --no-sandbox --hide-scrollbars \
  --force-device-scale-factor=1 --window-size=1280,900 \
  --screenshot=thumb-N.raw.png thumb-N.html
python3 -c "from PIL import Image; \
  Image.open('thumb-N.raw.png').convert('RGB').crop((0,0,1280,720)).save('thumb-N.png')"
```

Then embed the PNGs into the .docx via `docx-js`'s `ImageRun`, displayed at 280×158 px so the 2x2 grid fits on page 1 alongside the title table.

**Palette to use — warm, never navy.** Sampled from thumbnails live on the
channel: wall-light `#E4DACA` / wall-mid `#D5C8B4` / wall-shadow `#BFB09A` /
wood `#9A6F41` / accent red `#E16E69` / white `#FFFFFF` / silhouette `#4A3F36`.

The channel shoots against a warm cream brick wall with wood floating shelves.
There is no navy, gold or cool colour anywhere in it — a navy thumbnail reads as
a different channel. Three rules the live thumbnails all follow:

- **One accent move per frame.** A badge pill, an underline bar, or an oversized
  numeral — never two at once.
- **Type overlaps the talent.** The headline sits partly behind and partly in
  front of Aaron. Type fully clear of the subject reads off-brand.
- **Case is a free choice.** `WILL IT LAST?` and `Should you tithe?` are both
  in-system, so pick per concept.

Heavy grotesque type (Archivo Black / Anton), white, tight leading (~0.86), with
a heavy drop shadow so it separates from the warm wall. Silhouette stand-in for
Aaron — flat bust, no likeness; it marks blocking only.

**Layout gotchas to watch for** when designing concepts:
- Don't stack a numbers row right above a large headline — the cards will visually collide. Use generous `gap` (60-80px+) and don't `transform: scale()` cards (it breaks flex gap calculations).
- Three-arrow / fork layouts: make sure the bottom arrow row doesn't sit at the same y-coordinate as the bottom-right headline. Move arrows up.

### Step 3 — Video description (page 2)

Structure:

1. **Hook line** (1 sentence) — restates the title's core promise in plain language
2. **Body** (~400-500 chars total) — short paragraph + a 3-4 bullet preview of what the viewer learns + soft CTA to thinkpinnacle.com
3. **Disclaimer** — read `assets/disclaimer.txt` and append the full text verbatim. No header above it, no "Compliance disclaimer:" label. Mendo copy-pastes the whole page-2 description block straight into YouTube Studio; anything that isn't part of the actual description text adds friction.

**The disclaimer NEVER changes.** Treat the file as read-only source-of-truth. Do not paraphrase, abbreviate, modernize phrasing, or split it into bullets — every word, including the slightly awkward repetition at the end about written agreements, stays as-is.

### Step 4 — Tags (page 2, same page as description)

YouTube's hard cap is 500 characters across all tags combined (commas + spaces count). **Mendo wants the tag field MAXIMIZED.** Floor is 480 characters; ceiling is 500. Anything under 480 is unacceptable — it means free packaging value was left on the table.

Build a pool of tags in priority order:

1. **Exact-match episode phrasings** (multiple variants of the core query — "social security claiming age", "when to claim social security", "social security at 62", etc.)
2. **Related search queries** ("should i claim social security early", "social security break even age", "spousal social security benefits")
3. **Authority / credential terms** ("certified financial planner", "CFP advice", "fiduciary advisor")
4. **Channel / brand tags** ("Aaron Christopherson", "Pinnacle Wealth Advisors", "thinkpinnacle")

Pack greedily from the pool, skipping any tag that would push the total over 500 chars but continuing to try shorter ones to fill remaining space. Aim for the 480-500 sweet spot.

Show the count and char meter above the tag string, colored green if ≥480, red if not:

```
17 tags  ·  492 / 500 chars
```

## Assembling the .docx

Use `docx-js`. Read `/mnt/skills/public/docx/SKILL.md` first if you haven't this session — it has the API patterns for tables, images, and page breaks.

Key build details:
- **US Letter page size** (12240 × 15840 DXA), 0.75" top/bottom margins, 1" side margins — gives a bit more vertical room to fit two pages
- **Force page break before "Video Description"** using `new PageBreak()` inside a Paragraph
- **Headings**: Arial bold 16pt in warm espresso `#4A3F36` (not navy)
- **Body text**: Arial 12pt
- **Tables**: light grey 1px borders, light grey header shading, generous cell padding (top/bottom 100 DXA, left/right 160 DXA for readability)
- **Title scoring table column widths** (in DXA, sum = 9360): `#`=500, `Title`=4700, `Search`=1200, `Len`=900, `Pattern`=2060
- **Thumbnail grid**: 2 rows × 2 columns, each cell shows a 280×158 PNG with a centered italic grey caption underneath

Save the final `.docx` to `/mnt/user-data/outputs/` and call `present_files`. After presenting, **do not pad the response with a long postamble** — Mendo just wants to open the file.

## Things to avoid

- **Never modify the disclaimer text.** Compliance text is locked. If you're tempted to "clean up" the phrasing, don't.
- **Never use a thumbnail archetype already live on the channel as the recommended pick.** Check `references/thumbnail-archetypes.md`. The "$100K MISTAKE" warning frame is locked to the previous Social Security episode and cannot be reused even with a different number.
- **Never let tags land below 480 chars.** That's the floor, not an aspiration. If your pool is too thin, expand the search-query and authority-term sections — they have the most room to grow.
- **Never let the deliverable exceed 2 pages.** If it's running long, cut detail, not depth. The title scoring table stays. The thumbnail grid stays. The disclaimer stays. Everything else is negotiable.
- **Never editorialize Aaron's content.** Titles and descriptions reflect what the script actually says. Channel authority comes from accurate representation of a CFP®'s advice.

## References

- `references/thumbnail-archetypes.md` — current archetype landscape on the channel; design new concepts to avoid reusing live archetypes for the recommended pick
- `assets/disclaimer.txt` — the locked compliance disclaimer text; appended verbatim to every description
