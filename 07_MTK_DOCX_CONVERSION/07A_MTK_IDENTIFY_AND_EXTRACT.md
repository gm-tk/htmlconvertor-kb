> **Last updated:** Thursday, 16th July, 2026 9:30 PM
> **Granular part A (1 of 4) of `07_MTK_DOCX_CONVERSION.md`** — MTK: identify, structure, extraction, menu tabs, page boundaries, bilingual rules (SS1-6).
> All sibling parts live in `07_MTK_DOCX_CONVERSION/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
> **Last updated:** Thursday, 16th July, 2026 9:30 PM

# 07 — MTK Writers Template Direct Conversion (Docx-to-HTML)

> **When to load:** When a user uploads a `.docx` Writers Template from the MTK (Marau Takiwā Reo / Te Reo Rangatira) curriculum area and NO PageForge `.txt` file is available. This file provides the rules for converting directly from the raw `.docx` format, bypassing the normal PageForge pipeline.

---

## PURPOSE

The standard conversion pipeline requires a PageForge-generated `.txt` file as input. However, MTK Writers Templates use a non-standard document structure that the PageForge converter cannot process. This file documents how to extract, interpret, and convert the raw `.docx` content into finalized HTML, based on analysis of completed TRR-series modules (TRR104, TRR105, TRR107, TRR108).

**This file supplements — does NOT replace — the core pipeline files (00–06).** All structural rules from those files still apply. This file only addresses the unique challenges of reading the `.docx` directly.

### Self-Contained Mode — No Reference HTML Files Required

Unlike other template types, MTK modules have a **fixed, predictable skeleton** that is identical across all TRR-series modules. The full HTML skeletons for overview pages and lesson pages are embedded in **Section 19** of this file. This means:

- **No structural reference files (Mode A or Mode B) are required** for MTK conversions.
- The user only needs to upload the `.docx` Writers Template — nothing else is mandatory.
- The converter extracts the module code, titles, page count, and all content directly from the `.docx`, then populates the embedded skeleton.

If the user happens to provide reference HTML files alongside the `.docx`, those files may be consulted for developer-specific style choices (e.g., how a particular interactive was implemented), but they are **not structurally necessary**.

---

## 1. IDENTIFYING AN MTK WRITERS TEMPLATE

### Detection Signals

An MTK Writers Template can be identified by these characteristics in the extracted text:

1. **"MTK WRITERS TEMPLATE: SUBMISSION CHECKLIST"** heading near the top
2. **Course code `TRR900`** in the metadata table
3. **Subject `Te Reo Rangatira`** in the metadata table
4. **Module codes beginning with `TRR`** (e.g., TRR104, TRR105, TRR107, TRR108)
5. **Bilingual table format** with `English` and `Māori` (or `Te Reo Māori`) column headers
6. **Navigation key table** at the very beginning listing sections like "Whenu / Strand", "Toi Mokopuna", etc.
7. **Template level is ALWAYS `1-3`** for these modules (early primary / Years 1–3)

### Template Sub-Type

All MTK modules are **Bilingual (reoTranslate)** sub-type:
- `<body class="container-fluid reoTranslate" language="reo" translation="eng">`
- `template="1-3"` on `<html>`
- Content elements use `reo` and `eng` attributes

### ⚠️ MTK Docx vs. Standard Writers Template Docx

A `.docx` content source is **not automatically an MTK template.** When a `.docx` is supplied, first decide which kind it is:

- **It IS an MTK template** if it shows the MTK detection signals above (MTK heading, `TRR`-series code, course code `TRR900`, bilingual English/Māori column tables, navigation key). → Use **this file (`07`)** — the self-contained MTK pathway.
- **It is NOT an MTK template** — it is a **standard (English, non-bilingual) Writers Template `.docx`**. → Do **NOT** use this file. Instead follow the **"Raw Writers Template Docx Format"** rules in `01_PIPELINE_EXTRACTION_TAGS.md` Section 02. That pathway uses the normal pipeline (PageForge-equivalent tags, standard skeleton from a structural reference) — it simply reads the raw `.docx`, skips the administrative front-matter, and converts from the first `[TITLE BAR]` onward.

In short: MTK `.docx` → file 07 (here). Standard Writers Template `.docx` → file 01 Section 02.

---

## 2. DOCUMENT STRUCTURE — What to Ignore vs. Extract

### Sections to IGNORE (do not convert to HTML)

These sections are administrative and do not appear in the student-facing HTML:

| Section | How to Identify | Action |
|---------|----------------|--------|
| Navigation Key | "How to Use the Navigation Key" table | Skip entirely |
| Back To Top | "Back To Top" at document start | Skip |
| Submission Checklist | "MTK WRITERS TEMPLATE: SUBMISSION CHECKLIST" | Skip |
| LOT Tags | "Pangarau / Te Reo Rangatira" measured skills table | Skip |
| Sign-off line | "Signed off at completion by:" | Skip |
| Writer instructions | Paragraphs about using tags, Writer's Guide links | Skip |
| PR1/PR2 columns | Review columns in tables — always empty or irrelevant | Skip (extract only English and Māori columns) |
| Kaiwhakamāori notes | "Kaiwhakamāori Team" review notes | Skip |

### Sections to EXTRACT

| Section | How to Identify | Maps To |
|---------|----------------|---------|
| Metadata table | "Subject", "Course", "Module Code", "SME Contact" rows | Module code, title extraction |
| `[TITLE BAR]` row | Row containing `[TITLE BAR]` in both columns | Page title for `<h1>` headers |
| Overview / Tirohanga Whānui | `[H2] Overview` / `[H2] Tirohanga Whānui` | Overview menu Tab 1 |
| Strand / Whenu | `[H1] Strand:` / `[H1] Whenu:` | Overview menu Tab 2 |
| Dispositions / Toi Mokopuna | `[H1] Dispositions...` / `[H1] Toi Mokopuna` | Overview menu Tab 3 |
| Key Objectives / Ngā Whāinga Matua | `[H1] Key Objectives:` / `[H1] Ngā Whāinga Matua:` | Overview menu Tab 4 |
| Critical Point / Kia Mataara | `[H1] Critical Point of Learning` / `[H1] Kia Mataara` | Overview menu Tab 5 |
| Learning Intentions / Ngā Whainga Ako | `[H1] Learning Intentions` / `[H1] Ngā Whainga Ako` | Overview menu Tab 5 or Tab 6 (see Section 4) |
| Module Introduction | `[H2] Module Introduction` / `[H2] Kōwae Ako Whakataki` | Body content of overview page (page 0.0) |
| Proverb / Whakataukī | `[H1] Proverb` / `[H1] Whakataukī` | `whakatauki` component on overview or first lesson page |
| Lesson/Activity content | Activity labels like `Activity 1A:` / `Ngohe 1A:` | Lesson page body content |
| What have I learned? | `He aha tāku i ako ai?` / `What have I learned?` | Self-check / selectionBox on final lesson page |
| Acknowledgements | Writer-provided copyright attributions | Accordion at the bottom of the overview page (page 0.0) — after the footer |

---

## 3. EXTRACTING TEXT FROM THE DOCX

### Method

Use `extract-text` to get the raw markdown from the `.docx`:

```bash
extract-text /mnt/user-data/uploads/FILENAME.docx
```

### Understanding the Output Format

The extracted text renders Word tables as markdown tables:

```
| **English** | **Māori** | **PR1** | **PR2** |
| --- | --- | --- | --- |
| [H1] **Strand:** | [H1] **Whenu:** |  |  |
| [Body] English text here... | [Body] Māori text here... |  |  |
```

**Key parsing rules:**
- Each table row `|...|...|` contains one bilingual content pair
- Column 1 = English content
- Column 2 = Māori/Te Reo content
- Columns 3–4 (PR1/PR2) = always empty — ignore
- Tags like `[H1]`, `[H2]`, `[H3]`, `[Body]` appear at the start of cell content
- `[Item N]` references indicate media assets (images, audio, video)
- `[Activity: Embedded]` rows indicate interactive components
- Bold `**text**` in markdown corresponds to `<b>text</b>` in HTML
- Italic `*text*` or `***text***` corresponds to `<i>text</i>` or `<b><i>text</i></b>`

### Handling Bilingual Tables with Only 2 Columns

Some tables have only English and Māori columns (no PR1/PR2):

```
| **English** | **Māori** |
| --- | --- |
| [Body] English text | [Body] Māori text |
```

Parse identically — the only difference is the column count.

---

## 4. OVERVIEW PAGE STRUCTURE — Module Menu Tabs

### Tab Count Variation

MTK modules use either **5 tabs** or **6 tabs** in the overview menu:

**5-tab structure** (TRR104, TRR105, TRR108 pattern — most common):
1. Tirohanga whānui / Overview
2. Whenu / Strand
3. Toi mokopuna / Dispositions
4. Ngā whāinga matua / Key objectives
5. Kia mataara / Information

In the 5-tab structure, Learning Intentions, Success Criteria, Planning Time, What Do I Need, and Connections are ALL placed inside Tab 5 (the last tab), in a two-column layout.

**6-tab structure** (TRR107 pattern):
1. Tirohanga whānui / Overview
2. Whenu / Strand
3. Toi mokopuna / Dispositions
4. Ngā Whāinga Matua / Key objectives
5. Kia Mataara / Critical Point of Learning
6. Ngā Whainga Ako / Learning Intentions

In the 6-tab structure, Learning Intentions, Success Criteria, etc. get their own dedicated tab.

### How to Determine Tab Count

Look at the writer's `[H1]` section markers. If `Kia Mataara` and `Learning Intentions` appear as separate `[H1]` sections with substantial content under each, use 6 tabs. If Learning Intentions content appears minimal or is positioned under the same structural area as Key Objectives, use 5 tabs with the combined layout.

**When in doubt:** Default to 5 tabs (the more common pattern).

### Tab 5 Label Variation

- In 5-tab modules: Tab 5 is labelled `Kia mataara / Information`
- In 6-tab modules: Tab 5 is `Kia Mataara / Critical Point of Learning`, Tab 6 is `Ngā Whainga Ako / Learning Intentions`

### Learning Intentions Tab Internal Structure

The Learning Intentions tab (whether the final tab in 5-tab or Tab 6 in 6-tab) uses a **two-column layout** with `col-md-6 paddingR` and `col-md-6 paddingL`:

- **Left column:** Learning Intentions heading (`<h4><span>`) + `<h5>` "I can:" + `<ul>` list, then Success Criteria heading + list
- **Right column:** Planning your time heading + text, then "What do I need to get started?" heading + `<ul>` checklist, then "Connections" heading + lists

### Overview Bilingual Content Rules

In the Overview tab (Tab 1), the writer's `[H3]` heading (which is typically a bold introductory sentence) maps to `<h5>` with `<b>` in the HTML:

```html
<h5 reo><b>Bold introductory text in Māori...</b></h5>
<h5 eng><b>Bold introductory text in English...</b></h5>
```

The subsequent `[Body]` paragraphs are standard `<p reo>` / `<p eng>` pairs.

### Strand/Dispositions/Key Objectives Internal Structure

Each of these tabs uses the same pattern:
```html
<h5 reo>Kia tika:</h5>
<h5 eng>Technical Precision:</h5>
<p reo>Māori body text...</p>
<p eng>English body text...</p>
```

The four sub-headings are always: Kia tika / Kia mārama / Kia whakahangahanga / Kia auaha (in Māori) and Technical Precision / Critical awareness / Diplomatic communication / Linguistic creativity (in English).

### 5-Tab Combined Tab Pattern (Key Objectives + Critical Point)

In 5-tab modules (TRR104, TRR105, TRR108), the fourth tab combines Key Objectives content with Critical Point of Learning content. The writer's `[H1] Key Objectives` and `[H1] Critical Point of Learning` sections are merged into a single tab. The Key Objectives content uses the standard `<h5>` sub-heading pattern, followed by the Critical Point content with its own `<h5>` sub-headings (e.g., "Hei te mutunga o ngā marama e 6 i te kura:").

---

## 5. PAGE BOUNDARY DETECTION

### Explicit Markers

Look for these markers in the extracted text:

- `[End Page]` — explicit page break
- `[LESSON 1 CONTENT]` / `[LESSON 2 CONTENT]` — lesson section headers (appear as centred text between tables)
- `[Lesson 2]` / `[Lesson 3]` — variant lesson markers
- Title bar repetitions: `[H1] TRR1XX The vowels: Xx | Ngā Oropuare: Xx` — these appear before each new page's content

### Implicit Boundaries

When explicit markers are absent, infer page breaks from:

- New `[H2] Lesson N` / `[H2] Hei Mahi N` headers (lesson number changes)
- Lesson numbering patterns in activity labels (Activities 1A–1I on one page, 2A–2D on the next)
- Structural repetition of the module title banner

### Page Numbering

- Page 0.0 = Overview (module intro + menu)
- Page 1.0 = First lesson
- Page 2.0 = Second lesson
- etc.

The **overview page (page 0.0)** carries the acknowledgements accordion at the bottom of the page (placed after `</div><!-- #footer -->`). The acknowledgements cover the whole module — one `acksLesson` div per page — but appear only on page 0.0. They are NOT placed on the last lesson page.

---

## 6. BILINGUAL CONTENT EXTRACTION RULES

### Table Cell → HTML Element Mapping

The writer's tables contain bilingual pairs. Each row produces TWO HTML elements:

| Writer Cell Content | HTML Output |
|---|---|
| `[H1] **Text**` in English + Māori | Context-dependent: see heading rules below |
| `[H2] **Text**` | `<h2 reo>Māori</h2>` + `<h2 eng>English</h2>` (lesson headings); `<h3 reo>` / `<h3 eng>` (activity headings within body content) |
| `[H3] **Text**` | `<h3 reo>Māori</h3>` + `<h3 eng>English</h3>` (sub-headings); `<h4 reo>` / `<h4 eng>` (activity instructions, "Finished!", "What have I learned?") |
| `[H5] Text` | `<h5 reo>Māori</h5>` + `<h5 eng>English</h5>` (menu headings, accordion headings) |
| `[Body] Text` | `<p reo>Māori</p>` + `<p eng>English</p>` |
| `[Body] [Checklist] ☒ Items` | `<ul reo><li>...</li></ul>` + `<ul eng><li>...</li></ul>` |

### Critical: [H1] Tag Context Rules

The `[H1]` tag in the writer's template does NOT always map to `<h1>`. Its HTML output depends on context:

| Writer [H1] Context | HTML Output |
|---|---|
| Menu section headers (Strand, Dispositions, etc.) | Consumed into menu tab label — no body element |
| Kia tika / Kia mārama sub-headings under Strand | `<h5 reo>` / `<h5 eng>` within menu tabs |
| Learning Intentions / Success Criteria | `<h4 reo><span>` / `<h4 eng><span>` within menu tabs |
| Planning your time / What do I need | `<h5 reo>` / `<h5 eng>` within menu tabs |
| `[H1] TRR900` course code row | `<h1 reo>TRR900</h1>` + `<h1 eng>TRR900</h1>` in body |

### Paragraph Splitting

The writer often places multiple paragraphs within a single `[Body]` cell, separated by line breaks. Each paragraph should become a separate `<p reo>` / `<p eng>` pair:

```
[Body] First paragraph text.

Second paragraph text.

Third paragraph text.
```

Becomes:
```html
<p reo>First Māori paragraph.</p>
<p eng>First English paragraph.</p>

<p reo>Second Māori paragraph.</p>
<p eng>Second English paragraph.</p>
```

### Bold/Italic Handling

- `**text**` → `<b>text</b>`
- `*text*` → `<i>text</i>`
- `***text***` → `<b><i>text</i></b>`
- Strip italics from full headings (likely a `.docx` artefact)

---

