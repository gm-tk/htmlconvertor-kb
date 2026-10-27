> **Last updated:** Tuesday, 27th October, 2026 2:44 PM
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
