> **Last updated:** Wednesday, 28th October, 2026 1:05 PM
> **Granular part H (16 of 16) of `12_CHANGE_LEDGER.md`** — PART 4, the PageForge Amalgamation Log, continued: entries CL-0116 onward. **THE OPEN PART: append new entries here**, in CL order, newest last, in the ENTRY FORMAT set out in `12G` (whose WHY / WHAT GOES IN / ENTRY FORMAT / BACKFILL sections govern every part of this log). Opened 27 October 2026 when `12G` would have passed the 30 KB soft limit and was closed at CL-0115 (`CLAUDE.md` §4).
> All sibling parts live in `12_CHANGE_LEDGER/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# PART 4 — THE PAGEFORGE AMALGAMATION LOG (continued from `12G`: CL-0116 onward)

> The rules of this log — the front-facing test, the entry format, append-only, `PageForge status:` the only field edited in place — are in `12G_PAGEFORGE_AMALGAMATION_LOG.md` and are not repeated here.

### CL-0116 — `[Writing Process …]` writer tags build the centralised `writingProcess` component
- **Date:** Tuesday, 27th October, 2026
- **Scope:** (c) Universal — the component is centralised and identical in every phase
- **Source:** ADMIN MODE (authorised — Gavin, relaying Persephone Samuels, Design Team Lead, 27 October 2026; `writingProcess.html`)
- **Writer input (what triggers it):** `[Writing Process]`, `[Writing Process all]`, `[Writing Process all year 1]`, `[Writing Process all year 2-3]`, `[Writing Process all activeStage <stage>]`, `[Writing Process single <stage>]`, and the interim `[<stage> icon from the Writing Process English Universal parameters]`.
- **Required output:** full circle `<div class="writingProcess" phase="…"></div>` alone in its own `div.row > div.col-md-8.col-12`; `phase` from the page's `template` band (`4-6` → `2-yr-456`, `7-8` → `3-yr-78`, `9-10` → `4-yr9-10`, `NCEA` → `5-NCEA1`; `1-3` from the named year — `1-yr-1` / `1-yr-23`, default `1-yr-23` + a `Designer/Developer To Do:`); `activeStage="<Stage>"` when named. Single stage `<div class="writingProcess singleStage" stage="<Stage>"></div>`, `stage` in `Plan` / `Draft` / `Edit` / `Revise` / `Publish` / `Reflect` / `Checkpoint` / `Checkpoint_1` / `Checkpoint_2` / `Checkpoint_3`; icons one `col-2` each, consecutive icons sharing one row. Never an image, never a red note; built modules are not retrofitted.
- **Supersedes:** — (CL-0113 recorded the component; this adds the writer tags that reach it)
- **KB rule:** `14_SUBJECT_GLOBAL_PARAMETERS/14B2_SGP_FAMILIES_BLLR_MIW.md` §14.10; `01D` Media Tags; `00H` constraint 94
- **PageForge status:** Amalgamated (Tuesday, 27th October, 2026, round 1041, build 260625.70 — `Tag_Lexicon._meta.unresolved_marker_retag` rule + `Emit_Templates.elements.writing_process`; env `WRITEPROC_OFF`)

### CL-0117 — Science and Maths characters: centralised `imageCentral` assets from the registry
- **Date:** Tuesday, 27th October, 2026
- **Scope:** (b) Cohort — Science modules; Cohort — Maths modules (identified by subject)
- **Source:** ADMIN MODE (authorised — Gavin, relaying Meredith Lees, 23 October 2026; `Global Edits Science.docx`, `Global Edits Maths.docx`, `refresh_imageCentral.html`, the server folders `imageCentral\Science Characters` and `imageCentral\Maths Characters`)
- **Writer input (what triggers it):** `[Centralised image: <name> <n>]`, `[Image centralised <name>]`, `[Central image: <name>]` naming Aroha / Lani / Max / Quinn (Science), Ada / Omar / Hypi / Erni / Lara (Maths), or the scenes *clubhouse* / *kowhai reserve*.
- **Required output:** `<img class="img-fluid imageCentral" loading="lazy" src="…" alt="<Name>" />` — Science `science characters/<Name>-<n>.jpg` (poses 1–3 body, 4–5 head, Quinn 4–7; no number → 1), scenes `science characters/comic scenes/clubhouse_1.png` / `kowhai_reserve_1.png`; Maths `Maths Characters/maths_characters_<name>.jpg` (numbered poses `Maths Characters/ada/maths_characters_ada_<1-3>.jpg`, `Maths Characters/omar/maths_characters_omar_<1-16>.jpg` only when the number is named). Folder casing verbatim. Unknown name or pose → a red `Red Flag:` / `Designer/Developer To Do:`, never a guessed file; a centralised-image tag naming nothing registered is an ordinary image request (unchanged output).
- **Supersedes:** —
- **KB rule:** `14_SUBJECT_GLOBAL_PARAMETERS/14E_SGP_FAMILIES_SCIENCE_MATHS.md` §14.13 / §14.14; `01D` Media Tags; `01E`; `00H` constraint 95
- **PageForge status:** Amalgamated (Tuesday, 27th October, 2026, round 1041, build 260625.70 — `Emit_Templates.elements.central_image` registry; env `CENTRALIMG_OFF`)

### CL-0118 — Languages FUN level tiles: *Novice* → `First Steps`, *Emergent* → `Next Steps`
- **Date:** Tuesday, 27th October, 2026
- **Scope:** (b) Cohort — Languages Fundamentals (every Language FUN module)
- **Source:** ADMIN MODE (authorised — Gavin, relaying Persephone Samuels, 27 October 2026; the curriculum leads' request of 16 October 2026, example CHFUN08)
- **Writer input (what triggers it):** a Language FUN module's level markers — `[PAGE N Novice]`, `[Novice Page 1]`, `[Novice Content starts here]`, `[Tab 1] Novice Learning Intentions` and their Emergent twins (or templates already typing the new names).
- **Required output:** the level name shown as `First Steps` / `Next Steps` wherever it is displayed — module-menu level tabs `<li><a>First Steps</a></li>`, `.phases` strip `<div phase="1"><p>First Steps</p></div>`, `phaseLink` tile `<h3>First Steps</h3>` + image `alt`, the multi-file levels overview's panel `<h2>`. The writer's word remains the key the level is matched on; prose is never renamed; nothing structural changes.
- **Supersedes:** — (the pre-ledger `14A` two-tile wording named the tiles Novice / Emergent)
- **KB rule:** `14_SUBJECT_GLOBAL_PARAMETERS/14A_SGP_PURPOSE_FAMILIES_1_5.md` §14.1 (two-tile bullet)
- **PageForge status:** Amalgamated (Tuesday, 27th October, 2026, round 1042, build 260625.71 — `Emit_Templates.body_region.fundamentals_panels.level_labels` display map, `ContentConverter.LevelDisplayLabel`; env `LEVELNAMES_OFF`; eleven level-dialect golds diverge by these words only, NAMED)

### CL-0119 — Science characters: the folder is `Science Characters/` (server spelling) — casing correction to CL-0117
- **Date:** Tuesday, 27th October, 2026
- **Scope:** (b) Cohort — Science modules
- **Source:** ADMIN MODE (authorised — Gavin, 27 October 2026)
- **Writer input (what triggers it):** as CL-0117 — `[Centralised image: Quinn 4]`, `[Central image: clubhouse]` and the other Science character / scene names.
- **Required output:** `<img class="img-fluid imageCentral" loading="lazy" src="Science Characters/Quinn-4.jpg" alt="Quinn" />`; scenes `Science Characters/comic scenes/clubhouse_1.png` / `kowhai_reserve_1.png`. The capitalised, spaced folder exactly as on the server; never the template page's lower-case form.
- **Supersedes:** CL-0117 (its `science characters/` paths only)
- **KB rule:** `14_SUBJECT_GLOBAL_PARAMETERS/14E_SGP_FAMILIES_SCIENCE_MATHS.md` §14.13; `00H` constraint 95
- **PageForge status:** Amalgamated (27 October 2026, round 1043 — `Emit_Templates.elements.central_image.assets` `src` paths)

### CL-0120 — The older loose writing-process wording builds the component (widens CL-0116)
- **Date:** Tuesday, 27th October, 2026
- **Scope:** (c) Universal
- **Source:** ADMIN MODE (authorised — Gavin, 27 October 2026)
- **Writer input (what triggers it):** an image-tagged span whose bracket asks for an image / icon(s) / picture / graphic of the writing process or the MTK writing cycle (`[insert image of writing process from ENFUN09 …]`, `[Insert right, image of the draft icon from the global parameters image of MTK writing cycle]`, `[add writing process image in from TK …]`), or `[<Stage> icon from English universal parameters]` — also inside a layout-table image cell.
- **Required output:** as CL-0116: a named stage (`plan` / `planning`, `draft` / `drafting`, `edit` / `editing`, `revise` / `revising`, `publish` / `publishing`, `reflect` / `reflecting`, `checkpoint [N]`) → `<div class="writingProcess singleStage" stage="…"></div>`; no stage → `<div class="writingProcess" phase="…"></div>` in its own row; no writer-image placeholder, no red note for the fulfilled request. A button link, a flowchart to re-create or a span with a pasted picture renders as before.
- **Supersedes:** — (widens CL-0116; its no-retrofit sentence is rewritten)
- **KB rule:** `14_SUBJECT_GLOBAL_PARAMETERS/14B2_SGP_FAMILIES_BLLR_MIW.md` §14.10; `00H` constraint 94; `01D`
- **PageForge status:** Amalgamated (27 October 2026, round 1043 — `Emit_Templates.elements.writing_process.legacy_cue` + stage synonyms, `ContentConverter.#writingProcessLegacy` / `WritingProcessCell` (layout-grid cells); env `WRITEPROCLEGACY_OFF`)

### CL-0121 — Maths: the Global Edits conventions — three-tab overview, Lesson Summary alert, phase dropbox copy
- **Date:** Tuesday, 27th October, 2026
- **Scope:** (b) Cohort — Maths modules
- **Source:** ADMIN MODE (authorised — Gavin, 27 October 2026; Meredith Lees's *Global Edits Maths.docx*)
- **Writer input (what triggers it):** a Maths module's `[Overview]` with `[Tab 1]` … `[Tab 3]` lines (Information / Maths No Problem / Curriculum content); a lesson `[Overview]`; the `[Alert] [H3] Lesson summary … [Hint button] Need help? … [End summary]` block; `[ActivityDropbox] [H3] Checkpoint` and `[H3] Share Your Learning` boxes with or without body copy; `[Math] **4/5**`.
- **Required output:** the module menu as three tabs with those labels and the MNP tab's fixed lead / closing lines around the writer's verbatim book, chapter and lesson lines; lesson menus with that lesson's LI / SC; an alert holding `<h3>Lesson summary</h3>`, the body, and a hint button revealing the kaiako paragraph (*Email or phone your kaiako. You can ring 0800 65 99 88 …*); dropbox activity boxes whose empty body takes the phase's suggested copy (14E §14.14, Phases 1–4) and whose writer copy is kept verbatim; `[Math]` fractions as MathML. No intro alert is invented.
- **Supersedes:** — (extends CL-0117's §14.14)
- **KB rule:** `14_SUBJECT_GLOBAL_PARAMETERS/14E_SGP_FAMILIES_SCIENCE_MATHS.md` §14.14
- **PageForge status:** Not yet amalgamated — recorded inertly 27 October 2026 (round 1043, `Subject_Global_Parameters.json` 14.14, active:false); the builds await Maths Writers Templates in the corpus (a measured round)

### CL-0122 — The standard speech bubble is always text-left / image-right, whatever the Writers Template's order
- **Date:** Wednesday, 28th October, 2026
- **Scope:** (c) Universal — every standard single-character speech bubble (text + image side by side)
- **Source:** ADMIN MODE (authorised — Gavin, 28 October 2026, with a Writers Template screenshot: `[image] <iStock link>` in the left cell, the bubble text in the right cell)
- **Writer input (what triggers it):** a `[speech bubble]` paired with an `[image]` — the 1x2 table in either cell order, or the one-paragraph `[Image] … [speech bubble] …` form; a writer's "RHS" / "LHS" note
- **Required output:** `<div class="row speechBubble" layout="speech">` with the bubble column FIRST (`bubble-basic no-hover bubble-left`, or `bubble-left no-hover` for a one-paragraph bubble) and the image column SECOND (`paddingL` where the column carries padding) — never `bubble-right` for a standard bubble; a writer's above / below instruction still gives `bubble-top` / `bubble-bottom`; the conversation layout and the WJ Kea bubble are unchanged
- **Supersedes:** the `speechBubble` exception in constraint 35 and the "positional class from the Writers Template layout" wording of constraint 29 / 45 and COMP_09
- **KB rule:** `02_DATA_CONTENT_VERIFICATION/02B_CONTENT_RULES.md` (constraint 35 paragraph); `02D` 35 / 45; `00D` 29; `02A`; `02C`; `04_COMP_SEGMENTS_OVERLAYS/04C_COMP09_10_11_BUBBLES_DIAGRAMS_TOOLS.md`; `14B2` §14.10 (Kea exception)
- **PageForge status:** Amalgamated 28 October 2026 (round 1055, build 260625.83 — `Emit_Templates.interactive_builders.speechBubble.fixed_side`, env `SBSIDE_OFF`, read by the table form, the paragraph form, the composer's avatar rows and the placeholder character; the human pages are a recorded gold override, `Subject_Global_Parameters._universal_conventions.bubble_text_left_image_right`); the corpus follows on the next regeneration

### CL-0123 — MXEX central Maths characters + character/bubble row (merged 28 October 2026: filenames per CL-0121 §14.14; the bubble's side per CL-0122 — text left, picture right)
- **Date:** Tuesday, 20th October, 2026
- **Scope:** (b) Module-series — MXEX
- **Source:** Finalized difference report — `MXEX105`, Difference 1
- **Writer input (what triggers it):** `[Image Centralised {Name}]` (e.g. `Archi`) followed by a `[Speech bubble]`, in an MXEX module.
- **Required output:** inside `col-md-8 col-12`, one `row speechBubble` (`layout="speech"`): image column `col-md-3 col-4 paddingR` holding `<img class="img-fluid imageCentral" loading="lazy" src="Maths Characters/Maths Characters_DRAFT_{Name}.jpg" alt="{Name}">`; bubble column `col-md-9 col-10 paddingL` holding `<div class="bubble-right no-hover"><p>…</p></div>`.
- **Supersedes:** — (generic `bubble-basic` single-character form for MXEX central characters only)
- **KB rule:** `14_SUBJECT_GLOBAL_PARAMETERS/14D` §14.15; `04_COMP_SEGMENTS_OVERLAYS/04C` → imageCentral Rule
- **PageForge status:** Not yet amalgamated

### CL-0124 — MXEX `[RHS alert]` → `alert top`
- **Date:** Tuesday, 20th October, 2026
- **Scope:** (b) Module-series — MXEX
- **Source:** Finalized difference report — `MXEX105`, Difference 2
- **Writer input (what triggers it):** `[RHS alert]` beside body content in an MXEX module.
- **Required output:** `<div class="alert top">…</div>` in the `col-md-4` sidebar column — not `alertActivity`.
- **Supersedes:** —
- **KB rule:** `14D` §14.15; `05_COMP_LANGUAGE_MEDIA_LAYOUT/05B` → Activity sidebar
- **PageForge status:** Not yet amalgamated

### CL-0125 — MXEX click drop inside one content column
- **Date:** Tuesday, 20th October, 2026
- **Scope:** (b) Module-series — MXEX
- **Source:** Finalized difference report — `MXEX105`, Difference 5
- **Writer input (what triggers it):** any click-drop set in an MXEX module.
- **Required output:** `row` > `col-md-8 col-12` holding the trigger row then every `clickDropContent` (grouping unchanged); a revealed bubble is `col-md-12 col-12` + `bubble-basic no-hover bubble-bottom`.
- **Supersedes:** —
- **KB rule:** `14D` §14.15; `04A` → Click Drop
- **PageForge status:** Not yet amalgamated

### CL-0126 — Multi-value `option` for identical drag answers
- **Date:** Tuesday, 20th October, 2026
- **Scope:** (c) Universal
- **Source:** Finalized difference report — `MXEX105`, Difference 3
- **Writer input (what triggers it):** two or more drag items with the same answer text, each correct in either slot.
- **Required output:** each such drag lists every slot it may fill, own slot first (`option="3 4"`, `option="4 3"`); drops keep single values; no red flag.
- **Supersedes:** —
- **KB rule:** `03_COMP_CORE_INTERACTIVES/03B` → Standard Layout
- **PageForge status:** Not yet amalgamated

### CL-0127 — Drag columns match drop columns; labelled image drags
- **Date:** Tuesday, 20th October, 2026
- **Scope:** (c) Universal
- **Source:** Finalized difference reports — `MXEX105` Difference 10; `SCBI202` Difference 5
- **Writer input (what triggers it):** a column-layout drag and drop; drag items given as image + label.
- **Required output:** `dragContainer` `.ddColumn` count = `dropContainer` `.ddColumn` count (first populated, rest empty); a labelled image drag is `<div class="drag" option="N"><p><img …> Label</p></div>`; no inline styles.
- **Supersedes:** the "maximum of 3 `.ddColumn`" cap and the 4–6 / 7+ table (pre-ledger)
- **KB rule:** `03B` → Column Layout
- **PageForge status:** Not yet amalgamated

### CL-0128 — Journal references (constraint 6)
- **Date:** Tuesday, 20th October, 2026
- **Scope:** (c) Universal
- **Source:** Finalized difference reports — `MXEX105` Differences 7–8; `SCBI202` Difference 1
- **Writer input (what triggers it):** any journal reference — `[button]` / `[journal]` "Go to journal", "Go to your journal", "Download journal".
- **Required output:** FIRST in the module → `<a href="docs/{CODE} Journal.docx" target="_blank"><div class="button downloadButton">Download journal</div></a><div class="hint"></div><div class="hintDropContent" hintType="oneDrive"></div>` (`googleDrive` when the writer's link is a Google Docs "make a copy" link; a writer-supplied link replaces the `docs/` href). Every later → `<h4 class="goJournal">Go to your journal</h4>`. No To Do notes. The HPE celebration page included.
- **Supersedes:** CL-0022 / CL-0023 "Go to your journal button" wording (HPE)
- **KB rule:** `05_COMP_LANGUAGE_MEDIA_LAYOUT/05D` → Buttons → Journal references; `00_MASTER_INSTRUCTIONS/00H` constraint 6
- **PageForge status:** Not yet amalgamated

### CL-0129 — Untitled activity still gets an `<h3>`
- **Date:** Tuesday, 20th October, 2026
- **Scope:** (c) Universal
- **Source:** Finalized difference report — `SCBI202`, Difference 2
- **Writer input (what triggers it):** an `[Activity nX]` with no title.
- **Required output:** `<h3>` = the matching journal task's title from the template, verbatim; if none, no heading + a visible `Red Flag:` asking for one.
- **Supersedes:** —
- **KB rule:** `05B` → Activities
- **PageForge status:** Not yet amalgamated

### CL-0130 — autoCheck by module level; no Check button under autoCheck
- **Date:** Tuesday, 20th October, 2026
- **Scope:** (c) Universal
- **Source:** Finalized difference report — `SCBI202`, Difference 3
- **Writer input (what triggers it):** any autoCheck-capable interactive in an ECH / `1-3` / `4-6` module, however the module was built.
- **Required output:** `autoCheck` applied; Undo / Check buttons dropped (typing quiz excepted) — e.g. `<div class="dropQuiz autoCheck" layout="paragraph">` with a Reset-only button row.
- **Supersedes:** constraint 38's template-FILE trigger
- **KB rule:** `00D` constraint 38; `03A` → autoCheck Auto-Application; `03C` → Dropdown Quiz
- **PageForge status:** Not yet amalgamated

### CL-0131 — Memory game: exactly two cards per match
- **Date:** Tuesday, 20th October, 2026
- **Scope:** (c) Universal
- **Source:** Finalized difference report — `SCBI202`, Difference 6
- **Writer input (what triggers it):** `[memory game]` with groups of three or more matching cards.
- **Required output:** one pair per group from its first two cards (`match="1"`, `"2"`, …); remaining cards listed in one visible `Red Flag:` above the game; never commented out.
- **Supersedes:** —
- **KB rule:** `03E` → Memory Game
- **PageForge status:** Not yet amalgamated

### CL-0132 — Static labels with lines → `imageLabel layout="line"`
- **Date:** Tuesday, 20th October, 2026
- **Scope:** (c) Universal
- **Source:** Finalized difference report — `SCBI202`, Differences 8–9
- **Writer input (what triggers it):** a request for an image labelled with lines (non-clickable), with a label list.
- **Required output:** `<div class="imageLabel" layout="line">` + `img.imgLabel` + one `<div class="label" direction top left pointTop pointLeft><p>…</p></div>` per label (`||` for multiple lines), evenly spaced starting positions, one `Designer/Developer To Do:` to position them; two-picture requests add `<h5>` captions in a `row paddingB` and a To Do for a combined image.
- **Supersedes:** the To-Do-only fallback for these requests
- **KB rule:** `04_COMP_SEGMENTS_OVERLAYS/04B` → Image Label
- **PageForge status:** Not yet amalgamated

### CL-0133 — Standalone link in a click-drop panel → `externalButton`
- **Date:** Tuesday, 20th October, 2026
- **Scope:** (c) Universal
- **Source:** Finalized difference report — `SCBI202`, Difference 11
- **Writer input (what triggers it):** a link on its own line inside `clickDropContent`.
- **Required output:** `<a href="URL" target="_blank"><div class="externalButton">Text</div></a>`.
- **Supersedes:** —
- **KB rule:** `00G` constraint 75; `05D` → Buttons
- **PageForge status:** Not yet amalgamated

### CL-0134 — Click-drop choice sets and picture triggers
- **Date:** Tuesday, 20th October, 2026
- **Scope:** (c) Universal
- **Source:** Finalized difference report — `SCBI202`, Difference 12
- **Writer input (what triggers it):** a choice-style click drop "with image tile and title"; or "images with captions" to be clicked.
- **Required output:** choice set — buttons only in the trigger row, each picture inside its panel under the panel's `<h3>`; picture triggers — `<div class="col"><h5>Caption</h5><img class="img-fluid clickDrop imgBorder" …></div>`; no inline styles, no comments.
- **Supersedes:** —
- **KB rule:** `04A` → Click Drop → Choice Sets and Picture Triggers
- **PageForge status:** Not yet amalgamated

### CL-0135 — Text + side image as sibling columns with padding
- **Date:** Tuesday, 20th October, 2026
- **Scope:** (c) Universal
- **Source:** Finalized difference report — `SCBI202`, Difference 13
- **Writer input (what triggers it):** body text with an image (or sidebar alert) beside it.
- **Required output:** one `row`: `col-md-8 col-12 paddingR` (text, heading included) + `col-md-4 col-12 paddingL` (image) — never an inner row inside the text column; `paddingR` / `paddingL` on every side-by-side pair.
- **Supersedes:** the pre-ledger `02B` "inner row pattern"
- **KB rule:** `02_DATA_CONTENT_VERIFICATION/02B` → Column Class Reference; `05D` → Columns
- **PageForge status:** Not yet amalgamated

### CL-0136 — Floating-nav glossary → glossary page + stickyNav
- **Date:** Tuesday, 20th October, 2026
- **Scope:** (c) Universal
- **Source:** Finalized difference report — `SCBI202`, Difference 15
- **Writer input (what triggers it):** a writer request for a glossary in a floating / sticky nav.
- **Required output:** a separate `{CODE}_glossary.html` page (standard skeleton, `<h1><span>Glossary</span></h1>`, `glossary` / `search-table` in `#body`); `<script src="js/stickyNav.js" type="text/javascript" class="stickyNav"></script>` in every page's `<head>`; no glossary on 0.0; no red flag.
- **Supersedes:** —
- **KB rule:** `05_COMP_LANGUAGE_MEDIA_LAYOUT/05A` → Glossary
- **PageForge status:** Not yet amalgamated

### CL-0137 — No `<h5>` inside a drag and drop
- **Date:** Wednesday, 21st October, 2026
- **Scope:** (c) Universal
- **Source:** ADMIN MODE (authorised) — direct-typed
- **Writer input (what triggers it):** any heading the writer asks for inside a drag and drop (e.g. an `[H5]` tag on a column heading or group label), in any layout.
- **Required output:** `<p><b>Heading text</b></p>` — never `<h5>` anywhere inside `.dragAndDrop`; no inline style. An unrequested column heading stays `<p>Column heading</p>`.
- **Supersedes:** —
- **KB rule:** `03_COMP_CORE_INTERACTIVES/03B` → Headings inside a drag and drop; `00H` constraint 7
- **PageForge status:** Not yet amalgamated

### CL-0138 — `dropbox` modifier on any activity containing a dropbox button (not BLL)
- **Date:** Wednesday, 21st October, 2026
- **Scope:** (c) Universal — BLL excepted
- **Source:** ADMIN MODE (authorised) — direct-typed
- **Writer input (what triggers it):** an activity holding a "Go to dropbox" / "Upload to dropbox" button or a `[trigger engagement]` tag, anywhere in the activity.
- **Required output:** append `dropbox` to the activity's classes — `activity dropbox` or `activity interactive dropbox` (keep any other modifiers). BLL: keep the button, no `dropbox` modifier. BLLR is not BLL.
- **Supersedes:** the `01F` sentence saying the modifier applies to BLL modules only (stale; never the intended rule)
- **KB rule:** `00D` constraint 43; `05_COMP_LANGUAGE_MEDIA_LAYOUT/05B` → Activities
- **PageForge status:** Not yet amalgamated

### CL-0139 — Every task interactive inside an activity box; tools exempt
- **Date:** Wednesday, 21st October, 2026
- **Scope:** (c) Universal
- **Source:** ADMIN MODE (authorised) — direct-typed
- **Writer input (what triggers it):** a task interactive tag (drag and drop, any quiz, self check, game, ordering, slider, sketcher) — including one the writer placed outside any `[Activity …]`.
- **Required output:** the widget always sits inside `<div class="activity interactive" number="…">`. An untagged one gets its own activity with the next consecutive number, the following activities renumbered, and one visible `<p style="color: red; font-weight: bold;">Red Flag: …</p>` at the top of the new box. Stop watch and number line (tools) need no activity box. Display components unchanged.
- **Supersedes:** —
- **KB rule:** `03_COMP_CORE_INTERACTIVES/03A` → Universal Rules; `00H` constraint 8
- **PageForge status:** Not yet amalgamated
