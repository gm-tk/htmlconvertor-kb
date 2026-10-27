> **Last updated:** Tuesday, 27th October, 2026 2:44 PM
> **Granular part G (15 of 16) of `12_CHANGE_LEDGER.md`** — the PageForge Amalgamation Log: its rules (WHY / WHAT GOES IN / ENTRY FORMAT / BACKFILL) and the entries CL-0089 to CL-0115. **CLOSED at CL-0115 on 27 October 2026** (the next entries would have taken it past the 30 KB soft limit, `CLAUDE.md` §4); the filename is kept because twelve files cite it as the log's home. **New entries go in `12H_PAGEFORGE_AMALGAMATION_LOG_CL0116_ONWARD.md` — THE OPEN PART.**
> All sibling parts live in `12_CHANGE_LEDGER/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# PART 4 — THE PAGEFORGE AMALGAMATION LOG

> **When to load:** At the end of any **Admin Mode** (`17_ADMIN_MODE.md`) or **Update Mode** (`11_UPDATE_MODE.md`) run in which at least one actioned change is **front-facing** — i.e. it changes the generated HTML or CSS. Conversion, Comparison, Split, Interactives, Support and **PageForge Compare** modes never read or write this log — Mode 7 reports PageForge's faults on ONE module to Gavin, which is a different artefact from this standing record of what PageForge must be taught in general (`17_ADMIN_MODE.md` → Section 11).

---

## WHY THIS LOG EXISTS

**PageForge** — the standalone HTML Generator (`pageforge-site` / `CONVERTER_V2`) — is being developed to do automatically what this project does by instruction. The two must eventually agree: every decision made here about **what the finished module looks like** is a decision PageForge will have to mirror, or the same Writers Template will produce two different modules depending on which tool built it.

Those decisions are already recorded in **Part 3 (Change History)** — but Part 3 is an *audit trail*. Its rows are written to answer "what was decided, by whom, when, and what did it displace", and they are interleaved with mechanism changes that PageForge has no equivalent of (chat wording, mode triage, ledger machinery, repo housekeeping). A PageForge developer picking the thread up months later should not have to read the whole audit history and sort the relevant rows out of it.

**This log is that sorted, implementable subset**: front-facing decisions only, newest last, each written so it can be built from without reading the rest of the knowledge base.

**Nothing in this log obliges anyone to change PageForge now.** No mode in this project ever edits PageForge's code, and writing an entry here is not a work order. The log is a **standing record for a future amalgamation pass**, at whatever time PageForge development next takes it up.

---

## WHAT GOES IN — THE FRONT-FACING TEST

> **Would a developer comparing two generated modules — one built before the change, one after, from the same Writers Template — see any difference in the HTML or CSS?**

- **YES → log it here** (as well as in Part 3).
- **NO → Part 3 only.**
- **Borderline → log it here.** An unnecessary entry costs one block; a missing one costs PageForge a silent divergence.

**IN (front-facing):** which element a writer tag becomes · what content appears, is omitted or is added · nesting, wrappers, grid/column structure · page scaffold, head, header, footer, menus · page boundaries and page-to-file mapping · class names, ids, data attributes, answer-key attributes, component defaults (`autoCheck`, shuffle, …) · any CSS-affecting or layout rule · titles and headings · red flags, `Writers Note:`, `Note from {author}:` and `Designer/Developer To Do:` messages *as rendered into the page* · acknowledgements format and placement · image output modes and alt text · interactive build rules · subject global parameters (`14`) that alter output.

**OUT (mechanism — Part 3 only):** mode definitions, triggers and triage · what the Convertor *says in the chat* (progress messages, verification reporting, summaries, phrasing to a designer) · how the knowledge base is structured, split, indexed or committed · intake, conflict-checking, ledger and approval machinery · which files to load for which task.

The full statement of the two lanes is `17_ADMIN_MODE.md` → Section 5.

---

## ENTRY FORMAT

One block per decision, **appended in CL order, newest last**. The `CL-nnnn` id is the same id the change carries in Part 3 — never a separate numbering.

```
### CL-nnnn — <one-line title of the decision>
- **Date:** Weekday, Dth Month, YYYY
- **Scope:** (a/b/c) + the resolved breadth in plain English
- **Source:** ADMIN MODE (authorised — <who>) | UPDATE MODE (finalized difference report <ref>) | UPDATE MODE (direct-typed)
- **Writer input (what triggers it):** the tag, pattern or condition in the Writers Template / Media List that this rule reacts to
- **Required output:** exactly what the Convertor now produces — the markup itself where it is short enough to quote
- **Supersedes:** CL-nnnn (what it replaced) — or `—`
- **KB rule:** the part file(s) and constraint number that own this rule
- **PageForge status:** Not yet amalgamated | Amalgamated (date, round)
```

**Rules for maintaining it:**

- **Append-only.** Never rewrite or delete an entry. A later decision that changes an earlier one is a **new entry** naming the earlier in its `Supersedes:` line; the superseded entry stays, and its `PageForge status:` is left as it was.
- **`PageForge status:` is the only field ever edited in place** — updated to `Amalgamated (date, round)` when a PageForge development round implements the rule.
- **Split at 30 KB.** When the open part passes the soft limit, close it to its CL range and open the next part (`12I_…_CLnnnn_ONWARD.md`) per the repo `CLAUDE.md` §4, updating `INDEX.md` for both. *(Done once already: this part closed at CL-0115 on 27 October 2026 and `12H_PAGEFORGE_AMALGAMATION_LOG_CL0116_ONWARD.md` is the open part — the rules above still govern every part.)*
- Every run that touches this part refreshes its header `Last updated` stamp.

---

## BACKFILL NOTE — THIS LOG STARTS AT CL-0086

The log was created on **Friday, 28th August, 2026** (`CL-0087`). Decisions **CL-0001 to CL-0085** predate it, and many of them are front-facing — they are all recorded in the **Part 3 history parts** (`12B` through `12E5`), which remain complete and authoritative.

Backfilling them into this format is a **separate, one-off pass** that has not been run. It is not automatic and no mode performs it in passing. When PageForge development is ready to amalgamate, either run that backfill as its own Admin Mode round, or read Part 3 directly for anything earlier than `CL-0086`. **Do not assume this log is the complete front-facing history until that backfill is recorded here.**

---

## LOG

The first entries were appended on Friday, 28th August, 2026 (CL-0089 to CL-0091). The log was created on Friday, 28th August, 2026 and the round that created it (`CL-0086` to `CL-0088`) contained **no front-facing change** — Admin Mode itself, this log, and the designer-facing output policy are all Lane 1 mechanism changes (`17_ADMIN_MODE.md` → Section 5.2), so none of them is entered here. The next Admin Mode or Update Mode run that changes the generated HTML or CSS appends its entry below, in CL order.

Append new entries below this line, in CL order, newest last, using the format above.

### CL-0089 — `learningSupport` on `<html>` is driven by an `X` module-code prefix
- **Date:** Friday, 28th August, 2026
- **Scope:** Cohort — every module whose code begins with the letter `X`
- **Source:** ADMIN MODE (authorised — Persephone Samuels, Design Team Lead)
- **Writer input (what triggers it):** none in the template — the trigger is the **module code itself**. First character of the code is `X` (case-sensitive): LS, XLP, XDLS, XFUN, XWHA, XMES, XTAS and any future X-prefixed series.
- **Required output:** `learningSupport` appended to the `<html>` class list on **every page** of the module, e.g. `<html lang="en" level="" template="NCEA" class="notranslate learningSupport" translate="no">`. Appended, never replacing `notranslate`; `template=` is unchanged and still derived from the code. Non-X-prefixed code → class NOT emitted (unless a Mode B sibling carries it, in which case follow the sibling and emit a `Red Flag:`). The larger font is the stylesheet's response to the class — emit **no** font-size CSS and **no** inline font style.
- **Supersedes:** — (extends CL-0020, which required the class for LS but left identification to the reference files)
- **KB rule:** `06_TEMPLATE_RECOGNITION.md` §4.4 / §2 / §5; `14_SUBJECT_GLOBAL_PARAMETERS/14B_SGP_FAMILIES_6_11.md` §14.6; `00_MASTER_INSTRUCTIONS/00H_CONSTRAINTS_4.md` constraint 89
- **PageForge status:** Not yet amalgamated

### CL-0090 — acks: `acksTemplate` / `acksAI` generate three statements; never emit them as text
- **Date:** Friday, 28th August, 2026
- **Scope:** (c) Universal — every module, every conversion route (PageForge `.txt`, raw Writers Template `.docx`, MTK `.docx`)
- **Source:** ADMIN MODE (authorised — Persephone Samuels, Design Team Lead)
- **Writer input (what triggers it):** none — this is unconditional acknowledgements-block construction. It applies to every module that emits an acks block, i.e. every module (constraint 33: bottom of the overview page, after the footer).
- **Required output:** the wrapper is `<div class="acks acksTemplate">`, or `<div class="acks acksTemplate acksAI">` where the module has AI-generated or AI-requested media (constraint 72). Inside `accContent`, emit **only** the per-page media `acksLesson` divs (each opening `<!-- Lesson N.N -->`, constraint 73) followed by ONE unlabelled boilerplate div:
```html
  <div class="acksLesson">
      <p>All other images © Te Aho o Te Kura Pounamu, Wellington, New Zealand.</p>
  </div>
```
  Emit **NO** `<p>` containing any of the following — the template generates all three, and typing them double-ups the statement on the published page:
  - *Every effort has been made to acknowledge and contact copyright holders. Te Aho o Te Kura Pounamu apologises for any omissions and welcomes more accurate information.* (from `acksTemplate`)
  - *Parts of this resource were created with assistance from AI tools. For more information on the extent and nature of this AI usage, please contact Te Aho o Te Kura Pounamu.* (from `acksAI`)
  - *Copyright © [year] Board of Trustees of Te Aho o Te Kura Pounamu, Private Bag 39992, Wellington Mail Centre, Lower Hutt 5045, New Zealand. All rights reserved. No part of this publication may be reproduced or transmitted in any form or by any means without the written permission of Te Aho o Te Kura Pounamu.* (from `acksTemplate`)
  `<span class="currentYear"></span>` must not appear anywhere in the block — it belonged only to the typed copyright line. Reported example of the incorrect double-up: `WJFUN105_0.0.html`.
- **Supersedes:** —
- **KB rule:** `05_COMP_LANGUAGE_MEDIA_LAYOUT/05C_COMP14_ACKNOWLEDGEMENTS.md` → Basic block / Accordion structure / Structure notes; `07_MTK_DOCX_CONVERSION/07C`, `07D`; `00_MASTER_INSTRUCTIONS/00H_CONSTRAINTS_4.md` constraint 90
- **PageForge status:** Not yet amalgamated

### CL-0091 — iStock ID is the FIRST (gm-leading) number, never the trailing segment
- **Date:** Friday, 28th August, 2026
- **Scope:** (c) Universal
- **Source:** ADMIN MODE (authorised — Persephone Samuels, Design Team Lead)
- **Writer input (what triggers it):** any iStock asset URL in the Writers Template, Media List, or iStock acknowledgements file. Current format is dual-ID — `…/photo/{slug}-gm{A}-{B}` (e.g. `gm2219277340-935873810`); the legacy format carries one number, `gm{A}`.
- **Required output:** the ID is **`A`**, the number immediately following `gm` — equal to the asset page's **"Stock photo ID"** field and the preview watermark. Extraction aid: `gm(\d+)(?:-\d+)?`, capture group 1. The trailing `B` is a secondary catalogue identifier and is **NEVER** used. The same `A` must appear in all three places for a given asset: the Mode D / Mode P filename `images/iStock-{A}.jpg`, the acknowledgements citation `iStock {A}`, and the key used to match a line in a supplied iStock acknowledgements file (matching on `B` falsely reports "no matching line" and raises a spurious red flag). **Position decides — never digit count, recency, or proximity to the query string.**
- **Supersedes:** — (originating decision CL-0029, 14 July 2026, unchanged and still in force; this entry carries it into the log, which begins at CL-0086)
- **KB rule:** `00_MASTER_INSTRUCTIONS/00E_CONSTRAINTS_2.md` constraint 61; `01_PIPELINE_EXTRACTION_TAGS/01E_TAG_INTERPRETATION.md` (Mode D + Mode P filename construction); `01C` (iStock Acknowledgements File → How To Use It); `05C` (Entry format → iStock ID consistency); `02C` (iStock ID cross-check)
- **PageForge status:** Not yet amalgamated

### CL-0093 — Japanese, Chinese and pinyin text must carry `jp-text` / `ch-text` / `pinyin`, everywhere
- **Date:** Sunday, 13th September, 2026
- **Scope:** (c) Universal
- **Source:** ADMIN MODE (authorised — design-team instruction relayed to Gavin)
- **Writer input (what triggers it):** any run of Japanese text (hiragana, katakana, kanji), Chinese text (Han characters, simplified or traditional) or pinyin (romanised Chinese, with or without tone marks) anywhere in the content source — body prose, headings, list items, table cells, or the `[TITLE BAR]` title itself.
- **Required output:** every such run is wrapped in its class — `jp-text`, `ch-text`, `pinyin` — with the **whole run** inside the wrapper including its internal punctuation (`<span class="ch-text">他(她)是我的(哥哥/弟弟/姐姐/妹妹</span>`, `<span class="pinyin">Tā jīntiān bā suì.</span>`) and surrounding English outside it. The class sits on a `<span>` around the run **or** directly on an inline element containing only that run — `<b class="ch-text">x</b>`, `<span class="ch-text"><b>x</b></span>`, `<b><span class="ch-text">x</span></b>` are all valid. Inside an `<h1>` header title it nests within the title `<span>`. A colour class is appended in the same attribute (`class="jp-text green-text"`), never substituted. **Detection:** kana ⇒ Japanese always. **Han characters are shared and cannot be separated by character range** — take the class from the module's language (JPN/JPNFUN ⇒ `jp-text`, CH/CHFUN ⇒ `ch-text`); bilingual or undeterminable ⇒ red flag, no guess. **Pinyin vs te reo Māori:** `ā ē ī ō ū` are shared and decide nothing — pinyin requires a non-te-reo tone mark (`á ǎ à`, `ü`, `ǖǘǚǜ`), adjacency to the Chinese it romanises, or a writer label; te reo and English words are **never** wrapped; ambiguous romanisation is left bare with a red flag.
- **Supersedes:** — (the `05A` five-class table is pre-ledger documentation, extended not reversed)
- **KB rule:** `05_COMP_LANGUAGE_MEDIA_LAYOUT/05A_COMP12_13_LANGUAGE_MEDIA.md` → Language Fonts; `00_MASTER_INSTRUCTIONS/00H_CONSTRAINTS_4.md` constraint 92; `02_DATA_CONTENT_VERIFICATION/02C_VERIFICATION_CHECKLIST.md` → Language Fonts
- **PageForge status:** Not yet amalgamated

### CL-0094 — AI Guidelines PDF renamed: *Responding to Suspected Use in Assessments*
- **Date:** Sunday, 13th September, 2026
- **Scope:** (c) Universal
- **Source:** ADMIN MODE (authorised — Central Files naming change relayed to Gavin)
- **Writer input (what triggers it):** the *Responding to Suspected Use* AI Guidelines tag in a Writers Template, in either its current form `[Kaimahi AI Guidelines- Responding to Suspected Use in Assessments PDF]` or its retired form `[Kaimahi AI Guidelines - Responding to Suspected use in Assessments for Years 11-13 and NCEA PDF]` (still matched — templates in flight carry it).
- **Required output:** the `embedPDF` / `centralFile` block with the **new** filename in both positions, and the retired filename nowhere:
  ```html
  <div class="embedPDF" layout="portrait">
  <object class="centralFile" data="AI-guidelines/Kaimahi AI Guidelines Responding to Suspected Use in Assessments.pdf#view=fit&amp;toolbar=0" type="application/pdf">
  <p>Unable to display PDF file. <a href="AI-guidelines/Kaimahi AI Guidelines Responding to Suspected Use in Assessments.pdf" target="_blank" class="centralFile">Download</a> here</p>
  </object>
  </div>
  ```
  **No hyphen** after `Guidelines` in the filename (the tag keeps an unspaced one — do not carry it across), **no year range**, **capital `Use`**. The old path `AI-guidelines/Kaimahi AI Guidelines - Responding to Suspected use in Assessments for Years 11–13 and NCEA.pdf` no longer resolves on the server: any module still emitting it has a broken embed. The other seven assets, `layout="portrait"`, the `&amp;` entity, the unencoded path spaces and the verbatim fallback paragraph are all unchanged.
- **Supersedes:** CL-0084 (21 August 2026) — one registry row only; the rest of CL-0084 stands in full.
- **KB rule:** `05_COMP_LANGUAGE_MEDIA_LAYOUT/05A_COMP12_13_LANGUAGE_MEDIA.md` → AI Guidelines PDFs (registry + RENAMED/RETIRED note); `00_MASTER_INSTRUCTIONS/00G_CONSTRAINTS_3.md` constraint 84 (amended); `01D` Media tag taxonomy; `01E` Media → AI Guidelines PDFs; `02C`
- **PageForge status:** Not yet amalgamated

### CL-0095 — Strip a leading label prefix (e.g. `FUNdamental:`) from a body heading
- **Date:** Sunday, 13th September, 2026
- **Scope:** (c) Universal
- **Source:** Finalized difference report — `WJFUN112`, Difference 1
- **Writer input (what triggers it):** a body heading opening with a label and a colon where the text after the colon is the module's or lesson's `<h1>` header title — reported case: body `[H1]`/`[H2]` `FUNdamental: Audience and Purpose` under the header title `Audience and Purpose`.
- **Required output:** the label and its colon removed, the heading emitted bare — `<h2>Audience and Purpose</h2>`. **Boundary (this is the part that must not be over-applied):** strip only the documented labels — any `Lesson N` form, and `FUNdamental:` — or a short leading `Word:` / `Word Word:` label whose remainder is **identical** (ignoring case and punctuation) to the `<h1>` header title. If stripping does not leave the header title, it is not a label: emit the heading unchanged. Never strip a meaning-bearing colon (`Activity 2: Commas in lists`, `Links to: …`). **Strip, then drop, as two steps:** on an introduction/overview page the stripped heading is **kept**; on a lesson page it then meets the existing duplicate-heading rule and is dropped if it now matches that lesson's own header title. No red flag, no comment — this is a format normalisation, not a wording change.
- **Supersedes:** — (extends the pre-ledger duplicate-heading rule by adding a prior step; that rule's own behaviour is unchanged)
- **KB rule:** `01_PIPELINE_EXTRACTION_TAGS/01E_TAG_INTERPRETATION.md` → Headings → label-prefix strip; `00_MASTER_INSTRUCTIONS/00D_CONSTRAINTS_1.md` constraint 1; `02_DATA_CONTENT_VERIFICATION/02C_VERIFICATION_CHECKLIST.md` → Headings & Titles
- **PageForge status:** Not yet amalgamated

### CL-0109 — The writing font is `writeFont`; sassoon classes are legacy (never emitted, never removed)
- **Date:** Wednesday, 23rd September, 2026
- **Scope:** (c) Universal
- **Source:** claude-audit decisions (Chris, 23 September 2026) — kickoff Phase 1, brief A; design-team Teams thread 2–4 September 2026; `writeFont.html`
- **Writer input (what triggers it):** any place a writing / handwriting font is called for — a BLL / phase-1 interactive or text the ākonga reads or writes, a letter grid, a memory-game text card, a typing quiz — and the new writer tag `[writing font]` (aliases `handwriting font`, `write font`).
- **Required output:** class `writeFont` on the element holding the text (`<p class="memText writeFont">`, `<td class="writeFont">`, `class="crossword row writeFont"`); `writeFontGuide` / `writeFontCursive` / `writeFontCursiveGuide` / `writeFontLinked` / `writeFontLinkedGuide` only where the Writers Template names them. `sassoon-text` / `sassoonI-text` / `sassoonIB-text` are never emitted in a new build and never stripped from an existing one.
- **Supersedes:** the sassoon guidance of CL-0021 (BLL writing font) and the pre-ledger `05A` / `03E` / `03D` examples
- **KB rule:** `05_COMP_LANGUAGE_MEDIA_LAYOUT/05A_COMP12_13_LANGUAGE_MEDIA.md` → Writing Font; `00_MASTER_INSTRUCTIONS/00H_CONSTRAINTS_4.md` constraint 93; `01D` / `01F` `writing_font`
- **PageForge status:** Not yet amalgamated

### CL-0110 — Fundamentals: plain intro + content panels numbered from 1
- **Date:** Wednesday, 23rd September, 2026
- **Scope:** (a) Template — Fundamentals
- **Source:** claude-audit decisions (Chris, 23 September 2026) — kickoff Phase 1, brief A (answer 2)
- **Writer input (what triggers it):** a Fundamentals-template module.
- **Required output:** `<div class="introduction">` (no phase attribute) holding the `row phaseContainer` tile row; content panels `<div class="fundamentalsPanel" phase="1">` … N; tiles `phaseLink phase="1"` …; `noPhase` on `phaseContainer`, or on the body's `fundamentals` class where there is no `phaseContainer`. The older `introduction fundamentalsPanel phase="1"` form only where a same-series sibling uses it. **Never `phase="0"`.**
- **Supersedes:** — (pre-ledger `06` §3.3 wording, which described the minority HPFUN form)
- **KB rule:** `06_TEMPLATE_RECOGNITION.md` §3.3
- **PageForge status:** No change needed — PageForge already emits the plain-intro majority form (claude-audit answer 2, 23 September 2026)

### CL-0111 — HPE: the Health-and-Safety supervisor block, the WATER alert rule, all five characters delivered, the two-bubble rule
- **Date:** Wednesday, 23rd September, 2026
- **Scope:** (b) Cohort — HPE content lessons
- **Source:** claude-audit decisions (Chris, 23 September 2026) — kickoff Phase 1, brief A; Global Edits HPE (September 2026); `imageCentral_server_file_list.txt`
- **Writer input (what triggers it):** `[Supervisor Button RHS activity] [H4] Guidance for supervisors [Body] … [End supervisor button]` on an HPE activity; water-safety content; a character reference; a character conversation longer than two bubbles.
- **Required output:** the supervisor block as the Shape A (activity-bound) supervisor button, wording verbatim; water-safety content in a visible `alert`, never behind the supervisor button; every character image as a real `imageCentral` reference (`health & PE characters/phase #/HP_<Name>_<pose>_phase_#.png`, head-only under `head_only/`, pairs under `phase 1/combination/` — filenames copied from the server list) with **no** missing-character `Designer/Developer To Do:` note; beyond two bubbles, faces only, and a longer conversation in a carousel.
- **Supersedes:** CL-0067's availability note (the missing-character To Do)
- **KB rule:** `14_SUBJECT_GLOBAL_PARAMETERS/14B_SGP_FAMILIES_6_11.md` §14.8
- **PageForge status:** Not yet amalgamated (the SGP 14.8 family is CAPTURED-INERT; its text is refreshed in the same kickoff's Phase 3b)

### CL-0112 — Languages: central language icons, the Samoan phrase images, the Spanish un-numbered family tree
- **Date:** Wednesday, 23rd September, 2026
- **Scope:** (b) Cohort — Languages
- **Source:** claude-audit decisions (Chris, 23 September 2026) — kickoff Phase 1, brief A; `languages_html_versions/current.html`; `imageCentral_server_file_list.txt`
- **Writer input (what triggers it):** `[Audiovisual package Icon <Name>]`; a Samoan phrase-image reference; the Spanish family tree without numbers.
- **Required output:** `<img class="img-fluid imageCentral" loading="lazy" src="Language icons/Language icons_<Name>.jpg" alt="…" />` (phase-coloured `… P1.jpg`–`P4.jpg` only when named; the server's mixed case verbatim); never `images/Icons/black icons/…` or `images/Icons/phase colour/…`. Samoan: `Samoan character assets/Samoan_<phrase>.jpg` (19 files, `14C` §8). Spanish: `Spanish assets/Spanish_Family tree_no numbers.jpg`. Never the Felix 'Co-pilot test' images.
- **Supersedes:** CL-0070's icon path (`images/Icons/…`)
- **KB rule:** `14_SUBJECT_GLOBAL_PARAMETERS/14C_LANGUAGES_AV_ASSET_REGISTRY.md` §2, §3, §7, §8; `14A` §14.1
- **PageForge status:** Not yet amalgamated (inert 14.1 family refreshed in Phase 3b)

### CL-0113 — BLLR bookworms + the bookshelf, MiW kea + the writing process, Pathways personas: deferrals retired
- **Date:** Wednesday, 23rd September, 2026
- **Scope:** (b) Module-series — BLLR, MiW, Pathways
- **Source:** claude-audit decisions (Chris, 23 September 2026) — kickoff Phase 1, brief A; `bookshelf.html`, `refresh_pathwaysPersonas.html`, `writingProcess.html`; `imageCentral_server_file_list.txt`
- **Writer input (what triggers it):** a BLLR bookworm or secret-shelf reference; a MiW kea or writing-process reference; a Pathways `[Persona box]`.
- **Required output:** real `imageCentral` references with no art To Do note — `bookworms/bookworm_N.jpg`, `kea_characters/kea_N.jpg` (+ `customKea/…`), `pathwaysPersonas/<name>.jpg`; the `bookshelf` markup (`div.bookshelf.row > div.shelf > div.bookCover`, one `bookContent` carousel per cover); `<div class="writingProcess" phase="…">` / `singleStage stage="…"` in its own row; the `pathwaysPersona` markup (`id` = audio filename, empty buttons, inside a row and col, optional `noAudio`). Audio To Do notes stay for bookworm and kea audio; the Whispering Archives red note stays. Kea 5: the server's `Kea_5.jpg` vs the modules' `kea_5.jpg` is unresolved — follow the modules and raise a Red Flag.
- **Supersedes:** the bookworm and secret-shelf deferrals of CL-0024 (§14.9), the kea-art deferral of CL-0025 (§14.10) and the persona deferral of CL-0016 (§14.2)
- **KB rule:** `14_SUBJECT_GLOBAL_PARAMETERS/14B2_SGP_FAMILIES_BLLR_MIW.md` §14.9, §14.10; `14A` §14.2
- **PageForge status:** Not yet amalgamated (inert SGP families refreshed in Phase 3b)

### CL-0114 — `[thought bubble]` / `[thinking speech bubble]` builds `speechBubble layout="thought"`
- **Date:** Wednesday, 23rd September, 2026
- **Scope:** (c) Universal
- **Source:** claude-audit decisions (Chris, 23 September 2026) — kickoff Phase 1, brief A (answer 7 re-check)
- **Writer input (what triggers it):** `[thought bubble]`, `[thinking speech bubble]`, `[green thought bubble]` and similar.
- **Required output:** `<div class="row speechBubble" layout="thought">` with the standard bubble children; no thought-bubble red flag.
- **Supersedes:** — (the pre-ledger `04C` Writer Tag Variants row that asked for a red flag)
- **KB rule:** `04_COMP_SEGMENTS_OVERLAYS/04C_COMP09_10_11_BUBBLES_DIAGRAMS_TOOLS.md` → COMP_09 → Writer Tag Variants
- **PageForge status:** Amalgamated (pre-existing — the `thought bubble` lexicon family already builds `layout="thought"`; verified 23 September 2026)

### CL-0115 — Equations: output is always MathML, whatever the input form
- **Date:** Wednesday, 23rd September, 2026
- **Scope:** (c) Universal
- **Source:** claude-audit decisions (Chris, 23 September 2026) — kickoff Phase 1, brief A (answer 3 — the owed D10-7 edit)
- **Writer input (what triggers it):** a Word equation (OMML); LaTeX typed as text (`\( … \)`, `\[ … \]`, `\frac`, `$…$`); pasted MathML; a `[Math]` / `[Mathjax]`-tagged plain expression (`[Math] 4/5`).
- **Required output:** `<math xmlns="http://www.w3.org/1998/Math/MathML">…</math>` (`display="block"` when displayed) and `mathJax` on the `<body>` class; LaTeX optionally kept in an HTML comment beside it; never raw LaTeX or a bare `[Mathjax]` tag as visible text.
- **Supersedes:** — (the pre-ledger `05A` LaTeX-output example)
- **KB rule:** `05_COMP_LANGUAGE_MEDIA_LAYOUT/05A_COMP12_13_LANGUAGE_MEDIA.md` → MathJax / Equations
- **PageForge status:** Partly amalgamated — OMML → MathML is live (`MATHML_OFF`); LaTeX-text and `[Math]`-fraction inputs are a future round

---

> **This part is CLOSED at CL-0115.** Entries from CL-0116 continue in `12H_PAGEFORGE_AMALGAMATION_LOG_CL0116_ONWARD.md`, in the format above.
