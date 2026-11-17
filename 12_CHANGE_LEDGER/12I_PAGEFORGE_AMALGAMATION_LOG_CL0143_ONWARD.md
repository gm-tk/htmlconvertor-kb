> **Last updated:** Tuesday, 17th November, 2026 7:41 PM
> **Granular part I (20 of 20) of `12_CHANGE_LEDGER.md`** — PART 4, the PageForge Amalgamation Log, continued: entries CL-0143 onward. **THE OPEN PART: append new entries here**, in CL order, newest last, in the ENTRY FORMAT set out in `12G` (whose WHY / WHAT GOES IN / ENTRY FORMAT / BACKFILL sections govern every part of this log). Opened 17 November 2026 when the ledger merge CL-0144 took `12H` past the 30 KB soft limit; `12H` was closed at CL-0141 and its last entry, CL-0143, moved here verbatim (`CLAUDE.md` §4).
> All sibling parts live in `12_CHANGE_LEDGER/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# PART 4 — THE PAGEFORGE AMALGAMATION LOG (continued from `12H`: CL-0143 onward)

> The rules of this log — the front-facing test, the entry format, append-only, `PageForge status:` the only field edited in place — are in `12G_PAGEFORGE_AMALGAMATION_LOG.md` and are not repeated here.

### CL-0143 — The Pathways Assessment Activities Template (Level 1 Pathways unit-standard assessment pages)
- **Date:** Sunday, 15th November, 2026
- **Scope:** (a) Series + level — Pathways Level 1 unit-standard assessments (Assessment Mode single pages, not modules)
- **Source:** ADMIN MODE (authorised — Gavin, relaying Persephone Samuels, Design Team Lead, 12 November 2026: *"update the assessments pageforge for specifically pathways"*; `Pathways Assessment Activities Template.docx` from Stephanie Charles via Kate Scanlon)
- **Writer input (what triggers it):** an NCEA Assessment Activity `.docx` with `Subject:` Pathways and a `Classification` row or the `Option 1: Separate assessment document` / `Option 2: Instructions included in this assessment` lines; within it `[Centralised image: AI traffic light - red]`, `[Button] Go to assessment`, `[Link to module] PWY1009`, one-cell `Example` boxes, the colour-key note and bracketed red instructions.
- **Required output:** header bar — `Activity name:` → `<h3>`, `Classification` → the `<p>` beneath (`&gt;` escaped), `<p class="standard"><b>US{nnnn} (Version {v}), Pathways</b></p>`, `Title:` → `<p class="description">`, credits line always `Level {n} Internal Assessment`, level from the module code (default 1); the note line, Example boxes, Option labels, `OR`, the stray `.` and replaced bracketed instructions emit nothing (an unreplaced one → `Red Flag:`); Option 1 → `<p>Complete the tasks in the Word document linked below.</p>` + `<a href="https://tekura.desire2learn.com/shared/assessment/NCEA%20Level%20{n}/{COURSE}/{CODE}/pdf/{code}-assessment.docx" target="_blank" rel="noopener"><div class="button">Go to assessment</div></a>` + upload To Do; Option 2 → `<p>Complete the tasks that follow.</p>` + tasks; both → both + `Red Flag:`; AI traffic light → `Designer/Developer To Do:` red note at that spot (no `<img>` until the central path is registered); `[Link to module]` → `<a href="" target="_blank" rel="noopener"><div class="button">{module code}</div></a>` + To Do; dropbox `<h3>` = standard code and the writer's full dropbox text (`<p>`, `<p>Make sure:</p>`, `<ul>`) before the quickLink button.
- **Supersedes:** for these documents only — the general `18A` §4.1 header-bar mapping, `18B` §6.6 (cited module code = plain text) and the skeleton's single `{dropbox body}` paragraph
- **KB rule:** `18_ASSESSMENT_MODE/18D_PATHWAYS_ASSESSMENT_TEMPLATE.md`; `00H` constraint 100
- **PageForge status:** Not yet amalgamated — PageForge's assessment generator is the target the source email names

### CL-0145 — The warning alert (`[Alert warning]` / `[Safety Alert]`)
- **Date:** Tuesday, 17th November, 2026
- **Scope:** (c) Universal
- **Source:** ADMIN MODE (authorised — Gavin, 17 November 2026; Design Team Lead's request of 10 Nov, Sam Sharpe's `new-alert-warning-code.html` of 17 Nov)
- **Writer input (what triggers it):** `[Alert warning]`, `[Safety Alert]` (case-insensitive; hyphen/space variants), optional `[H4]` heading, body, optional `[button]` / `[external link]` / click-drop.
- **Required output:** `<div class="row"><div class="col-md-8 col-12"><div class="alert warning"><div class="row"><div class="col-12">[<h4>heading</h4>]<p>…</p>[buttons]</div></div></div></div></div>` at page level; inside an activity the `div.alert.warning` block sits in the activity's content column. No colour class, inline style or icon element. No invented heading.
- **Supersedes:** HPE WATER rule's "a visible `alert`" (now `alert warning`)
- **KB rule:** `05B` → Warning Alert; `00H` constraint 101; `01D`; `01F`
- **PageForge status:** Not yet amalgamated

### CL-0146 — HPE — `[Safety Alert]` before the supervisor button; WATER → the warning alert; The Hub; the `[image Centralised Ph<N> <Name>]` tag
- **Date:** Tuesday, 17th November, 2026
- **Scope:** Cohort (HPE content lessons)
- **Source:** ADMIN MODE (authorised — Gavin, 17 November 2026; *Global Edits HPE*, re-exported 16 November 2026)
- **Writer input (what triggers it):** `[Safety Alert] [Supervisor Button RHS activity] [H4] Guidance for supervisors …`; water-safety content; `[floating nav]`; `[image Centralised Ph1 Sura]` (phase and character, no pose).
- **Required output:** The warning alert (`div.alert.warning`, CL-0145) first, then the supervisor button (Shape A, constraint 68); water-safety content in a `div.alert.warning` in the lesson body, never behind the supervisor button; sticky nav links **Fundamentals** and **The Hub**; `[image Centralised Ph1 Sura]` → `<img class="img-fluid imageCentral" loading="lazy" src="health & PE characters/phase 1/HP_Sura_1_phase_1.png" alt="">` + a `Designer/Developer To Do:` to confirm the pose; a pose named in the tag builds with no note.
- **Supersedes:** CL-0111's WATER wording ("a visible `alert`"); the nav label "Help page" (now The Hub)
- **KB rule:** `14B` §14.8; `14F` §14.16 (Health and PE characters)
- **PageForge status:** Not yet amalgamated

### CL-0147 — Social Sciences — a new §14 family (§14.17)
- **Date:** Tuesday, 17th November, 2026
- **Scope:** Cohort (Social Sciences)
- **Source:** ADMIN MODE (authorised — Gavin, 17 November 2026; *Global Edits Soc Sci*, re-exported 16 November 2026)
- **Writer input (what triggers it):** `[Subject code] [H1]`; `[Overview] [tab] [H4] …`; `[Whakataukī]`; `[Alert]` (fundamental links, lesson introduction, lesson summary with `[Checklist]` and `[Hint Button] [Title] Need help?`); `[RHS alert]` in an activity; `[Image] [Speech bubble]`; `[Think about it alert] … [Button] Reveal`; `[Safety Alert]`; `[Alert blank] [H3] Sensitive content`; `[Dropbox] … [Button] Go to your journal [Button] Upload to dropbox`; `[Hint Button] [Title] Capability spotlight`; `[H1] Congratulations!` + `[RHS image] [Centralised image Congratulations]`.
- **Required output:** Ordinary `alert`s for the fundamental links, lesson introduction and lesson summary (success criteria as a checkbox list; a `hint` titled *Need help?* holding the kaiako paragraph as written); `[RHS alert]` → the activity sidebar; speech bubble with the writer's image (no `imageCentral`); *Think about it* → an `alert` with `<h3>Think about it</h3>`, the questions and the reveal (hint / clickDrop pattern; `Red Flag:` where the shape is uncertain); `[Safety Alert]` → `div.alert.warning`; *Sensitive content* → `alert blank` with the writer's `<h3>` and body at the top of the item; checkpoint dropbox with the §14.8 phase 1–4 copy and the *Upload to dropbox* label; *Capability spotlight* → a `hint`; module summary page with no overview, the text column beside `congradulations/Congradulations animation.gif` (`imageCentral`).
- **Supersedes:** —
- **KB rule:** `14G` §14.17
- **PageForge status:** Not yet amalgamated

### CL-0148 — Technology — §14.12 expanded (TEFUN, `[Tech Banner]`, new strand names, floating nav, activity choices, resource links, TENZ, characters) + §14.16 tag aliases
- **Date:** Tuesday, 17th November, 2026
- **Scope:** Cohort (Technology)
- **Source:** ADMIN MODE (authorised — Gavin, 17 November 2026; *Global Edits Technology* and the *TENZ Design Thinking Icons/Images List*, re-exported 16 November 2026)
- **Writer input (what triggers it):** `[Tech Banner]`; `[Centralised image Spatial and Product Design]` / `… Food and Processing Technology` / `… Systems and Control` / `… Digital Technology` / `… Materials Technology`; `[floating nav]`; `[activitychoice.imageclickdrop]`, `[activitychoice.clickdrop]`, `[activity.singlemulti]`; `[alert.top] … [M.modal] [title] [PDF Link]`; `[RHS alert.lines] [M.modal]`; `[thought bubble]`; `[Centralised image Technology Matauranga māori fern]`; `[DTP Centralised Notice Blue]`, `[DTP Empathise Blue]`, `[Centralised DTP Model Blue]`; `[Image Centralised Jo]`, `[Image] 'avatar' 'Tina'`; a request for the Critical / Creative Thinkers Keys.
- **Required output:** New strand names → the existing icons by colour (red `active-Spacial-and-Design.svg`, blue `active-Materials-processing.svg`, pink `active-Electronics.svg`, green `active-Computer-Science.svg`), `alt` / caption = the new name; Materials Technology → `Designer/Developer To Do:` (no logo yet); `stickyNav` script in every `<head>` + the set-up To Do; activity-choice tags → clickDrop / `choicePage` (max 4 per choice set; `Red Flag:` where uncertain); `alert top` holding a `TKmodalButton` + a `TKmodal` with `size="M"` and the PDF; in an activity, the activity sidebar holding the modal button (no `lines` class); the thought bubble (`04` COMP_09); the `DTP` / character / fern aliases → their §14.16 images; Thinkers Keys → `Red Flag:`, never built.
- **Supersedes:** §14.12's "module-code prefix not stated" (now TEFUN); on the new five-strand list *Digital Technology* means green `active-Computer-Science.svg` (before CL-0148 it named yellow `active-Digital-Technology.svg`)
- **KB rule:** `14D` §14.12; `14F` §14.16; `01D` (Centralised image row)
- **PageForge status:** Not yet amalgamated

### CL-0149 — Science — character roles, lesson ending, equipment alert + list, practical instructions
- **Date:** Tuesday, 17th November, 2026
- **Scope:** Cohort (Science)
- **Source:** ADMIN MODE (authorised — Gavin, 17 November 2026; *Science – Global Parameters*, re-exported 16 November 2026)
- **Writer input (what triggers it):** A lesson-ending *Key Points* / *You have learned…*; `[Alert on RHS]` on the intro page; the overview's equipment list; practical *Materials:* / *Method*.
- **Required output:** The lesson-ending `alert` + success-criteria checkbox list only as the writer supplies it (never invented); the equipment reminder as a sidebar alert beside the intro content, with the supplied copy; the equipment headings as supplied (*Equipment* → *Full-time ākonga and fee-paying students* → *Dual ākonga* → *Overseas ākonga:* → *From your science box:* → *From around your home:*), the year copied as written; **Materials:** lists and a **Method** `<ol>`.
- **Supersedes:** —
- **KB rule:** `14E` §14.13
- **PageForge status:** Not yet amalgamated

### CL-0150 — Languages — Learning Systems vocabulary quizzes; floating-nav contents
- **Date:** Tuesday, 17th November, 2026
- **Scope:** Cohort (Languages Phase 1–4)
- **Source:** ADMIN MODE (authorised — Gavin, 17 November 2026; *2026 Refreshed 000 Language Global Parameters*, re-exported 16 November 2026)
- **Writer input (what triggers it):** `[Learning systems vocab quiz]` … `[Learning systems quiz end]`; `[quiz – vocab, module]` / `[quiz – vocab, course]`; `[floating nav]`.
- **Required output:** The constraint-65 MTK-quiz activity shell — title *Vocabulary quiz* unless the writer gives one; the To Do: *Learning Systems to create this vocabulary quiz (MTKQuiz question pool, `module` / `course` as tagged) from the writer's word list, then orgunit-link it and insert its quicklink*; nothing between the two tags is emitted; the `stickyNav` To Do names the links (the Fundamentals list + The Hub, or Fundamentals + The Hub + the Module Word list).
- **Supersedes:** —
- **KB rule:** `14A` §14.1
- **PageForge status:** Not yet amalgamated

### CL-0151 — Pathways — the Te Reo section titles
- **Date:** Tuesday, 17th November, 2026
- **Scope:** (a) Series + level (Pathways Level 1)
- **Source:** ADMIN MODE (authorised — Gavin, 17 November 2026; *Pathways Global Parameters Document*, re-exported 16 November 2026)
- **Writer input (what triggers it):** The Section tiles of the course navigation.
- **Required output:** Section titles *Ka haere ahau ki hea?* / *Where am I going?*, *Me pehea ahau ki reira?* / *How do I get there?*, *He aha te heke mai?* + the Writers Template's English wording for Section 3; no Te Reo To Do.
- **Supersedes:** the *Te Reo translations pending* `Designer/Developer To Do:` (§14.2)
- **KB rule:** `14A` §14.2
- **PageForge status:** Not yet amalgamated

### CL-0152 — Taonga — steps A–E (step F removed)
- **Date:** Tuesday, 17th November, 2026
- **Scope:** Cohort (Taonga)
- **Source:** ADMIN MODE (authorised — Gavin, 17 November 2026; *Essentials Global Parameters* (The Arts), re-exported 16 November 2026)
- **Writer input (what triggers it):** A Taonga lesson's steps.
- **Required output:** Steps A–E only; there is no *Links to* step.
- **Supersedes:** the A–F per-lesson layout (§14.3)
- **KB rule:** `14A` §14.3
- **PageForge status:** Not yet amalgamated

### CL-0153 — BLLR — library avatar, no zoom, reading texts, shelf placement and covers, the Whispering Archives puzzle piece
- **Date:** Tuesday, 17th November, 2026
- **Scope:** (b) Module-series (BLLR)
- **Source:** ADMIN MODE (authorised — Gavin, 17 November 2026; *All BLL Modules - Global edits* and *BLLR - Blended Literacy Global Parameters*, re-exported 16 November 2026)
- **Writer input (what triggers it):** The library-character avatar; `[image zoom]` on a BLLR text; reading texts; the secret shelf; a journal story with no cover; the end-of-module map.
- **Required output:** The video scaffold + `Designer/Developer To Do: Audiovisual item to be added by designer/developer`; no zoom built (noted in the Designer Summary); the text only, book-style carousel, a whole text's cover opening a clickDrop; the shelf on every module's intro page from the second of each suite; the story's first picture as the `bookCover` image (`bookCover blank` only where there is no picture); `<p style="color: red; font-weight: bold;">Designer/Developer To Do: Add Whispering Archives puzzle piece N (Kōwhai Quill holding it) from the BLLR EDR Puzzle folder.</p>`.
- **Supersedes:** the map's "Design is under construction" red note (§14.9)
- **KB rule:** `14B2` §14.9
- **PageForge status:** Not yet amalgamated

### CL-0154 — Maths — floating nav Fundamentals + The Hub
- **Date:** Tuesday, 17th November, 2026
- **Scope:** Cohort (Maths)
- **Source:** ADMIN MODE (authorised — Gavin, 17 November 2026; *Global Edits Maths*, re-exported 16 November 2026)
- **Writer input (what triggers it):** `[floating nav]`.
- **Required output:** `<script src="js/stickyNav.js" type="text/javascript" class="stickyNav"></script>` in every page's `<head>` + the `Designer/Developer To Do:` *set up the `stickyNav.js` file* at the top of the 0.0 content (links Fundamentals and The Hub).
- **Supersedes:** §14.14's "nothing is recorded; follow a built Maths sibling"
- **KB rule:** `14E` §14.14
- **PageForge status:** Not yet amalgamated

### CL-0155 — MTK Quiz Guidance tags — `[MTK quiz]` … `[MTK quiz end]`
- **Date:** Tuesday, 17th November, 2026
- **Scope:** (c) Universal
- **Source:** ADMIN MODE (authorised — Gavin, 17 November 2026; *MTK Quiz Guidance.docx*, design team, November 2026)
- **Writer input (what triggers it):** `[MTK quiz]` / `[MTKquiz]` / `[MTK Quiz]` … `[MTK quiz end]`, with an `[H3]` title, settings (`[Section]`, `[Triggers engagement]`, `[Number of attempts]` …), question types, grading modifiers, options and question markers between.
- **Required output:** The constraint-65 MTK quiz shell — the quiz-title `<h3>` from the `[H3]`, the writer's student-facing instructions, the To Do, the *Go to quiz* button; nothing else between the tags is emitted; ordinary content resumes after `[MTK quiz end]`.
- **Supersedes:** —
- **KB rule:** `05D` → MTK Quiz; `01D`
- **PageForge status:** Not yet amalgamated
