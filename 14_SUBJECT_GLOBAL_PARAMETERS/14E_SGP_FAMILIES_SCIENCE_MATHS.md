> **Last updated:** Wednesday, 28th October, 2026 1:05 PM
> **Granular part E (6 of 6) of `14_SUBJECT_GLOBAL_PARAMETERS.md`** — Families 14.13 (Science), 14.14 (Maths) and 14.15 (the MXEX series): the centralised character images, the Maths conventions, the MXEX layouts. Opened 27 October 2026 (CL-0117) as a new part rather than growing `14D`.
> All sibling parts live in `14_SUBJECT_GLOBAL_PARAMETERS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## 14.13 Science — the four characters + the comic scenes
**Scope — Cohort:** all **Science** modules. *(The module-code prefix was not stated in the source; identify these modules by subject until a prefix is recorded here. Do not guess one.)* Source: Meredith Lees → Gavin McGruddy, *"New template items"*, 23 October 2026 — `Global Edits Science.docx`, the template's Centralised Images page (`refresh_imageCentral.html` → *Science Characters*) and the server folder `imageCentral\Science Characters`. Actioned through the authorised channel 27 October 2026 (CL-0117; constraint 95).

- **Four characters — Aroha, Lani, Max, Quinn.** Each has **three full-body poses, numbered 1–3**, and **two head shots, numbered 4–5**. **Quinn is the exception with FOUR head shots:** 4–5 with her safety goggles **on**, 6–7 with them **on her head**. Every image is a `.jpg`.
- **Folder and filename — copy verbatim.** `Science Characters/<Name>-<n>.jpg` — the folder **capitalised with a space, exactly as it is on the server** (`imageCentral\Science Characters`), the name capitalised, a hyphen, the pose number: `Science Characters/Aroha-1.jpg`, `Science Characters/Quinn-6.jpg`. *(The template's Centralised Images page writes the folder lower-case, `Science Characters/`; Chris ruled on 27 October 2026 — CL-0119 — that the server's spelling is the one to emit, since that is the folder that exists. A `draft/` sub-folder exists on the server and is never referenced.)*
- **Supplied markup** (the Global Edits document's form — the `alt` is the character's name; the template page leaves it empty, use the name):
  ```html
  <img class="img-fluid imageCentral" loading="lazy" src="Science Characters/Quinn-1.jpg" alt="Quinn" >
  ```
- **Writer tag.** `[Centralised image: Quinn 4]`, `[Image centralised Quinn 4]`, `[Central image: Quinn]` — the centralised-image tag in any of its forms (`01` → Tag Taxonomy) plus the character's name and, optionally, the pose number. **No number → pose 1** (the full-body image the Global Edits document shows first). A name or number that does not exist in the set (`Aroha-6`, `Max-7`) is a `Red Flag:` naming the request, never a guessed file. The characters appear in `[Speech bubble]`s like every other character set — mechanics stay in `04_COMP_SEGMENTS_OVERLAYS.md` → COMP_09 (its `imageCentral` rule already covers central characters).
- **Comic scenes — designer-made, always `.png`.** `Science Characters/comic scenes/clubhouse_1.png` (*Clubhouse*) and `Science Characters/comic scenes/kowhai_reserve_1.png` (*Kōwhai Reserve*). Writer tag `[Centralised image: clubhouse]` / `[Centralised image: kowhai reserve]`. **A scene not in this list must be created by a designer** — emit a visible `Designer/Developer To Do:` naming the scene the writer asked for; never compose one from the character images.
  ```html
  <img class="img-fluid imageCentral" loading="lazy" src="Science Characters/comic scenes/clubhouse_1.png" alt="Clubhouse" >
  ```

---

## 14.14 Maths — the five characters
**Scope — Cohort:** all **Maths** modules. *(Identify by subject; no prefix list is asserted here.)* Source: as §14.13 — `Global Edits Maths.docx`, the template page's *Maths characters* panel, server folder `imageCentral\Maths Characters`. Actioned 27 October 2026 (CL-0117; constraint 95).

- **Five characters — Ada, Omar, Hypi, Erni, Lara** — hand-drawn, "all based on real-life figures". One portrait each on the template page.
- **Folder and filename — copy verbatim.** `Maths Characters/maths_characters_<name>.jpg` — the folder **capitalised with a space**, the filename **lower-case with underscores**: `Maths Characters/maths_characters_ada.jpg`, `…_omar.jpg`, `…_hypi.jpg`, `…_erni.jpg`, `…_lara.jpg`.
  > **⚠️ The Global Edits Maths document is OLDER than the template page and its snippets are superseded.** It writes `maths characters_ada.jpg` (a space), names a `Maths Characters_DRAFT_<Name>.jpg` set (now in the server's `archive/` folder) and labels the fifth character *Archi*; the template page's five files above are current, and the fifth character is **Erni**. The `archive/` and `do not use/` folders are never referenced. The document also says the characters are drafts carrying a watermark until finalised — the current files are the ones to emit regardless; no `Designer/Developer To Do:` is raised for the watermark.
- **Supplied markup:**
  ```html
  <img class="img-fluid imageCentral" loading="lazy" src="Maths Characters/maths_characters_ada.jpg" alt="Ada" >
  ```
- **Writer tag.** `[Image centralised Hypi]` (the Global Edits document's own form), `[Centralised image: Hypi]`, `[Central image: Hypi]`. **Numbered poses exist on the server for two characters** — `Maths Characters/ada/maths_characters_ada_1.jpg` … `_3.jpg` and `Maths Characters/omar/maths_characters_omar_1.jpg` … `_16.jpg` — and are used **only when the writer names the pose number** (`[Centralised image: Omar 7]` → `Maths Characters/omar/maths_characters_omar_7.jpg`); an un-numbered tag always builds the portrait above. A pose that does not exist (`Hypi 2`, `Ada 4`) is a `Red Flag:`, never a guessed file.
- **The Global Edits Maths document is the Maths master (Chris, 27 October 2026 — CL-0121).** It is the design team's up-to-date record of every Maths module convention, so its other items are folded in here as the Maths family's rules (the same shape as the HPE Global Edits of §14.8; where the two documents supply the same copy, the copy is the same):
  - **Overview page = a three-part module menu.** `[Overview]` builds the module menu as **three tabs**: **Tab 1 — Information** (the module's Learning intentions and Success criteria); **Tab 2 — Maths No Problem** (`[Tab 2] Maths No Problem:` → `[Body] This module links to this learning in Maths No Problem:` then the writer's book reference — e.g. *Year 5 > Book B > Chapter 10 - Length, Mass & Volume* — then `Lessons:` and the writer's list of MNP lessons — *Bridging lesson 1 - Volume of solids* … — then *Talk to your kaiako if you have any questions.*); **Tab 3 — Overview: Curriculum Knowledge and Practices content**. Tab labels come from the writer's `[Tab N]` lines; the MNP book, chapter and lesson lines are module-specific and copied verbatim (constraint 1). Menu mechanics stay in `01_PIPELINE_EXTRACTION_TAGS.md` → Module Menu Structures; this bullet records the Maths shape and labels.
  - **Content-page overview / lesson introduction.** Each lesson's `[Overview]` carries **lesson-specific** Learning intentions and Success criteria (agreed). The document's *"Do we want an intro alert/character"* is still an open question (its highlight marks it as undecided): **where the writer supplies an `[Alert]` / speech-bubble introduction, build it** (the supplied example — *We are going to learn about shapes, focusing on both 2D and 3D shapes. In this lesson, you will explore …*); **never invent one**, and raise no To Do when it is absent.
  - **Lesson Summary alert.** `[Alert]` → `[H3] Lesson summary` → `[Body] Ka pai!` → `[body] You…` (the writer's summary) → `[Hint button] Need help?` → `[body] Email or phone your kaiako. You can ring 0800 65 99 88 and ask for them, or email your kaiako. If you do not know the name of your kaiako click on the word My Te Kura at the top left of your screen. Your kaiako can be seen at the right of this page. It may take a minute to upload.` → `[End summary]`. An alert box holding the heading and body, with the hint button revealing the kaiako-contact paragraph (`04_COMP_SEGMENTS_OVERLAYS.md` → Hint). The kaiako paragraph is the design team's fixed wording — copy it exactly.
  - **Floating / sticky nav** is listed in the document with no detail yet — nothing is recorded; follow a built Maths sibling.
  - **Math writing.** `[Math] **4/5**` — a fraction must look like a fraction; writers tag `[Math]` and bold the symbols; **Creative Services use MathML for all numbers and equations in Maths** — already the universal rule (CL-0115; `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` → Equations).
  - **Dropboxes — up to 3, suggest 2.** Up to three dropboxes are allowed; **two is suggested — one Checkpoint midway and one end-of-module.** Additional activities can be linked to the **checkpoint** dropbox so kaiako know the ākonga is still working through the module.
  - **Checkpoint (midway).** `[ActivityDropbox] [H3] Checkpoint [Body] …` — midway through the module, for ākonga to upload their learning journal. Suggested wording by phase (the design team's; a writer's own wording wins where it is supplied):
    - **Phase 1:** *It's time to show your kaiako what you've been working on! Upload your work to the dropbox so they can see how you're going. They will tell you what you're doing well and give you some ideas to help you with your next steps. If you have any questions or want to say something about your learning, you can write a message in the comment box.*
    - **Phase 2:** *Please upload the work you've done so far to the dropbox. This helps your kaiako see how you're going in this module. They'll give you feedback on what you're doing well and share some next steps to help you keep improving. If you have any questions or thoughts about your learning, you can message your kaiako in the comment box.*
    - **Phase 3:** *Upload your work so far to the dropbox so your kaiako can check in on your progress. They'll let you know what's going well and give you helpful tips for your next steps. If you have any questions or want to share how you're finding the learning, feel free to message your kaiako in the comment box.*
    - **Phase 4:** *It's time to upload the work you've done so far to the dropbox. Your kaiako will let you know what you're doing well and give you helpful tips on what to work on next. If you've got any questions or want to share how you're finding things, just pop a message to your kaiako in the comment box.*
  - **End-of-module dropbox (final submission of learning).** `[H3] Share Your Learning [Body] …` — suggested wording by phase:
    - **Phase 1:** *You've finished the whole module, ka rawe! Now it's time to share your final work. Upload your learning journal to the dropbox so your kaiako can see all the great learning you've done. If you want to tell your kaiako something about your work, you can say it in the comment box.*
    - **Phase 2:** *You've reached the end of the module, ka pai! Upload your learning journal to the dropbox so your kaiako can see everything you've learned and created. If you'd like to explain your thinking, ask a question, or share what you're most proud of, add a message in the comment box.*
    - **Phase 3:** *Mīharo, you've completed the module! Upload your learning journal to the dropbox so your kaiako can review your full learning journey and see how your ideas have developed. If you want to reflect, explain your choices, or share insights about your learning, you can write in the comment box.*
    - **Phase 4:** *You've reached the end of the module, tau kē! Upload your learning journal to the dropbox so your kaiako can see your full understanding and the thinking behind your completed task. If you'd like to reflect on your learning, discuss your process, or ask questions, feel free to write in the comment box.*
  - **Where the dropbox copy is missing.** A Maths `[ActivityDropbox]` checkpoint or end-of-module box whose writer supplied **no body copy** takes the phase's suggested wording above (the design team's standard for the family), and the run notes that it did so in the Designer Summary; where the writer wrote their own copy it is kept verbatim (constraint 1).
  - **Image library — consistency.** The design team is building a document of consistent Maths images (shapes, arrows …); until the Educational Design Review is complete, image-consistency guidance comes from Eliza. Creative Services rules recorded verbatim: *use object `.svg`s where possible to ensure text is highlightable (or manually place the text on top of the image); use templated colours where possible; ensure text on an image passes WCAG.* (The document writes "WAAG"; the standard meant is WCAG.) These govern developer-made images — the Convertor emits the writer's image references as usual.
  - **Marking guide** (*identify progress marker*, *LOTs*) and **Characters across the curriculum** (`Characters.pptx`) are listed with no convention yet — nothing recorded.

## 14.15 MXEX — Maths modules of the MXEX series (right-hand alerts, click drops; the character row)
**Scope — (b) Module-series:** every **`MXEX`** module, all year levels. Source: MXEX105 finalized difference report, Differences 1, 2 and 5 (CL-0123, CL-0124, CL-0125 — the GitHub session's rows, renumbered by the ledger merge CL-0140).

- **Central Maths characters — `[Image Centralised {Name}]` (CL-0123, read with §14.14).** The Maths characters are design-team **central-store assets**, not writer images, so an MXEX writer tag `[Image Centralised Archi]` (any character name) takes `class="img-fluid imageCentral"` with `alt` = the character's name. **The path is §14.14's** (CL-0117 / CL-0121): `Maths Characters/maths_characters_<name>.jpg`. MXEX105's finished module shipped the pre-delivery names `Maths Characters/Maths Characters_DRAFT_{Name}.jpg`; that form is recorded here as what that module carries, not as the path to emit. Never derive a variant filename from a writer's costume or pose request.
- **The character and its speech bubble share ONE row (CL-0123), on the universal side rule (CL-0122).** The whole `speechBubble` row sits inside a `col-md-8 col-12` content column; the bubble column comes first — `col-md-9 col-10 paddingR` holding `bubble-left no-hover` — and the character column second — `col-md-3 col-4 paddingL`. MXEX105's finished module has the picture on the left (`paddingR` image column, `bubble-right`); it predates CL-0122 and is not the form to copy:
  ```html
  <div class="col-md-8 col-12">
      <div class="row speechBubble" layout="speech">
          <div class="col-md-9 col-10 paddingR">
              <div class="bubble-left no-hover">
                  <p>“Beep! Boop! Calling all robot inventors!”</p>
              </div>
          </div>
          <div class="col-md-3 col-4 paddingL">
              <img class="img-fluid imageCentral" loading="lazy" src="Maths Characters/maths_characters_archi.jpg" alt="Archi">
          </div>
      </div>
  </div>
  ```
  This MXEX column pairing (`col-md-9 col-10` / `col-md-3 col-4`, a plain `bubble-left no-hover`) replaces the generic `bubble-basic` form of constraint 29 for MXEX central characters; the side and the inner-side padding (image right → `paddingL`) follow CL-0122 / constraint 29.
- **`[RHS alert]` beside body content → `alert top` (CL-0124).** In MXEX modules a writer's right-hand-side alert sitting beside body content renders as `<div class="alert top">` inside its sidebar column — **not** `alertActivity`. Column classes follow `05` → Columns (sidebar column at `col-md-4`, padding per CL-0135). Content inside follows the alert's normal rules:
  ```html
  <div class="alert top">
      <p>Did you see some 3D shapes that you have seen before? …</p>
  </div>
  ```
- **A click drop sits inside ONE content column (CL-0125).** The whole block — the trigger row **and** every `clickDropContent` panel — sits inside a single `col-md-8 col-12` content column, never loose at page level. The grouping rule is unchanged: all triggers first in their own row, then all panels. The panels are outside the **trigger row** but inside the **same content column**. A speech bubble revealed in a panel fills that column: `col-md-12 col-12` with `bubble-basic no-hover bubble-bottom`.
  ```html
  <div class="row">
      <div class="col-md-8 col-12">
          <div class="row">
              <!-- trigger columns: every clickDrop trigger -->
          </div>
          <div class="clickDropContent">
              <div class="row speechBubble" layout="speech">
                  <div class="col-md-12 col-12">
                      <div class="bubble-basic no-hover bubble-bottom">
                          <p>I have one curved side and no corners. I am round. I am a circle.</p>
                      </div>
                  </div>
              </div>
          </div>
          <!-- further clickDropContent panels -->
      </div>
  </div>
  ```
