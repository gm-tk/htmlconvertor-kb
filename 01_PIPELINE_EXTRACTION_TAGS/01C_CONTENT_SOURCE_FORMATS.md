> **Last updated:** Thursday, 16th July, 2026 9:30 PM
> **Granular part C (3 of 5) of `01_PIPELINE_EXTRACTION_TAGS.md`** — Content source formats: PageForge txt, raw WT docx, Media List, iStock acks.
> All sibling parts live in `01_PIPELINE_EXTRACTION_TAGS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# 02 — Content Source Formats

> **When to load:** At the start of every conversion, during Phase 2.

---

## Overview

The conversion accepts the module content from **three possible content-source formats**. Whichever format is supplied, only the relevant student-facing content (everything from the first `[TITLE BAR]` tag onward) is converted.

| Format | When used | Processing |
|---|---|---|
| **PageForge `.txt`** | Preferred/standard. A PageForge-generated text file. | Read directly — content begins at `--- CONTENT START ---` then `[TITLE BAR]`. See "PageForge Text File Format" below. |
| **Raw Writers Template `.docx`** | When no PageForge `.txt` is available for a standard (non-MTK) module. | Extract text with `extract-text`, skip ALL front-matter, convert from the first `[TITLE BAR]` onward. See "Raw Writers Template Docx Format" below. |
| **MTK Writers Template `.docx`** | Bilingual Te Reo Rangatira (`TRR`-series) modules. | Follow `07_MTK_DOCX_CONVERSION.md` — a separate, self-contained pathway. |

Additionally, a **Media List `.docx`** may be optionally supplied alongside any of the above — see "Media List Companion Document" below.

**Preference order:** If both a PageForge `.txt` and a raw `.docx` of the same module are supplied, use the `.txt` (PageForge has already resolved tracked changes, unwrapped SDTs, and cleaned formatting).

---

## PageForge Text File Format

The PageForge `.txt` is pre-extracted from the Writer Template `.docx` file by an external web application called **PageForge**. PageForge handles all Word document processing (SDT unwrapping, tracked-change resolution, hyperlink extraction, formatting detection, etc.) and outputs a clean, structured text file.

When a PageForge `.txt` is supplied, it is your sole content input — you do NOT also need the `.docx`.

---

## File Structure

A PageForge output file has two sections:

### 1. Metadata Block

```
=====================================
MODULE METADATA
=====================================
Module Code: OSAI201
Course: in My Te Kura
Date: 8/12/2020
=====================================
```

**Rules:**
- Skip everything before `--- CONTENT START ---`
- Extract the **Module Code** from the metadata block for file naming (e.g., `OSAI201` → `OSAI201-00.html`)
- The Course and Date fields are informational only — they are not used in the HTML output

### 2. Content Section

All convertible content appears after the `--- CONTENT START ---` marker. This is the ONLY section you process.

---

## Format Conventions

### Red Text (Writer Instructions)

Writer instructions to CS/developers are wrapped in red text markers:

```
🔴[RED TEXT] content here [/RED TEXT]🔴
```

**Rules:**
- Strip all red text markup from output
- Parse red text for embedded tags — if the red text contains ONLY a tag (e.g., `🔴[RED TEXT] [body] [/RED TEXT]🔴`), extract and process the tag
- If red text contains substantive **writer** CS instructions (e.g., design direction, image sourcing notes the writer placed in red text), render them as a VISIBLE red **bold** note with the `Writers Note:` prefix (`<p style="color: red; font-weight: bold;">Writers Note: ...</p>`) — NOT a hidden HTML comment. See `02_DATA_CONTENT_VERIFICATION.md` → Comment & Red Flag Policy (Source-Specific Red-Note Prefixes)
- If red text (or a subject **global-parameter** convention) marks a **deferred piece of a known, correctly-built pattern** — a "TO DO / TBC / placeholder / under development" asset, URL, or setup the developer must supply during production (e.g. `TO DO: Audiovisual item to be added`, an image to create and embed, a `stickyNav.js` file to set up) — build the pattern and render the pending piece as a VISIBLE red **bold** note with the `Designer/Developer To Do:` prefix (`<p style="color: red; font-weight: bold;">Designer/Developer To Do: ...</p>`) — NOT a hidden HTML comment. This is distinct from `Red Flag:` (which signals a genuine defect/ambiguity); `Designer/Developer To Do:` signals something right-but-pending. See `02_DATA_CONTENT_VERIFICATION.md` → Source-Specific Red-Note Prefixes and `14_SUBJECT_GLOBAL_PARAMETERS.md`
- **Never render red text as visible student content**

**Common patterns:**
- Tag-only: `🔴[RED TEXT] [H2] [/RED TEXT]🔴` → extract `[H2]` tag
- Tag + instruction: `🔴[RED TEXT] [drag and drop column autocheck] They are currently in the correct place [/RED TEXT]🔴` → extract tag `[drag and drop column autocheck]`; if the trailing instruction is substantive, surface it as a VISIBLE red **bold** `Writers Note:`
- Pure instruction: `🔴[RED TEXT] CS: please make the images small [/RED TEXT]🔴` → VISIBLE red **bold** note (`<p style="color: red; font-weight: bold;">Writers Note: CS instruction — please make the images small</p>`), NOT a hidden HTML comment
- **Captured reviewer comment** (the `Note from {author}:` lead): `🔴[RED TEXT] Note from Kate Scanlon: Please replace this stock image with an iStock photo of a NZ classroom. [/RED TEXT]🔴` → VISIBLE red **bold** **designer message** preserving the lead + author + text verbatim: `<p style="color: red; font-weight: bold;">Note from Kate Scanlon: Please replace this stock image with an iStock photo of a NZ classroom.</p>` — see **Captured Reviewer Comments** below
- Whitespace-only red text: `🔴[RED TEXT]   [/RED TEXT]🔴` → disregard entirely

#### Captured Reviewer Comments (author-prefixed red text)

PageForge reads the writer `.docx`'s **native Word margin comments** (`word/comments.xml`), keeps only the **actionable** ones authored by the whitelisted Creative-Services reviewers, and re-emits each into the parsed `.txt` using the **same red-text marker**, **already carrying the `Note from {author}:` lead**:

```
🔴[RED TEXT] Note from {Author}: {the reviewer's comment text, verbatim} [/RED TEXT]🔴
```

These are a **PageForge-`.txt` feature** (PageForge does the capture, normalisation, whitelist, and actionability filtering; a raw non-PageForge `.docx` carries no such notes). Handle them as follows:

- **Six whitelisted authors only.** Surface a note only if its `{Author}` (inside the `Note from {author}:` lead) resolves to one of: **Kate Scanlon, Nadia Stanton, Caroline Schwer, Simon Vita, Amanda Griffiths, Creative Services** (PageForge has already normalised Word's inconsistent author strings to these canonical display names before matching). Recognition is by the `Note from {whitelisted author}:` lead.
- **Already filtered to the actionable.** PageForge omits pure copyright/permission/attribution boilerplate *unless* it also carries an action signal (e.g. "Replace with iStock. Used with permission." is kept because "replace" wins). So any note that reaches you is something a designer must see — render it; do **not** re-suppress it as boilerplate.
- **Render as a VISIBLE red bold designer message**, using the established `<p style="color: red; font-weight: bold;">…</p>` form (the sole permitted designer-message inline style). Canonical rendering:
  ```html
  <p style="color: red; font-weight: bold;">Note from {Author}: {verbatim comment text}</p>
  ```
  The `Note from {author}:` lead distinguishes a captured reviewer comment from a writer's own red-font CS instruction (which renders `Writers Note: …`), from a Convertor-detected issue (`Red Flag: …`), and from a deferred developer action on a known pattern (`Designer/Developer To Do: …`) — see `02_DATA_CONTENT_VERIFICATION.md` → Source-Specific Red-Note Prefixes. PageForge supplies the `Note from {author}:` lead already; render it **verbatim** — do not reword it, drop the author, or substitute another prefix. The **firm requirement** is the **red bold style**, the **preserved lead + author + text**, and that the attribution is **never lost**.
- **Verbatim.** Do not paraphrase, summarise, truncate, or drop the author name or comment text. (The comment text is not student content, but it is passed through unchanged.)
- **In position.** PageForge places each note **immediately before the element it refers to** in the `.txt` (a comment anchored to a Media List row is placed before the body element that uses the **same media item**). Render the red message in that same "note → then the thing it's about" order.
- **Designer-facing, never student-facing**, and **never** relocated into an HTML comment (consistent with "comments are not a communication channel").
- **Do not tag-parse a prose comment.** These are sentences, not tag carriers — the tag-only → extract-the-tag branch must not swallow or mangle an author-prefixed comment.
- **Edge cases:** multiple notes before one element each surface in order; a note mixing a copyright/permission phrase with an action has already passed PageForge's filter and **must be shown**; a media-anchored note renders before the body element using that media even though the media row is not itself body text; a note referencing an interactive is fine because it is a *visible* red message (the answer-secrecy rule is specifically about *hidden* comments).

See `02_DATA_CONTENT_VERIFICATION.md` → Comment & Red Flag Policy (Captured Reviewer Comments) and `00_MASTER_INSTRUCTIONS.md` constraint 57.

### Formatting Markers

| Marker | Meaning | HTML |
|--------|---------|------|
| `**text**` | Bold | `<b>text</b>` or `<strong>text</strong>` |
| `*text*` | Italic | `<i>text</i>` or `<em>text</em>` |
| `***text***` | Bold + Italic | `<b><i>text</i></b>` |
| `__text__` | Underline | `<u>text</u>` |

### Hyperlinks

Text hyperlinks (where visible text differs from URL):
```
__link text__ [LINK: https://example.com]
```

Bare media URLs (video, image references) appear as plain URLs without `[LINK:]`:
```
https://www.youtube.com/watch?v=4NS7L9jH_pg
```

**Rule:** When you see `[LINK: URL]`, the preceding underlined text is the visible link text. When you see a bare URL after a media tag (e.g., `[video]`, `[image]`), it is a media reference.

### Bullet Lists

```
• Item 1
• Item 2
  • Sub-item (2-space indent per level)
```

### Tables

```
┌─── TABLE ───
│ Cell 1 ║ Cell 2 ║ Cell 3
│ Cell 4 ║ Cell 5 ║ Cell 6
└─── END TABLE ───
```

- `║` separates columns
- `/` within a cell represents a line break within that cell
- Each `│` line represents a row
- Red text markers may appear inside table cells (process normally)

### Special Characters

PageForge preserves all special characters:
- Macronised characters: ā, ē, ī, ō, ū, Ā, Ē, Ī, Ō, Ū
- Subscripts: CO₂
- Emoji: ⚠️ ❤️ 🔒 ✅ 🤔 — **preserved by PageForge in the `.txt`, but NOT carried into the HTML.** See No Emoji in Modules below (constraint 74): the Convertor **strips** emoji from the output (ticks and crosses excepted) and discloses the removal with a visible `Red Flag:` note. PageForge's job is faithful extraction; the removal happens at conversion.
- En-dash, em-dash, and other punctuation preserved as-is

### No Emoji in Modules (constraint 74)

**⚠️ CRITICAL — Emoji are removed from module output.** Finished modules carry **no emoji**. Where the writer's content contains emoji, the Convertor **strips them** and discloses the removal with a visible red note. This is a **documented exception to constraint 1** (never modify writer wording) — the only exception that permits *removing* writer characters rather than re-casing them — granted by the design team on 16 July 2026.

**The exempt set — ticks and crosses stay exactly as written:**

| Keep (verbatim) | Strip |
|---|---|
| ✅ ✓ ✔ ☑ ✗ ✘ ❌ ❎ | every other emoji — 🪤 ⚠️ 🤖 ❤️ 🔒 🤔 😀 🎉 👍 etc. |

Ticks and crosses **carry meaning** (correct/incorrect, done/not done, true/false) and are frequently load-bearing in answers, checklists, and tables; every other emoji is decorative. When a glyph is genuinely borderline, **keep it and raise a `Red Flag:`** rather than stripping it — a wrong removal silently destroys meaning, a wrong keep is merely visible.

**How to strip:**

1. **Emoji leading a line/paragraph** — remove the emoji **and** the whitespace that separated it from the text; the text is otherwise untouched.
2. **A RUN of emoji-prefixed lines becomes a list.** Where two or more consecutive lines each open with an emoji, they are the writer's list formatting: render the run as a single `<ul>` with one `<li>` per line (emoji stripped), rather than as separate `<p>` paragraphs. A **single** isolated emoji-prefixed line stays a `<p>` — one item is not a list.
3. **Emoji inside prose** (mid-sentence or trailing, e.g. `be kind ❤️ to yourself`) — remove the emoji and **normalise the surrounding spacing to a single space** (→ `be kind to yourself`). Never re-word to "fill the gap".
4. **Everything else is preserved verbatim** — wording, typos, casing, punctuation, macrons (constraint 1 is otherwise fully in force).

**Disclose the removal — one visible note per page:**

```html
<p style="color: red; font-weight: bold;">Red Flag: Emoji have been removed from this content per the no-emoji rule. Ticks and crosses are retained.</p>
```

The prefix is **`Red Flag:`** — this is a **Convertor-made change to writer content**, which is exactly what `Red Flag:` marks on the `02` taxonomy (not `Writers Note:`, which is the writer's own note, and not `Designer/Developer To Do:`, which is right-but-pending). Emit **one note per page** on which any emoji was removed, placed at the point of the **first** removal on that page — not one per emoji. If emoji were removed but only from the exempt set (i.e. none), emit no note.

Example — a run of emoji-prefixed lines:

```html
<!-- Writer source: 🪤An online scam is… / ⚠️Get to know common scams… / 🤖AI scams can clone voices… -->
<h4>Let's sum up!</h4>
<p style="color: red; font-weight: bold;">Red Flag: Emoji have been removed from this content per the no-emoji rule. Ticks and crosses are retained.</p>
<ul>
    <li>An <b>online scam</b> isa trap set up to fool people into giving up personal information with the intent to steal from them.</li>
    <li>Get to know common scams to help you spot them like malware, fake competition, impersonation, romance, parcel and tech-support scams.</li>
    <li>AI scams can clone voices, companies and people so be vigilant.</li>
</ul>
```

(The writer's typo "isa" is preserved — constraint 1 still governs wording.) This rule is **universal** — every series, every level, every template. Self-reflection emoji **images** (`self-reflection-emoji/*.png`, an `imageCentral` template asset) are **images, not characters**, and are entirely unaffected.

---

## Content Integrity

PageForge handles tracked changes correctly:
- Deleted content (`<w:del>`) is already removed
- Inserted content (`<w:ins>`) is already kept as normal text
- SDT wrappers (`<w:sdt>`) are already unwrapped

**The text in the PageForge file represents the writer's final intended content.** Trust it as-is. Do not second-guess apparent case changes or unusual text — these reflect the writer's post-edit state.

---

## What to IGNORE in the Text File

- Everything before `--- CONTENT START ---` (metadata block)
- Document header ("MTK WRITERS TEMPLATE" title) — if present
- Submission Checklist — if present
- To-do notes / internal comments — if present
- LOT tags table — if present
- Sign-off line — if present
- Contents page — if present
- Section A — Merging Resources — if present
- "Understanding which sections to complete" block — if present
- Writer's guidance box — if present
- "For text" / "For media" red instruction blocks — if present

**Note:** PageForge typically strips most of these before output. If any remnants appear, ignore them.

## What to CONVERT

Only content from the first `[TITLE BAR]` tag onward.

---

## Raw Writers Template Docx Format

> **When to load:** When the content source is a raw (non-MTK) Writers Template `.docx` and no PageForge `.txt` is available.

When no PageForge `.txt` exists, the **original, unprocessed Writers Template `.docx`** is accepted as the content source. This is the same Word document that PageForge would normally process — but here it is read directly.

### How It Differs From the PageForge `.txt`

The raw `.docx` carries a large amount of **excess administrative front-matter** that PageForge would strip. It also presents tags and tables differently:

| Aspect | PageForge `.txt` | Raw Writers Template `.docx` |
|---|---|---|
| Tags | Wrapped in red markers: `🔴[RED TEXT] [H2] [/RED TEXT]🔴` | Bare brackets: `[H2]` (no red markers) |
| Tables | `┌─── TABLE ───` / `║` / `└─── END TABLE ───` | Markdown tables: `| cell | cell |` with a `| --- | --- |` separator row |
| Front-matter | Already stripped by PageForge | **Present in full — must be skipped** |
| Metadata | `MODULE METADATA` block before `--- CONTENT START ---` | Module code appears in a small metadata table, in the `[TITLE BAR]` content, and/or in the filename |
| Italic placeholder text | Resolved | Template placeholder text may still be italicised; the writer was instructed to remove italics where they replaced placeholder text |

### Extraction Method

1. Run `extract-text` on the `.docx` to obtain markdown.
2. **Confirm it is NOT an MTK template** (no "MTK WRITERS TEMPLATE" heading, not a `TRR`-series code, no bilingual English/Māori column table). If it IS MTK → switch to `07_MTK_DOCX_CONVERSION.md`.
3. Extract the **module code** from the metadata table, the `[TITLE BAR]` content, or the filename.
4. **SKIP ALL front-matter** (see list below).
5. **Convert ONLY the content from the first `[TITLE BAR]` tag onward** — this is the sole student-facing content.

### Front-Matter to SKIP (raw `.docx` only)

The raw `.docx` typically opens with these administrative sections. **None of them are converted — they are not student-facing content:**

- The "MTK WRITERS TEMPLATE" / "WRITERS TEMPLATE" title block at the very top
- **Submission Checklist** ("On completion of the Writer's template ensure you have checked off these tasks…")
- **LOT tags table** (Numeracy / Literacy "Measured Skill / Activity Tagged" grid)
- **Sign-off line** ("Signed off at completion by: ___")
- **Contents** list ("Understanding which sections to complete / Section A / Section B")
- **"Understanding which section/s to complete"** explanatory block
- **Section A — Merging Resources** (First/Second/Third source tables, "% Content from this module used", merged-item tables)
- **Section B — New Content Development** header and the **writer's guidance box** ("When writing, please don't attempt to add to, or change, the layout of this document…")
- Any "Adjust the italicised text below to suit your resource" instruction line
- Trailing empty tables at the end of the document

**The actual convertible content begins at the first `[TITLE BAR]` tag** — exactly the same boundary used for PageForge files. Everything before it is front-matter; everything from it onward is content.

### Tag and Table Handling in the Raw `.docx`

- **Tags** appear as bare `[tag]` text (e.g., `[H2]`, `[body]`, `[image]`, `[drag and drop autocheck]`). Normalise them exactly as for PageForge tags (Section 04) — there are simply no `🔴[RED TEXT]🔴` markers to strip.
- **CS instructions** that PageForge would have placed in red text appear as ordinary text near a tag (e.g., `[drag and drop autocheck] CS – Single column. More answers provided than needed.`). Treat the trailing instruction the same way: extract the tag, then surface any substantive writer CS instruction as a VISIBLE red **bold** `Writers Note:` (`<p style="color: red; font-weight: bold;">Writers Note: ...</p>`) — never as a hidden HTML comment, and never as plain student-facing content.
- **Tables** are markdown tables. The header separator row (`| --- | --- |`) is structural — ignore it. Each remaining `| … | … |` line is a table row; the `|` delimiters are the column separators (equivalent to `║`).
- All other format conventions (formatting markers `**bold**`/`*italic*`/`__underline__`, hyperlinks, bullet lists, special characters, content integrity) are the same as for PageForge — see "Format Conventions" above.

### Constraint

Trust the raw `.docx` content as-is, exactly as you would trust PageForge output. Do NOT reword, "improve", or re-order writer text. The ONLY difference from the PageForge pathway is the front-matter skipping and the bare-tag / markdown-table formatting.

---

## Media List Companion Document

> **When to load:** Whenever a Media List `.docx` is supplied alongside the content source.

The user **may optionally upload a Media List `.docx`** in addition to the content source. It is a *separate companion document* to the Writers Template and is **optional** — conversions proceed normally without it.

### What It Is

A Media List is a single Word table cataloguing **every external media item** used in the module. Its columns are:

| Column | Meaning |
|---|---|
| **Item No.** | Sequential item identifier (often blank except for the example row) |
| **WTPg No.** | The page number in the Writers Template `.docx` where the item appears |
| **Item Type** | `photo`, `image`, or `video` |
| **Description** | A short human-readable description (e.g., "Fun unicorn 3d", "Magnifying glass over AI") |
| **Source** | The provider — e.g. `iStock`, `youtube`, `Getty Images` |
| **URL** | The direct source URL (iStock page URL, YouTube watch URL, etc.) |
| **ECR approval** | Early copyright review status (usually blank — administrative) |

The first row is always an **example row** ("Example | 5 | Photo | Stock photo of a cheetah…") — skip it. The table may also contain reminder/instruction rows (e.g., "Reminder: List all external platforms…") spanning the row — skip these too.

### How To Use It

The Media List does **NOT** supply student content and does **NOT** affect page boundaries. It is a *reference aid* for media. When a Media List is provided:

1. **Verify media links.** Cross-check every `[image]` / `[video]` URL in the content source against the Media List. The Media List is the authoritative catalogue of external media — use it to confirm you have captured every media reference and to catch any the content source omitted or mangled.
2. **Source accurate media data.** Use the `Description`, `Source`, `URL`, and `WTPg No.` columns to attribute each item. Note: for acknowledgements the `Description` column is a *writer-descriptive label*, **not** the final entry title — the acks entry uses the asset's **published title, exactly as published** — casing, punctuation, and any trailing ". stock photo" suffix included when it is part of the official platform title (constraint 66; a URL-slug derivation is only an approximation — the slug loses casing, punctuation, and the suffix — so where the official title is available from the iStock acknowledgements file or the asset page, it wins verbatim; for stock photos / illustrations the slug remains the usual fallback recovery route) and, for stories / journals, a full byline (`words by …`, `illustrations by …`, series name) sourced from the cited source page. **Video titles are NOT taken from the Media List.** A video's acks title is always the video's **full published title**; the Media List label for a video is routinely abbreviated, inaccurate, or invented from the writer's own description of the video's subject, so it is used only to identify *which* video is meant, never as title text. Where the two differ, the published title wins; if it cannot be confirmed, raise a VISIBLE red flag rather than falling back to the Media List label. **If a separate iStock acknowledgements file is also supplied (see below), its API-sourced iStock entries are authoritative and used verbatim — they take precedence over URL-slug title derivation for those items.** See `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` → Entry format for the exact patterns.
3. **Build the acknowledgements.** The Media List is the primary *inventory* for the acknowledgements block — it tells you every item, its page (`WTPg No.`), provider, ID, and URL — but the entry wording follows the Entry format and URL-wrapping rules in `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` (Acknowledgements), not a verbatim copy of the `Description` column.

### When No Media List Is Supplied

Proceed normally. Extract media references directly from the `[image]` / `[video]` tags in the content source. Where a video title or image description is not available from the content source, use a placeholder title and raise a VISIBLE red flag (`<p style="color: red; font-weight: bold;">Red Flag: ...</p>`) for the developer to complete — not a hidden HTML comment. (A missing title/description the Convertor detects takes the `Red Flag:` prefix — see `02_DATA_CONTENT_VERIFICATION.md` → Source-Specific Red-Note Prefixes.)

### Constraint

The Media List is a verification/attribution aid only. Never treat Media List rows as student-facing content, and never let the Media List override the content source's own structure or page boundaries.


## iStock Acknowledgements File

> **When to load:** Whenever a developer pastes or uploads a list of iStock/Getty acknowledgement lines alongside (or during) a module build.

Separately from the Media List, a developer **may optionally supply a short list of iStock acknowledgement lines** — typically a `.txt` containing one `<p>…</p>` per iStock image, in the exact form the acks block uses:

```html
<p>Photo: Confident boy sitting on bicycle in the forest, iStock 1366211873, Getty Images. Used with permission.</p>
<p>Photo: Zugspitze ski resort, iStock 537208613, Getty Images. Used with permission.</p>
<p>Photo: Tranquil morning, Lake Wanaka, New Zealand, iStock 1687649052, Getty Images. Used with permission.</p>
```

### What It Is

This list is pulled **directly from the iStock / Getty API**, so it is **perfectly accurate** — the published title, the iStock ID, the provider, and the permission string are all correct as written. It is the authoritative record for the iStock items it covers.

### How To Use It

When an iStock acknowledgements file is supplied, it becomes the **single source of truth** for those iStock items, in two places:

1. **Acknowledgements block (verbatim).** When assembling the acks block in lesson order (`05_COMP_LANGUAGE_MEDIA_LAYOUT.md` → Acknowledgements), and the point is reached to credit an iStock image, **insert the matching line from this list exactly as it appears** — do not re-derive the title from the URL slug, do not reword, do not reformat. Match each line to its image by iStock ID (and/or the descriptive name). Matching "by iStock ID" means the **`gm`-leading (first) number** in the asset URL — the same number as the asset page's **"Stock photo ID"** and the `images/iStock-{ID}.jpg` filename — **never** the trailing segment of a dual-ID URL (`gm{A}-{B}` → match on `A`; constraint 61). A trailing-segment lookup will falsely report "no matching line" and trigger a spurious red flag. Place the line under the `acksLesson` div for the page on which that image is used.
2. **Image `alt` text (preferred name).** The descriptive **image name** in each line — the text between `Photo:` and the `, iStock [ID]` (e.g. *"Confident boy sitting on bicycle in the forest"*) — is the **preferred `alt` value** for that iStock image (see the Images → alt text rules below).

### Notes

- It supplies **no student content** and does **not** change page boundaries — exactly like the Media List.
- It covers **iStock items only**. Non-iStock acknowledgements (Shutterstock, Ministry of Education stories/journals, videos, etc.) still follow the normal sourcing rules in `05_COMP_LANGUAGE_MEDIA_LAYOUT.md`.
- If a referenced iStock image has **no** matching line in the supplied list, fall back to the normal sourcing route (URL-slug title / Media List) and raise a VISIBLE red flag for the developer to confirm — never invent an entry.
- If no iStock acknowledgements file is supplied at all, proceed normally.

### Constraint

The iStock acknowledgements file is an authoritative attribution/alt-text aid only. Never treat its lines as student-facing content, and never let it change page boundaries or the content source's structure.



