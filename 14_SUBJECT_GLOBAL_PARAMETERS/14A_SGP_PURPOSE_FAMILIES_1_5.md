> **Last updated:** Thursday, 16th July, 2026 11:05 AM
> **Granular part A (1 of 2) of `14_SUBJECT_GLOBAL_PARAMETERS.md`** — Purpose + families 14.1-14.5 (Languages, Pathways, Taonga, CED, FUNdamentals).
> All sibling parts live in `14_SUBJECT_GLOBAL_PARAMETERS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
> **Last updated:** Thursday, 16th July, 2026 11:05 AM

# 14 — Subject Global Parameters

> **When to load:** When converting or advising on a module that belongs to one of the subject **cohorts / series** documented below (Languages Phase 1–4, Pathways, Taonga, CED Phase 5, FUNdamentals H&PE, LS, BLL, BLLR, MiW/WJ, HPE content lessons), and whenever these conventions are changed in Update Mode. These are the design team's per-subject "global parameters" — the standing look-and-feel and structural conventions each subject wants applied to every one of its modules.

---

## PURPOSE

The design team (Persephone / Gavin) maintains a set of **global-parameter documents** — one per subject family — that every module in that family is checked against. Historically a developer opened the reference document beside the built module and compared by eye. This file folds those conventions into project knowledge so the Convertor applies them automatically.

**How this file relates to the rest of the knowledge base:**

- **Scope-bound.** Every section below carries a **scope tag** naming exactly which modules it governs. A convention here applies **only within its scope** — it is not a universal rule unless it also appears in `00`'s constraints.
- **Mode B sibling authority still wins.** The closest same-series predecessor module remains the most reliable structural reference (`06_TEMPLATE_RECOGNITION.md`). Where a built sibling and this file disagree on structure, follow the sibling and raise a `Red Flag:`.
- **This file does not re-own existing components.** Where a convention uses a component another file owns (carousel, alert, flipCard, clickDrop, speech bubble, sticky nav, activity/dropbox), the mechanics stay in `03`/`04`/`05` and this file only records the **subject-specific choice** (which option, which colour, which label) and cross-references the owner.
- **Deferred items are visible, not silent.** Any convention whose asset/URL/setup is not yet finalised is emitted as a **visible `Designer/Developer To Do:` red-note placeholder** (red + bold — see `02_DATA_CONTENT_VERIFICATION.md` → Source-Specific Red-Note Prefixes; constraint 59). The pattern is built; the pending piece is flagged for the developer to complete during production. Nothing is buried in an HTML comment.
- **No new CSS/JS, no invented classes.** Every class and code block below was **supplied by the design team** in the global-parameter documents; this file documents them, it does not invent them (constraint 2).

### Scope key

| Tag | Meaning |
|---|---|
| **Cohort** | A named group of modules that spans **more than one `[PREFIX]`** (e.g. all six Languages prefixes; all Taonga modules; all H&PE content modules). Documented as a cohort because the a/b/c single-prefix vocabulary cannot express it. |
| **(a) Series + level** | One `[PREFIX]` at one level only. |
| **(b) Module-series** | One `[PREFIX]`, all levels. |

---

## 14.1 Languages Phase 1–4
**Scope — Cohort:** the six Languages prefixes (Chinese, French, Gagana Samoan, German, Japanese, Spanish) at **Phases 1–4**. Reference examples: `JAPFUN01_0_0`, `JAPFUN04_0_0`, `20260511_Language_HTML` (supplied — layout/asset examples only, not content to copy).

- **All Languages modules are combo.** Every page of every Languages-cohort module ships `template="combo"` on `<html>` — e.g. `<html lang="en" level="" template="combo" class="notranslate" translate="no">`, per the supplied `20260511_Language_HTML` reference ("Languages are all combo — should be reflected in the code"). The sub-type within combo (Fundamentals tiles / Inquiry crumbs / standalone) still comes from the `<body>` class per `06_TEMPLATE_RECOGNITION.md` §2, and `06` §5's Mode B template-level check expects `combo` — not a year-band value — for this cohort. Consequence: `combo` is **not** one of the three autoCheck auto-apply template files (constraint 38 / `03` COMP_00), so `autoCheck` is applied in Languages output only when the writer's intended behaviour calls for it.
- **Central images — `imageCentral` character/persona assets.** The recurring Languages characters and persona images are **centralised template assets**: they are served from the design team's central per-language asset folders and carry `class="img-fluid imageCentral"` (the class that applies the central-store filepath prefix). Canonical supplied form, from the updated `20260511_Language_HTML` reference ("updated to the central images"):
  ```html
  <img class="img-fluid imageCentral" loading="lazy" src="German assets/Salsi_certificate.jpg" alt="pretzel character holding certificate" />
  ```
  Central folders observed in the reference: `German assets/`, `Chinese assets/`, `Japanese assets/`, `Samoan character assets/`. (The French and Spanish characters still appear under module-local `images/…` in the reference — where a language's central folder or asset filename is not confirmed, emit the pattern with a visible `Designer/Developer To Do:` note rather than inventing a path.) **Writer-specified module images are unchanged** — they stay in `images/…` and **never** take `imageCentral` (`01_PIPELINE_EXTRACTION_TAGS.md` → Rules Common to Both Modes); the class is reserved for centralised template assets exactly like these.
- **Two-tile Fundamentals split.** A Fundamentals WT that carries **Novice** content and then **Emergent** content is separated into **two tiles**: a **Novice Tile** and an **Emergent Tile** (per the JAPFUN01 / JAPFUN04 set-up — currently one tile for Phase 4 and one for Phase 5). Each tile leads to that stream's content. Use the `phaseContainer` / `choicePage` tile pattern the reference files use; the sub-type width follows constraint 56 (`col-md-11 col-12` for the Fundamentals sub-type, `col-md-8` when paired with an `alertImage`).
- **Set characters in red brackets.** Languages define recurring characters written in red brackets (e.g. a named speaker/character tag). **Once a character has been introduced for the first time, that character is added every subsequent time its tag is used** — the tag is never left as bare bracket text (constraint 3) and the character is not dropped on later uses.
- **Videos are added manually by the developer.** The videos in the supplied `.html` examples are **template placeholders only** — do **not** reuse them. Real videos come from Audiovisual and are inserted by the designer/developer. Emit each video slot with a visible `Designer/Developer To Do:` note: *Audiovisual item to be added by designer/developer from Audiovisual.* A Creative-Services-produced (Audiovisual) video slot uses the pending-ID **Vimeo scaffold** of constraint 64 (`05` → Video Embed → Creative Services Videos).
- **Sticky nav on every page.** Add `<script src="js/stickyNav.js" type="text/javascript" class="stickyNav"></script>` to the `<head>` of **every** page. At the **top of the 0.0 content**, emit a visible `Designer/Developer To Do:` note: *set up the `stickyNav.js` file.*
- **Provisional asset state.** The character/asset set "will continue to be updated" — treat the supplied examples as current-but-not-final and prefer a built sibling where one exists.

---

## 14.2 Pathways
**Scope — (a) Series + level:** **Pathways Level 1** (development focus Terms 2–3). **Level 2 is HELD** — see the note at the end of this section.

- **Course navigation = "Sections", not "Fundamentals".** The course home reveals **Section** tiles, each opening to its modules. The three sections are: **1. Where am I going?**, **2. How do I get there?**, **3. What might the future hold?** (Te Reo translations pending — emit a `Designer/Developer To Do:` note where a Te Reo section title is required.)
- **Lesson structure.** Most Level 1 Pathways modules have **three lessons with sub-parts** (`1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 3.1, 3.2, 3.3`). Some modules have fewer sub-parts depending on content. Content is a mixture of refreshed, new, and merged material from the old Pathways course.
- **Persona tagging pattern.** Level 1 Pathways uses rangatahi **personas** that guide the learning, shown with a recognisable **circle image**. The tagging pattern is:
  - `[Persona box]`
  - `[Audioimage]` (with play button)
  - `[Photograph in a circle]` — the persona image
  - `[Audiovisual item N {name}]` — the audio recording (the persona transcripts are **real audio recordings, not AI**)
  - `[Transcript button]` — reveals the transcript
- **Persona details are DEFERRED.** The persona identities and images (Section 1: **Whai**; Section 2: **Leilani** and **Bailey**; Section 3: **Māia**) are still being finalised — the interactive and central images are under development as an EDR, and some images are TBC (e.g. Māia). **Emit the persona pattern with a `Designer/Developer To Do:` placeholder** (persona identity + circle image + audio to be confirmed once the EDR is finalised); use a placeholder image in the meantime.
- **Knowledge & Practice (Ks/Ps) statements.** There is **no new Pathways curriculum yet**, so the overview does **not** include new-curriculum K/P statements — the writers' template leaves a placeholder. In the meanwhile, only short **learning intentions and success criteria** are included. **Do NOT add curriculum K/P statements in-module**; this is a **revision request** once the curriculum is announced — emit a `Designer/Developer To Do:` note to that effect at the placeholder.
- **Overview is DEFERRED.** The Pathways overview is **to be set once the first module is complete** — emit the overview scaffold with a `Designer/Developer To Do:` note rather than a finalised overview.

> **Pathways Level 2 — HELD (no action this scope).** Level 2 is on pause. Six Level 2 "green" edit-proof modules exist for the refreshed template — **PWO2004, PWO2007, PWO2009, PWO2010, PWO2021, PWO2028** — with an edit-proof sheet set up. Developers revisit these next term when a Level 2 timeline is set and the edits are provided. Recorded here for reference only; no Level 2 conventions are active yet.

---

## 14.3 Taonga (The Arts)
**Scope — Cohort:** all **Taonga** modules (all phases). Taonga modules resemble FUNs but are **Taonga, not FUNs**, because they have **dropboxes attached**.

- **Intro page + clickable lesson images.** Set out like a FUN: an **introduction page**, then **images to click** that take the ākonga to specific lessons. **Lessons can be done in any order** (use the Maths 1-10 FUNS pattern as the model).
- **Side-navigation tabs inside each lesson.** Each lesson has **side-nav tabs** so ākonga work through it in any order, exactly like the Maths 1-10 FUNS.
- **Per-lesson layout (A–F).** Every lesson follows the same layout:
  - **A. Overview** — LI and SC plus a **vocab pull-out box**.
  - **B. Engage (I do)** — a short, simple stimulus to spark interest.
  - **C. Explore (We do)** — a simple online activity or interactive to practise learning.
  - **D. Create (You do)** — a hands-on activity away from the screen, **kaiako-assessed through a dropbox**.
  - **E. Extend (Optional)** — a simple challenge for learners ready to go further.
  - **F. Links to: (Optional)** — connects learning across the programme.
- **Unique overview.** Taonga modules use a **unique overview** (not the generic pattern).
- **Overview + images are DEFERRED.** The overview is **to be set once the first module is complete**, and images are still to come — **use placeholder images until updated links come through from the first module's Comparison Mode run.** Emit a `Designer/Developer To Do:` note at the overview and at each pending image.
- **Tui character (markup supplied — art DEFERRED).** A tui character (**Tui Toi**) features in each Taonga module and **varies from phase to phase**. The design team's ARTs global-template update (July 2026 — *"Update template to include tui chars"*) supplies the central-asset convention: folder `tui_characters/`, one image per phase — `tui_phase_1.jpg`, `tui_phase_2.jpg`, `tui_phase_3.jpg`, `tui_phase_4.jpg` — select the file whose phase number matches the module's phase. Supplied markup:
  ```html
  <img class="img-fluid imageCentral" loading="lazy" src="tui_characters/tui_phase_1.jpg" alt="Tui character" >
  ```
  The tui characters are **still under development** — emit the `<img>` scaffold above with a visible `Designer/Developer To Do:` note (*Tui character art still under development — confirm final asset at production*), never a silently swapped placeholder and never a hidden comment. Where the module's phase is not stated, raise a `Red Flag:` rather than guessing the `tui_phase_N` file.

---

## 14.4 ConnectED (CED) Phase 5
**Scope — (a) Series + level:** **CED Phase 5**. Reference: the CED Phase 5 global-parameters document (CEDT501 shown).

- **Overview = 3 tabs.** Overview, Information, Standards.
- **Intro-page dictionary box.** The intro page carries the standard dictionary alert. Supplied code:
  ```html
  <div class="alert">
    <h5>Want to use paper for this module?</h5>
    <p>Use the <b>floating navigation arrow</b> at any time to access printable versions of the activities and resources for this module.</p>
    <h4>Not sure about a word?</h4>
    <p>Use the <b>floating navigation arrow</b> at any time to access the Collins Dictionary or Te Aka Māori Dictionary.</p>
    <a href="https://www.collinsdictionary.com/" target="_blank"><div class="externalButton">Collins Dictionary</div></a>
    <a href="https://maoridictionary.co.nz/" target="_blank"><div class="externalButton">Te Aka Māori Dictionary</div></a>
  </div>
  ```
- **Sticky-nav dictionary links.** The sticky nav carries the two dictionary external links (supplied):
  ```js
  var links = [
    ['Collins Dictionary', 'https://www.collinsdictionary.com/', 'externalLink'],
    ['Te Aka Māori Dictionary', 'https://maoridictionary.co.nz/', 'externalLink'],
  ]
  ```
- **Wānanga / talanoa boxes.** Framed with a **culturally appropriate border**, standardised across the modules, using the **green** option from the colour palette. Cropped/cut from iStock imagery; **koru and Pasifika imagery must be clearly differentiated.** Supplied designer note — **all alerts are combined unless otherwise specified**:
  ```html
  <div class="alert cultural" layout="combined">
  ```
- **Flip cards.** Thin border so images are as large as possible; the **text on the flipped side is on a white background — not blue**. Supplied designer note: use **`.noBG`** on the `.flipCard`.
- **PDF resources are DEFERRED.** All PDFs are created as **separate lessons/resources** and are submitted as separate lessons, then linked in when ready. In the writers' templates these come out as **revision requests**. **For now: remove the PDF from the module and emit a visible `Designer/Developer To Do:` note listing the pending printable resources** (lesson name → intended resource), so the developer links them once delivered.
  > **Divergence from the source document — recorded decision.** The CED global-parameter document suggests holding these as **commented-out** printable-resource links in the sticky nav (`// ['Lesson 1: …', 192664], …`). That would place designer-facing information inside an HTML comment, which conflicts with the project's **"Comments Are Not a Communication Channel"** philosophy (constraint 5). Per the Update Mode decision that actioned this file (Fork C — bake deferred items in as visible red-note placeholders; **no new permitted-comment exception was granted**), the pending printable resources are rendered as a **visible `Designer/Developer To Do:` note** instead of commented-out links. If a commented-out-links approach is later preferred, it requires a **separate permitted-comment-exception sign-off** (it would join the Mode P / MTK / PAGEFORGE-marker exceptions in `02` → Comment & Red Flag Policy).

---

## 14.5 FUNdamentals (Health & PE, Y1–10)
**Scope — Cohort:** the H&PE **FUNdamentals** (16 FUNs coming). This **refines the existing Fundamentals sub-type** documented in `06_TEMPLATE_RECOGNITION.md` §3.3 — it does not replace it.

- **Tab-nav layout, 5–6 tabs down the RHS.** Each module uses the Fundamentals tab-nav layout with **5–6 tabs** on the right-hand side.
- **First tab = introduction; last tab = reflection.** In every instance the **first** tab is an introduction and the **last** tab is a reflection.
- **Each tab is a short "lesson."**
- **Inline interactives + one engagement quiz.** Each module has inline interactives and **one quiz to trigger engagement, placed in the reflection tab**.

> Sub-type **recognition** (body class `fundamentals container-fluid`, `div.phases` → `div.fundamentalsPanel` navigation, `footer-nav fundamentals-nav`) stays in `06` §3.3. This section adds the H&PE FUNdamentals **content conventions** on top of that recognised structure.

---

