> **Last updated:** Friday, 28th August, 2026 2:54 PM
> **Granular part G (11 of 11) of `12_CHANGE_LEDGER.md`** — the PageForge Amalgamation Log: every FRONT-FACING decision, in a form PageForge's developer can implement. THE OPEN PART: append new entries here.
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
- **Split at 30 KB.** When this part passes the soft limit, close it to its CL range and open the next part (`12H_PAGEFORGE_AMALGAMATION_LOG_CLnnnn_ONWARD.md`) per the repo `CLAUDE.md` §4, updating `INDEX.md` for both.
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
