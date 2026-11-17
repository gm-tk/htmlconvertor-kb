> **Last updated:** Tuesday, 17th November, 2026 7:37 PM
> **Granular part A2 (2 of 9) of `14_SUBJECT_GLOBAL_PARAMETERS.md`** — Families 14.4 (ConnectED (CED) Phase 5) and 14.5 (FUNdamentals H&PE). Split from `14A` on 17 November 2026 when it passed the 30 KB soft limit (`CLAUDE.md` §4); content moved verbatim.
> All sibling parts live in `14_SUBJECT_GLOBAL_PARAMETERS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
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

  > **Carve-out — the eight AI Guidelines PDFs are DELIVERED and are never deferred.** `[AI Use Guidelines Traffic Light PDF]`, the three `[Ākonga AI Use Guide Years …]` tags and the four `[Kaimahi …]` tags resolve against real files in `AI-guidelines/` and always build their `embedPDF` / `centralFile` block, in CED as anywhere else. Do not strip them and do not raise a `Designer/Developer To Do:` note for them. See `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` → AI Guidelines PDFs; constraint 84.
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

