> **Last updated:** Thursday, 16th July, 2026 9:30 PM
> **Granular part A (1 of 2) of `09_COMPARISON_MODE.md`** — Comparison Mode: trigger, inputs, workflow, differences, exclusions, inclusion gate (SS1-5).
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
 
## 4.1 DIFFERENCES NOT TO CAPTURE (EXCLUSIONS)
 
Some categories of difference are **never reported**, even though they would otherwise look like meaningful changes. These are not "noise" in the whitespace sense — they are substantive edits that the designer has explicitly directed should be excluded from difference reports, because they do not indicate a rule fault or a conversion error. Do NOT create a comparison bundle for any difference that falls into these categories.
 
> These exclusions are applied **in addition to** the inclusion gate in Section 5. A difference must clear *both* — it must be knowledge-derived (Section 5) *and* not fall into an exclusion below — to be reported.
 
### Exclusion 1 — Red flags & designer notes (ALL templates, ALL modules)
 
Never report a difference that consists of a **red flag or designer note** being added, removed, reworded, or reformatted. This includes any change of prefix among the source-specific designer-note prefixes (`Note from {author}:`, `Writers Note:`, `Red Flag:`, `Designer/Developer To Do:`), the **substitution of any of them for a non-standard label the designer prefers** (e.g. `RED FLAG:` → `Designer note:`), the dropping of any such prefix, a change in font weight or styling of the note (including the presence or absence of the trailing semicolon in `style="color: red;"` / `style="color: red"`, and the addition or removal of `font-weight: bold`), the removal of a restated writer instruction or source link, and any change to the wording or formatting of an in-progress `<p style="color: red; font-weight: bold;">…</p>` message.
 
Rationale: red flags and designer notes are developer scaffolding, **not module content**. They are expected to change — each initial red flag is resolved and removed as the designer actions it; some are rewritten to convey a different task to be actioned later; some are added in this style specifically to generate a front-end message aimed at the original course writer (asking them to clarify something to the human developer). Because their presence and wording are inherently transient and developer-facing, comparing them tells us nothing about whether a project file needs refining. Ignore them entirely.
 
> **Scope of this exclusion (confirmed 9 July 2026).** This covers **every** red-flag / designer-note difference without exception — prefix, label, wording, inline style, font weight, and presence/absence alike. Nothing in this category is ever reported by Comparison Mode. It therefore already subsumes designer relabelling of a Convertor red flag (e.g. `RED FLAG:` / `style="color: red;"` → `Designer note:` / `style="color: red"`); no separate exclusion is needed for it.
 
### Exclusion 2 — Overview module-menu heading styling (currently suspended)
 
Do NOT report `<span>`-wrapper additions/removals or heading-level styling differences on **overview-page module-menu headings** (the `<h4>`/`<h5>` headings inside `#header` / `#module-menu-content`, e.g. the Overview / Knowledge / Practices / Learning Intentions / Success Criteria labels).
 
Rationale: the team is currently **reinforcing the one source of truth for overview information**, so overview-page module-menu content is in flux. Overview information must not be updated or flagged at this time. This exclusion is temporal ("at this time") — revisit it once the one-source-of-truth work concludes. (The underlying rule — constraint #7, no `<span>` on body headings — is unchanged; this exclusion only suppresses *reporting* the difference.)

> *Status note (16 July 2026):* the one-source-of-truth work has now landed as the **canonical overview module-menu specification** (`01_PIPELINE_EXTRACTION_TAGS.md` → Module Menu Structures → Module Overview Pages (`-00`) — Canonical Tabbed Menu; `00` constraint 67). This exclusion is deliberately **retained as-is** until the designer explicitly asks for it to be lifted; it continues to suppress *reporting* only and never changes conversion behaviour.
 
### Exclusion 3 — Bespoke designer presentation / composition decisions (ALL templates, ALL modules)
 
Do NOT report a difference that is a **bespoke, one-off presentation or composition choice** the designer made for specific content — a choice that is not a documented rule and is not expected to become one. These are editorial/layout calls made per module; they do not indicate a rule fault. Observed examples that must NOT be captured:
 
- **Bespoke content-presentation layouts** — e.g. wrapping a sentence-parts-with-labels example in a `table` (with a `<th>` label row) instead of stacked `<p>` paragraphs.
- **Bespoke compositions of documented components for an undocumented writer request** — e.g. realising an `[embed book]` / `[embed story]` request as a cover image with a `clickDrop` that opens a page-image `carousel`.
- **Bespoke component substitutions for an undocumented writer request** — e.g. using `bingo` (with permissive `value="correct"` tiles) instead of `selectionBox` for a "click-the-tile-to-change-colour" word grid.
- **Bespoke per-row column-order / column-width refinements** — e.g. swapping or resizing the text and image columns in a particular content row to suit that specific content.
Rationale: in each case the designer is exercising judgement about how a specific piece of content should look, not correcting a systematic fault in the project's rules. Capturing these would generate churn against decisions that are expected to vary module-to-module. (If a genuinely systematic, repeating fault against an existing constraint is observed across many modules, that is a different matter — but a single bespoke styling choice for one activity is not reportable.)
 
### Exclusion 4 — Designer supplying media metadata the conversion could not confirm (ALL templates, ALL modules)

Do NOT report a difference in which the designer has **filled in acknowledgement media metadata that the conversion could not confirm from the supplied materials and therefore correctly placeholdered or red-flagged**. Observed examples that must NOT be captured:

- Resolving `[title to be confirmed]` / `[author to be confirmed]` in a video acknowledgement entry to the real published title and channel.
- Supplying an image/asset title, author, or source line that the Media List, iStock acknowledgements file, or writer's template did not carry.

Rationale: **supplying media metadata the source did not contain is expected designer production work, not a rule fault.** The conversion behaved correctly — the rules require a visible placeholder or red flag rather than an invented title (`05` → Acknowledgements → Video entries; constraint 54/66), and the designer then did exactly the production step that flag exists to request. Reporting it would generate churn against a rule that is working as designed. **This suppresses *reporting* only — the conversion behaviour is unchanged:** unconfirmable media metadata is still placeholdered/red-flagged, never invented. *(Established via the OSSC401 finalized difference report, Difference 7, scope (e), 16 July 2026.)*

### Exclusion 5 — Per-instance presentational modifier classes with no documented trigger (ALL templates, ALL modules)

Do NOT report a difference in which the designer has **added or removed a documented presentational modifier class on an otherwise correctly-built component, where that modifier has no documented trigger condition and is applied per-instance to taste**. Observed examples that must NOT be captured:

- `noBG` added to one `dragAndDrop` but not to another in the same module.
- Comparable "to taste" presentational modifiers toggled on a single component instance.

Rationale: these are **styling calls that vary activity-to-activity within a single module**, not rule faults — the very same module often shows the modifier applied to one instance and omitted from the next, so there is no consistent rule to derive. The component itself was built correctly; only its presentation was tuned. **Scope limit:** this covers modifiers that are **documented but trigger-less** (available for the designer to apply at discretion). A modifier that *does* carry a documented trigger condition (e.g. `autoCheck`'s template-based auto-application, constraint 38) is **not** covered — a wrong `autoCheck` is a genuine rule fault and stays reportable. *(Established via the OSSC401 finalized difference report, Difference 20, scope (e), 16 July 2026.)*

> **Note on Phase 2 option (e).** When the designer assigns scope **(e) — Ignore always** to a difference (Section 7), they are telling you that an *entire category* of change like this should never be reported again. That is the designer-driven way to *grow* this exclusions list. A difference scoped (e) is kept in the finalized report **with an explicit instruction for the future project-file-update conversation (Update Mode, `11_UPDATE_MODE.md`)** to add it here as a new standing exclusion (Section 9.3). Comparison Mode itself does not edit this list — it only records the instruction.
 
### Applying the exclusions
 
Run the exclusion check during Phase 1, Detect Differences, before applying the inclusion gate and before building any bundle: if a detected change falls into **any** of Exclusions 1–5, drop it silently — do not mention it.
 
---
 
## 5. THE INCLUSION GATE — KEEP KNOWLEDGE-DERIVED, FILTER OUT TEMPLATE-DERIVED
 
This is the defining rule of Comparison Mode. **Only differences whose project output (B) was produced by the stored project instructions are reported. Differences whose output (B) was engineered by Claude from the uploaded structural reference / example module / other templated file are filtered out entirely.**
 
The question for every difference is always: *"Where did the project get that chunk of HTML from?"* — and the answer decides whether the difference is reported at all.
 
### 5.1 Why the gate exists
 
The whole point of the report is to refine the project's **own** stored instruction files. The project owns and can change those files. It does **not** own the structural reference the designer supplied for a given conversion — that template is external input. If the designer corrected a chunk that the project merely **copied from the supplied template**, updating the project files would not prevent the same chunk recurring on the next module (because the next template still ships it). So those differences are noise for this purpose, and are dropped. Only differences the project files can actually fix are worth reporting.
 
### 5.2 What is KEPT (knowledge-derived → report it)
 
A difference is **kept and reported** when the project's output (B) was **primarily produced by following a stored rule, constraint, or component pattern from project knowledge** (`00`–`08`, COMP_*, hard constraints, tag taxonomy, autoCheck auto-application, the comment & red-flag policy, the acknowledgements placement rule, the image output mode rules, etc.):
 
- The HTML in B does **not** appear in R but **does** match a documented pattern in project knowledge.
- The HTML in B was inserted because of a hard constraint, a tag-to-component mapping, or an automatic rule (e.g. `autoCheck` auto-application, acknowledgements placement, image output mode).
- The HTML in B contradicts what R actually shows because a stored constraint overrode the template.
### 5.3 What is FILTERED OUT (template-derived → drop it silently)
 
A difference is **dropped and never reported** when the project's output (B) was **primarily produced by copying, mirroring, or referencing the supplied structural reference (R), example module, or other templated file**:
 
- The HTML in B reproduces a block from R verbatim or near-verbatim (the `<head>` block, the `#header` skeleton, the `#footer` skeleton, the acknowledgements wrapper shell, the module-menu tab skeleton, etc.).
- The HTML in B is page chrome that was lifted from R as a skeleton.
- The class names, attribute values, or markup conventions in B were taken from a pattern visible in R rather than from a documented project-knowledge rule.
Drop these silently — do not bundle them, do not mention them, do not count them.
 
### 5.4 Boundary cases — items that touch both origins
 
Some differences sit at the boundary: the template ships *something* AND a stored rule *also* affects the same element. Examples:
 
- The template ships a bare `acks` wrapper; project knowledge adds the `acksAI` modifier when the module uses AI-generated media. → The wrapper shell is template-derived (drop); the `acksAI` modifier is knowledge-derived (keep, if the designer changed it).
- The template ships a `<title>` placeholder; project knowledge dictates the actual `<title>` content per page. → The element's presence is template-derived (drop); its content is knowledge-derived (keep, if changed).
- The template ships a 3-item footer-nav skeleton; project knowledge says trim and populate. → The skeleton is template-derived (drop); the trimming/populating is knowledge-derived (keep, if changed).
**Handling rule for boundary cases:**
 
1. Identify which **portion** of the changed chunk the designer actually corrected.
2. If that portion is **knowledge-derived**, report only that portion as a normal difference and note in "What changed" that the surrounding shell is template-derived and out of scope.
3. If the corrected portion is **template-derived**, or if the difference is dominantly template-derived, **drop the whole item.**
4. When the dominant origin genuinely cannot be determined, default to **keeping** the item but tag it `ORIGIN UNCERTAIN — verify before actioning`, so the developer can confirm before refining a project file on its basis.
### 5.5 Practical inclusion checklist
 
For each surviving (post-exclusion) difference, ask in order:
 
1. **Does the changed chunk in (B) appear in the structural reference (R), copied or mirrored?**
   - Yes → **template-derived → DROP.**
   - No → continue.
2. **Did a stored project-knowledge rule produce the chunk in (B)?**
   - Yes (note which file/section — you will cite it in the Phase 2 report) → **KEEP.**
   - No → re-examine; if still unclear, KEEP and tag `ORIGIN UNCERTAIN`.
3. **Does the difference touch both origins?**
   - Yes → keep only the knowledge-derived portion; drop the template-derived portion (Section 5.4).
---
 
