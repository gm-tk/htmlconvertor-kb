> **Last updated:** Thursday, 16th July, 2026 9:30 PM
> **Granular part F (6 of 6) of `00_MASTER_INSTRUCTIONS.md`** — When to load which files.
> All sibling parts live in `00_MASTER_INSTRUCTIONS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## WHEN TO LOAD WHICH FILES
 
| Situation | Load These |
|-----------|------------|
| Determining which mode a request belongs to | `00_MASTER_INSTRUCTIONS.md` (Operating Modes) |
| The message contains `COMPARISON MODE` + uploaded finished HTML | `09_COMPARISON_MODE.md` (whole file) |
| The message contains `UPDATE MODE` (changes follow in any format) | `11_UPDATE_MODE.md` (whole file) + `12_CHANGE_LEDGER.md` (read for conflicts/locks) |
| The message contains `SPLIT MODE` (single-page module too long to emit at once) | `13_SPLIT_MODE.md` (whole file) + the normal conversion files (`01` sections 01–02, the relevant COMP files) — all conversion rules still apply |
| Converting/advising on a module in a documented subject cohort/series (Languages Phase 1–4, Pathways, Taonga, CED Phase 5, FUNdamentals H&PE, LS, BLL, BLLR, MiW/WJ, HPE content) | `14_SUBJECT_GLOBAL_PARAMETERS.md` (the relevant subject section) + the normal conversion files + `06_TEMPLATE_RECOGNITION.md` (sub-type/sibling authority) |
| Checking whether a proposed change conflicts with, or is locked by, a past decision | `12_CHANGE_LEDGER.md` + `11_UPDATE_MODE.md` (Sections 4, 6, 7) |
| A designer asks for a one-off, module-specific deviation from the documented patterns | `08_MODULE_SUPPORT_DEBUGGING.md` (One-Off Module Overrides) |
| User asks an advisory question about a component / tag / rule | `08_MODULE_SUPPORT_DEBUGGING.md` (Section 2) + the file that owns the topic |
| User pastes a half-finished module to complete | `08_MODULE_SUPPORT_DEBUGGING.md` (Section 3) + `06_TEMPLATE_RECOGNITION.md` + relevant COMP files |
| User pastes a broken interactive to debug | `08_MODULE_SUPPORT_DEBUGGING.md` (Section 4) + the relevant COMP section |
| Starting any conversion | `01_PIPELINE_EXTRACTION_TAGS.md` (sections 01–02) |
| Content source is a raw (non-MTK) Writers Template `.docx` | `01_PIPELINE_EXTRACTION_TAGS.md` (section 02 — Raw Writers Template Docx Format) |
| Content source is an MTK `.docx` | `07_MTK_DOCX_CONVERSION.md` |
| A Media List `.docx` is supplied | `01_PIPELINE_EXTRACTION_TAGS.md` (section 02 — Media List Companion Document) + `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` (Acknowledgements) |
| An iStock acknowledgements file (API-sourced acks lines) is supplied | `01_PIPELINE_EXTRACTION_TAGS.md` (section 02 — iStock Acknowledgements File) + `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` (Acknowledgements — Sourcing) |
| Starting a Mode B conversion (reference module files) | `06_TEMPLATE_RECOGNITION.md` + `01_PIPELINE_EXTRACTION_TAGS.md` (sections 01–02) |
| User uploads HTML files of unknown type | `06_TEMPLATE_RECOGNITION.md` (sections 1–2 for identification) |
| Validating structural patterns in reference files | `06_TEMPLATE_RECOGNITION.md` (section 5 checklist) |
| Processing tags | `01_PIPELINE_EXTRACTION_TAGS.md` (sections 04–05) |
| Interpreting ambiguous writer/CS requests | `01_PIPELINE_EXTRACTION_TAGS.md` (Writer Intent Interpretation section) |
| Building page structure | `01_PIPELINE_EXTRACTION_TAGS.md` (section 03) + `02_DATA_CONTENT_VERIFICATION.md` (section 07) |
| Header title casing, menu archetype fallbacks, or a series with a non-standard lesson menu | `10_CORPUS_VALIDATED_SCAFFOLDING.md` (corpus evidence) + `01`/`06` for the how-to rules |
| Any interactive component | `03_COMP_CORE_INTERACTIVES.md` (COMP_00 + specific COMP section) or `04_COMP_SEGMENTS_OVERLAYS.md` / `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` as needed |
| Deciding whether to auto-apply `autoCheck` | `03_COMP_CORE_INTERACTIVES.md` (COMP_00 — autoCheck Auto-Application) |
| Building the acknowledgements block | `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` (Acknowledgements — always on page 0.0) |
| Extracting interactive data | `02_DATA_CONTENT_VERIFICATION.md` (section 06) + relevant component file |
| Handling images in output | `01_PIPELINE_EXTRACTION_TAGS.md` (Images section — Mode P/D rules) |
| Deciding whether something is a comment or a red flag | `02_DATA_CONTENT_VERIFICATION.md` (Comment & Red Flag Policy) |
| Final review | `02_DATA_CONTENT_VERIFICATION.md` (section 08) |
 
---