> **Last updated:** Thursday, 13th August, 2026
> **Granular part B (2 of 5) of `02_DATA_CONTENT_VERIFICATION.md`** — Content rules: preservation, grids, merging, perspective, red text, headings.
> All sibling parts live in `02_DATA_CONTENT_VERIFICATION/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# 07 — Content Rules
 
> **When to load:** During Phase 6, when producing HTML output.
 
---
 
## Content Preservation Rules
 
### Writer Error vs Extraction Artefact
 
**Writer Errors** (spelling, grammar, punctuation) → **Preserve VERBATIM**. Do not correct, flag, or change.
 
**PageForge Text Content** → **Trust the file output as-is.** PageForge has already handled tracked-change resolution (deletions removed, insertions kept), SDT unwrapping, and formatting extraction. The text in the PageForge file represents the writer's final intended content.
 
**Genuine Artefacts** (truly corrupt text that is clearly nonsensical) → Extremely rare with PageForge output. If encountered, RED FLAG and preserve visible content with best-guess reconstruction.
 
### General Preservation
 
- Do not rephrase or reword anything
- Do not change punctuation (including en-dash vs em-dash)
- Preserve macronised characters: ā, ē, ī, ō, ū, Ā, Ē, Ī, Ō, Ū
- Preserve bold → `<b>` or `<strong>`, italic → `<i>` or `<em>`, bold italic → `<b><i>`
- **Preserve bold/italic from within table cells**, not just body paragraphs
- Labels functioning as sub-headings (e.g., "What it does:", "Example:") retain bold formatting
---
 
## Grid Structure Rules
 
ALL content inside `<div id="body">` must be inside Bootstrap grid:
 
```html
<div class="row"><div class="col-...">content</div></div>
```
 
### Default Column Width Rule
 
**⚠️ CRITICAL:** The default column class for the DIRECT CHILD div of any `.row` element is `col-md-8 col-12`. This applies to standard content blocks, activity/interactive containers, and all new content rows.
 
**IMPORTANT:** Apply `col-md-8` ONLY to the FIRST and ONLY direct child `<div>` of the `.row` element. Do NOT apply `col-md-8` to any grandchildren or deeper descendants within the row.
 
**A `col-md-8` never sits directly inside another `col-md-8`.** An inner `row` placed inside a `col-md-8 col-12` column must not use a `col-8`-family class (`col-md-8`, `col-8`) for its own column(s) — use `col-md-12 col-12` (or a documented inner pattern such as the `col-md-6` pair). Both directions of mixed nesting are fine: a `col-md-8` inside a `col-md-12`, and a `col-md-12` inside a `col-md-8`. This applies inside activities too: an `.activity` whose outer wrapper is `col-md-8 col-12` keeps its inner columns at `col-12`; an activity that genuinely needs an inner `col-8` takes a `col-md-12 col-12` outer wrapper instead. (Design-authority instruction, 29 July 2026.)
 
```html
<!-- CORRECT: col-md-8 on direct child of .row only -->
<div class="row">
    <div class="col-md-8 col-12">
        <p>Content here</p>
        <div class="someComponent">
            <!-- No col-md-8 on inner elements -->
        </div>
    </div>
</div>
 
<!-- WRONG: col-12 only — content spans full width -->
<div class="row">
    <div class="col-12">
        <p>This is too wide.</p>
    </div>
</div>
```
 
### Column Class Reference
 
| Use Case | Column Classes |
|---|---|
| Standard content (DEFAULT) | `col-md-8 col-12` |
| Content + sidebar image (inner row) | Outer: `col-md-8 col-12` containing inner `row` with `col-md-6 offset-md-0 col-12 paddingR` + `col-md-6 offset-md-0 col-12 paddingL` |
| Content + sidebar alert | `col-md-8 col-12` + `col-md-4 offset-md-0 col-6 offset-3` |
| Two equal images | `col-md-4 col-6 paddingR` + `col-md-4 col-6 paddingL` |
| Standard text + image side-by-side | Text: `col-md-8 col-12` (LEFT) + Image: `col-md-4 col-12` (RIGHT) — text always left, image always right (except speech bubbles) |
| Info trigger image (needs full width for trigger positioning) | `col-md-12 col-12` |
| Drag & Drop column layout (`layout="column"`) | `col-md-12 col-12` — needs wider container for multiple drop columns + drag items |
| Drag & Drop column with many images (`images` class, 6+ items) | `col-12` (Standard) / `col-md-11 col-12` (Inquiry & Fundamentals) — never `col-md-10` (see constraint 56) |
| Interactive activity + alertImage pairing | Activity: `col-md-8 col-12` (outer container); alertImage: `col-md-4 offset-md-0 col-12` (nested inside, 8 + 4 = 12) — applies in every module type, overriding the sub-type default |
| Carousel — image (`.viewer` column) | `col-md-12 col-12` when nested inside a `col-md-8` wrapper; `col-md-8 col-12` standalone (`col-md-12` permitted for large/book-page content) — see constraint 17 |
| Carousel — video (`.viewer` column) | `col-md-12 col-12` when nested inside a `col-md-8` wrapper; `col-md-8 col-12` standalone (`col-md-12` permitted for large/book-page content) — see constraint 17; `<h5>` titles + description above video |
| Carousel — external nav buttons (`.viewer` column) | `col-md-12 col-12` when nested inside a `col-md-8` wrapper; `col-md-8 col-12` standalone (`col-md-12` permitted for large/book-page content) — see constraint 17; external `carousel-btns` provide navigation |
 
### Interactive Wrapper Width — Fit-Based Principle
 
The outer activity / interactive wrapper defaults to `col-md-8 col-12`. **Widen it ONLY when the interactive's content does not fit comfortably in a `col-8` — never as a fixed per-component lookup.** There is no "this component always uses col-X" table; the width follows the content's horizontal needs:
 
- **`col-md-8 col-12` (default):** prose-and-image activities, MCQs, dropdown quizzes, and any interactive whose content sits comfortably in the standard content width.
- **`col-12` (Standard) or `col-md-11 col-12` (Inquiry & Fundamentals) (widen as needed):** activity/interactive wrappers that need more horizontal room than `col-md-8` — e.g. a wordSelect with an options column beside a text column, a typing quiz with side-by-side image + sentence rows, a vocabulary clickDrop strip of several side-by-side images, or a memory-game grid — use `col-12` in Standard modules and `col-md-11 col-12` in Inquiry/Fundamentals modules. Activity wrappers **never** use `col-md-10` (see constraint 56). **WJ-series exception (CL-0065):** WJ modules never use `col-md-11 col-12` — a WJ wrapper that outgrows `col-md-8` widens straight to `col-md-12 col-12`.
- **`col-md-12 col-12` (full width):** reserved for activities that are simply **too large to fit a `col-8`** — e.g. a Drag & Drop `layout="column"` with multiple drop columns plus a drag bank. Use full width only when narrower wrappers would crowd or clip the content.
The specific entries in the table above (D&D column → `col-md-12`, activity + alertImage → `col-md-8` with the image at `col-md-4`, carousel viewer → contextual (`col-md-12` nested / `col-md-8` standalone), etc.) are concrete instances of this same fit-based principle, not exceptions to it. When in doubt, start at `col-md-8` and step up only if the component genuinely needs the room.

> **Activity/interactive wrappers never use `col-md-10`.** A wide interactive that needs more than `col-md-8` uses `col-12` (Standard) or `col-md-11 col-12` (Inquiry & Fundamentals); an activity paired with an `alertImage` uses `col-md-8 col-12` with the image at `col-md-4`. `col-md-10` is no longer an activity width. Plain content **sectioning** uses `col-md-8 col-12` (standard) or `col-12` / `col-md-12 col-12` (full width); a plain, non-activity *narrowed* content block may still use `col-md-10` (it is outside this rule). This is forward-only — existing `col-md-10` activity wrappers are pre-rule and not retro-flagged. See constraint 56.

**The inner text column is `col-12`, and the row split depends on the wrapper's width (constraint 63).** An activity's plain text content — headings, instructions, paragraphs, lists — sits in a **`col-12`** inner column, **never** `col-md-8 col-12`: the wrapper already sets the reading width, so an inner `col-md-8` narrows the prose twice. Whether the interactive shares that column or gets its own row is then decided by the wrapper:

- **DEFAULT wrapper (`col-md-8 col-12`) — ONE inner row.** Heading, instructions and the interactive sit together in a single `<div class="row"><div class="col-12">…</div></div>`. Nothing is split, because there is no width difference to express.
- **WIDENED wrapper (`col-12` Standard / `col-md-11 col-12` Inquiry & Fundamentals / `col-md-12 col-12` full width — constraint 56) — TWO inner rows.** The text sits in its own `row` > `col-12`, and the interactive follows in a **separate** `row` at the wrapper's own width.

A **text-only** activity (no interactive) needs no split at either width. Patterns:

```html
<!-- DEFAULT wrapper — one shared inner row -->
<div class="activity interactive" number="2B">
    <div class="row">
        <div class="col-12">
            <h3>Activity heading</h3>
            <p>Instructions</p>
            <!-- interactive component here, in the same column -->
        </div>
    </div>
</div>

<!-- WIDENED wrapper — the split is retained -->
<div class="row">
    <div class="col-12"><!-- widened activity wrapper (Standard) -->
        <div class="activity interactive" number="3C">
            <div class="row">
                <div class="col-12">
                    <h3>Activity heading</h3>
                    <p>Instructions</p>
                </div>
            </div>
            <div class="row">
                <div class="col-12"><!-- interactive spans the widened width -->
                    <!-- wide interactive component here -->
                </div>
            </div>
        </div>
    </div>
</div>
```
 
**Content + Sidebar Image — Inner Row Pattern:** When body text and an image need to appear side-by-side within the content area, maintain the `col-md-8 col-12` outer wrapper and create an inner `<div class="row">` with two columns inside it. Do NOT break the outer `col-md-8` default for text+image layouts within body content.
 
**⚠️ CRITICAL — Text/Image Side-by-Side Ordering:** When standard body text appears alongside a standard image (e.g., from a writer's table with an image in one column and text in another), the text ALWAYS goes on the LEFT and the image ALWAYS goes on the RIGHT:
 
```html
<div class="row">
    <div class="col-md-8 col-12">
        <p>Text content goes on the left (8 columns wide)</p>
    </div>
    <div class="col-md-4 col-12">
        <img class="img-fluid" loading="lazy" src="images/image.jpg" alt="">
    </div>
</div>
```
 
This applies regardless of the order in which the writer's template presents the image and text (e.g., even if the writer's table shows the image in the left column and text in the right column, the HTML output should place text on the left and image on the right). **The only exception** to this rule is when using the `speechBubble` design pattern, which has its own documented layout structure — see COMP_09 in `04_COMP_SEGMENTS_OVERLAYS.md`.
 
When text and image are WITHIN the standard `col-md-8` content area (inner row pattern):
 
```html
<!-- CORRECT: Inner row within col-md-8 outer wrapper -->
<div class="row">
    <div class="col-md-8 col-12">
        <div class="row">
            <div class="col-md-6 offset-md-0 col-12 paddingR">
                <p>Body text here</p>
            </div>
            <div class="col-md-6 offset-md-0 col-12 paddingL">
                <img class="img-fluid" loading="lazy" src="images/image.jpg" alt="">
            </div>
        </div>
    </div>
</div>
 
<!-- WRONG: Breaking outer col-md-8 default -->
<div class="row">
    <div class="col-md-8 col-12 paddingR">
        <p>Body text here</p>
    </div>
    <div class="col-md-4 col-12 paddingL">
        <img class="img-fluid" loading="lazy" src="images/image.jpg" alt="">
    </div>
</div>
```
 
**Activity and interactive divs** MUST be inside `<div class="row"><div class="col-md-8 col-12">`, EXCEPT for wide interactive components (D&D column layout) which use `col-md-12 col-12`, and a D&D column with many images which uses `col-12` / `col-md-11 col-12` by module type (never `col-md-10`). Activity wrappers never use `col-md-10` — where more width than `col-md-8` is needed use `col-12` (Standard) / `col-md-11 col-12` (Inquiry & Fundamentals) / `col-md-8 col-12` with an alertImage at `col-md-4` (see constraint 56). Note: carousel `.viewer` width is contextual — `col-md-12 col-12` when nested inside a `col-md-8` wrapper, `col-md-8 col-12` standalone — see COMP_07 in `04_COMP_SEGMENTS_OVERLAYS.md` and constraint 17.
 
```html
<!-- CORRECT: Activity with col-md-8 -->
<div class="row">
    <div class="col-md-8 col-12">
        <div class="activity interactive" number="1A">
            <div class="row"><div class="col-12">
                <!-- Interactive component here — inner rows use col-12 -->
            </div></div>
        </div>
    </div>
</div>
```
 
**Note on inner rows:** Rows INSIDE components (e.g., inside an activity, inside a dragAndDrop, inside an accordion) follow their own documented patterns and typically use `col-12` or component-specific column classes. The `col-md-8 col-12` rule applies to the TOP-LEVEL content rows that are direct children of `<div id="body">`.
 
---
 
## Content Merging Rules
 
When content clearly belongs together across structural boundaries, merge into a single component. Do NOT create duplicates.
 
**Speech bubble merging:** Table rows with text + image reference → merge into single visual component (text + image side by side or vertically stacked per writer instruction), NOT separate table + paragraph. Determine positional class from writer template layout; apply `paddingL`/`paddingR` on image column in horizontal layouts. See COMP_09 in `04_COMP_SEGMENTS_OVERLAYS.md`.
 
**Content in Word tables (NOT tagged `[TABLE]`):** Render as Bootstrap grid, NOT HTML tables.
 
---
 
## Writer Perspective Notes
 
Writers follow a structured template and Writer's Guide:
- Tag every element with square brackets
- Use **red text** for CS/developer instructions (NOT student content)
- Describe interactives by name from the Tools section
- Supply media references to match Media List
- Follow word limits for certain elements
### Key Writer Variability Patterns
 
1. **Case inconsistency** — `[body]`, `[Body]`, `[Body text]` in same document
2. **Lesson numbering** — `[LESSON]` vs `[LESSON 1]` vs mixed
3. **Interactive tag phrasing** — `[click drop]`, `[Click drop]`, `[clickdrop]`, `[drop click]`
4. **Numbered sub-items** — `[flip card 1]`, `[Flip Card 1]`, `[flip card1]`
5. **Activity end markers** — `[end activity]`, `[end of activity]`, or none
As Te Kura staff note: "writers and teachers all do things slightly differently."
 
---
 
## Red Text Rules
 
Content flagged as `🔴[RED TEXT]...[/RED TEXT]🔴` is CS/developer instruction (or, when author-prefixed, a captured reviewer comment):
- Strip from output
- Parse for embedded tags
- If ONLY tag + whitespace → extract and process
- If substantive **writer** instructions (a CS instruction the writer placed in red text) → VISIBLE red **bold** note with the `Writers Note:` prefix (`<p style="color: red; font-weight: bold;">Writers Note: ...</p>`), never a hidden comment
- **Captured reviewer comment** (the red-text note begins with the `Note from {author}:` lead from a whitelisted reviewer — Kate Scanlon, Nadia Stanton, Caroline Schwer, Simon Vita, Amanda Griffiths, Creative Services) → VISIBLE red **bold** designer message preserving the lead + author + text verbatim, in position: `<p style="color: red; font-weight: bold;">Note from {Author}: {verbatim text}</p>`. Never paraphrase, drop, comment-bury, or tag-parse it. See Comment & Red Flag Policy → Source-Specific Red-Note Prefixes and Captured Reviewer Comments
- **Never render as student content**
- Whitespace-only red text blocks → disregard entirely
---
 
## Heading Formatting
 
- Never wrap entire headings in italic/bold (usually .docx artefact)
- If only specific words are styled, preserve partial styling
- Exception: Module menu headings follow their own rules (see section 01 in `01_PIPELINE_EXTRACTION_TAGS.md`)
**⚠️ CRITICAL — Module Menu List Item Formatting:**
- Learning intention and success criteria list items in the module menu must NOT be wrapped in `<i>` tags, even if the PageForge source text appears in italic. Full-item italic on these list items is a .docx formatting artefact and must be stripped.
- List items should begin lowercase with verb form matching the heading context:
  - Under "We are learning:" → "to [verb]..." (e.g., "to understand the history...")
  - Under "I can:" → base verb (e.g., "sort cinematic advancements...")
  - Under "You will show your understanding by:" → gerund (e.g., "matching book covers...")
- If the PageForge source uses capitalisation or different verb forms, normalise to match the heading context
---
 
## Numbered Instructions in Activities
 
When the writer numbers the **instructions, steps, or sub-questions** of an activity or interactive (e.g. "1. Drag and drop the labels…", "2. Drag these images…"), render them as a semantic **ordered list** — `<ol><li>…</li></ol>` — never as paragraphs with a typed-in number (`<p>1. …</p>`). This is a format normalisation, not a wording change: the visible number is produced by the `<ol>`, so strip the literal "1." / "2." that the writer typed.
 
```html
<!-- writer wrote: "1. Drag and drop the labels into the right place…" -->
<ol>
    <li>Drag and drop the labels into the right place to show what each word means.</li>
</ol>
```
 
- **Continuation across split content.** When numbered items are separated by other content (for example an interactive sits between step 1 and step 2), continue the count with the `start` attribute rather than restarting at 1:
  ```html
  <ol start="2">
      <li>Drag these images into place to show examples of cells, tissues, organs, organ systems and organisms.</li>
  </ol>
  ```
- **Applies to every interactive, everywhere** — D&D sub-questions, quiz/instruction lists, ordering tasks, etc. (See `03_COMP_CORE_INTERACTIVES.md` → COMP_00 Universal Rules.)
- **Do not carry a typed number inside a quiz/MCQ question string.** Strip a leading "1." / "Q1." from an `mcqQuestionText` (or equivalent) — the component supplies its own question numbering.
---
 
## Square-Bracket Tags
 
**NEVER render square-bracket tags as visible text.** Every tag must be mapped to its HTML component or flagged.
 
 
 
 
