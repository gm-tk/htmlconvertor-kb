# INDEX — Te Kura HTML Convertor Knowledge Base (granular layout)
> **Last updated:** Tuesday, 22nd September, 2026 12:35 PM

This repository holds the complete knowledge base for the Te Kura **HTML Convertor** Claude project, split into **granular part files** so no single file is ever too large to read, edit, or regenerate. The original sixteen knowledge files still exist as **topics**: a large topic is now a **folder** of lettered parts (e.g. `02_DATA_CONTENT_VERIFICATION/02D_COMMENT_POLICY_CONSTRAINTS.md`); a small topic remains a single file. Any reference elsewhere in the KB to an original filename (e.g. "see `02_DATA_CONTENT_VERIFICATION.md`") resolves to the folder of the same name — each part's header states which original file it belongs to.

**Rules of the repo** (enforced by `tools/check_kb.py` — see `CLAUDE.md`): no content file may exceed **40,000 bytes** (hard fail); at **30,000 bytes** it must be split at the next update. Edit parts in place — never regenerate a whole topic. Sizes below are whole kilobytes, **rounded down** (`floor(bytes / 1024)`) — refresh an entry's figure in the same commit as any edit that changes that file's length.


## 00_MASTER_INSTRUCTIONS
- **`00_MASTER_INSTRUCTIONS/00A_CONTROL_CORE.md`** (9 KB) — Role, philosophy, timestamps, input files (operating modes moved to `00A2` on 16 September 2026 at the 30 KB soft limit)
  - Sections: Te Kura HTML Template Conversion — Master Instructions · ROLE · CORE PHILOSOPHY · FILE TIMESTAMP CONVENTION · INPUT FILES
- **`00_MASTER_INSTRUCTIONS/00A2_OPERATING_MODES.md`** (25 KB) — Operating modes (Modes 1–9, incl. **Mode 9 — Assessment**) and mode triage. Split from `00A` on 16 September 2026
  - Sections: OPERATING MODES · Mode 1 — Conversion · Mode 2 — Advisory & Support · Mode 3 — Comparison · Mode 4 — Update · Mode 5 — Split · Mode 6 — Interactives Build · Mode 7 — PageForge Compare · Mode 8 — Admin · Mode 9 — Assessment · Mode triage
- **`00_MASTER_INSTRUCTIONS/00B_CONVERSION_PIPELINE.md`** (19 KB) — Conversion pipeline (Mode 1 pseudo-code)
  - Sections: CONVERSION PIPELINE (Mode 1 — Pseudo-code)
- **`00_MASTER_INSTRUCTIONS/00C_FILE_REFERENCE_INDEX.md`** (21 KB) — File reference index (now lists `18_ASSESSMENT_MODE.md`)
  - Sections: FILE REFERENCE INDEX
- **`00_MASTER_INSTRUCTIONS/00D_CONSTRAINTS_1.md`** (29 KB) — Constraints quick reference, part 1 of 4 — **constraints 1–57** (constraint 1 now lists the label-prefix strip among the permitted format normalisations — CL-0095) — constraint 2 now records the Assessment Mode inline-style exception (`18` §6.4)
  - Sections: CONSTRAINTS (Quick Reference) — the list opens here and runs on through `00E`, `00G` and `00H` as ONE continuous numbering
- **`00_MASTER_INSTRUCTIONS/00E_CONSTRAINTS_2.md`** (22 KB) — Constraints quick reference, part 2 of 4 — **constraints 58–74**
  - Sections: (continuation of the numbered list from `00D` — no headings of its own)
- **`00_MASTER_INSTRUCTIONS/00F_WHEN_TO_LOAD.md`** (7 KB) — When to load which files (now routes the `ASSESSMENT MODE` phrase / Assessment Activity `.docx` to `18`)
  - Sections: WHEN TO LOAD WHICH FILES
- **`00_MASTER_INSTRUCTIONS/00G_CONSTRAINTS_3.md`** (24 KB) — Constraints quick reference, part 3 of 4 — **constraints 75–85** (latest: 85, a three-part `[TITLE BAR]` builds three `<h1><span>` titles in the Languages cohort only; **84 amended 13 Sept 2026** — the *Responding to Suspected Use* AI Guidelines PDF renamed, CL-0094). **CLOSED** at 85 on 28 August 2026 — appending constraints 86-88 would have taken it past the 30 KB soft limit, so they were written into the new `00H` instead and nothing was moved out of this part
  - Sections: (continuation of the numbered list from `00E` — no headings of its own). Opened 6 August 2026 when `00E` passed the 30 KB soft limit
- **`00_MASTER_INSTRUCTIONS/00H_CONSTRAINTS_4.md`** (18 KB) — Constraints quick reference, part 4 of 4 — **constraints 86 onward** (86 `ADMIN MODE` precedence + override; 87 the front-facing test + the PageForge Amalgamation Log; 88 the designer-facing output policy; 89 `learningSupport` required by an `X` module-code prefix; 90 `acksTemplate`/`acksAI` generate their statements — never typed as text; 91 the Admin Mode front-end output policy — `<omit_from_frontend>`, the plain-English visible half and the conflict heads-up; 92 `jp-text` / `ch-text` / `pinyin` mandatory on every occurrence, with the te reo macron boundary). **THE OPEN PART, new constraints are appended here**
  - Sections: (continuation of the numbered list from `00G` — no headings of its own). Opened 28 August 2026 when `00G` passed the 30 KB soft limit

## 01_PIPELINE_EXTRACTION_TAGS
- **`01_PIPELINE_EXTRACTION_TAGS/01A_TEMPLATE_LEVELS_CORE.md`** (28 KB) — Template levels: structural reference workflow, levels, head/heading/title patterns
  - Sections: 01 — Template Levels Reference · CRITICAL WORKFLOW — Structural Reference Approach · Level Identification · Template HTML Tag Patterns · Template Head Sections · Template Heading Patterns · Template Title Patterns
- **`01_PIPELINE_EXTRACTION_TAGS/01B_MODULE_MENUS_FOOTER.md`** (27 KB) — Module menu structures; footer and acknowledgements
  - Sections: Module Menu Structures · Footer and Acknowledgements
- **`01_PIPELINE_EXTRACTION_TAGS/01C_CONTENT_SOURCE_FORMATS.md`** (28 KB) — Content source formats: PageForge txt, raw WT docx, Media List, iStock acks
  - Sections: 02 — Content Source Formats · Overview · PageForge Text File Format · File Structure · Format Conventions · Content Integrity · What to IGNORE in the Text File · What to CONVERT · Raw Writers Template Docx Format · Media List Companion Document · iStock Acknowledgements File
- **`01_PIPELINE_EXTRACTION_TAGS/01D_PAGE_BOUNDARIES_TAG_TAXONOMY.md`** (20 KB) — Page boundary system; tag taxonomy & normalisation (incl. the five tolerant-match `ai_guidelines_pdf` media rows — constraint 84, with the renamed `responding` row and its still-matched retired wording, CL-0094)
  - Sections: 03 — Page Boundary System · Standard Page Structure · Page Boundary Validation Rules · Page-to-File Mapping · Lesson Numbering · Multi-Page vs Single-Page Modules (and when to offer Split Mode) · 04 — Tag Taxonomy & Normalisation Rules · Normalisation Algorithm · Complete Normalisation Table · Red Text Handling · Writer Intent Interpretation (Ambiguous Requests) · Document Parsing: What to IGNORE · What to CONVERT
- **`01_PIPELINE_EXTRACTION_TAGS/01E_TAG_INTERPRETATION.md`** (26 KB) — Tag interpretation, first half: structural, headings (incl. the duplicate-heading drop and the **label-prefix strip** — `FUNdamental:` and `Lesson N` forms, constraint 1 / CL-0095), body, media (incl. the constraint-83 no-`loading="lazy"`-inside-moving-interactives table and the eight AI Guidelines PDF teacher tags — constraint 84, *Responding to Suspected Use* renamed CL-0094). **Split at the 30 KB soft limit, 14 September 2026** — styling, activities and links moved verbatim to `01F`
  - Sections: 05 — Tag Interpretation · Structural & Page Tags · Headings · Body Text · Media
- **`01_PIPELINE_EXTRACTION_TAGS/01F_TAG_INTERPRETATION_STYLING_ACTIVITIES.md`** (5 KB) — Tag interpretation, second half: content styling, activities, links & buttons, interactive components. Opened 14 September 2026 when `01E` passed the 30 KB soft limit; content moved verbatim from `01E`
  - Sections: Content Styling · Activities · Links & Buttons · Interactive Components

## 02_DATA_CONTENT_VERIFICATION
- **`02_DATA_CONTENT_VERIFICATION/02A_DATA_PATTERNS.md`** (9 KB) — Interactive data pattern recognition (patterns 1-13, speech bubbles, tag primacy)
  - Sections: 06 — Interactive Data Pattern Recognition · Overview · Pattern 1: Single Data Table (Most Common) · Pattern 2: Front/Back Table Rows · Pattern 3: Hint/Slide Table · Pattern 4: Numbered Items (Dropdown Paragraph) · Pattern 5: Numbered Slides · Pattern 6: Numbered Shapes/Tabs · Pattern 7: Numbered Accordions · Pattern 8: Speech Bubble in Table Row · Pattern 9: Conversation Layout · Pattern 10: Word Select Table · Pattern 11: Axis Labels (Slider Chart) · Pattern 12: Info Trigger Image (Labelled Image Overlay) · …
- **`02_DATA_CONTENT_VERIFICATION/02B_CONTENT_RULES.md`** (18 KB) — Content rules: preservation, grids, merging, perspective, red text, headings
  - Sections: 07 — Content Rules · Content Preservation Rules · Grid Structure Rules · Content Merging Rules · Writer Perspective Notes · Red Text Rules · Heading Formatting · Numbered Instructions in Activities · Square-Bracket Tags
- **`02_DATA_CONTENT_VERIFICATION/02C_VERIFICATION_CHECKLIST.md`** (25 KB) — Verification checklist, incl. a **Language Fonts** block (constraint 92) (unchanged and still run in full; **constraint 88** banner — run every check, narrate almost none: a passing check is silent, a failing one becomes a plain-English red flag)
  - Sections: 08 — Verification, Constraints & Output · Verification Checklist
- **`02_DATA_CONTENT_VERIFICATION/02D_COMMENT_POLICY_CONSTRAINTS.md`** (27 KB) — Comment & red flag policy; constraints (incl. 28 `never_lazy_load_moving_interactive_images`)
  - Sections: Comment & Red Flag Policy · Constraints
- **`02_DATA_CONTENT_VERIFICATION/02E_EDGE_CASES_OUTPUT.md`** (9 KB) — Edge cases, component whitelist, output specifications — incl. **THE DESIGNER SUMMARY** (constraint 88: verify in full, report by exception; convention departures first; counts and clean confirmations never narrated)
  - Sections: Edge Cases · Component Whitelist — Known Partial/No-Match (v6) · Output Specifications · Post-output — The Designer Summary

## 03_COMP_CORE_INTERACTIVES
- **`03_COMP_CORE_INTERACTIVES/03A_COMP00_INDEX_UNIVERSAL.md`** (11 KB) — COMP_00 component index & universal rules
  - Sections: COMP_00 — Component Index & Universal Rules · Universal Rules · autoCheck Auto-Application · Component File Index · Button Class Quick Reference · Deprecated Components — DO NOT USE · Show/Hide Answer Pattern (Cross-Component) · Key Rules (Repeated for Emphasis)
- **`03_COMP_CORE_INTERACTIVES/03B_COMP01_DRAG_AND_DROP.md`** (15 KB) — COMP_01 drag and drop (all layouts)
  - Sections: COMP_01 — Drag and Drop · Available Layouts · Modifier Classes (on `dragAndDrop` div) · Standard Layout · Column Layout · FIB (Fill in Blank) Layout · Scatter Layout · Area Layout (Free-form, no correct answer) · Venn Layout
- **`03_COMP_CORE_INTERACTIVES/03C_COMP02_QUIZZES_1.md`** (17 KB) — COMP_02 quizzes: dropdown, MCQ, survey variant
  - Sections: COMP_02 — Quizzes · Dropdown Quiz · Multiple Choice Quiz (MCQ) · Multi Choice Quiz — Survey/Self-Assessment Variant (multiChoiceQuiz)
- **`03_COMP_CORE_INTERACTIVES/03D_COMP02_QUIZZES_2.md`** (15 KB) — COMP_02 quizzes: graded multi-select, radio, typing
  - Sections: Multi Choice Quiz — Graded Multi-Select Variant (multiChoiceQuiz mcqSomeSelected) · Radio Quiz · Typing Quiz
- **`03_COMP_CORE_INTERACTIVES/03E_COMP03_04_SELFCHECK_GAMES.md`** (9 KB) — COMP_03 self check & reflection; COMP_04 games & word components
  - Sections: COMP_03 — Self Check & Reflection · Self Check · Self Reflection · Reflection Slider · COMP_04 — Games & Word Components · Memory Game · Puzzle · Crossword · Word Find · Bingo · Word Drag
- **`03_COMP_CORE_INTERACTIVES/03F_COMP05_06_ORDERING_SLIDERS.md`** (11 KB) — COMP_05 ordering & selecting; COMP_06 sliders
  - Sections: COMP_05 — Ordering & Selecting · Reorder · Clicking Order · Word Select · Checklist / Selection Box · COMP_06 — Sliders · Slider (Scale/Survey) · Slider Chart

## 04_COMP_SEGMENTS_OVERLAYS
- **`04_COMP_SEGMENTS_OVERLAYS/04A_COMP07_SEGMENTATION.md`** (20 KB) — COMP_07 content segmentation (accordion, carousel, banner, clickDrop, flipCard, tabs, hint, modal) — each moving component now carries its own no-`loading="lazy"` rule (constraint 83)
  - Sections: COMP_07 — Content Segmentation · Accordion · Carousel · Rotating Banner · Click Drop · Flip Card · Tabs · Hint · Hint Slider · Modal
- **`04_COMP_SEGMENTS_OVERLAYS/04B_COMP08_TRIGGERS_OVERLAYS.md`** (15 KB) — COMP_08 triggers & overlays (infoTrigger, audio, image label/zoom, word highlighter)
  - Sections: COMP_08 — Triggers & Overlays · Info Trigger / Hover Trigger · Info Trigger Image · Audio Trigger · Audio Image · Image Label · Image Zoom · Word Highlighter
- **`04_COMP_SEGMENTS_OVERLAYS/04C_COMP09_10_11_BUBBLES_DIAGRAMS_TOOLS.md`** (19 KB) — COMP_09 speech bubbles; COMP_10 diagrams & timelines; COMP_11 drawing tools
  - Sections: COMP_09 — Speech Bubbles · Basic Conversation Layout · No-Hover Rule · imageCentral Rule · Bubble Direction Classes · Colour Modifier Classes · Other Modifier Classes · With Audio · Height Equalisation · Single Character Speech Bubble · Writer Tag Variants · COMP_10 — Diagrams & Timelines · Shape Hover · Timeline · …

## 05_COMP_LANGUAGE_MEDIA_LAYOUT
- **`05_COMP_LANGUAGE_MEDIA_LAYOUT/05A_COMP12_13_LANGUAGE_MEDIA.md`** (20 KB) — COMP_12 language & specialist (incl. **Language Fonts** — `jp-text` / `ch-text` / `pinyin` **mandatory on every occurrence**, the four markup carriers, the te reo macron boundary and the shared-Han Japanese-vs-Chinese resolution rule; constraint 92); COMP_13 media & embeds (incl. **AI Guidelines PDFs** — the eight delivered `AI-guidelines/` teacher tags, their tag→filename registry — *Responding to Suspected Use* **renamed 13 Sept 2026, CL-0094** — and the `embedPDF`/`centralFile` block; constraint 84)
  - Sections: COMP_12 — Language & Specialist · Glossary · Kanji Cards / Language Letter · Language Fonts · Translate Section · Reo Translate (Full Page Translate) · MathJax / Equations · COMP_13 — Media & Embeds · Video Embed · Audio Player · Embed PDF (generic — scoped to non-AI-Guidelines PDFs) · AI Guidelines PDFs (the eight teacher tags) · Embed Padlet · Embed Desmos Graph
- **`05_COMP_LANGUAGE_MEDIA_LAYOUT/05B_COMP14_LAYOUT_STRUCTURE.md`** (11 KB) — COMP_14 Layout & Structure, first half: Activities (inner column `col-12`; one shared inner row at default wrapper width, split only when widened — constraint 63) and Alerts
  - Sections: COMP_14 — Layout & Structure · Activities · Alerts (Cultural Alert · Translate Section in Alert Solid · Activity Image Sidebar · Activity + AlertImage Pairing)
- **`05_COMP_LANGUAGE_MEDIA_LAYOUT/05C_COMP14_ACKNOWLEDGEMENTS.md`** (19 KB) — COMP_14 acknowledgements
  - Sections: Acknowledgements
- **`05_COMP_LANGUAGE_MEDIA_LAYOUT/05D_COMP14_BUTTONS_TABLES_COLUMNS.md`** (21 KB) — COMP_14 Layout & Structure, second half: Buttons (incl. the "Go to website" default label for an unlabelled standalone external link, and the MTK Quiz activity shell — the four-element box, and the never-generate-the-quiz-content rule), Supervisor Button, Tables, Columns
  - Sections: Buttons (MTK Quiz — the activity shell `[MTKquiz]` builds) · Supervisor Button (Shape A/B/C · the reveal panel · edge cases) · Tables · Columns & Floating Columns (Standard Grid · Floating clearfix) · Quote Text · Whakatauki · Rhetorical Question

## 06_TEMPLATE_RECOGNITION
- **`06_TEMPLATE_RECOGNITION.md`** (24 KB) — single-file topic (small enough to stay whole)
  - Sections: 06 — Template Recognition & Structural Validation · PURPOSE · 1. TEMPLATE SYSTEM DETECTION — Legacy vs Refresh · 2. REFRESH SUB-TYPE IDENTIFICATION · 3. STRUCTURAL NORMS BY SUB-TYPE · 4. KNOWN PITFALLS IN REFERENCE FILES · 5. VALIDATION CHECKLIST — Mode B Reference Files · 6. ELEMENT REFERENCE — Refresh Baseline

## 07_MTK_DOCX_CONVERSION
- **`07_MTK_DOCX_CONVERSION/07A_MTK_IDENTIFY_AND_EXTRACT.md`** (14 KB) — MTK: identify, structure, extraction, menu tabs, page boundaries, bilingual rules (SS1-6)
  - Sections: 07 — MTK Writers Template Direct Conversion (Docx-to-HTML) · PURPOSE · 1. IDENTIFYING AN MTK WRITERS TEMPLATE · 2. DOCUMENT STRUCTURE — What to Ignore vs. Extract · 3. EXTRACTING TEXT FROM THE DOCX · 4. OVERVIEW PAGE STRUCTURE — Module Menu Tabs · 5. PAGE BOUNDARY DETECTION · 6. BILINGUAL CONTENT EXTRACTION RULES
- **`07_MTK_DOCX_CONVERSION/07B_MTK_CONTENT_PATTERNS.md`** (14 KB) — MTK: body content, alerts, interactive mapping, media, bilingual buttons (SS7-11)
  - Sections: 7. BODY CONTENT PATTERNS · 8. ALERT AND SIDEBAR PATTERNS · 9. INTERACTIVE COMPONENT MAPPING · 10. MEDIA ASSET HANDLING · 11. BILINGUAL BUTTON PATTERNS
- **`07_MTK_DOCX_CONVERSION/07C_MTK_PAGE_FURNITURE.md`** (10 KB) — MTK: header, footer, acks, word/image, Kiwi Kaiarahi, checklist, pitfalls (SS12-18)
  - Sections: 12. HEADER CONSTRUCTION · 13. FOOTER CONSTRUCTION · 14. ACKNOWLEDGEMENTS STRUCTURE · 15. WORD/IMAGE DISPLAY PATTERN · 16. KIWI KAIĀRAHI (LEARNING GUIDE) PATTERN · 17. CONVERSION CHECKLIST (MTK Docx-to-HTML) · 18. COMMON PITFALLS
- **`07_MTK_DOCX_CONVERSION/07D_MTK_HTML_SKELETONS.md`** (14 KB) — MTK: embedded HTML skeletons (SS19)
  - Sections: 19. EMBEDDED HTML SKELETONS

## 08_MODULE_SUPPORT_DEBUGGING
- **`08_MODULE_SUPPORT_DEBUGGING.md`** (18 KB) — single-file topic (small enough to stay whole) — the mode-triage table now sends an Assessment Activity `.docx` to Mode 9
  - Sections: 08 — Module Support, Advisory & Debugging Mode · PURPOSE · 1. SHARED DISCIPLINE — CARRIES OVER FROM CONVERSION MODE · 2. ADVISORY QUESTIONS — answering "how does X work?" · 3. MODULE COMPLETION — finishing a half-finished module · 4. INTERACTIVE DEBUGGING — diagnosing a broken interactive · 5. ONE-OFF MODULE OVERRIDES — applying a documented-pattern deviation for a single module · 6. SCOPE BOUNDARIES — what Support Mode does NOT do · 7. MODE TRIAGE — recap · 8. OUTPUT EXPECTATION FOR SUPPORT MODE

## 09_COMPARISON_MODE
- **`09_COMPARISON_MODE/09A_COMPARISON_CORE.md`** (16 KB) — Comparison Mode: trigger (incl. the PageForge discriminator and the prohibition on ever raising Mode 7 here), inputs, workflow, what counts as a difference (SS1-4)
  - Sections: 09 — Comparison Mode (Mode 3) · PURPOSE · 1. THE TRIGGER · 2. THE FOUR REQUIRED INPUTS · 3. WORKFLOW · 4. WHAT COUNTS AS A DIFFERENCE
- **`09_COMPARISON_MODE/09B_COMPARISON_EXCLUSIONS_GATE.md`** (20 KB) — Comparison Mode: the exclusions list (Section 4.1) and the inclusion gate (SS4.1-5)
  - Sections: 4.1 DIFFERENCES NOT TO CAPTURE (EXCLUSIONS) · Exclusion 1 — Red flags & designer notes · Exclusion 2 — Overview module-menu heading styling · Exclusion 3 — Bespoke designer presentation / composition decisions · Exclusion 4 — Designer supplying media metadata · Exclusion 5 — Per-instance presentational modifier classes · Exclusion 6 — Red Flag + visible fallback later realised with a library component · Exclusion 7 — Direct-Link (Mode D) derived filename swapped for the actual asset filename · Exclusion 8 — Designer removal of the on-page `[MTKquiz]` question set · Exclusion 9 — The filename a media asset is given in `images/` · Applying the exclusions · 5. THE INCLUSION GATE — KEEP KNOWLEDGE-DERIVED, FILTER OUT TEMPLATE-DERIVED
- **`09_COMPARISON_MODE/09C_COMPARISON_REPORTS.md`** (23 KB) — Comparison Mode: phase 1 & 2 reports, scope options, discipline (SS6-15)
  - Sections: 6. THE PHASE 1 REPORT — STRUCTURE (streamlined) · 7. THE FIVE SCOPE OPTIONS (the legend — shown once at the top of the report) · 8. PHASE 2 — PARSING THE DESIGNER'S SCOPE ASSIGNMENTS · 9. PHASE 2 OUTPUT — THE FINALIZED DETAILED REPORT · 10. WHAT HAPPENS AFTER — ACTIONING IS A SEPARATE CONVERSATION (UPDATE MODE) · 11. THE DOWNLOADABLE REPORT · 12. SHARED DISCIPLINE · 13. WHAT COMPARISON MODE DOES NOT DO · 14. RELATIONSHIP TO ONE-OFF OVERRIDES · 15. OUTPUT EXPECTATION

## 10_CORPUS_VALIDATED_SCAFFOLDING
- **`10_CORPUS_VALIDATED_SCAFFOLDING.md`** (5 KB) — single-file topic (small enough to stay whole)
  - Sections: 10 — Corpus-Validated Scaffolding Reference · 1. Header title casing · 2. Menu archetype — safe fallbacks (only when no reference/series precedent) · 3. Lesson-menu *style* deviations (series conventions — preserve, don't "correct") · 4. Series that ship NO lesson menu by design · 5. Source-limitation note (important honesty check)

## 11_UPDATE_MODE
- **`11_UPDATE_MODE/11A_UPDATE_MODE_CORE.md`** (26 KB) — Update Mode: purpose, trigger, input, scope, ledger use, classification, conflict check and escalation (SS1-7). Incl. the `Locked (admin)` status, the `ADMIN MODE (authorised)` intake channel, and the front-facing test that decides a `12G` entry
  - Sections: 11 — Update Mode (Mode 4) · PURPOSE · 1. THE TRIGGER · 2. ACCEPTED INPUT — ANY FORMAT · 3. SCOPE / GRANULARITY VOCABULARY · 4. THE CHANGE LEDGER (`12_CHANGE_LEDGER.md`) — CONFLICT & LOCK REGISTRY · 5. MAJOR vs ROUTINE CLASSIFICATION · 6. CONFLICT CHECK (runs before any file is edited) · 7. CONFLICT ESCALATION & LOCKING
- **`11_UPDATE_MODE/11B_UPDATE_MODE_WORKFLOW.md`** (17 KB) — Update Mode: the Repo Update Brief (SS10 — Claude Code actions edits on this repo; no file regeneration), exclusions, workflow pseudo-code, timestamps (SS10-16)
  - Sections: 10. THE REPO UPDATE BRIEF — PRECISE EDITS FOR CLAUDE CODE, NOT FILE REGENERATION · 11. (e) IGNORE ALWAYS — GROWING THE EXCLUSIONS LIST · 12. WORKFLOW (pseudo-code) · 13. THE TIMESTAMP CONVENTION (project-wide) · 14. RELATIONSHIP TO COMPARISON MODE & ONE-OFF OVERRIDES · 15. WHAT UPDATE MODE DOES NOT DO · 16. OUTPUT EXPECTATION
- **`11_UPDATE_MODE/11C_UPDATE_MODE_PREFLIGHT_SWEEP.md`** (7 KB) — Update Mode: the pre-flight confirmations (**none of which apply to an `ADMIN MODE` run**) (incl. **a settled universal constraint is never a pre-flight question**, and **superseding a rule is not finished until the retired wording is swept out**) and the blast-radius sweep (SS8-9)
  - Sections: 8. PRE-FLIGHT — WHAT TO CONFIRM BEFORE EDITING · 9. THE BLAST-RADIUS SWEEP — FIND *EVERY* FILE THAT MUST CHANGE

## 12_CHANGE_LEDGER
- **`12_CHANGE_LEDGER/12A_LEDGER_CORE_AND_LOCKS.md`** (17 KB) — Ledger purpose, status values (incl. **`Locked (admin)`**), PART 1 locked decisions (**CL-0086 to CL-0094**), PART 2 pending approval
  - Sections: 12 — Change Ledger (Conflict & Lock Registry) · PURPOSE · WHY ONE IN-HOUSE FILE IS FINE (feasibility note) · STATUS VALUES · HOW TO READ / MAINTAIN THIS LEDGER · PART 1 — LOCKED DECISIONS (binding & immutable — conflict check reads this FIRST) · PART 2 — PENDING APPROVAL (report-vs-report conflicts awaiting the design authority's resolution)
- **`12_CHANGE_LEDGER/12B_CHANGE_HISTORY_CL0001_0028.md`** (28 KB) — PART 3 change history: CL-0001 to CL-0028
  - Sections: PART 3 — CHANGE HISTORY (full append-only log — every actioned change)
- **`12_CHANGE_LEDGER/12C_CHANGE_HISTORY_CL0029_0040.md`** (20 KB) — PART 3 change history: CL-0029 to CL-0040 (continued)
  - Sections: 
- **`12_CHANGE_LEDGER/12D_CHANGE_HISTORY_CL0041_0062.md`** (25 KB) — PART 3 change history: CL-0041 to CL-0062 (continued) — CLOSED at CL-0062 (29 July 2026, 30 KB soft limit)
  - Sections: 
- **`12_CHANGE_LEDGER/12E2_CHANGE_HISTORY_CL0063_0071.md`** (23 KB) — PART 3 change history: CL-0063 to CL-0071 (continued) — CLOSED at CL-0071 (7 August 2026, 30 KB soft limit)
- **`12_CHANGE_LEDGER/12E3_CHANGE_HISTORY_CL0072_0077.md`** (23 KB) — PART 3 change history: CL-0072 to CL-0077 (continued) — CLOSED at CL-0077 (13 August 2026, 30 KB soft limit)
  - Sections: PART 3 history rows CL-0072 to CL-0077
- **`12_CHANGE_LEDGER/12E4_CHANGE_HISTORY_CL0078_0084.md`** (29 KB) — PART 3 change history: CL-0078 to CL-0084 (continued) — CLOSED at CL-0084 (26 August 2026, 30 KB soft limit)
- **`12_CHANGE_LEDGER/12E5_CHANGE_HISTORY_CL0085_0092.md`** (28 KB) — PART 3 change history: CL-0085 to CL-0092 (continued) — CLOSED at CL-0092 (14 September 2026, 30 KB soft limit)
  - Sections: PART 3 history rows CL-0085 to CL-0092
- **`12_CHANGE_LEDGER/12E6_CHANGE_HISTORY_CL0093_0097.md`** (24 KB) — PART 3 change history: CL-0093 to CL-0097 (continued) — CLOSED at CL-0097 (20 September 2026, 30 KB soft limit)
  - Sections: PART 3 history rows CL-0093 to CL-0097
- **`12_CHANGE_LEDGER/12E7_CHANGE_HISTORY_CL0098_ONWARD.md`** (6 KB) — PART 3 change history: CL-0098 onward (continued) — **THE OPEN PART: append new CL entries here**
  - Sections: PART 3 history rows CL-0098 onward
- **`12_CHANGE_LEDGER/12E_CHANGE_HISTORY_FOOTNOTES.md`** (15 KB) — PART 3 footnotes (locked-decision and grouped-change notes)
  - Sections: 
- **`12_CHANGE_LEDGER/12F_LEDGER_LOGS_AND_NOTES.md`** (2 KB) — Blocked-request log, housekeeping, notes
  - Sections: BLOCKED-REQUEST LOG (audit) · HOUSEKEEPING (optional — nothing here is a recurring task) · NOTES
- **`12_CHANGE_LEDGER/12G_PAGEFORGE_AMALGAMATION_LOG.md`** (18 KB) — **PART 4 — the PageForge Amalgamation Log**: every FRONT-FACING decision (one that changes the generated HTML or CSS), in a form PageForge's developer can implement. Written by both Admin Mode and Update Mode; append-only; starts at CL-0086 (earlier decisions stay in the Part 3 history and would need a one-off backfill). First entries appended 28 August 2026 (CL-0089 onward). **THE OPEN PART: append new entries here**
  - Sections: PART 4 — The PageForge Amalgamation Log · WHY THIS LOG EXISTS · WHAT GOES IN — THE FRONT-FACING TEST · ENTRY FORMAT · BACKFILL NOTE — THIS LOG STARTS AT CL-0086 · LOG

## 13_SPLIT_MODE
- **`13_SPLIT_MODE.md`** (28 KB) — single-file topic (small enough to stay whole)
  - Sections: 13 — Split Mode (Mode 5) · PURPOSE — what Split Mode is, and the problem it solves · 1. SPLIT MODE ≠ THE PAGE BOUNDARY SYSTEM (read first) · 2. PROACTIVE SINGLE-PAGE IDENTIFICATION + OFFERING SPLIT MODE · 3. TRIGGER, TRIAGE & APPLICABILITY · 4. OUTPUT #1 — THE BASE HOMEPAGE (`<CODE>-base.html`) · 5. OUTPUT #2 — ONE SECTION FILE PER SLOT (`<CODE>-lesson-<id>.html`) · 5A. EMISSION CADENCE — ONE FILE PER RESPONSE · 5B. MANUAL-STITCH GUIDANCE BLOCKS (`PAGEFORGE-GUIDE`) · 6. ID AND FILENAME CONVENTIONS · 7. KEYWORD / MARKER REFERENCE (reproduce these EXACTLY) · 8. THE ROUND-TRIP GUARANTEE (why the exactness matters) · 9. HOW PAGEFORGE'S PAGE STITCHER CONSUMES THE OUTPUT (so the split is valid) · 10. VALIDATION AND FAILURE HANDLING THE CONVERTER MUST HONOUR · …

## 14_SUBJECT_GLOBAL_PARAMETERS
- **`14_SUBJECT_GLOBAL_PARAMETERS/14A_SGP_PURPOSE_FAMILIES_1_5.md`** (23 KB) — Purpose + families 14.1-14.5 (Languages — finalised Audiovisual Package rules, registry data in `14C` —, Pathways, Taonga, CED — incl. the AI Guidelines carve-out on the §14.4 PDF deferral —, FUNdamentals)
  - Sections: 14 — Subject Global Parameters · PURPOSE · 14.1 Languages Phase 1–4 · 14.2 Pathways · 14.3 Taonga (The Arts) · 14.4 ConnectED (CED) Phase 5 · 14.5 FUNdamentals (Health & PE, Y1–10)
- **`14_SUBJECT_GLOBAL_PARAMETERS/14B_SGP_FAMILIES_6_11.md`** (28 KB) — Families 14.6-14.10 (LS, BLL, HPE, BLLR, MiW/WJ)
  - Sections: 14.6 LS — Learning Support · 14.7 BLL — Blended Literacy · 14.8 HPE — Health & PE content lessons (celebration .gif DELIVERED — deferral retired) · 14.9 BLLR — Blended Literacy (Reading) · 14.10 MiW — My Te Kura Writing
- **`14_SUBJECT_GLOBAL_PARAMETERS/14C_LANGUAGES_AV_ASSET_REGISTRY.md`** (14 KB) — The complete Languages Audiovisual Package asset registry, absorbed verbatim from the final `20260511_Language_HTML` (CL-0070) — the supplied HTML no longer needs to be consulted
  - Sections: 14C — Languages Audiovisual Package: the complete asset registry · 1. Delivery forms (the supplied markup shapes) · 2. Language icons · 3. German · 4. French · 5. Chinese · 6. Japanese · 7. Spanish · 8. Samoan · 9. Acknowledgements for the iStock-derived registry assets
- **`14_SUBJECT_GLOBAL_PARAMETERS/14D_SGP_CROSSCUTTING_AND_TECHNOLOGY.md`** (6 KB) — Cross-cutting notes (14.11) and the Technology family (14.12 — five `Technology/strand/active-*.svg` strand icons copied verbatim including their supplied spelling, the DELIVERED shared `congradulations/` celebration gif whose misspelling is a recorded design decision and is never corrected, suggested `col-8` text / `col-4` gif layout)
  - Sections: 14.11 Cross-cutting notes · 14.12 Technology — strand icons + the celebration gif

## 15_INTERACTIVES_BUILD_MODE
- **`15_INTERACTIVES_BUILD_MODE/15A_MODE_CORE_AND_CONTRACT.md`** (14 KB) — Mode 6 core: trigger/auto-detection, the `cv2-built` anchor contract, output files + splitting (ALL files in one response), quality gate, authority order
  - Sections: 15 — Interactives Build Mode (Mode 6) · 1. TRIGGER & AUTO-DETECTION · 2. WHERE THIS MODE SITS IN THE PIPELINE · 3. FIRST ACTION on every uploaded worklist · 4. THE ANCHOR CONTRACT — the golden rule · 5. WHAT THE PAGE STITCHER DOES WITH IT · 6. OUTPUT FILES + THE SPLITTING SAFEGUARD (all files emitted in ONE response) · 7. QUALITY CHECK before emitting each file · 8. WHICH KNOWLEDGE TO LOAD — and the authority order · 9. MULTI-COMPONENT ENTRIES AND THE ACTIVITY-BOX CARVE-OUT · 10. TONE + INTERACTION
- **`15_INTERACTIVES_BUILD_MODE/15B_WORKLIST_FORMAT_AND_BUILD_RULES.md`** (12 KB) — The `{CODE}_interactives.txt` anatomy and the fragment-specific build rules
  - Sections: 15B — The worklist format, and how to build from it · 1. THE INPUT FILE — `{CODE}_interactives.txt` (file header · one entry line by line · reading the `Content:` block) · 2. THE BUILD RULES (declarative only · build the widget not the page · writer content verbatim · media placeholders · choosing the type · answer keys — the load-bearing attributes · shuffle, feedback and buttons · never emit) · 3. FAMILY CONVENTIONS STILL APPLY
- **`15_INTERACTIVES_BUILD_MODE/15C_WORKED_EXAMPLE.md`** (6 KB) — One worklist entry end to end: input, reading, output, why it is right
  - Sections: 15C — Worked example: one worklist entry → one finished build · The input entry · Reading it · The output · Why this is right

## 16_PAGEFORGE_COMPARE_MODE
- **`16_PAGEFORGE_COMPARE_MODE/16A_MODE_CORE_AND_INPUTS.md`** (24 KB) — Mode 7 core: trigger + the `PAGEFORGE` discriminator + the never-advertise rule, same-chat-only rule, the tester workflow, the three required inputs (PageForge's ORIGINAL un-stitched HTML is the only upload — no worklist), the two PageForge upload formats, the workflow
  - Sections: 16 — PageForge Compare Mode (Mode 7) · 1. THE TRIGGER (same chat only · precedence and the one collision to watch · NEVER ADVERTISE THIS MODE) · 2. WHERE THIS SITS IN THE TESTER WORKFLOW · 3. WHAT THE REPORT IS FOR (and who reads it) · 4. THE THREE REQUIRED INPUTS (4.3 — upload PageForge's ORIGINAL output; why no worklist is needed; the stitched-upload limits) · 5. THE TWO PAGEFORGE UPLOAD FORMATS — AND HOW TO TELL THEM APART (hand-off · stitched · mixed) · 6. WORKFLOW · 7. TONE + INTERACTION
- **`16_PAGEFORGE_COMPARE_MODE/16B_WHAT_TO_REPORT.md`** (22 KB) — The five finding classes, the boundary check (reading PageForge's captured content and owning activity off the reference box on the page), complex vs non-complex interactives, the exclusions (incl. the total comments-and-developer-notes exclusion), the uncertainty rule
  - Sections: 1. THE FIVE FINDING CLASSES · 2. NOTES ON EACH CLASS · 3. THE BOUNDARY CHECK (class B) — SPILL/SWALLOW, the per-box membership procedure, boundaries checked for EVERY interactive · 4. COMPLEX vs NON-COMPLEX INTERACTIVES (class C) — the non-complex list · 5. THE EXCLUSIONS (incl. comments, developer notes & restated writer instructions — ignored entirely) · 6. WHEN THE ORIGIN IS UNCLEAR — "For Gavin to judge" · 7. WHAT THIS MODE NEVER DOES
- **`16_PAGEFORGE_COMPARE_MODE/16C_REPORT_FORMAT.md`** (14 KB) — The one-shot report for Gavin: header, finding bundle, uncertain section, interactive inventory, coverage + exclusion counts, worked examples
  - Sections: 1. REPORT HEADER · 2. SECTION 1 — FINDINGS (class B extra requirement · confidence) · 3. SECTION 2 — FOR GAVIN TO JUDGE · 4. SECTION 3 — INTERACTIVE INVENTORY · 5. SECTION 4 — SCOPE AND COVERAGE · 6. WORKED EXAMPLES · 7. HOW THE RUN CLOSES IN CHAT

## 17_ADMIN_MODE
- **`17_ADMIN_MODE.md`** (28 KB) — single-file topic; §10 is the **front-end / hidden output split** (`<omit_from_frontend>`, the plain-English visible half, the conflict heads-up — constraint 91)
  - Sections: 17 — Admin Mode (Mode 8) · PURPOSE · 1. THE TRIGGER AND ITS PRECEDENCE · 2. ACCEPTED INPUT · 3. SCOPE — UNIVERSAL BY DEFAULT · 4. THE OVERRIDE RULE — ADMIN MODE WINS (4.1 an Admin decision is locked against ordinary Update Mode) · 5. THE TWO LANES — WHAT GETS LOGGED WHERE (5.1 the front-facing test · 5.2 mechanism · 5.3 front-facing) · 6. THE LEDGER ROW · 7. WHAT ADMIN MODE STILL DOES · 8. WHAT ADMIN MODE DOES NOT DO · 9. WORKFLOW (pseudo-code) · 10. OUTPUT EXPECTATION · 11. RELATIONSHIP TO THE OTHER MODES

## 18_ASSESSMENT_MODE
- **`18_ASSESSMENT_MODE/18A_MODE_CORE_MAPPING_SKELETON.md`** (16 KB) — **Mode 9 — Assessment**, core: the `ASSESSMENT MODE` trigger (any capitalisation) **and** the self-identifying NCEA Assessment Activity `.docx` fingerprint, inputs (never a Media List; several `.docx` at once → one page each, one response), the details-table → header-bar mapping, NZQA link patterns, section → accordion mapping, the skeleton with its four corrections to the example (live script host, `<div id="body">`, blank footer links, four-space indentation) and the acknowledgements block, `{CODE}.html` filename. Topic split into a folder 18 September 2026
  - Sections: 18 — Assessment Mode (Mode 9) · PURPOSE · 1. THE TRIGGER · 2. THE FINGERPRINT · 3. INPUTS · 4. THE MAPPING (4.1 details table → header bar · 4.2 the NZQA link · 4.3 section headings → accordions) · 5. THE SKELETON (5.1 the four corrections to the example — and the indentation rule)
- **`18_ASSESSMENT_MODE/18B_CONTENT_RULES_ACKS_TODO_WORKFLOW.md`** (20 KB) — content rules inside the accordions: heading step-down, the nest-under-the-numbered-item rule with lettered sub-lists, the two permitted inline styles (constraint 2), table shapes (answer table kept / layout box flattened / empty box dropped), alerts, links, the dropbox accordion; **6.8 the acknowledgements block on every page** (`acksTemplate`, media isolated from the document, one unlabelled `acksLesson`, the typed "All other images" line); the visible `Designer/Developer To Do:` list (incl. the D2L media-upload destination convention, 7.2); workflow; never-does list
  - Sections: 6. CONTENT RULES INSIDE AN ACCORDION (6.1 text · 6.2 headings · 6.3 lists and the hierarchy rule · 6.4 tables — the constraint-2 exception · 6.5 alert boxes · 6.6 links, buttons and files · 6.7 the dropbox accordion · 6.8 the acknowledgements block) · 7. WHAT THE DOCUMENT CANNOT TELL YOU · 8. WORKFLOW · 9. WHAT THIS MODE NEVER DOES
- **`18_ASSESSMENT_MODE/18C_ASSESSMENT_COMPARISON_MODE.md`** (9 KB) — the **assessment variant of Comparison Mode**: same `COMPARISON MODE` phrase, routed per uploaded file (`alertAssessment` page in an assessment chat → here; module page → `09`), inputs with the fixed `18A` skeleton as R, partial re-uploads compared alone (the rest assumed unchanged), URL changes never logged, **no scopes** — one phase straight to the finalized report, assessment readings of the `09B` exclusions, the one report for Gavin (per-file sections, continuous numbering, every difference (c) Universal, Actioning summary)
  - Sections: 10. ASSESSMENT COMPARISON MODE (10.1 purpose, trigger and routing · 10.2 inputs · 10.3 no scopes · 10.4 what counts and what is excluded · 10.5 the report · 10.6 how the run closes · 10.7 what this mode never does)

## 19_SKILLS
The nine operating modes, also published as **Claude Skills** so a designer can reach a mode by describing it in plain English as well as by typing its trigger phrase. **Ten skills for nine modes:** Mode 3 (`COMPARISON MODE`) carries two procedures that behave quite differently — `09`'s two-pass, designer-scoped module comparison and `18C`'s immediate, Universal-by-rule assessment comparison — so it is published as two named skills. **The mode itself is not split:** both point at the one documented trigger, and the KB's file-based routing (`09A` §1, `18C` §10.1) is untouched, so a bare `COMPARISON MODE` still works out which procedure to run on its own. Paths here are deliberately NOT listed in the `**`path`**` form used above: a `SKILL.md` opens with YAML frontmatter and cannot carry the `> **Last updated:**` stamp or the `KB-PART-BODY-START` sentinel, so `19_SKILLS/` is exempt from the content checks and validated by check 6 of `tools/check_kb.py` instead (frontmatter present, `name` matches the folder, `description` within Claude.ai's 200-character limit).

- 19_SKILLS/README.md — what a skill here is (a signpost, never a rule book), the two upload limits, how to change a mode card
- 19_SKILLS/ROLLOUT.md — click-by-click instructions for provisioning the nine skills organisation-wide, the five-minute proving test, and what each upload error means
- 19_SKILLS/build_skills.sh — packages each skill folder into `19_SKILLS/dist/<name>.zip` in the shape Claude.ai's uploader requires
- 19_SKILLS/dist/ — the ten built `.zip` files, ready to upload
- One folder per skill, each holding a single `SKILL.md`. **The names are the picker's filter, so they are grouped by job** (`19_SKILLS/README.md` → *The naming scheme*): `/tk-module` → tk-module-conversion-mode (Mode 1) · tk-module-split-mode (5) · tk-module-comparison-mode (3, `09`); `/tk-assessment` → tk-assessment-mode (9) · tk-assessment-comparison-mode (3, `18C`); `/tk-support` → tk-support-mode (2); `/pageforge` → pageforge-interactives-mode (6) · pageforge-compare-mode (7); and, deliberately outside the `tk` group so an ordinary designer does not meet them while browsing, `/admin` → admin-mode (8) and `/update` → update-mode (4). `/tk` alone returns the six a designer normally needs. **That grouping is obscurity, not permission** — all ten are provisioned to everyone, and the typed `ADMIN MODE` phrase works for anyone regardless, by design (`17` §1)

Each `SKILL.md` does three things and nothing more: it **guards** (refuses to run outside the HTML Convertor project, and defers to a higher-precedence trigger), it **prints a mode card** — a plain-English panel naming the mode, what it needs, what it returns and what it will not do, so a designer can tell at once whether they picked the right mode — and it **points at the KB files** that own the mode's real rules. The two comparison skills add one guard of their own: a bare `COMPARISON MODE` that lands in the wrong half **switches silently** (the KB's own routing), but a **deliberately named** variant that contradicts the chat's evidence **stops and warns** instead of running, and waits for the designer to confirm or switch. It restates no conversion rule, no constraint and no markup pattern: the knowledge base stays the single source of truth, and the mode triage in `00A2_OPERATING_MODES.md` and `_project_instructions_.md` is unchanged and still authoritative, so every trigger phrase works with the skills switched off.

## Repo infrastructure
- **`_project_instructions_.md`** — the Claude.ai project's system-prompt text (paste into Project Instructions when it changes)
- **`CLAUDE.md`** — maintenance rules for Claude Code (the update ritual, size limits, how to split a growing file)
- **`README.md`** — plain-English overview for humans
- **`tools/check_kb.py`** — the guard script (size limits, index completeness, part headers, ledger integrity, and the `19_SKILLS` frontmatter/limits check)
- **`tools/kb_manifest.json`** — the one-time migration record proving the split was byte-identical to the 2026-07-16 originals
