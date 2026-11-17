> **Last updated:** Tuesday, 17th November, 2026 7:22 PM
> **Granular part I (18 of 18) of `12_CHANGE_LEDGER.md`** — PART 4, the PageForge Amalgamation Log, continued: entries CL-0143 onward. **THE OPEN PART: append new entries here**, in CL order, newest last, in the ENTRY FORMAT set out in `12G` (whose WHY / WHAT GOES IN / ENTRY FORMAT / BACKFILL sections govern every part of this log). Opened 17 November 2026 when the ledger merge CL-0144 took `12H` past the 30 KB soft limit; `12H` was closed at CL-0141 and its last entry, CL-0143, moved here verbatim (`CLAUDE.md` §4).
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
