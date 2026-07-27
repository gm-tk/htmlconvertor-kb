> **Last updated:** Thursday, 16th July, 2026 11:05 AM

# 10 — Corpus-Validated Scaffolding Reference
 
**What this file is.** A small set of scaffolding facts measured *directly* from the finished modules in `01-Finalized_Modules_` (388 developed modules across 128 subject×phase groups; ~2,000 page files). It is **descriptive evidence**, not a new rule set — it backs up the qualitative rules in `01_PIPELINE_EXTRACTION_TAGS.md` and `06_TEMPLATE_RECOGNITION.md` with numbers, and it records the handful of *series-specific* deviations so they are treated as legitimate conventions to preserve rather than errors to "fix."
 
**How it ranks against everything else.** A supplied structural reference ALWAYS wins (Absolute Rule 7 — derive the skeleton from the reference). Use this file only (a) as a cross-check, (b) when a NEW module belongs to one of the listed series and you must match that series' house style, or (c) to decide a sensible fallback when no reference and no series precedent exist. Never use it to override a reference or to edit student content.
 
---
 
## 1. Header title casing
 
Measured across every finished module header (`#header > h1 > span`):
 
- **Multi-word titles that are ALL-CAPS: 0 of 105.** Developers never ship an all-caps multi-word title.
- The only all-caps header spans found were **single tokens** — a brand/proper noun (`STOMP`) or a stray module code (`EXPFUN02`).
**Rule (see `01` → Title casing):** a **multi-word ALL-CAPS** writer title is normalised to **sentence case** (`ROARS AND WHISPERS` → `Roars and whispers`; Te Reo the same, macrons kept). A **single** all-caps token is left as written (proper noun/acronym); if it is really a code, raise a red flag rather than printing it as the title. Titles already in mixed/sentence/title case are rendered exactly as written.
 
---
 
## 2. Menu archetype — safe fallbacks (only when no reference/series precedent)
 
- **Lesson pages → `simplified`** is dominant by a wide margin (plain `<h5>` label menu inside `#module-menu-content`). A minority of series ship **no lesson menu at all** (`none`) — see §4.
- **Overview/landing pages → `tabbed`** is the most common, **but** a large group of subjects (e.g. **BLL**, and the English strands **ENGC / ENGI / ENGR / ENGS**) use a **simplified** overview. Because overview style splits by subject, prefer the supplied reference; fall back to tabbed only when you have nothing else.
  *(Archetype only. Whenever the overview menu IS tabbed, its **tab composition** is no longer taken from the reference — it follows the canonical content-driven tab set in `01_PIPELINE_EXTRACTION_TAGS.md` → Module Menu Structures → Module Overview Pages (`-00`), constraint 67. The subject split recorded here — tabbed vs simplified vs none — still stands.)*
These are fallbacks. They are NOT a licence to invent a menu when the source and reference have none.
 
---
 
## 3. Lesson-menu *style* deviations (series conventions — preserve, don't "correct")
 
Most lesson menus use the standard plain `<h5>` labels documented in `01`/`06`. A small, stable set of **series** instead use bold `<p><b>` lead-ins and/or a leading title heading. When you see these in a reference, they are CORRECT for that series; when generating a NEW module in one of these series without a reference, match the series.
 
**Bold `<p><b>` lead-in labels (measured series):**
 
| Series / phase | Lesson-menu lead-in |
|---|---|
| OSBY — Phases 1-3, 7-8, 9-10 | `<p><b>` bold |
| OSAI — Phase 7-8 | `<p><b>` bold |
| MXEO — Phase 1-3 | `<p><b>` bold |
| XDLS — NCEA | `<p><b>` bold |
 
**Leading title heading on the lesson menu (measured series):**
 
| Series / phase | Leading title |
|---|---|
| OSBY — Phase 7-8 | `Overview` |
| OSAI — Phase 7-8 | `Lesson Overview` |
| ENG — NCEA | `Overview` |
 
Other non-standard heading habits already catalogued in `06` (do not replicate for new modules): ENGI302/401 use `<h3><span>` instead of `<h5>`; XMES/XTAS use bare `<p>` labels with no heading tag.
 
---
 
## 4. Series that ship NO lesson menu by design
 
Some series legitimately have lesson pages with **no** `#module-menu-content` (archetype `none`) — e.g. several **BLL** Phase-1 number strands, **ANZH** Phase 1-3, **ART/ENG/PHE** NCEA lesson pages. If a reference in one of these series shows an empty/absent lesson menu, that is intended — do not fabricate one. Conversely, do not suppress a menu the reference clearly contains.
 
---
 
## 5. Source-limitation note (important honesty check)
 
Lesson-menu *content* (the learning-intentions / success-criteria wording) sometimes does **not** exist anywhere in the writer source — it was authored later by the developer. When the source has no such wording and no reference supplies it, you **cannot** invent it: build the empty `#module-menu-content` shell the skeleton requires and raise a visible red flag telling the designer the lesson-menu copy needs to be supplied. This is a source gap, not a conversion error — never paper over it by guessing learning intentions.
 
---
 
*Provenance: measured from `01-Finalized_Modules_` (the finalized human corpus). Re-measure if the corpus changes substantially. This file is descriptive; the authoritative how-to rules live in `01` and `06`.*