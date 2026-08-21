> **Last updated:** Friday, 21st August, 2026 6:30 PM
> **Granular part D (4 of 5) of `01_PIPELINE_EXTRACTION_TAGS.md`** — Page boundary system; tag taxonomy & normalisation.
> All sibling parts live in `01_PIPELINE_EXTRACTION_TAGS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# 03 — Page Boundary System

> **When to load:** During Phase 3, after reading the content source and before assigning content to pages.

---

## Standard Page Structure

```
[TITLE BAR] → overview → [MODULE INTRODUCTION] → intro content → [End page]
↓ produces -00 page

[LESSON n] → [Lesson Overview] → [Lesson content] → body → [End page]
↓ produces -01 page

[LESSON n+1] → [Lesson Overview] → [Lesson content] → body → [End page]
↓ produces -02 page
```

---

## Page Boundary Validation Rules

Apply ALL four rules BEFORE assigning content to pages.

### Rule 1 — Pre-MODULE-INTRODUCTION End Page → DISREGARD

**Pattern:** `[End page]` between `[TITLE BAR]` and `[MODULE INTRODUCTION]`.
**Observed in:** ALL five OSAI modules. Universal convention.
**Action:** DISREGARD. Title bar + module introduction combine into single -00 page.

```
IF [End page] encountered
AND [MODULE INTRODUCTION] NOT yet seen
THEN disregard — false boundary
```

### Rule 2 — Missing End Page Between Lessons → INSERT

**Pattern:** `[LESSON n]` appears without preceding `[End page]` since previous lesson.
**Observed in:** OSAI501 (LESSON 3 → LESSON 4 with no boundary).
**Action:** INSERT implicit boundary before new `[LESSON n]`.

```
IF [LESSON n] encountered
AND no [End page] since previous [LESSON] or [Lesson content]
THEN insert implicit boundary before this [LESSON n]
```

### Rule 3 — Empty Lesson Segment → DISREGARD End Page

**Pattern:** Segment has `[LESSON]` but NO body tags AND NO `[Lesson content]`.
**Action:** DISREGARD closing `[End page]` — extend previous page.

```
IF segment contains [LESSON]
AND contains NO body/Body/Body text tags
AND contains NO [Lesson content]
THEN [End page] is misplaced — disregard
```

### Rule 4 — Orphaned Title Bar → MERGE

**Pattern:** Segment contains ONLY `[TITLE BAR]` + headings + `[End page]`, no body content.
**Action:** MERGE with following segment.

```
IF segment contains [TITLE BAR]
AND contains NO [MODULE INTRODUCTION]
AND contains NO body content
THEN merge with following segment
```

---

## Page-to-File Mapping

After applying all rules:

| Content Segment | Output File |
|---|---|
| `[TITLE BAR]` + overview + `[MODULE INTRODUCTION]` + intro | `MODULE_CODE-00.html` |
| First `[LESSON]` through `[End page]` | `MODULE_CODE-01.html` |
| Second `[LESSON]` through `[End page]` | `MODULE_CODE-02.html` |
| Each subsequent lesson | `-03.html`, `-04.html`, etc. |

---

## Lesson Numbering

- `[LESSON]` (unnumbered) → sequential numbers by order of appearance
- `[LESSON 1]` → -01, `[LESSON 2]` → -02
- Mixed: unnumbered get sequential, explicit numbers preserved
- Example: `[LESSON]`, `[LESSON]`, `[LESSON]`, `[LESSON 4]` → -01, -02, -03, -04

**When converting, clearly identify which page you are producing.** If user sends complete template, ask whether they want all pages or specific ones.

---

## Multi-Page vs Single-Page Modules (and when to offer Split Mode)

The Page Boundary System above produces **genuinely separate lesson pages** (`-00`, `-01`, `-02`, …) and applies to **multi-page** modules — those delimited by `[LESSON]` / `[End page]` boundaries.

Some modules are instead **single-page**: the whole module lives in one `#body`, and each lesson is delimited only by its own `<!-- 1 -->`, `<!-- 2 -->`, … HTML comment (a structural delimiter, not a page break). A module is single-page when:

- it has **no** `[LESSON]` / `[End page]` page boundaries, **or**
- it is a module type that **ships as one page**.

**Identify page structure during this phase and act on it:**

1. **Multi-page** (boundaries present) → produce the separate `-00`/`-01`/… files exactly as the Page Boundary System describes. (Split Mode is **not** used.)
2. **Single-page** (no boundaries, or a one-page module type) → **say so to the user**, and **proactively offer Split Mode** in one line: *"This is a single-page module. If it's too long to build in one go, you can run `SPLIT MODE` and stitch it back together in PageForge"* (Split Mode emits the page in stitchable pieces that PageForge's Page Stitcher recombines into one file). Make the offer **more prominent** when the single-page output is **large** (many lessons / heavy interactive content) and so at real risk of exceeding one response.

The offer is an **offer, not an automatic action.** Split Mode runs **only** when the user explicitly invokes `SPLIT MODE`. If the user does nothing, continue producing the normal single-page file in one pass.

> **Split Mode ≠ the Page Boundary System.** Split Mode targets modules meant to be **one page** but too long to emit at once; it produces a base homepage + per-lesson section files that PageForge stitches back into a **single** page (byte-identical to a one-pass build). The Page Boundary System produces **separate** lesson pages for genuinely multi-page modules. **Never conflate the two**: a multi-page module is never split; a single-page module is never broken into separate `-NN` pages. Full Split Mode rules — the `SPLIT MODE` trigger, the base/section output contract, the exact `PAGEFORGE-SPLICE` / `PAGEFORGE-SECTION` marker tokens, the round-trip guarantee, and validation — live in **`13_SPLIT_MODE.md`**.



# 04 — Tag Taxonomy & Normalisation Rules

> **When to load:** During Phase 4, when processing the PageForge text content.

---

## Normalisation Algorithm

```
1. Strip red text markers: 🔴[RED TEXT] ... [/RED TEXT]🔴 → extract inner content
2. Identify square-bracket tags within extracted content
3. Trim whitespace from both ends of tag content
4. Compare case-insensitively against normalisation table
5. Extract trailing number or letter-number ID (e.g., "1A", "3", "5C")
6. Map to normalised form + extracted sub-identifier
```

---

## Complete Normalisation Table

### Page Structure Tags
| Writer Variants (case-insensitive) | Normalised Form |
|---|---|
| `title bar` | `title_bar` |
| `module introduction` | `module_introduction` |
| `lesson`, `lesson N` | `lesson` + number |
| `lesson overview` | `lesson_overview` |
| `lesson content` | `lesson_content` |
| `end page` | `end_page` |

### Heading & Body Tags
| Writer Variants | Normalised |
|---|---|
| `h1`–`h5` | `heading` + level |
| `body`, `body text` | `body` |

### Content Styling Tags
| Writer Variants | Normalised |
|---|---|
| `alert` | `alert` |
| `important` | `important` |
| `alert-wananga`, `alert wananga` | `alert_cultural_wananga` |
| `alert-talanoa`, `alert talanoa` | `alert_cultural_talanoa` |
| `alert-combined`, `alert combined` | `alert_cultural_combined` |
| `whakatauki` | `whakatauki` |
| `quote` | `quote` |
| `rhetorical question` | `rhetorical_question` |
| `full page translate`, `reo translate` | `reo_translate` |

### Media Tags
| Writer Variants | Normalised |
|---|---|
| `image`, `image N` | `image` |
| `video` | `video` |
| `audio` | `audio` |
| `audio image`, `audioimage`, `audioImage` | `audio_image` |
| `image zoom` | `image_zoom` |
| `image label` | `image_label` |
| `AI use guidelines traffic light PDF` | `ai_guidelines_pdf` + `traffic_light` |
| `Ākonga`/`Akonga` `AI use guide years 1-6`/`7-10`/`11-13 and NCEA` + `PDF` | `ai_guidelines_pdf` + akonga variant |
| `Kaimahi AI use guidelines years 1-6`/`7-10` + `PDF` | `ai_guidelines_pdf` + kaimahi variant |
| `Kaimahi AI guidelines - authenticity guidelines for years 11-13 and NCEA PDF` | `ai_guidelines_pdf` + `authenticity` |
| `Kaimahi AI guidelines - responding to suspected use in assessments for years 11-13 and NCEA PDF` | `ai_guidelines_pdf` + `responding` |

> **The eight `ai_guidelines_pdf` tags normalise tolerantly but emit exactly.** Match is case-insensitive, a hyphen / en dash / em dash in the year range are the **same** tag, and `Akonga` without the macron is accepted. The **emitted filename is always the exact supplied string** (en dash, macron, spaced hyphen and all) from the registry table in `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` → AI Guidelines PDFs. Constraint 84.

### Activity Tags
| Writer Variants | Normalised |
|---|---|
| `activity NA`, `activity` | `activity` + ID |
| `activity heading`, `activity title`, `heading` (in activity context) | `activity_heading` |
| `end activity`, `end of activity` | `end_activity` |

### Link/Button Tags
| Writer Variants | Normalised |
|---|---|
| `button` | `button` |
| `external link button` | `external_link_button` |
| `external link` | `external_link` (rendered as an inline anchor **or** an `externalButton` — the choice is **positional**, see constraint 75) |
| `engagement quiz button` | `engagement_quiz_button` |
| `MTKquiz`, `MTK quiz` | `mtk_quiz` |
| `supervisor note`, `supervisor button`, `supervisor` | `supervisor_button` |
| `modal button` | `modal_button` |
| `audio button` | `audio_button` |

### Interactive Component Tags
| Writer Variants | Normalised |
|---|---|
| `drag and drop` + variants | `drag_and_drop` |
| `dropdown`, `drop down`, `dropdown N` | `dropdown` |
| `dropdown quiz paragraph`, `drop down paragraph quiz`, `dropquiz`, `multi choice dropdown quiz paragraph` | `dropdown_quiz_paragraph` |
| `flip cards`, `flip card`, `flip card N`, `flip card image` | `flip_card` |
| `accordion`, `accordion N` | `accordion` |
| `end accordions` | `end_accordions` |
| `click drop`, `clickdrop`, `drop click`, `click drop N` | `click_drop` |
| `carousel`, `slide show` | `carousel` |
| `rotating banner` | `rotating_banner` |
| `slide N` | `carousel_slide` |
| `tabs` | `tabs` |
| `tab N` | `tab` |
| `speech bubble` + any suffix | `speech_bubble` |
| `hint slider`, `hint slider N` | `hint_slider` |
| `hint` | `hint` |
| `shape hover`, `shape hover with image` | `shape_hover` |
| `shape N` | `shape` |
| `reorder` | `reorder` |
| `slider chart` | `slider_chart` |
| `slider` | `slider` |
| `memory game` | `memory_game` |
| `word drag` | `word_drag` |
| `typing self-check`, `typing quiz` | `typing_quiz` |
| `self check`, `self-check` | `self_check` |
| `word highlighter`, `word select` | `word_select` |
| `mcq`, `multi choice quiz`, `multichoice quiz`, `multi choice` | `mcq` |
| `multi choice quiz survey`, `multichoice quiz survey` | `multichoice_quiz_survey` |
| `radio quiz`, `true false` | `radio_quiz` |
| `checklist` | `checklist` |
| `info trigger` + optional text | `info_trigger` |
| `info trigger image`, `info trigger] image`, `info trigger image]`, `infotrigger image`, `info trigger] [image` | `info_trigger_image` |
| `info audio trigger`, `audio trigger`, `audio triggers` | `audio_trigger` |
| `venn diagram` | `venn_diagram` |
| `timeline` | `timeline` |
| `self reflection`, `self-reflection` | `self_reflection` |
| `reflection slider` | `reflection_slider` |
| `stop watch`, `stopwatch` | `stop_watch` |
| `number line` | `number_line` |
| `crossword` | `crossword` |
| `word find`, `wordfind` | `word_find` |
| `bingo` | `bingo` |
| `clicking order` | `clicking_order` |
| `puzzle` | `puzzle` |
| `sketcher` | `sketcher` |
| `glossary` | `glossary` |
| `word highlighter` (standalone) | `word_highlighter` |
| `translate`, `translate section` | `translate_section` |
| `kanji cards`, `language letter` | `kanji_cards` |
| `embed pdf` | `embed_pdf` |
| `embed padlet` | `embed_padlet` |
| `embed desmos`, `desmos graph` | `embed_desmos` |

**⚠️ INFO TRIGGER IMAGE — Special Parsing Note:** Writers sometimes split this tag across bracket boundaries or use inconsistent spacing. The tag may appear as `[info trigger image]`, `[info trigger] image`, `[info trigger] [image]`, or other split variations. When the normaliser encounters `info trigger` followed immediately by `image` (whether inside the same brackets or as a separate adjacent tag/word), normalise to `info_trigger_image`. Do NOT confuse with standalone `[info trigger]` (which is an inline tooltip) or standalone `[image]` (which is a media tag).

**⚠️ WJ SERIES — `[MTK Quiz]` precedence:** in WJ-series modules an activity tagged both `[MTK Quiz]` and an in-page quiz tag (`[Multichoice quiz]`, `[Radio quiz]`, etc.) maps to the MTK quiz shell (`05` → Buttons → MTK Quiz), not to the in-page quiz component — and the question/answer content is not rendered. See constraint 65.

**⚠️ WJFUN SERIES — `[word highlighter]`:** in WJFUN modules a `[word highlighter]` is NOT built with the `wordHighlighter` / `highlightBtn` interactive component — it emits the static highlight spans documented at `04_COMP_SEGMENTS_OVERLAYS.md` → Word Highlighter (WJFUN series). A documented, WJFUN-scoped exception to constraint 2. See CL-0066.

### Structural Sub-tags
| Writer Variants | Normalised |
|---|---|
| `front` | `front` |
| `back` | `back` |
| `static heading` | `static_heading` |
| `static column` | `static_column` |
| `unsorted list`, `unordered list` | `unordered_list` |
| `table`, `table N`, `table wordselect` | `table` |

---

## Red Text Handling

Content flagged as `🔴[RED TEXT]...[/RED TEXT]🔴` is a **writer instruction to CS/developer** (or, when author-prefixed, a **captured reviewer comment** — see below). NOT student-facing.

**Rules:**
- Strip all red text markup from output
- Parse red text for embedded tags — if ONLY a tag + whitespace, extract and process the tag
- If substantive instructions, render as a VISIBLE red flag (`<p style="color: red; font-weight: bold;">Writers Note: ...</p>`) for CS — NOT a hidden HTML comment (writer's own instruction → `Writers Note:` prefix; see `02_DATA_CONTENT_VERIFICATION.md` → Source-Specific Red-Note Prefixes and Comment & Red Flag Policy)
- **Captured reviewer comment** (the red-text note begins with a `Note from {author}:` lead, where `{author}` is one of the six whitelisted reviewers — **Kate Scanlon, Nadia Stanton, Caroline Schwer, Simon Vita, Amanda Griffiths, Creative Services**): render as a VISIBLE red **designer message** preserving the lead + text verbatim and in position — `<p style="color: red; font-weight: bold;">Note from {author}: {verbatim text}</p>` — never paraphrased, never dropped, never a hidden comment, and never tag-parsed. PageForge supplies the `Note from {author}:` lead itself; emit it exactly as given (do not reword it, drop the author, or substitute any other prefix). The `Note from {author}:` lead is the only thing distinguishing it from a writer's own red-font instruction (which renders `Writers Note: …`). See **Captured Reviewer Comments** under Format Conventions above (full rules), `02_DATA_CONTENT_VERIFICATION.md` → Comment & Red Flag Policy, and `00` constraint 57.
- **Supervisor prose lead-in (carve-out):** a red-text line whose case-folded lead matches `^supervisor('s)?( note[s]?)?\s*:` (e.g. `Supervisor:`, `Supervisor's Notes:`, `Supervisors notes:`) is a **supervisor-button trigger**, not a `Writers Note:` — writers frequently type the supervisor note as red text after an `[Activity]` instead of bracketing a tag. Build the supervisor component (constraint 68; see `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` → Supervisor Button) with the note text passed through verbatim inside the reveal panel
- **Never render red text as visible student content**
- Whitespace-only red text blocks (e.g., `🔴[RED TEXT]   [/RED TEXT]🔴`) → disregard entirely

---

## Writer Intent Interpretation (Ambiguous Requests)

Writers sometimes describe what they want using informal language, keyword hints, or non-standard terminology in CS instructions (red text) rather than using exact component tag names. When a writer's request doesn't match an exact tag but contains recognisable keywords or describes a specific interactive pattern, use this guide to interpret their intent.

### Interpretation Methodology

1. **Extract keywords** from the writer's request (including CS red text instructions)
2. **Match keywords** against the keyword-to-component mapping below
3. **Examine the associated content** (tables, lists, statement structures) for additional signals
4. **Cross-reference** the content pattern with the component's documented data patterns (section 06 in `02_DATA_CONTENT_VERIFICATION.md`)
5. If confident in the match, implement the component. If uncertain, **RED FLAG** with the best interpretation + visible fallback.

### Keyword-to-Component Mapping

| Writer Keywords / Phrases | Likely Component | Content Signals |
|---|---|---|
| `tick box`, `tickbox`, `tick boxes`, `checkbox`, `check box`, `check boxes` | `multiChoiceQuiz` (survey variant) — see COMP_02 in `03_COMP_CORE_INTERACTIVES.md` | Self-assessment statements with rating columns (e.g., "Always / Sometimes / Not yet"); "I can..." or "I do..." statements |
| `columns where students can click`, `click what column they're in`, `select which level` | `multiChoiceQuiz` (survey variant) | Rating/frequency columns paired with statement rows |
| `rate yourself`, `self-rating`, `self-assessment checklist`, `reflection checklist` | `multiChoiceQuiz` (survey variant) OR `slider` | Statements with rating scales; if discrete categories → multiChoiceQuiz; if continuous scale → slider |
| `matching`, `match the pairs`, `match up` | `dragAndDrop` (standard layout) | Two-column table with items to pair |
| `sort`, `sorting`, `categorise`, `put into groups` | `dragAndDrop` (column layout) | Items with category headings |
| `fill in the blank`, `fill in the gap`, `cloze` | `dragAndDrop` (FIB layout) OR `typingQuiz` | Sentences with blanks; if word bank provided → D&D FIB; if free-text → typingQuiz |
| `slider`, `scale`, `rate on a scale` | `slider` | Continuous scale with endpoints |
| `true or false`, `true/false` | `radioQuiz` | Statements to mark true or false |
| `choose the correct answer`, `select the right one` | `mcq` (standard) | Questions with discrete answer options |
| `reveal`, `click to show`, `click to reveal` | `clickDrop` | Front/back content pairs |
| `flip`, `flip over`, `turn over` | `flipCard` | Front/back content pairs with visual emphasis |
| `slide show`, `slides` | `carousel` | Numbered slide content |
| `scrolling marquee`, `scrolling banner`, `marquee of images`, `scrolling images`, `image marquee`, `banner of images` | `rotateBanner` | Writer describes a scrolling/sliding display of images — implement as `rotateBanner` with placeholder images if no files provided. NEVER hide such requests as comments only — always create the component with visible content. See COMP_07 in `04_COMP_SEGMENTS_OVERLAYS.md` |
| `popup`, `pop up`, `hover over` | `infoTrigger` or `hint` | Terms with definitions/explanations |

### Example: Interpreting "tick boxes"

**Writer instruction (red text):**
```
🔴[RED TEXT] CS, please create three columns where ākonga can click what column they're in for each of the statements – tick boxes? [/RED TEXT]🔴
```

**Associated content:** A table with self-assessment statements ("I take turns and let others have a go") and rating column headers ("Always", "Sometimes", "Not yet").

**Interpretation process:**
1. Keywords: "tick boxes", "columns where ākonga can click", "what column they're in"
2. Keyword match → `multiChoiceQuiz` (survey variant)
3. Content confirms: self-assessment statements + discrete rating categories
4. **Implement as:** `<div class="multiChoiceQuiz autoCheck emptyOptions checkAll" columns="column-4">` with the documented structure from COMP_02

**⚠️ Do NOT implement as:** a plain HTML `<table>` (not interactive), a standard MCQ (wrong structure), or a radio quiz (wrong layout).

---

## Document Parsing: What to IGNORE

- Metadata block (everything before `--- CONTENT START ---`)
- Document header ("MTK WRITERS TEMPLATE" title) — if present
- Submission Checklist
- To-do notes / internal comments
- LOT tags table
- Sign-off line
- Contents page
- Section A — Merging Resources
- "Understanding which sections to complete" block
- Writer's guidance box
- "For text" / "For media" red instruction blocks

## What to CONVERT

Only content from the first `[TITLE BAR]` tag onward.



