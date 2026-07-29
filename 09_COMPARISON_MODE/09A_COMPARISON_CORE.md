> **Last updated:** Wednesday, 29th July, 2026 6:41 PM
> **Granular part A (1 of 3) of `09_COMPARISON_MODE.md`** — Comparison Mode: trigger, inputs, workflow, what counts as a difference (SS1-4).
> All sibling parts live in `09_COMPARISON_MODE/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
> **Last updated:** Thursday, 16th July, 2026 9:30 PM

# 09 — Comparison Mode (Mode 3)
 
> **When to load:** Whenever a message contains the trigger phrase **`COMPARISON MODE`** — almost always accompanied by uploaded finished HTML files — OR when the designer replies to a freshly-generated comparison report with a list of difference-number → scope-letter pairings (the Phase 2 scope-assignment step, see Section 8). This is **Mode 3 — Comparison** (see `00_MASTER_INSTRUCTIONS.md` → Operating Modes). The `COMPARISON MODE` trigger takes precedence over every other mode signal.
 
---
 
## PURPOSE
 
This project's primary job is converting Writer Templates into finalized HTML (Mode 1). But the conversion is only the *first draft*. After this project outputs the HTML files in a chat, a human designer downloads them, then manually refines and corrects the code — fixing structures, swapping components, adjusting layouts — until the module is correct and ready to go live.
 
**Comparison Mode is the feedback loop.** It lets the designer bring their finished, corrected HTML *back* and have Claude produce a **single, comprehensive, downloadable difference report** that documents the changes the designer made — comparing the original raw content, the project's original output, and the designer's corrected version — so the project's **stored instruction files** can later be refined.
 
**Comparison Mode reports ONLY on differences the project files can actually fix.** A difference is reported **only if** the project's original output (input B) was produced by the **stored project-knowledge instructions** (files `00`–`08`, the COMP sections, the hard constraints, the tag taxonomy, the auto-rules, the comment & red-flag policy, etc.). A difference whose output (B) was **engineered by Claude from the uploaded structural reference / example module / other templated file** — i.e. lifted or mirrored from material the project does not own — is **filtered out and never reported.** Refining the project files cannot change what an external template ships, so reporting those differences would only generate noise the developer cannot action. See Section 5 (the inclusion gate).
 
**Comparison Mode runs in two stages, and never regenerates the project files itself:**
 
1. **Phase 1 — Initial (streamlined) report.** Claude detects every qualifying difference and writes them up as **numbered**, deliberately lightweight bundles — three sections each: raw content → originally generated code → designer's refined code. The **five scope options are listed ONCE, at the very top of the report** (Section 7). No scope block is repeated after individual differences, and the "source of the project's output" detail is intentionally withheld at this stage.
2. **Phase 2 — Finalized (detailed) report.** The designer reads the numbered differences and replies in chat with simple `differenceNumber-scopeLetter` pairings (e.g. `1 - A, 2 - C, 3 - D`). Claude parses these (Section 8) and **regenerates a final, detailed report** (Section 9) in which each surviving difference carries **four** sections — now including the precise **source of the project's output** (the cited rule: file, section, constraint) — followed by **its chosen scope written out in full English**. Differences scoped **(d) Ignore once are dropped entirely**; differences scoped **(e) Ignore always are kept and annotated with explicit instructions for a future, separate Claude conversation** to add them as a standing exclusion.
**Comparison Mode does NOT edit student content, and does NOT regenerate the project files.** The finalized report is the deliverable. Actually editing the project files happens later, in **Update Mode** (`11_UPDATE_MODE.md`) — a separate conversation the developer starts with the `UPDATE MODE` trigger and the finalized report (Section 10). Comparison Mode itself only analyses and reports.
 
---
 
## 1. THE TRIGGER
 
There are two entry points, for the two stages.
 
**Phase 1 trigger — generate the initial report.** Entered when **both** of the following are present in a single message:
 
1. The literal phrase **`COMPARISON MODE`** (case-insensitive) somewhere in the message text.
2. One or more **finished/refined HTML files** uploaded by the designer for the module in question.
The designer types `COMPARISON MODE` **into the same chat that originally performed the conversion**. This is deliberate: that chat already contains the original raw content source, the supplied structural reference, and the project's original HTML output. Comparison Mode reuses all three.
 
If `COMPARISON MODE` appears **without** any uploaded HTML files, do not start the analysis — ask the designer to upload their refined HTML files for the module.
 
**Phase 2 trigger — assign scopes.** Entered when the **immediately-preceding** comparison step in this chat produced a Phase 1 report (numbered differences + the scope legend) **and** the designer's new message consists of one or more **difference-number → scope-letter pairings** (e.g. `1-A`, `2 B`, `3: D`). No keyword is required — the pairing pattern itself is the trigger. See Section 8 for parsing. If the pairings arrive but no Phase 1 report exists in the chat, ask the designer to run `COMPARISON MODE` first.
 
---
 
## 2. THE FOUR REQUIRED INPUTS
 
A difference report compares the same module across four artefacts. Claude must locate all four before producing the report — including **R**, which is what makes the inclusion gate possible.
 
| Input | What it is | Where it comes from |
|---|---|---|
| **A — Original raw content** | The unconverted module content — the uploaded Writers Template `.docx`, the PageForge `.txt`, or the MTK `.docx` | Already in the **same chat**, from the original conversion turn |
| **R — Structural reference** | The HTML template file (Mode A) or related-module HTML files (Mode B) the project derived its skeleton from | Already in the **same chat**, from the original conversion turn |
| **B — Original generated HTML** | The HTML this project produced and presented earlier in the chat | Already in the **same chat**, from the original conversion turn |
| **C — Designer's refined HTML** | The finished, manually corrected HTML the designer is now uploading | **Uploaded now**, alongside the `COMPARISON MODE` trigger |
 
**R is what powers the inclusion gate.** It is the artefact a difference must be checked against to decide whether the project's output (B) was lifted from the supplied template (→ **filter out**) or produced by the stored instructions (→ **report**). Without R, that distinction cannot be drawn reliably, and template-derived differences may leak into the report.
 
### Handling missing context
 
Comparison Mode assumes it is running in the original conversion chat, so inputs **A**, **R** and **B** are already available. If the conversation is very long and any of them is no longer visible in context:
 
- First try to recover them — `conversation_search` / `recent_chats` may surface the original conversion turn if it happened in a separate chat.
- If A or B still cannot be located, **ask the designer to re-supply the missing piece** (re-upload the raw source, and/or paste the original generated HTML). Do **not** guess or reconstruct any of them — accurate reporting depends on the genuine originals.
- If **R** cannot be supplied, say so plainly. Without R the inclusion gate cannot reliably separate template-derived output from knowledge-derived output, so **ask the designer to re-supply R** before producing the report. If they cannot, proceed only with a clear caveat at the top of the report stating that template-derived differences could not be filtered out, and tag any difference whose origin is uncertain as `ORIGIN UNCERTAIN — verify before actioning`.
Never treat input C (the designer's file) as the originally-generated output, and never treat input B as the designer's version. Keeping the four straight is essential.
 
---
 
## 3. WORKFLOW
 
```
# ============ PHASE 1 — GENERATE THE STREAMLINED REPORT ============
FUNCTION comparison_phase1(raw_source_A, structural_ref_R, original_html_B, designer_html_C):
 
    # 0 — VERIFY INPUTS
    CONFIRM the COMPARISON MODE trigger is present
    CONFIRM designer HTML files (C) are uploaded
    LOCATE raw source (A), structural reference (R), original generated HTML (B)
    IF A or B missing → ASK the designer to re-supply; STOP until received
    IF R missing → ASK the designer to re-supply R; if unavailable, WARN that
        template-derived differences cannot be filtered and flag uncertain items
    IDENTIFY the module: code (e.g. OSAI201), title, module series prefix (e.g. "OSAI")
    RESOLVE the level descriptor from R's <html> template attribute
        (e.g. template="4-6" → "Phase 2 (Years 4–6)" — see Section 7.2)
 
    # 1 — PAIR THE FILES
    MATCH each designer file (C) to its corresponding original file (B) by page
    NOTE any file present in one set but not the other (added/removed page)
 
    # 2 — DETECT DIFFERENCES
    FOR EACH paired file:
        COMPARE original generated HTML (B) against designer HTML (C)
        IDENTIFY every meaningful change (Section 4)
        DROP anything matching a Section 4.1 exclusion (silently)
        TRACE each change back to the raw content (A) it derives from
 
    # 3 — APPLY THE INCLUSION GATE (Section 5)
    FOR EACH surviving difference:
        DETERMINE the origin of the project's output (B):
            knowledge-derived (stored instructions) → KEEP
            template-derived (lifted/mirrored from R / example / templated file) → DROP silently
        FOR a boundary item that touches both origins:
            KEEP only the knowledge-derived portion; DROP the template-derived portion
            IF the difference is dominantly template-derived → DROP the whole item
 
    # 4 — BUILD THE SINGLE STREAMLINED REPORT (NUMBERED, NO "SOURCE" SECTION)
    ASSIGN every kept difference a single CONTINUOUS number (1..N)
    PUT the report header (Section 6.1) at the top
    PUT the SCOPE LEGEND (Section 7, all five options) immediately below the header — ONCE
    FOR EACH kept difference (in number order):
        BUILD a THREE-section bundle (Section 6.2):
            1. Original raw content (source)
            2. Originally generated code (this project's output — input B)
            3. Designer's refined code (the correct target — input C)
        (DO NOT include a "source of the project's output" section in Phase 1)
 
    # 5 — DELIVER
    SAVE the report as a downloadable file (Section 11) and PRESENT it
    TELL the designer how to assign scopes: reply with number-letter pairings (Section 8)
    END the message with the on-screen scope key (Section 6.4)
 
# ============ PHASE 2 — PRODUCE THE FINALIZED DETAILED REPORT ============
FUNCTION comparison_phase2(designer_pairings_text, phase1_report):
    PARSE designer_pairings_text into {differenceNumber → scopeLetter} (Section 8)
    VALIDATE every number maps to a real difference and every letter is a–e
    IF any difference has no assigned scope → LIST the missing numbers and ASK
    IF any pairing is invalid (bad number / bad letter) → SAY which and ASK
    REGENERATE the FINALIZED DETAILED REPORT (Section 9):
        FOR EACH difference, by its scope:
            (a)/(b)/(c) → INCLUDE with FOUR sections + chosen scope in full English
            (d) Ignore once → OMIT the difference entirely
            (e) Ignore always → INCLUDE with FOUR sections + an explicit
                "Instruction for the future project-file update" block (Section 9.3)
        The four sections per included difference are:
            1. Original raw content (source)
            2. Source of the project's output (cited rule: file/section/constraint)
            3. Originally generated code (input B)
            4. Designer's refined code (input C)
    SAVE and PRESENT the finalized report
    STATE plainly: the project files are NOT regenerated here; this report is
        handed off to a separate future conversation to action (Section 10)
```
 
---
 
## 4. WHAT COUNTS AS A DIFFERENCE
 
Report every change that is **meaningful for refining the project's stored instruction files** — anything that tells us the conversion did something the designer had to correct *and* that the project files could be taught to do differently.
 
**Report these (subject to the inclusion gate in Section 5):**
- **Component changes** — a different component chosen (e.g. accordion → tabs), a different layout (`standard` → `column`), a different variant.
- **Structural changes** — different grid wrappers, added/removed `row`/`col` structure, re-nested elements, moved blocks (e.g. acknowledgements relocated).
- **Class / attribute changes** — added, removed, or changed classes or attributes (`autoCheck` added, `noShuffle` removed, wrapper class corrected).
- **Heading / title changes** — heading level changes, `<span>` added/removed, title-pattern corrections.
- **Comment changes** — comments the designer deleted or converted to red flags (highly relevant to the comment policy in `02`).
- **Skeleton / `<head>` changes** — script URLs, `template`/`level` attributes, custom CSS links added or removed.
- **Image-handling changes** — placeholder vs direct-link decisions, filename corrections.
- **Content placement changes** — content moved between pages or sections.
- **Added or removed elements / pages.**
**Do NOT report (noise — ignore):**
- Pure whitespace, indentation, or line-ending differences.
- Re-ordering that has no semantic effect.
- Cosmetic reformatting that does not change rendered output or structure.
- Changes confined to genuine student-content wording **unless** they reveal a conversion error (Comparison Mode does not police writer content — but if the project altered writer text and the designer restored it, that *is* a reportable conversion fault).
When unsure whether a change is meaningful, include it (it still has to clear the Section 5 gate) — but keep the description tight.
 
---
 
