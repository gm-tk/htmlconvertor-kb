> **Last updated:** Tuesday, 17th November, 2026 7:34 PM
> **Granular part C2 (4 of 6) of `02_DATA_CONTENT_VERIFICATION.md`** — Verification checklist, second half: Media & Image Output Mode, Language Fonts, Class Attribute Integrity, Flags & Fallbacks, Comments & Designer-Facing Notes. Split from `02C` on 17 November 2026 when it reached the 30 KB soft limit (`CLAUDE.md` §4); content moved verbatim.
> All sibling parts live in `02_DATA_CONTENT_VERIFICATION/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.
> *(Continuation of `02C`'s Verification Checklist — the two parts are ONE checklist and every check in both is run.)*

<!-- KB-PART-BODY-START -->
### Media & Image Output Mode
- [ ] Image output mode (Mode P or Mode D) confirmed with user before generating HTML — not silently defaulted
- [ ] Image output mode applied uniformly to ALL images (no mixing within a single file)
- [ ] Mode P: visible placehold.co placeholder + commented-out real reference for each writer-specified image
- [ ] Mode D: clean `<img>` tags with direct filenames — no HTML comment blocks above images
- [ ] iStock ID cross-check (constraint 61): every `images/iStock-{ID}.jpg` emitted has `{ID}` equal to the first capture of `gm(\d+)` in the corresponding writer URL — the gm-leading number, which equals the asset page's "Stock photo ID"; NEVER the trailing segment of a dual-ID `gm{A}-{B}` URL — and the acknowledgements block cites the identical ID. Any mismatch is a build error — fix before presenting
- [ ] All images: `class="img-fluid"` and `loading="lazy"`
- [ ] **EXCEPTION — no `loading="lazy"` inside a moving-or-draggable interactive (constraint 83):** every `<img>` inside `.rotateBanner`, `.carousel`/`.viewer`/`.item`, `.dragAndDrop` (`.drag`/`.drop`/`.ddContainer`/`.ddColumn`), `.clickDrop`/`.clickDropContent`, `.flipCard`, `.memoryGame` (`.memCard`/`.cardHidden`) and sketcher `.canvasContainer` carries **no** `loading="lazy"` — real images and `placehold.co` placeholders alike, in both output modes
- [ ] Images the student only clicks or hovers **without movement** (`infoImage`/`infoTrigger` hotspots, `imageLabel` diagrams), plus `alertImage`, speech-bubble characters, accordion/tab-panel images and self-reflection emoji, DO still carry `loading="lazy"` (constraint 83)
- [ ] AI Guidelines PDF embeds cite the CURRENT filename (constraint 84, `CL-0094`): the *Responding to Suspected Use* asset is emitted as `AI-guidelines/Kaimahi AI Guidelines Responding to Suspected Use in Assessments.pdf` — **no hyphen, no year range, capital `Use`**. The retired `…Kaimahi AI Guidelines - Responding to Suspected use in Assessments for Years 11–13 and NCEA.pdf` appears NOWHERE in the output, in either the `data=` or the fallback `href=`
- [ ] YouTube: `youtube-nocookie.com/embed/`
- [ ] No TikTok embeds
- [ ] No `imageCentral` class on writer-specified images (a subject central-asset tag recorded in `14` — e.g. MXEX `[Image Centralised {Name}]` — is a template asset and does take it; CL-0123)
- [ ] `[Writing Process …]` tags built as the centralised `writingProcess` component — `phase` from the template band (phase 1 from the named year), `stage` capitalised with `Checkpoint_N` underscored, the full circle alone in its own row — never an image, never a To Do (constraint 94, `CL-0116`)
- [ ] Science / Maths character tags built from the central store with the exact folder casing and pose number (`Science Characters/Quinn-4.jpg`, `Maths Characters/maths_characters_ada.jpg`) and `class="img-fluid imageCentral"`; an unknown name or pose is a `Red Flag:`, never a guessed file (constraint 95, `CL-0117`)
- [ ] Image caption paragraphs (a `<p>` describing/naming an adjacent image) carry `class="captionText"` — in every context (standalone, in columns, inside accordion content); ordinary prose `<p>` stays unclassed
- [ ] Acknowledgements wrapper is `<div class="acks acksTemplate">` (the `acksTemplate` modifier is standard); add `acksAI` → `<div class="acks acksTemplate acksAI">` when the module uses AI-generated media — **including where the writer has only REQUESTED an AI asset that does not exist yet**, paired with a `Designer/Developer To Do:` note (constraint 72)
- [ ] Each media-carrying `acksLesson` div opens with a `<!-- Lesson N.N -->` page-label annotation — the word is **Lesson**, never **Page**; the one remaining boilerplate div ("All other images ©…") carries no label (constraints 73, 90)
- [ ] **No generated statement is duplicated as text (constraint 90):** the acks block contains NO `<p>` carrying the "Every effort has been made…" apology, the "Parts of this resource were created with assistance from AI tools…" statement, or the "Copyright © … Board of Trustees…" line — `acksTemplate` / `acksAI` generate all three. `<span class="currentYear"></span>` should not appear anywhere in the block
### Language Fonts
- [ ] **Every** run of Japanese text carries `jp-text`, **every** run of Chinese text carries `ch-text`, and **every** run of pinyin carries `pinyin` (constraint 92) — in headings, paragraphs, bold/italic runs, list items, table headers and cells, and nested inside the `<h1><span>` header title; not just the first occurrence and not just the vocabulary tables
- [ ] The whole run is wrapped, internal punctuation included (brackets, slashes, a trailing full stop inside the run); surrounding English sits outside the wrapper
- [ ] **No te reo Māori or English word carries a language class** — macronised vowels (`ā ē ī ō ū`) are New Zealand letters, so `Māori`, `Manawatū`, `ākonga` are unwrapped. Anything marked `pinyin` is identified by a non-te-reo tone mark (`á ǎ à`, `ü`), by pairing with the Chinese it sounds out, or by the writer; genuinely ambiguous romanisation is left unwrapped with a visible `Red Flag:`
- [ ] Japanese vs Chinese resolved correctly where the characters are shared Han: class taken from the module's language (JPN/JPNFUN → `jp-text`, CH/CHFUN → `ch-text`), any run containing kana treated as Japanese, and an undeterminable case red-flagged rather than guessed
- [ ] A colour class sits alongside the language class (`class="jp-text green-text"`), never in place of it
### Class Attribute Integrity
- [ ] NO class attribute values begin with a leading space (e.g., `class="activityButton reset"` not `class=" activityButton reset"`)
- [ ] Text+image side-by-side layouts: text on LEFT, image on RIGHT (except speech bubbles)
- [ ] Reorder (re-standard): uses `layout="re-standard"`, `row` class, `reorderList col-12`, NO `item` attributes, NO `grid` attribute
- [ ] Radio Quiz (True/False): includes `row headings` with T/F columns and Description label
- [ ] D&D column with many images: uses `col-12` / `col-md-11 col-12` wrapper (by module type, never `col-md-10`) and empty `.ddColumn` elements for image distribution — the `dragContainer` has exactly as many `.ddColumn` elements as the `dropContainer` (CL-0127)
- [ ] Writer visual element requests (marquees, banners, etc.) are implemented as visible components, not hidden in comments only
### Flags & Fallbacks
- [ ] Undocumented components → Tiered Fallback with visible content
- [ ] All red flags have visible fallback
- [ ] No inline CSS, JavaScript, or invented class names (exceptions: `infoTrigger` percentage positioning inside `infoImage`; WJFUN static word-highlighter spans — CL-0066)
### Comments & Designer-Facing Notes
- [ ] NO HTML comment discloses an interactive's correct answer(s) or answer key
- [ ] All designer-facing notes, CS instructions, and ambiguities are VISIBLE red **bold** flags — not hidden comments — each carrying its source-specific prefix (`Note from {author}:` / `Writers Note:` / `Red Flag:` / `Designer/Developer To Do:` — see Source-Specific Red-Note Prefixes)
- [ ] **No emoji anywhere in the output** except the exempt ticks/crosses (`✅ ✓ ✔ ☑ ✗ ✘ ❌ ❎`); every page from which emoji were removed carries exactly ONE visible `Red Flag: Emoji have been removed…` note at the first removal; a run of 2+ emoji-prefixed lines became a `<ul>`/`<li>` list; wording is otherwise untouched (constraint 74)
- [ ] Every standalone `[external link]` (own line / call to action) renders as `<div class="externalButton">`; every inline one (prose, list item, table cell) stays a plain `<a>` (constraint 75) — including a link on its own line inside a click-drop panel (CL-0133)
- [ ] **All series, all year levels (constraint 79 — universal; the former OSSC-only framing described the corpus norm, not an exception):** each lesson page carries a SINGLE `<h1><span>` holding the lesson title (no dual module title at any level, no duplicate body `<h3>`) — a second `<h1><span>` only where the writer gave that lesson its own bilingual name. **OSSC series:** a `[Lesson Overview]` descriptive sentence, where present, sits as a `<p>` ABOVE the first `<h5>` in the module menu — constraint 70
- [ ] Any captured whitelisted reviewer comment (the `Note from {author}:` red-text lead) is rendered as a VISIBLE red bold designer message (`<p style="color: red; font-weight: bold;">Note from {Author}: …</p>`), lead + author + text verbatim, in position — never a hidden comment, never dropped
- [ ] Every red designer note renders **red and bold** in the `<p style="color: red; font-weight: bold;">…</p>` form (the bold weight is required)
- [ ] The only comments present are the permitted exceptions (Mode P commented-out image reference; MTK `<!-- CS: Item N -->` annotation; the `<!-- &amp;start=0 --> <!-- &amp;end=0 -->` placeholders inside the Creative-Services Vimeo scaffold; the acknowledgements `<!-- Lesson N.N -->` page-label annotation; and — in Split Mode output only — the `PAGEFORGE-SPLICE` / `PAGEFORGE-SECTION` / `/PAGEFORGE-SECTION` markers and the `PAGEFORGE-GUIDE-START` … `PAGEFORGE-GUIDE-END` manual-stitch guidance blocks)
- [ ] No gratuitous "helpful" commentary left in the output
---
 
