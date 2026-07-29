> **Last updated:** Wednesday, 29th July, 2026 6:41 PM
> **Granular part C (3 of 5) of `02_DATA_CONTENT_VERIFICATION.md`** — Verification checklist.
> All sibling parts live in `02_DATA_CONTENT_VERIFICATION/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# 08 — Verification, Constraints & Output
 
> **When to load:** During Phase 7, for final review. Also reference constraints throughout conversion.
 
---
 
## Verification Checklist
 
Run ALL checks before presenting output:
 
### Template & Structure
- [ ] `<!doctype html>` (lowercase), html tag, head section, script URLs match structural reference (template file or reference module files)
- [ ] Void elements use XHTML-style self-closing syntax (e.g., `<meta ... />`, `<img ... />`, `<link ... />`)
- [ ] If Mode B (reference module): ALL reference module codes replaced with new module code
- [ ] If Mode B (reference module): ALL reference module titles replaced with new module titles
- [ ] If Mode B (reference module): template level attribute matches expected year level for new module code (auto-corrected if mismatch)
- [ ] If Mode B (reference module): NO module-specific CSS `<link>` elements carried over from reference
- [ ] If Mode B (reference module): stickyNav.js NOT automatically carried over (omit if uncertain)
- [ ] Content source format identified (PageForge `.txt` / raw Writers Template `.docx` / MTK `.docx`)
- [ ] If raw Writers Template `.docx`: ALL front-matter skipped (submission checklist, LOT tags, Section A merging, Section B guidance, contents, sign-off); conversion begins at first `[TITLE BAR]`
- [ ] All 4 Page Boundary Validation Rules applied; anomalies resolved
- [ ] Opening divs = closing divs exactly
- [ ] All body content inside row > col-* grid
- [ ] Top-level content rows use `col-md-8 col-12` as default (not bare `col-12`)
- [ ] Activity/interactive divs wrapped in `row > col-md-8 col-12`
- [ ] `col-md-8` applied ONLY to direct child of `.row`, NOT to deeper descendants
- [ ] Footer nav appropriate for page position
- [ ] Footer navigation `href`s are ALL empty (`href=""`) — `prev-lesson`, `next-lesson`, `home-nav`; no computed `MODULE_CODE-XX.html` values, and none carried over from a Mode B reference (constraint 71)
- [ ] Acknowledgements (when generated): present at the BOTTOM of the overview page (`-00` / lesson 0.0), after the footer `<div>` — NOT on the last page or any lesson page
- [ ] If a Media List `.docx` was supplied: every content-source media reference cross-checked against it; media titles/descriptions in acks sourced from it
### Content Integrity
- [ ] All writer text preserved verbatim (trust the content source as-is — PageForge `.txt`, raw `.docx`, or MTK `.docx`)
- [ ] No paragraphs ending mid-sentence without terminal punctuation
- [ ] ALL student-facing content exists as rendered HTML (not only in comments)
- [ ] All tags normalised before mapping; no unrecognised tags silently skipped
- [ ] No square-bracket tags rendered as visible text
- [ ] All red text stripped; substantive instructions rendered as VISIBLE red flags (not hidden comments)
- [ ] Macronised characters preserved
- [ ] Bold/italic from table cells preserved
- [ ] Formatting markers (`**bold**`, `*italic*`, `__underline__`) converted to HTML tags
### Headings & Titles
- [ ] Body headings (`<h2>`–`<h5>`) have NO `<span>` wrappers at any year level
- [ ] `<span>` wrappers used ONLY inside `<h1>` header titles
- [ ] No full-heading italic wrapping
- [ ] English and Te Reo titles in separate `<h1><span>` elements
- [ ] `<title>` element: overview pages use `MODULE_CODE English Title`; lesson pages use `MODULE_CODE lesson#` only (no lesson-specific title, no Te Reo)
- [ ] Lesson pages: `#module-code` contains zero-padded lesson number only (e.g., `01`), NOT full module code, NOT decimal format (e.g., `1.0`)
- [ ] Lesson pages: `<h1><span>` uses MODULE title (not lesson-specific title); first "Lesson N" H2 rendered as body `<h3>`
- [ ] Years 9–10 / NCEA lesson pages: dual `<h1><span>` titles (English + Te Reo) present on EVERY lesson page
- [ ] Module menu (overview pages, tabbed): built from the CANONICAL tab set (Overview → Knowledge → Practices → Information → Standards/Assessment), content-driven omission — never mirrored from the reference's tab selection; each `<li>` paired 1:1 with its `.tab-pane` (constraint 67)
- [ ] Module menu (overview pages, tabbed): headings follow the canonical table — `<h4><span>` for Overview/Knowledge/Practices titles; `<h5>` no-span for the We-are-learning:/I-can: labels and ALL Information/Standards headings; success title reads "How will I know I have learned it?"
- [ ] Module menu (overview pages, tabbed): exactly ONE variation emitted per variable panel (Overview Var 1/2; Standards Var A ≤3 / Var B >3 standards); every `Designer note:` line stripped; long panels carry `overflowYScroll` + `scroll="500"`
- [ ] Module menu (lesson pages): uses `<h5>` headings as label text (e.g., `<h5>We are learning:</h5>`, `<h5>I can:</h5>`)
- [ ] Module menu (lesson pages): labels normalised to standard patterns for template level (not writer's verbatim text)
- [ ] Module menu (lesson pages): NO `<h4>` headings, NO `<p>` lead-in text between headings and lists, NO "Learning intentions"/"Success criteria" section titles
- [ ] Module menu (lesson pages, simplified): `tooltip="Overview"` on `#module-menu-button` (NOT on `#module-menu-content`)
- [ ] Module menu: content inside `col-md-8 col-12`
- [ ] List items in module menu: no full-item italic (`<i>` wrapping), lowercase start, verb form matches heading context
### Interactive Components
- [ ] Every component cross-referenced with component files
- [ ] Drag items = drop zones (parity)
- [ ] D&D column layout uses `col-md-12 col-12` outer wrapper (not `col-md-8`)
- [ ] Tab labels = tab panes (parity)
- [ ] clickDrop triggers = clickDropContent divs (parity)
- [ ] clickDrop buttons grouped together, then content divs grouped after
- [ ] clickDrop: NO `active` class on any `.clickDrop` button (JS handles initial state)
- [ ] clickDrop: NO inline `style` attributes on any `.clickDropContent` div (JS handles visibility)
- [ ] clickDrop: NO `rel` attribute by default — pairing is auto-calculated from document order; a single clickDrop pair never carries `rel`; only add `rel="N"` to override out-of-order multi-pair authoring
- [ ] Memory cards in matching pairs
- [ ] Shapes = shapeContents (parity)
- [ ] Shape hover: `layout="clockwise"` when content shows sequential steps
- [ ] All option/answer/match attributes correct
- [ ] `noShuffle` only when writer explicitly requested
- [ ] MCQ button spelling: Standard = `mcqAswers` (no 'n'); Image = `mcqAnswers` (with 'n')
- [ ] TKmodalButton and TKmodal in matching sequential order
- [ ] Exact button classes per component (see COMP_00 in `03_COMP_CORE_INTERACTIVES.md`)
- [ ] Speech bubbles: `no-hover` on all text-only/display-only bubbles
- [ ] Speech bubbles: single-character uses `bubble-basic` + positional class (`bubble-left`/`bubble-right`/`bubble-top`/`bubble-bottom`) — see COMP_09
- [ ] Speech bubbles: positional class matches writer template layout (text-left/image-right → `bubble-left`; image-left/text-right → `bubble-right`)
- [ ] Speech bubbles: writer CS positional instructions (e.g., "above the cat's head") override default layout → use `bubble-top`/`bubble-bottom` with image in separate row
- [ ] Speech bubbles: multi-paragraph content wrapped in `<div>` inside bubble element; single-paragraph content has no wrapper
- [ ] Speech bubbles: image column has `paddingL` (image on right) or `paddingR` (image on left) in horizontal layouts
- [ ] Speech bubble images: NO `imageCentral` class on writer-specified images
- [ ] Flip cards: `flipCardsContainer` on wrapper row; `flipImage` on `.front` with images; `<h5>` for titles
- [ ] Carousel (image): viewer width per context (constraint 17); `image` class on items containing images
- [ ] Carousel (video): viewer width per context (constraint 17); `<h5>` titles; description `<p>` above video embed
- [ ] Carousel (external nav buttons): `carousel-btns` with matching `exSlideBtns` attribute; button count = item count; viewer width per context (constraint 17); `item video` class; description below video
- [ ] multiChoiceQuiz (survey/self-assessment): `autoCheck emptyOptions checkAll`; `mcqOption` count per question = rating column count; all options `value="correct"`
- [ ] multiChoiceQuiz (graded multi-select): uses `multiChoiceQuiz mcqSomeSelected` with `mcqQuestion`/`mcqQuestionText`/`mcqOptions`/`mcqOption`; correct options `value="correct"`, wrong options have NO `value` attribute; NOT built as `multiQuiz`/`mQContainer`/`mQOption`
- [ ] Graded MCQ that is SINGLE-answer / two-option (e.g. "plant cell or animal cell?"): also uses the `multiChoiceQuiz` family (`mcqQuestion`/`mcqQuestionText`/`mcqOptions`/`mcqOption`, correct option `value="correct"`), NEVER the legacy `multiQuiz`/`mQContainer`/`mQOption`/`.answer`; no typed number inside `mcqQuestionText`
- [ ] Dropdown quiz paragraph: uses `dropParaContainer` + `dropQuestion` + `dropDown` structure (ONLY for inline fill-in-the-blank style)
- [ ] Dropdown quiz list layout: NO `layout` attribute, NO `dropParaContainer`; uses `<ol><li>` with row/column structure (`col-md-6 paddingR` question + `col-md-6 dropQuestion` dropdown)
- [ ] Dropdown quiz list layout: wider container (`col-md-8 col-12`, alertImage `col-md-4`) when paired with alertImage
- [ ] D&D standard with `images` class: text in `questionContainer` (col-7), images in `dragContainer` (col-5); NOT images in questionContainer
- [ ] D&D standard with `images` class: `margB0` on images inside `.drag` items
- [ ] Sketcher images: `canvasImage` class present on image inside `.canvasContainer`
- [ ] Sketcher images: NO `loading="lazy"` attribute on images inside `.canvasContainer`
- [ ] Clickable labelled DIAGRAM (labels point to parts of an image, reveal text on click): uses `imageLabel` + `layout="labelLine"` with `<div class="label infoTrigger" … direction/top/left/pointTop/pointLeft><p>…</p></div>` children and `imgLabel` on the image — NOT `infoImage` with `<span/p class="infoTrigger" style="top/left">`, NOT flip cards
- [ ] Simple hotspot overlay (labels float over an image, NO leader lines to parts): uses `infoImage` with positioned `<p class="infoTrigger">` elements
- [ ] Numbered activity/interactive instructions use `<ol><li>` (with `start="N"` for continuation) — NEVER `<p>1. …</p>` manual numbering; no typed leading number left inside a quiz question string
- [ ] Each `activity` wrapper contains at most ONE interactive component; two or more interactives under one writer activity heading are split into separate sequential activities, the following activities renumbered, and the split flagged with a visible `Red Flag:` note (constraint 62)
- [ ] Activity containing a dropbox / "Go to dropbox" / "Upload to dropbox" button carries the `dropbox` modifier on the activity wrapper (`activity dropbox` or `activity interactive dropbox`) — applies to ALL module series
- [ ] `[MTKquiz]` activities: "Go to quiz" button with blank `href="#"` + visible `Designer/Developer To Do:` note (create the quiz in MTK) — NEVER a dropbox button; writer-supplied quiz content stays rendered on the page; no `dropbox` wrapper modifier (constraint 65)
- [ ] EVERY activity with an interactive: heading/intro prose sits at `col-md-8 col-12` in its own inner row, and the interactive sits in a separate inner row at the wrapper's width — default or widened (constraint 63)
- [ ] Supervisor buttons: `super-content-button` family only — outer `<div class="row supervisor">` (except when nested inside another widget); Shape A activity-bound (class + `number` on `.activity`, reveal panel FIRST child) / Shape B standalone (class on `.col`) / Shape C paired (`paddingL` button col + `paddingR` content col); reveal panel keeps the invariant 4-level nesting; the legacy `supervisorContainer` trio is NEVER emitted (constraint 68)
- [ ] Acknowledgements entry titles: official published title verbatim — casing, punctuation, and any trailing ". stock photo" suffix retained when part of the official title (constraint 66); alt text still NEVER contains "stock photo" (constraint 52)
- [ ] Creative Services videos: Vimeo `videoSection` scaffold with pending ID + visible `Designer/Developer To Do:` note per audiovisual item — never a YouTube embed for a CS production (constraint 64)
- [ ] Audio triggers in table cells: use `audioButton` (not `audioTrigger`)
- [ ] WJFUN `[Audio image]` grids: built as `audioImage`/`audioImageOption` (audio filename on the option `id`) — never `audioTrigger` spans wrapping images
- [ ] Activity + alertImage pairing: `col-md-8 col-12` outer container; alertImage `col-md-4` nested inside with inner row/col structure (8 + 4 = 12)
### Media & Image Output Mode
- [ ] Image output mode (Mode P or Mode D) confirmed with user before generating HTML — not silently defaulted
- [ ] Image output mode applied uniformly to ALL images (no mixing within a single file)
- [ ] Mode P: visible placehold.co placeholder + commented-out real reference for each writer-specified image
- [ ] Mode D: clean `<img>` tags with direct filenames — no HTML comment blocks above images
- [ ] iStock ID cross-check (constraint 61): every `images/iStock-{ID}.jpg` emitted has `{ID}` equal to the first capture of `gm(\d+)` in the corresponding writer URL — the gm-leading number, which equals the asset page's "Stock photo ID"; NEVER the trailing segment of a dual-ID `gm{A}-{B}` URL — and the acknowledgements block cites the identical ID. Any mismatch is a build error — fix before presenting
- [ ] All images: `class="img-fluid"` and `loading="lazy"` (EXCEPTION: images inside sketcher `.canvasContainer` must NOT have `loading="lazy"`)
- [ ] YouTube: `youtube-nocookie.com/embed/`
- [ ] No TikTok embeds
- [ ] No `imageCentral` class on writer-specified images
- [ ] Image caption paragraphs (a `<p>` describing/naming an adjacent image) carry `class="captionText"` — in every context (standalone, in columns, inside accordion content); ordinary prose `<p>` stays unclassed
- [ ] Acknowledgements wrapper is `<div class="acks acksTemplate">` (the `acksTemplate` modifier is standard); add `acksAI` → `<div class="acks acksTemplate acksAI">` when the module uses AI-generated media — **including where the writer has only REQUESTED an AI asset that does not exist yet**, paired with a `Designer/Developer To Do:` note (constraint 72)
- [ ] Each media-carrying `acksLesson` div opens with a `<!-- Lesson N.N -->` page-label annotation — the word is **Lesson**, never **Page**; the three boilerplate divs carry no label (constraint 73)
### Class Attribute Integrity
- [ ] NO class attribute values begin with a leading space (e.g., `class="activityButton reset"` not `class=" activityButton reset"`)
- [ ] Text+image side-by-side layouts: text on LEFT, image on RIGHT (except speech bubbles)
- [ ] Reorder (re-standard): uses `layout="re-standard"`, `row` class, `reorderList col-12`, NO `item` attributes, NO `grid` attribute
- [ ] Radio Quiz (True/False): includes `row headings` with T/F columns and Description label
- [ ] D&D column with many images: uses `col-12` / `col-md-11 col-12` wrapper (by module type, never `col-md-10`) and empty `.ddColumn` elements for image distribution
- [ ] Writer visual element requests (marquees, banners, etc.) are implemented as visible components, not hidden in comments only
### Flags & Fallbacks
- [ ] Undocumented components → Tiered Fallback with visible content
- [ ] All red flags have visible fallback
- [ ] No inline CSS, JavaScript, or invented class names (exceptions: `infoTrigger` percentage positioning inside `infoImage`; WJFUN static word-highlighter spans — CL-0066)
### Comments & Designer-Facing Notes
- [ ] NO HTML comment discloses an interactive's correct answer(s) or answer key
- [ ] All designer-facing notes, CS instructions, and ambiguities are VISIBLE red **bold** flags — not hidden comments — each carrying its source-specific prefix (`Note from {author}:` / `Writers Note:` / `Red Flag:` / `Designer/Developer To Do:` — see Source-Specific Red-Note Prefixes)
- [ ] **No emoji anywhere in the output** except the exempt ticks/crosses (`✅ ✓ ✔ ☑ ✗ ✘ ❌ ❎`); every page from which emoji were removed carries exactly ONE visible `Red Flag: Emoji have been removed…` note at the first removal; a run of 2+ emoji-prefixed lines became a `<ul>`/`<li>` list; wording is otherwise untouched (constraint 74)
- [ ] Every standalone `[external link]` (own line / call to action) renders as `<div class="externalButton">`; every inline one (prose, list item, table cell) stays a plain `<a>` (constraint 75)
- [ ] **OSSC series only:** each lesson page carries a SINGLE `<h1><span>` holding the lesson title (no dual module title at any level, no duplicate body `<h3>`) — constraint 69; and a `[Lesson Overview]` descriptive sentence, where present, sits as a `<p>` ABOVE the first `<h5>` in the module menu — constraint 70
- [ ] Any captured whitelisted reviewer comment (the `Note from {author}:` red-text lead) is rendered as a VISIBLE red bold designer message (`<p style="color: red; font-weight: bold;">Note from {Author}: …</p>`), lead + author + text verbatim, in position — never a hidden comment, never dropped
- [ ] Every red designer note renders **red and bold** in the `<p style="color: red; font-weight: bold;">…</p>` form (the bold weight is required)
- [ ] The only comments present are the permitted exceptions (Mode P commented-out image reference; MTK `<!-- CS: Item N -->` annotation; the `<!-- &amp;start=0 --> <!-- &amp;end=0 -->` placeholders inside the Creative-Services Vimeo scaffold; the acknowledgements `<!-- Lesson N.N -->` page-label annotation; and — in Split Mode output only — the `PAGEFORGE-SPLICE` / `PAGEFORGE-SECTION` / `/PAGEFORGE-SECTION` markers and the `PAGEFORGE-GUIDE-START` … `PAGEFORGE-GUIDE-END` manual-stitch guidance blocks)
- [ ] No gratuitous "helpful" commentary left in the output
---
 
