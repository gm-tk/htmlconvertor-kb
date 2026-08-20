> **Last updated:** Friday, 21st August, 2026
> **Granular part B (2 of 7) of `00_MASTER_INSTRUCTIONS.md`** — Conversion pipeline (Mode 1 pseudo-code).
> All sibling parts live in `00_MASTER_INSTRUCTIONS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## CONVERSION PIPELINE (Mode 1 — Pseudo-code)
 
> Applies to **Conversion Mode** only. For **Advisory & Support Mode (Mode 2)** — answering questions, completing half-finished modules, debugging interactives — follow `08_MODULE_SUPPORT_DEBUGGING.md` instead.
 
```
FUNCTION convert_writer_template(content_source, structural_reference, media_list=OPTIONAL):
 
    # ── PHASE 0: VERIFY INPUTS ──
    IF content_source NOT provided:
        ASK user for a content source — PageForge .txt, raw Writers Template .docx,
            or MTK Writers Template .docx
        STOP until received
    DETERMINE content source format:
        IF .txt file → PageForge pathway (standard)
        IF .docx file:
            IF MTK template (MTK heading / TRR code / bilingual table) → MTK pathway
            ELSE → standard Writers Template .docx pathway
        IF BOTH a .txt and a .docx of the same module supplied → prefer the .txt
    IF a Media List .docx is also supplied:
        REGISTER it as the optional media reference (used for media verification + acks)
    IF an iStock acknowledgements file is also supplied (API-sourced list of iStock acks lines):
        REGISTER it as authoritative for its iStock items — used VERBATIM in the acks block
            and as the preferred alt-text image name for those iStock images
    IF structural_reference NOT provided:
        # Exception: MTK pathway is self-contained (skeletons embedded in file 07)
        IF pathway is NOT MTK:
            ASK user: "Do you have a dedicated template HTML file, or completed
                       HTML files from a closely related module I can use as reference?"
            STOP until received
    DETERMINE structural reference mode:
        IF single template file → Mode A (Dedicated Template)
        IF multiple module HTML files → Mode B (Reference Module)
 
    # ── IMAGE OUTPUT MODE ──
    # → See: Images section in 01_PIPELINE_EXTRACTION_TAGS.md
    DETERMINE image output mode BEFORE generating any HTML:
        IF user has stated a preference (e.g., "use placeholders", "direct links",
           "skip placeholders", "I'm a direct-link designer"):
            USE stated mode silently
        ELSE:
            PROMPT user: "Which image output mode would you like?
                • Placeholder Mode — visible placehold.co placeholders with the
                  real image references commented out for CS to swap in later.
                • Direct Link Mode — direct image filenames (e.g., images/iStock-XXXXXXXXX.jpg)
                  with no placeholder or comment block."
            STOP until user responds
    APPLY chosen mode uniformly to ALL images in the conversion
 
    # ── ⚠️ THESE ARE THE ONLY TWO PRE-FLIGHT QUESTIONS ──
    # A settled UNIVERSAL constraint is NEVER offered to the designer as a choice.
    #   The structural reference and the image output mode are asked because the
    #   project genuinely cannot know them. Everything a "(Universal)" constraint
    #   already settles is NOT a question — do not surface it as one, do not offer
    #   it as an A-or-B, and do not treat a superseded rule found in the knowledge
    #   base as a live alternative to the rule that superseded it.
    #   Worked failure (SCES302, Aug 2026): the retired "lesson <h1> = MODULE title"
    #   wording was surfaced and put to the designer as "module title (constraint 16)
    #   vs lesson title"; the designer answered "module title" and 8 lesson pages
    #   shipped with the wrong <h1>. Constraint 79 had already settled it universally.
    # IF a designer instruction CONTRADICTS a universal constraint:
    #     SAY SO plainly, cite the constraint, and ask them to confirm the override
    #     STOP until confirmed — never follow it silently
    #     (a confirmed override is then a Mode 4 / Update Mode change, not a one-off)
 
    # ── PHASE 1: ANALYZE STRUCTURAL REFERENCE ──
    # → See: section 01 in 01_PIPELINE_EXTRACTION_TAGS.md
 
    IF Mode A (Dedicated Template):
        EXTRACT from template_html:
            - exact <html> tag attributes
            - exact <head> section (script URLs are NOT interchangeable)
            - heading patterns (`<span>` only in `<h1>` header titles, never in body headings)
            - module menu structure (2 tabs vs 3 tabs)
            - title pattern (single vs dual h1)
            - footer/acknowledgements pattern
 
    IF Mode B (Reference Module):
        # → See: 06_TEMPLATE_RECOGNITION.md for detection, validation, and known pitfalls
        CLASSIFY reference files:
            - DETECT Legacy vs Refresh (06_TEMPLATE_RECOGNITION.md Section 1)
            - IF Legacy: FLAG to user, confirm intent before proceeding
            - IDENTIFY Refresh sub-type (06_TEMPLATE_RECOGNITION.md Section 2)
            - VALIDATE against structural norms for that sub-type (06_TEMPLATE_RECOGNITION.md Section 3)
            - CHECK for known pitfalls (06_TEMPLATE_RECOGNITION.md Section 4)
            - RUN Mode B validation checklist (06_TEMPLATE_RECOGNITION.md Section 5)
        ANALYZE all provided reference HTML files:
            - IDENTIFY the overview page (-00) and lesson pages (-01, -02, etc.)
            - EXTRACT the shared skeleton: <html> tag, <head> section (exact script URLs),
              header structure, module menu pattern, body grid pattern, footer pattern
            - NOTE the year level template attribute (e.g., template="9-10")
            - NOTE whether the reference uses dual titles (English + Te Reo)
            - NOTE the module menu structure (simplified vs full tabs, heading levels used)
              (lesson-page menus only — the overview (-00) module-menu TAB SET is never
               copied from the reference: it is built from the canonical tab set,
               driven by the new module's own content — constraint 67)
            - CATALOGUE structural patterns observed across pages (activity wrappers,
              component usage, alert styles, etc.) as guidance for the new module
        DERIVE a composite skeleton by:
            - Using the <html> and <head> from any reference page (they share these)
            - Using the overview page (-00) as the template for the new -00 page
            - Using a lesson page (-01 or -02) as the template for new lesson pages
            - REPLACING the reference module code with the NEW module code
            - REPLACING reference titles with NEW module titles from the content source
            - KEEPING all structural patterns, script URLs, and class usage intact
 
    # ── PHASE 2: READ CONTENT SOURCE ──
    # → See: section 02 in 01_PIPELINE_EXTRACTION_TAGS.md
    READ the content source:
        IF PageForge .txt:
            - Extract module code from metadata block (Module Code: field)
            - Skip everything before --- CONTENT START ---
            - Content begins from the first [TITLE BAR] tag onward
        IF standard Writers Template .docx:
            - Extract text with `extract-text`
            - Extract module code from the metadata table / [TITLE BAR] / filename
            - SKIP ALL front-matter: submission checklist, LOT tags table,
              Section A (Merging Resources), Section B guidance box, contents page,
              sign-off line, writer-guidance notes
            - Content begins from the first [TITLE BAR] tag onward — convert ONLY this
            - Tags appear as bare [tag] (no 🔴[RED TEXT]🔴 markers); tables are
              markdown tables (| cell | cell | with |---| separator rows)
        IF MTK Writers Template .docx:
            - Follow 07_MTK_DOCX_CONVERSION.md
    IF a Media List .docx was supplied:
        - Extract its table (Item No. | WTPg No. | Item Type | Description | Source | URL)
        - Use it to verify media URLs and to source titles/descriptions for acks
    FORMAT CONVENTIONS (PageForge .txt):
        - Red text: 🔴[RED TEXT] content [/RED TEXT]🔴 (writer instructions)
        - Formatting: **bold**, *italic*, ***bold italic***, __underline__
        - Hyperlinks: __text__ [LINK: URL] (text links) or bare URLs (media refs)
        - Tables: ┌─── TABLE ───  / └─── END TABLE ─── with ║ column separators
        - Bullets: • with 2-space indent per nesting level
        - In-cell line breaks: /
 
    # ── PHASE 3: PAGE BOUNDARIES ──
    # → See: section 03 in 01_PIPELINE_EXTRACTION_TAGS.md
    APPLY all 4 Page Boundary Validation Rules:
        Rule 1: DISREGARD [End page] before [MODULE INTRODUCTION]
        Rule 2: INSERT implicit boundary before [LESSON n] if no [End page] since last lesson
        Rule 3: DISREGARD [End page] closing empty lesson segments
        Rule 4: MERGE orphaned title bar segments with next segment
    DETERMINE page structure (multi-page vs single-page):
        IF [LESSON] / [End page] page boundaries exist → MULTI-PAGE → produce separate -00/-01/... pages (normal)
        ELSE (no page boundaries, or a module type that ships as ONE page) → SINGLE-PAGE:
            SAY SO, and PROACTIVELY OFFER Split Mode (one line: emit the page in stitchable
                pieces that PageForge's Page Stitcher recombines into one file) —
                make the offer MORE PROMINENT when the single-page output is large
                (many lessons / heavy interactives) and at real risk of exceeding one response.
            Split Mode is an OFFER, not automatic — run it only if the user invokes `SPLIT MODE`.
            Once invoked, emit ONE file per response (base first, then one section per prompt, in order).
            If the user does nothing, continue producing the normal single-page file.
            # → See: 13_SPLIT_MODE.md (Split Mode is a packaging variant only — all conversion rules unchanged)
 
    # ── PHASE 4: NORMALIZE TAGS ──
    # → See: section 04 in 01_PIPELINE_EXTRACTION_TAGS.md
    FOR EACH square-bracket tag in the content:
        STRIP red text markers if present
        TRIM whitespace
        COMPARE case-insensitively against normalization table
        EXTRACT trailing number/ID (e.g., "1A", "3")
        MAP to normalized form + sub-identifier
 
    # ── PHASE 5: MAP TAGS TO COMPONENTS ──
    # → See: section 05 in 01_PIPELINE_EXTRACTION_TAGS.md (for structural/content tags)
    # → See: Writer Intent Interpretation in 01_PIPELINE_EXTRACTION_TAGS.md (for ambiguous CS requests)
    # → See: section 06 in 02_DATA_CONTENT_VERIFICATION.md (for interactive data extraction)
    # → See: the relevant COMP_XX section in 03_COMP_CORE_INTERACTIVES.md,
    #         04_COMP_SEGMENTS_OVERLAYS.md, or 05_COMP_LANGUAGE_MEDIA_LAYOUT.md
    FOR EACH normalized tag:
        IDENTIFY HTML component
        IF interactive component:
            CONSULT the relevant COMP_XX section for exact HTML structure
            IDENTIFY data pattern (table, front/back, numbered, etc.)
            PARSE all data points
            APPLY Component Whitelist Check:
                FULL MATCH → generate using documented structure
                PARTIAL MATCH → Tiered Fallback Protocol
                NO MATCH → red flag + closest alternative with visible content
    ENFORCE one interactive per activity (constraint 62):
        IF two or more interactives fall under ONE writer activity heading →
            SPLIT into separate sequential activities (the first interactive keeps the
            writer's activity number; each subsequent interactive takes the next letter),
            RENUMBER all following activities accordingly, and FLAG the split with a
            visible Red Flag: note so the renumbering is auditable against the source
 
    # ── PHASE 6: PRODUCE HTML ──
    # → See: section 07 in 02_DATA_CONTENT_VERIFICATION.md (preservation, grid, merging)
    # → See: section 01 in 01_PIPELINE_EXTRACTION_TAGS.md (skeleton structure)
    # → See: Images section in 01_PIPELINE_EXTRACTION_TAGS.md (image output mode rules)
    COPY complete skeleton from structural reference (template or derived from reference module)
    POPULATE with converted content:
        - ALL body content inside row > col-* grid
        - ALL activity divs inside row > col-md-8 col-12 (EXCEPT wide components like D&D column layout which uses col-md-12 col-12, and a D&D column with many images which uses col-12 / col-md-11 col-12 by module type — never col-md-10, see constraint 56; carousel viewer width is contextual — col-md-12 col-12 when nested inside a col-md-8 wrapper, col-md-8 col-12 when standalone, see constraint 17). Activity/interactive wrappers NEVER use col-md-10: where more width than col-md-8 is needed, use col-12 (Standard) / col-md-11 col-12 (Inquiry & Fundamentals) / col-md-8 col-12 with a paired alertImage at col-md-4. Inside an activity wrapper the inner text column is col-12 (never col-md-8 col-12); at the DEFAULT wrapper width text and interactive share ONE inner row, and the two-row split is retained ONLY in a WIDENED wrapper, where the interactive spans the widened width (constraint 63)
        - [MTKquiz] builds a numbered activity box (next consecutive number, even if the writer
          assigned none) holding only these, in order — quiz title h3 (default "Quiz"),
          the writer's quiz instructions where the writer supplied any, a visible Designer/Developer To Do: note (create the quiz in
          MTK DEV and orgunit link it), and a blank-href "Go to quiz" button — and NEVER the quiz's
          own questions/options/answers, which are silently omitted (constraint 65); Creative Services videos embed as the pending-ID Vimeo scaffold + Designer/Developer To Do: note (constraint 64); supervisor triggers build the super-content-button family, never the retired supervisorContainer trio (constraint 68)
        - Lesson pages: use THAT LESSON'S OWN title in the header <h1><span> (never the module title) and the zero-padded lesson number (not the module code) in #module-code — constraint 79. Source order: text inside the boundary tag ([LESSON 2: Puanga]) > text after the boundary tag ([LESSON 1] The night sky) > the opening [H2] after [Lesson content] > a [Lesson Overview] heading naming the lesson > module title + a visible Designer/Developer To Do: note. A boundary label that normalises to nothing (e.g. "[LESSON 2] Lesson 2") falls through to the next source. Strip any leading "Lesson N"/"Lesson N:" prefix — a prefix is NEVER a reason to demote the title to a body <h3>, and a lesson name the writer wrote twice is one title, not a conflict. Drop the duplicate body heading (constraint 47). One title <h1> per lesson page at every level unless the writer gave that lesson its own bilingual name
        - Preserve writer text verbatim (trust the content source as-is)
        - Convert formatting markers to HTML tags
        - Strip red text; render any substantive writer note / CS instruction as a VISIBLE red flag prefixed `Writers Note:` (red + bold), never a hidden comment
        - A captured whitelisted reviewer comment — a red-text note carrying a leading `Note from {author}:`
          lead from one of the six reviewers (Kate Scanlon, Nadia Stanton, Caroline Schwer,
          Simon Vita, Amanda Griffiths, Creative Services) — is rendered as a VISIBLE red + bold designer
          message preserving the lead + text verbatim, in position (immediately before the element
          it refers to), never tag-parsed, never a hidden comment, never dropped → See 01 Red Text Handling / 02 Comment & Red Flag Policy
        - Never render square-bracket tags as visible text
        - APPLY image output mode (Mode P or Mode D) consistently to ALL images
        - ACKNOWLEDGEMENTS: when generating the overview page (-00), place the
          acknowledgements accordion at the BOTTOM of page 0.0 (after the footer).
          Acknowledgements ALWAYS go on the first page (0.0) — never on any other page.
          → See: Acknowledgements in 05_COMP_LANGUAGE_MEDIA_LAYOUT.md
    IF Mode B:
        - ENSURE all reference module codes are replaced with the new module code
        - ENSURE all reference module titles are replaced with new module titles
        - FIX any known structural issues identified during validation (missing <body>, malformed paths)
        - NOTE in verification summary that reference module files were used (not a dedicated template)
 
    # ── PHASE 7: VERIFY ──
    # → See: section 08 in 02_DATA_CONTENT_VERIFICATION.md
    RUN full verification checklist
    CONFIRM every images/iStock-{ID}.jpg ID equals the gm-leading number of its
        writer URL and that the acknowledgements cite the SAME ID (constraint 61)
    CONFIRM all student-facing content is visible HTML
    CONFIRM every tabbed -00 module menu uses the canonical tab set with 1:1 li/tab-pane
        pairing and content-driven omission (constraint 67), and every supervisor button
        uses the super-content-button family (constraint 68)
    CONFIRM acknowledgements (if generated) are at the bottom of page 0.0 — not elsewhere
    REPORT: content source format (PageForge .txt / standard Writers Template .docx / MTK .docx),
            whether a media list was supplied and used,
            template source (dedicated or reference module + which files),
            level confirmed, boundary results, div counts,
            interactive counts, red flags, ambiguities,
            image output mode used (Mode P or Mode D)
    IF Mode B:
        REPORT: detected sub-type, any pitfalls found and how they were handled,
                heading pattern used (standard or reference-matched), domain (prod or dev)
```
 
---
 
