const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, ImageRun, PageBreak, AlignmentType, BorderStyle, ShadingType,
} = require("docx");

// Usage: node build-docx.js ep3.json — one JSON config per episode.
const path = require("path");
const T = __dirname;
const cfg = JSON.parse(fs.readFileSync(path.resolve(process.argv[2] || "ep1.json"), "utf8"));
const WARM = "4A3F36", GREY = "8A7F73", GREEN = "2E7D32";
const ARIAL = "Arial";

const disclaimer = fs.readFileSync(
  "/root/.claude/skills/synced/5889914a-16cc-4050-bfe8-25c9b56091c0_894aa5a2-86e6-42a8-bb71-cdbab25185a3/pinnacle-episode-packaging/assets/disclaimer.txt",
  "utf8").trim();
const tags = fs.readFileSync(`${T}/${cfg.tagsFile}`, "utf8").trim();
const tagCount = tags.split(",").length, tagChars = tags.length;

const h = (t) => new Paragraph({
  spacing: { before: 260, after: 130 },
  children: [new TextRun({ text: t, bold: true, size: 32, font: ARIAL, color: WARM })],
});
const body = (t, o = {}) => new Paragraph({
  spacing: { after: o.after ?? 110 },
  children: [new TextRun({ text: t, size: 24, font: ARIAL, ...o.run })],
});

const cell = (children, width, opts = {}) => new TableCell({
  width: { size: width, type: WidthType.DXA },
  margins: { top: 100, bottom: 100, left: 160, right: 160 },
  shading: opts.head ? { type: ShadingType.CLEAR, fill: "F2F2F2" } : undefined,
  borders: opts.none ? Object.fromEntries(["top","bottom","left","right"]
    .map(k => [k, { style: BorderStyle.NONE, size: 0, color: "FFFFFF" }])) : undefined,
  children,
});

const txt = (t, o = {}) => new Paragraph({
  alignment: o.align,
  children: [new TextRun({ text: t, size: o.size ?? 22, font: ARIAL,
    bold: o.bold, color: o.color, italics: o.italics })],
});

// ---- Title scoring table -------------------------------------------------
const W = [500, 4700, 1200, 900, 2060];
const titles = cfg.titles;
const titleTable = new Table({
  width: { size: 9360, type: WidthType.DXA },
  rows: [
    new TableRow({ tableHeader: true, children:
      ["#", "Title", "Search", "Len", "Pattern"].map((t, i) =>
        cell([txt(t, { bold: true })], W[i], { head: true })) }),
    ...titles.map(r => new TableRow({ children: r.map((t, i) =>
      cell([txt(t, i === 3 ? { color: GREEN, bold: true } : {})], W[i])) })),
  ],
});

// ---- Thumbnail 2x2 grid --------------------------------------------------
const caps = cfg.captions;
const thumbCell = (i) => cell([
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 },
    children: [new ImageRun({ type: "png", data: fs.readFileSync(`${T}/${cfg.thumbPrefix}${i + 1}.png`),
      transformation: { width: 280, height: 158 } })] }),
  txt(caps[i], { align: AlignmentType.CENTER, italics: true, color: GREY, size: 18 }),
], 4680, { none: true });

const grid = new Table({
  width: { size: 9360, type: WidthType.DXA },
  rows: [0, 2].map(o => new TableRow({ children: [thumbCell(o), thumbCell(o + 1)] })),
});

// ---- Document ------------------------------------------------------------
const doc = new Document({
  sections: [{
    properties: { page: {
      size: { width: 12240, height: 15840 },
      margin: { top: 1080, bottom: 1080, left: 1440, right: 1440 } } },
    children: [
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 200 },
        children: [new TextRun({ text: cfg.docTitle,
          bold: true, size: 36, font: ARIAL, color: WARM })] }),

      h("Title Options"),
      txt("Search = how closely the title matches what a retirement viewer actually types into YouTube (1–10).   Len = character count; green stays visible on mobile.",
        { italics: true, color: GREY, size: 18 }),
      new Paragraph({ spacing: { after: 80 }, children: [] }),
      titleTable,

      h("Thumbnail Concepts"),
      grid,

      new Paragraph({ children: [new PageBreak()] }),

      h("Video Description"),
      ...cfg.description.map((t, i, a) => body(t, i === a.length - 1 ? { after: 240 } : {})),
      body(disclaimer),

      h("Tags"),
      txt(`${tagCount} tags  ·  ${tagChars} / 500 chars`, { bold: true, color: GREEN, size: 22 }),
      new Paragraph({ spacing: { before: 100 },
        children: [new TextRun({ text: tags, size: 22, font: ARIAL })] }),
    ],
  }],
});

Packer.toBuffer(doc).then(b => {
  const out = path.join(T, "..", cfg.outName);
  fs.writeFileSync(out, b);
  console.log("wrote", out, b.length, "bytes");
  console.log(`tags: ${tagCount} / ${tagChars} chars`);
  console.log("disclaimer chars:", disclaimer.length);
});
