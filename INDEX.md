# INDEX — Te Kura HTML Convertor Knowledge Base (granular layout)
> **Last updated:** Monday, 10th August, 2026 10:45 AM

This repository holds the complete knowledge base for the Te Kura **HTML Convertor** Claude project, split into **granular part files** so no single file is ever too large to read, edit, or regenerate. The original sixteen knowledge files still exist as **topics**: a large topic is now a **folder** of lettered parts (e.g. `02_DATA_CONTENT_VERIFICATION/02D_COMMENT_POLICY_CONSTRAINTS.md`); a small topic remains a single file. Any reference elsewhere in the KB to an original filename (e.g. "see `02_DATA_CONTENT_VERIFICATION.md`") resolves to the folder of the same name — each part's header states which original file it belongs to.

**Rules of the repo** (enforced by `tools/check_kb.py` — see `CLAUDE.md`): no content file may exceed **40,000 bytes** (hard fail); at **30,000 bytes** it must be split at the next update. Edit parts in place — never regenerate a whole topic.


## 00_MASTER_INSTRUCTIONS
- **`00_MASTER_INSTRUCTIONS/00A_CONTROL_CORE.md`** (19 KB) — Role, philosophy, timestamps, operating modes, input files
  - Sections: Te Kura HTML Template Conversion — Master Instructions · ROLE · CORE PHILOSOPHY · FILE TIMESTAMP CONVENTION · OPERATING MODES · INPUT FILES
- **`00_MASTER_INSTRUCTIONS/00B_CONVERSION_PIPELINE.md`** (16 KB) — Conversion pipeline (Mode 1 pseudo-code)
  - Sections: CONVERSION PIPELINE (Mode 1 — Pseudo-code)
- **`00_MASTER_INSTRUCTIONS/00C_FILE_REFERENCE_INDEX.md`** (16 KB) — File reference index
  - Sections: FILE REFERENCE INDEX
- **`00_MASTER_INSTRUCTIONS/00D_CONSTRAINTS_1.md`** (28 KB) — Constraints quick reference, part 1 of 3 — **constraints 1–57**
  - Sections: CONSTRAINTS (Quick Reference) — the list opens here and runs on through `00E` and `00G` as ONE continuous numbering
- **`00_MASTER_INSTRUCTIONS/00E_CONSTRAINTS_2.md`** (21 KB) — Constraints quick reference, part 2 of 3 — **constraints 58–74**
  - Sections: (continuation of the numbered list from `00D` — no headings of its own)
- **`00_MASTER_INSTRUCTIONS/00F_WHEN_TO_LOAD.md`** (5 KB) — When to load which files
  - Sections: WHEN TO LOAD WHICH FILES
- **`00_MASTER_INSTRUCTIONS/00G_CONSTRAINTS_3.md`** (13 KB) — Constraints quick reference, part 3 of 3 — **constraints 75 onward; THE OPEN PART, new constraints are appended here**
  - Sections: (continuation of the numbered list from `00E` — no headings of its own). Opened 6 August 2026 when `00E` passed the 30 KB soft limit

## 01_PIPELINE_EXTRACTION_TAGS
- **`01_PIPELINE_EXTRACTION_TAGS/01A_TEMPLATE_LEVELS_CORE.md`** (22 KB) — Template levels: structural reference workflow, levels, head/heading/title patterns
  - Sections: 01 — Template Levels Reference · CRITICAL WORKFLOW — Structural Reference Approach · Level Identification · Template HTML Tag Patterns · Template Head Sections · Template Heading Patterns · Template Title Patterns
- **`01_PIPELINE_EXTRACTION_TAGS/01B_MODULE_MENUS_FOOTER.md`** (27 KB) — Module menu structures; footer and acknowledgements
  - Sections: Module Menu Structures · Footer and Acknowledgements
- **`01_PIPELINE_EXTRACTION_TAGS/01C_CONTENT_SOURCE_FORMATS.md`** (29 KB) — Content source formats: PageForge txt, raw WT docx, Media List, iStock acks
  - Sections: 02 — Content Source Formats · Overview · PageForge Text File Format · File Structure · Format Conventions · Content Integrity · What to IGNORE in the Text File · What to CONVERT · Raw Writers Template Docx Format · Media List Companion Document · iStock Acknowledgements File
- **`01_PIPELINE_EXTRACTION_TAGS/01D_PAGE_BOUNDARIES_TAG_TAXONOMY.md`** (19 KB) — Page boundary system; tag taxonomy & normalisation
  - Sections: 03 — Page Boundary System · Standard Page Structure · Page Boundary Validation Rules · Page-to-File Mapping · Lesson Numbering · Multi-Page vs Single-Page Modules (and when to offer Split Mode) · 04 — Tag Taxonomy & Normalisation Rules · Normalisation Algorithm · Complete Normalisation Table · Red Text Handling · Writer Intent Interpretation (Ambiguous Requests) · Document Parsing: What to IGNORE · What to CONVERT
- **`01_PIPELINE_EXTRACTION_TAGS/01E_TAG_INTERPRETATION.md`** (24 KB) — Tag interpretation: structural, headings, body, media, styling, activities, links
  - Sections: 05 — Tag Interpretation · Structural & Page Tags · Headings · Body Text · Media · Content Styling · Activities · Links & Buttons · Interactive Components

## 02_DATA_CONTENT_VERIFICATION
- **`02_DATA_CONTENT_VERIFICATION/02A_DATA_PATTERNS.md`** (10 KB) — Interactive data pattern recognition (patterns 1-13, speech bubbles, tag primacy)
  - Sections: 06 — Interactive Data Pattern Recognition · Overview · Pattern 1: Single Data Table (Most Common) · Pattern 2: Front/Back Table Rows · Pattern 3: Hint/Slide Table · Pattern 4: Numbered Items (Dropdown Paragraph) · Pattern 5: Numbered Slides · Pattern 6: Numbered Shapes/Tabs · Pattern 7: Numbered Accordions · Pattern 8: Speech Bubble in Table Row · Pattern 9: Conversation Layout · Pattern 10: Word Select Table · Pattern 11: Axis Labels (Slider Chart) · Pattern 12: Info Trigger Image (Labelled Image Overlay) · …
- **`02_DATA_CONTENT_VERIFICATION/02B_CONTENT_RULES.md`** (17 KB) — Content rules: preservation, grids, merging, perspective, red text, headings
  - Sections: 07 — Content Rules · Content Preservation Rules · Grid Structure Rules · Content Merging Rules · Writer Perspective Notes · Red Text Rules · Heading Formatting · Numbered Instructions in Activities · Square-Bracket Tags
- **`02_DATA_CONTENT_VERIFICATION/02C_VERIFICATION_CHECKLIST.md`** (18 KB) — Verification checklist
  - Sections: 08 — Verification, Constraints & Output · Verification Checklist
- **`02_DATA_CONTENT_VERIFICATION/02D_COMMENT_POLICY_CONSTRAINTS.md`** (26 KB) — Comment & red flag policy; constraints
  - Sections: Comment & Red Flag Policy · Constraints
- **`02_DATA_CONTENT_VERIFICATION/02E_EDGE_CASES_OUTPUT.md`** (6 KB) — Edge cases, component whitelist, output specifications
  - Sections: Edge Cases · Component Whitelist — Known Partial/No-Match (v6) · Output Specifications

## 03_COMP_CORE_INTERACTIVES
- **`03_COMP_CORE_INTERACTIVES/03A_COMP00_INDEX_UNIVERSAL.md`** (11 KB) — COMP_00 component index & universal rules
  - Sections: COMP_00 — Component Index & Universal Rules · Universal Rules · autoCheck Auto-Application · Component File Index · Button Class Quick Reference · Deprecated Components — DO NOT USE · Show/Hide Answer Pattern (Cross-Component) · Key Rules (Repeated for Emphasis)
- **`03_COMP_CORE_INTERACTIVES/03B_COMP01_DRAG_AND_DROP.md`** (15 KB) — COMP_01 drag and drop (all layouts)
  - Sections: COMP_01 — Drag and Drop · Available Layouts · Modifier Classes (on `dragAndDrop` div) · Standard Layout · Column Layout · FIB (Fill in Blank) Layout · Scatter Layout · Area Layout (Free-form, no correct answer) · Venn Layout
- **`03_COMP_CORE_INTERACTIVES/03C_COMP02_QUIZZES_1.md`** (17 KB) — COMP_02 quizzes: dropdown, MCQ, survey variant
  - Sections: COMP_02 — Quizzes · Dropdown Quiz · Multiple Choice Quiz (MCQ) · Multi Choice Quiz — Survey/Self-Assessment Variant (multiChoiceQuiz)
- **`03_COMP_CORE_INTERACTIVES/03D_COMP02_QUIZZES_2.md`** (16 KB) — COMP_02 quizzes: graded multi-select, radio, typing
  - Sections: Multi Choice Quiz — Graded Multi-Select Variant (multiChoiceQuiz mcqSomeSelected) · Radio Quiz · Typing Quiz
- **`03_COMP_CORE_INTERACTIVES/03E_COMP03_04_SELFCHECK_GAMES.md`** (10 KB) — COMP_03 self check & reflection; COMP_04 games & word components
  - Sections: COMP_03 — Self Check & Reflection · Self Check · Self Reflection · Reflection Slider · COMP_04 — Games & Word Components · Memory Game · Puzzle · Crossword · Word Find · Bingo · Word Drag
- **`03_COMP_CORE_INTERACTIVES/03F_COMP05_06_ORDERING_SLIDERS.md`** (11 KB) — COMP_05 ordering & selecting; COMP_06 sliders
  - Sections: COMP_05 — Ordering & Selecting · Reorder · Clicking Order · Word Select · Checklist / Selection Box · COMP_06 — Sliders · Slider (Scale/Survey) · Slider Chart

## 04_COMP_SEGMENTS_OVERLAYS
- **`04_COMP_SEGMENTS_OVERLAYS/04A_COMP07_SEGMENTATION.md`** (19 KB) — COMP_07 content segmentation (accordion, carousel, banner, clickDrop, flipCard, tabs, hint, modal)
  - Sections: COMP_07 — Content Segmentation · Accordion · Carousel · Rotating Banner · Click Drop · Flip Card · Tabs · Hint · Hint Slider · Modal
- **`04_COMP_SEGMENTS_OVERLAYS/04B_COMP08_TRIGGERS_OVERLAYS.md`** (14 KB) — COMP_08 triggers & overlays (infoTrigger, audio, image label/zoom, word highlighter)
  - Sections: COMP_08 — Triggers & Overlays · Info Trigger / Hover Trigger · Info Trigger Image · Audio Trigger · Audio Image · Image Label · Image Zoom · Word Highlighter
- **`04_COMP_SEGMENTS_OVERLAYS/04C_COMP09_10_11_BUBBLES_DIAGRAMS_TOOLS.md`** (18 KB) — COMP_09 speech bubbles; COMP_10 diagrams & timelines; COMP_11 drawing tools
  - Sections: COMP_09 — Speech Bubbles · Basic Conversation Layout · No-Hover Rule · imageCentral Rule · Bubble Direction Classes · Colour Modifier Classes · Other Modifier Classes · With Audio · Height Equalisation · Single Character Speech Bubble · Writer Tag Variants · COMP_10 — Diagrams & Timelines · Shape Hover · Timeline · …

## 05_COMP_LANGUAGE_MEDIA_LAYOUT
- **`05_COMP_LANGUAGE_MEDIA_LAYOUT/05A_COMP12_13_LANGUAGE_MEDIA.md`** (10 KB) — COMP_12 language & specialist; COMP_13 media & embeds
  - Sections: COMP_12 — Language & Specialist · Glossary · Kanji Cards / Language Letter · Language Fonts · Translate Section · Reo Translate (Full Page Translate) · MathJax / Equations · COMP_13 — Media & Embeds · Video Embed · Audio Player · Embed PDF · Embed Padlet · Embed Desmos Graph
- **`05_COMP_LANGUAGE_MEDIA_LAYOUT/05B_COMP14_LAYOUT_STRUCTURE.md`** (26 KB) — COMP_14 layout & structure (activities, alerts, buttons, tables, columns)
  - Sections: COMP_14 — Layout & Structure · Activities · Alerts · Buttons · Supervisor Button (constraint 68) · Tables · Columns & Floating Columns · Quote Text · Whakatauki · Rhetorical Question
- **`05_COMP_LANGUAGE_MEDIA_LAYOUT/05C_COMP14_ACKNOWLEDGEMENTS.md`** (19 KB) — COMP_14 acknowledgements
  - Sections: Acknowledgements

## 06_TEMPLATE_RECOGNITION
- **`06_TEMPLATE_RECOGNITION.md`** (21 KB) — single-file topic (small enough to stay whole)
  - Sections: 06 — Template Recognition & Structural Validation · PURPOSE · 1. TEMPLATE SYSTEM DETECTION — Legacy vs Refresh · 2. REFRESH SUB-TYPE IDENTIFICATION · 3. STRUCTURAL NORMS BY SUB-TYPE · 4. KNOWN PITFALLS IN REFERENCE FILES · 5. VALIDATION CHECKLIST — Mode B Reference Files · 6. ELEMENT REFERENCE — Refresh Baseline

## 07_MTK_DOCX_CONVERSION
- **`07_MTK_DOCX_CONVERSION/07A_MTK_IDENTIFY_AND_EXTRACT.md`** (15 KB) — MTK: identify, structure, extraction, menu tabs, page boundaries, bilingual rules (SS1-6)
  - Sections: 07 — MTK Writers Template Direct Conversion (Docx-to-HTML) · PURPOSE · 1. IDENTIFYING AN MTK WRITERS TEMPLATE · 2. DOCUMENT STRUCTURE — What to Ignore vs. Extract · 3. EXTRACTING TEXT FROM THE DOCX · 4. OVERVIEW PAGE STRUCTURE — Module Menu Tabs · 5. PAGE BOUNDARY DETECTION · 6. BILINGUAL CONTENT EXTRACTION RULES
- **`07_MTK_DOCX_CONVERSION/07B_MTK_CONTENT_PATTERNS.md`** (15 KB) — MTK: body content, alerts, interactive mapping, media, bilingual buttons (SS7-11)
  - Sections: 7. BODY CONTENT PATTERNS · 8. ALERT AND SIDEBAR PATTERNS · 9. INTERACTIVE COMPONENT MAPPING · 10. MEDIA ASSET HANDLING · 11. BILINGUAL BUTTON PATTERNS
- **`07_MTK_DOCX_CONVERSION/07C_MTK_PAGE_FURNITURE.md`** (11 KB) — MTK: header, footer, acks, word/image, Kiwi Kaiarahi, checklist, pitfalls (SS12-18)
  - Sections: 12. HEADER CONSTRUCTION · 13. FOOTER CONSTRUCTION · 14. ACKNOWLEDGEMENTS STRUCTURE · 15. WORD/IMAGE DISPLAY PATTERN · 16. KIWI KAIĀRAHI (LEARNING GUIDE) PATTERN · 17. CONVERSION CHECKLIST (MTK Docx-to-HTML) · 18. COMMON PITFALLS
- **`07_MTK_DOCX_CONVERSION/07D_MTK_HTML_SKELETONS.md`** (15 KB) — MTK: embedded HTML skeletons (SS19)
  - Sections: 19. EMBEDDED HTML SKELETONS

## 08_MODULE_SUPPORT_DEBUGGING
- **`08_MODULE_SUPPORT_DEBUGGING.md`** (18 KB) — single-file topic (small enough to stay whole)
  - Sections: 08 — Module Support, Advisory & Debugging Mode · PURPOSE · 1. SHARED DISCIPLINE — CARRIES OVER FROM CONVERSION MODE · 2. ADVISORY QUESTIONS — answering "how does X work?" · 3. MODULE COMPLETION — finishing a half-finished module · 4. INTERACTIVE DEBUGGING — diagnosing a broken interactive · 5. ONE-OFF MODULE OVERRIDES — applying a documented-pattern deviation for a single module · 6. SCOPE BOUNDARIES — what Support Mode does NOT do · 7. MODE TRIAGE — recap · 8. OUTPUT EXPECTATION FOR SUPPORT MODE

## 09_COMPARISON_MODE
- **`09_COMPARISON_MODE/09A_COMPARISON_CORE.md`** (16 KB) — Comparison Mode: trigger (incl. the PageForge discriminator and the prohibition on ever raising Mode 7 here), inputs, workflow, what counts as a difference (SS1-4)
  - Sections: 09 — Comparison Mode (Mode 3) · PURPOSE · 1. THE TRIGGER · 2. THE FOUR REQUIRED INPUTS · 3. WORKFLOW · 4. WHAT COUNTS AS A DIFFERENCE
- **`09_COMPARISON_MODE/09B_COMPARISON_EXCLUSIONS_GATE.md`** (17 KB) — Comparison Mode: the exclusions list (Section 4.1) and the inclusion gate (SS4.1-5)
  - Sections: 4.1 DIFFERENCES NOT TO CAPTURE (EXCLUSIONS) · Exclusion 1 — Red flags & designer notes · Exclusion 2 — Overview module-menu heading styling · Exclusion 3 — Bespoke designer presentation / composition decisions · Exclusion 4 — Designer supplying media metadata · Exclusion 5 — Per-instance presentational modifier classes · Exclusion 6 — Red Flag + visible fallback later realised with a library component · Exclusion 7 — Direct-Link (Mode D) derived filename swapped for the actual asset filename · Exclusion 8 — Designer removal of the on-page `[MTKquiz]` question set · Applying the exclusions · 5. THE INCLUSION GATE — KEEP KNOWLEDGE-DERIVED, FILTER OUT TEMPLATE-DERIVED
- **`09_COMPARISON_MODE/09C_COMPARISON_REPORTS.md`** (25 KB) — Comparison Mode: phase 1 & 2 reports, scope options, discipline (SS6-15)
  - Sections: 6. THE PHASE 1 REPORT — STRUCTURE (streamlined) · 7. THE FIVE SCOPE OPTIONS (the legend — shown once at the top of the report) · 8. PHASE 2 — PARSING THE DESIGNER'S SCOPE ASSIGNMENTS · 9. PHASE 2 OUTPUT — THE FINALIZED DETAILED REPORT · 10. WHAT HAPPENS AFTER — ACTIONING IS A SEPARATE CONVERSATION (UPDATE MODE) · 11. THE DOWNLOADABLE REPORT · 12. SHARED DISCIPLINE · 13. WHAT COMPARISON MODE DOES NOT DO · 14. RELATIONSHIP TO ONE-OFF OVERRIDES · 15. OUTPUT EXPECTATION

## 10_CORPUS_VALIDATED_SCAFFOLDING
- **`10_CORPUS_VALIDATED_SCAFFOLDING.md`** (5 KB) — single-file topic (small enough to stay whole)
  - Sections: 10 — Corpus-Validated Scaffolding Reference · 1. Header title casing · 2. Menu archetype — safe fallbacks (only when no reference/series precedent) · 3. Lesson-menu *style* deviations (series conventions — preserve, don't "correct") · 4. Series that ship NO lesson menu by design · 5. Source-limitation note (important honesty check)

## 11_UPDATE_MODE
- **`11_UPDATE_MODE/11A_UPDATE_MODE_CORE.md`** (28 KB) — Update Mode: trigger, input, scope, ledger use, classification, conflicts, sweep (SS1-9)
  - Sections: 11 — Update Mode (Mode 4) · PURPOSE · 1. THE TRIGGER · 2. ACCEPTED INPUT — ANY FORMAT · 3. SCOPE / GRANULARITY VOCABULARY · 4. THE CHANGE LEDGER (`12_CHANGE_LEDGER.md`) — CONFLICT & LOCK REGISTRY · 5. MAJOR vs ROUTINE CLASSIFICATION · 6. CONFLICT CHECK (runs before any file is edited) · 7. CONFLICT ESCALATION & LOCKING · 8. PRE-FLIGHT — WHAT TO CONFIRM BEFORE EDITING · 9. THE BLAST-RADIUS SWEEP — FIND *EVERY* FILE THAT MUST CHANGE
- **`11_UPDATE_MODE/11B_UPDATE_MODE_WORKFLOW.md`** (12 KB) — Update Mode: the Repo Update Brief (SS10 — Claude Code actions edits on this repo; no file regeneration), exclusions, workflow pseudo-code, timestamps (SS10-16)
  - Sections: 10. THE REPO UPDATE BRIEF — PRECISE EDITS FOR CLAUDE CODE, NOT FILE REGENERATION · 11. (e) IGNORE ALWAYS — GROWING THE EXCLUSIONS LIST · 12. WORKFLOW (pseudo-code) · 13. THE TIMESTAMP CONVENTION (project-wide) · 14. RELATIONSHIP TO COMPARISON MODE & ONE-OFF OVERRIDES · 15. WHAT UPDATE MODE DOES NOT DO · 16. OUTPUT EXPECTATION

## 12_CHANGE_LEDGER
- **`12_CHANGE_LEDGER/12A_LEDGER_CORE_AND_LOCKS.md`** (9 KB) — Ledger purpose, status values, PART 1 locked decisions, PART 2 pending approval
  - Sections: 12 — Change Ledger (Conflict & Lock Registry) · PURPOSE · WHY ONE IN-HOUSE FILE IS FINE (feasibility note) · STATUS VALUES · HOW TO READ / MAINTAIN THIS LEDGER · PART 1 — LOCKED DECISIONS (binding & immutable — conflict check reads this FIRST) · PART 2 — PENDING APPROVAL (report-vs-report conflicts awaiting the design authority's resolution)
- **`12_CHANGE_LEDGER/12B_CHANGE_HISTORY_CL0001_0028.md`** (28 KB) — PART 3 change history: CL-0001 to CL-0028
  - Sections: PART 3 — CHANGE HISTORY (full append-only log — every actioned change)
- **`12_CHANGE_LEDGER/12C_CHANGE_HISTORY_CL0029_0040.md`** (20 KB) — PART 3 change history: CL-0029 to CL-0040 (continued)
  - Sections: 
- **`12_CHANGE_LEDGER/12D_CHANGE_HISTORY_CL0041_0062.md`** (25 KB) — PART 3 change history: CL-0041 to CL-0062 (continued) — CLOSED at CL-0062 (29 July 2026, 30 KB soft limit)
  - Sections: 
- **`12_CHANGE_LEDGER/12E2_CHANGE_HISTORY_CL0063_0071.md`** (24 KB) — PART 3 change history: CL-0063 to CL-0071 (continued) — CLOSED at CL-0071 (7 August 2026, 30 KB soft limit)
- **`12_CHANGE_LEDGER/12E3_CHANGE_HISTORY_CL0072_ONWARD.md`** (11 KB) — PART 3 change history: CL-0072 onward (continued) — THE OPEN PART: append new CL entries here (close it and start the next part at 30 KB)
  - Sections: 
- **`12_CHANGE_LEDGER/12E_CHANGE_HISTORY_FOOTNOTES.md`** (16 KB) — PART 3 footnotes (locked-decision and grouped-change notes)
  - Sections: 
- **`12_CHANGE_LEDGER/12F_LEDGER_LOGS_AND_NOTES.md`** (2 KB) — Blocked-request log, housekeeping, notes
  - Sections: BLOCKED-REQUEST LOG (audit) · HOUSEKEEPING (optional — nothing here is a recurring task) · NOTES

## 13_SPLIT_MODE
- **`13_SPLIT_MODE.md`** (28 KB) — single-file topic (small enough to stay whole)
  - Sections: 13 — Split Mode (Mode 5) · PURPOSE — what Split Mode is, and the problem it solves · 1. SPLIT MODE ≠ THE PAGE BOUNDARY SYSTEM (read first) · 2. PROACTIVE SINGLE-PAGE IDENTIFICATION + OFFERING SPLIT MODE · 3. TRIGGER, TRIAGE & APPLICABILITY · 4. OUTPUT #1 — THE BASE HOMEPAGE (`<CODE>-base.html`) · 5. OUTPUT #2 — ONE SECTION FILE PER SLOT (`<CODE>-lesson-<id>.html`) · 5A. EMISSION CADENCE — ONE FILE PER RESPONSE · 5B. MANUAL-STITCH GUIDANCE BLOCKS (`PAGEFORGE-GUIDE`) · 6. ID AND FILENAME CONVENTIONS · 7. KEYWORD / MARKER REFERENCE (reproduce these EXACTLY) · 8. THE ROUND-TRIP GUARANTEE (why the exactness matters) · 9. HOW PAGEFORGE'S PAGE STITCHER CONSUMES THE OUTPUT (so the split is valid) · 10. VALIDATION AND FAILURE HANDLING THE CONVERTER MUST HONOUR · …

## 14_SUBJECT_GLOBAL_PARAMETERS
- **`14_SUBJECT_GLOBAL_PARAMETERS/14A_SGP_PURPOSE_FAMILIES_1_5.md`** (21 KB) — Purpose + families 14.1-14.5 (Languages — finalised Audiovisual Package rules, registry data in `14C` —, Pathways, Taonga, CED, FUNdamentals)
  - Sections: 14 — Subject Global Parameters · PURPOSE · 14.1 Languages Phase 1–4 · 14.2 Pathways · 14.3 Taonga (The Arts) · 14.4 ConnectED (CED) Phase 5 · 14.5 FUNdamentals (Health & PE, Y1–10)
- **`14_SUBJECT_GLOBAL_PARAMETERS/14B_SGP_FAMILIES_6_11.md`** (26 KB) — Families 14.6-14.11 (LS, BLL, HPE, BLLR, MiW/WJ, cross-cutting)
  - Sections: 14.6 LS — Learning Support · 14.7 BLL — Blended Literacy · 14.8 HPE — Health & PE content lessons · 14.9 BLLR — Blended Literacy (Reading) · 14.10 MiW — My Te Kura Writing · 14.11 Cross-cutting notes
- **`14_SUBJECT_GLOBAL_PARAMETERS/14C_LANGUAGES_AV_ASSET_REGISTRY.md`** (15 KB) — The complete Languages Audiovisual Package asset registry, absorbed verbatim from the final `20260511_Language_HTML` (CL-0070) — the supplied HTML no longer needs to be consulted
  - Sections: 14C — Languages Audiovisual Package: the complete asset registry · 1. Delivery forms (the supplied markup shapes) · 2. Language icons · 3. German · 4. French · 5. Chinese · 6. Japanese · 7. Spanish · 8. Samoan · 9. Acknowledgements for the iStock-derived registry assets

## 15_INTERACTIVES_BUILD_MODE
- **`15_INTERACTIVES_BUILD_MODE/15A_MODE_CORE_AND_CONTRACT.md`** (13 KB) — Mode 6 core: trigger/auto-detection, the `cv2-built` anchor contract, output files + splitting, quality gate, authority order
  - Sections: 15 — Interactives Build Mode (Mode 6) · 1. TRIGGER & AUTO-DETECTION · 2. WHERE THIS MODE SITS IN THE PIPELINE · 3. FIRST ACTION on every uploaded worklist · 4. THE ANCHOR CONTRACT — the golden rule · 5. WHAT THE PAGE STITCHER DOES WITH IT · 6. OUTPUT FILES + THE SPLITTING SAFEGUARD · 7. QUALITY CHECK before emitting each file · 8. WHICH KNOWLEDGE TO LOAD — and the authority order · 9. MULTI-COMPONENT ENTRIES AND THE ACTIVITY-BOX CARVE-OUT · 10. TONE + INTERACTION
- **`15_INTERACTIVES_BUILD_MODE/15B_WORKLIST_FORMAT_AND_BUILD_RULES.md`** (12 KB) — The `{CODE}_interactives.txt` anatomy and the fragment-specific build rules
  - Sections: 15B — The worklist format, and how to build from it · 1. THE INPUT FILE — `{CODE}_interactives.txt` (file header · one entry line by line · reading the `Content:` block) · 2. THE BUILD RULES (declarative only · build the widget not the page · writer content verbatim · media placeholders · choosing the type · answer keys — the load-bearing attributes · shuffle, feedback and buttons · never emit) · 3. FAMILY CONVENTIONS STILL APPLY
- **`15_INTERACTIVES_BUILD_MODE/15C_WORKED_EXAMPLE.md`** (6 KB) — One worklist entry end to end: input, reading, output, why it is right
  - Sections: 15C — Worked example: one worklist entry → one finished build · The input entry · Reading it · The output · Why this is right

## 16_PAGEFORGE_COMPARE_MODE
- **`16_PAGEFORGE_COMPARE_MODE/16A_MODE_CORE_AND_INPUTS.md`** (20 KB) — Mode 7 core: trigger + the `PAGEFORGE` discriminator + the never-advertise rule, same-chat-only rule, the tester workflow, the four required inputs (incl. the `{CODE}_interactives.txt` worklist), the two PageForge upload formats, the workflow
  - Sections: 16 — PageForge Compare Mode (Mode 7) · 1. THE TRIGGER (same chat only · precedence and the one collision to watch · NEVER ADVERTISE THIS MODE) · 2. WHERE THIS SITS IN THE TESTER WORKFLOW · 3. WHAT THE REPORT IS FOR (and who reads it) · 4. THE FOUR REQUIRED INPUTS (the worklist — who built each widget, the boundary evidence, reconciling the inventory) · 5. THE TWO PAGEFORGE UPLOAD FORMATS — AND HOW TO TELL THEM APART (hand-off · stitched · mixed) · 6. WORKFLOW · 7. TONE + INTERACTION
- **`16_PAGEFORGE_COMPARE_MODE/16B_WHAT_TO_REPORT.md`** (21 KB) — The five finding classes, the boundary check (incl. reading the worklist's `Activity:` / `Content:` evidence), complex vs non-complex interactives, the exclusions (incl. the total comments-and-developer-notes exclusion), the uncertainty rule
  - Sections: 1. THE FIVE FINDING CLASSES · 2. NOTES ON EACH CLASS · 3. THE BOUNDARY CHECK (class B) — SPILL/SWALLOW, the per-box membership procedure, boundaries checked for EVERY interactive · 4. COMPLEX vs NON-COMPLEX INTERACTIVES (class C) — the non-complex list · 5. THE EXCLUSIONS (incl. comments, developer notes & restated writer instructions — ignored entirely) · 6. WHEN THE ORIGIN IS UNCLEAR — "For Gavin to judge" · 7. WHAT THIS MODE NEVER DOES
- **`16_PAGEFORGE_COMPARE_MODE/16C_REPORT_FORMAT.md`** (14 KB) — The one-shot report for Gavin: header, finding bundle, uncertain section, interactive inventory, coverage + exclusion counts, worked examples
  - Sections: 1. REPORT HEADER · 2. SECTION 1 — FINDINGS (class B extra requirement · confidence) · 3. SECTION 2 — FOR GAVIN TO JUDGE · 4. SECTION 3 — INTERACTIVE INVENTORY · 5. SECTION 4 — SCOPE AND COVERAGE · 6. WORKED EXAMPLES · 7. HOW THE RUN CLOSES IN CHAT

## Repo infrastructure
- **`_project_instructions_.md`** — the Claude.ai project's system-prompt text (paste into Project Instructions when it changes)
- **`CLAUDE.md`** — maintenance rules for Claude Code (the update ritual, size limits, how to split a growing file)
- **`README.md`** — plain-English overview for humans
- **`tools/check_kb.py`** — the guard script (size limits, index completeness, part headers, ledger integrity)
- **`tools/kb_manifest.json`** — the one-time migration record proving the split was byte-identical to the 2026-07-16 originals
