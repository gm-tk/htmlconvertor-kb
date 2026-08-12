> **Last updated:** Thursday, 13th August, 2026
> **Granular part B (2 of 4) of `14_SUBJECT_GLOBAL_PARAMETERS.md`** — Families 14.6-14.10 (LS, BLL, HPE, BLLR, MiW/WJ). Cross-cutting notes (14.11) and Technology (14.12) live in `14D`.
> All sibling parts live in `14_SUBJECT_GLOBAL_PARAMETERS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## 14.6 LS — Learning Support
**Scope — (b) Module-series:** **LS** modules (including the **XLP** Learning Partner Toolkits and **XDLS** exemplars). Reference exemplar: `XDLS501`.

- **`.learningSupport` on `<html>`.** Add the `learningSupport` class to the root tag, e.g. `<html lang="en" level="" template="NCEA" class="notranslate learningSupport" translate="no">`. (This is the existing CSS hook already noted in `06` §3.3 / the sub-type detection tree — LS modules always carry it.)
- **Larger font.** The module font is **bigger — the same font as the LS Whakatau.**
- **Terminology + brackets.** Correct spelling **hoa ako (learning partner)**; **hua ako** → check → **hoa ako**; learner → **ākonga**; WE/US → **you**. **Brackets are used only on the first instance** a term is used in a module (first mention `hoa ako (learning partner)`, plain `hoa ako` thereafter).
- **Remove tab navs.** LS modules are **lesson-based, not inquiry-based** — remove tab navs (they carry too much media). **Prompts to move on go at the bottom of each page.**
- **clickDrop activity layout (supplied).** LS activities use the choicePage clickDrop pattern with per-choice icons; the `choicePage` **wrapper** sits below in `col-md-8 col-12` (constraint 56 — activity wrappers off `col-md-10`). Note this is the OUTER wrapper width: an activity's *inner* column is `col-12` (constraint 63). Representative supplied structure:
  ```html
  <div class="row">
    <div class="col-md-8 col-12 choicePage choiceHeightMatch">
      <div class="choice clickDrop dropBox col-md-4 col-6">
        <div class="choiceImg hoverSwitch">
          <img alt="" src="../Images/Learning support/Activity clickdrops/Learn by heart.jpg">
          <div class="iconCentral iconD" iconType="learnByHeart"></div>
        </div>
        <div class="choiceText"><h5>Learn by heart</h5></div>
      </div>
      <!-- … further choices: explain, do / compare, judge, create … -->
    </div>
  </div>
  ```
  Observed `iconType` values: `learnByHeart`, `explain`, `do`, `compare`, `judge`, `create`. The full multi-activity sequence (1A–1G) is in the supplied `ls-modules-global-edit.docx` — follow it as the pattern for a 6-activity LS lesson.
- **Action prompts = colour-coded speech-bubble character.** In-page action prompts are **not activity boxes** — use a **man-with-speech-bubble**, **colour-coded to the module**, with a **bold heading** (clear about what they are looking at) and **bullet-point prompting questions**.
- **Prompting questions in speech bubbles.** General prompting questions are placed in **speech bubbles** (`04_COMP_SEGMENTS_OVERLAYS.md`).
- **Too many videos/images → slideshow.** When a page has many videos/images, put them in a **video/image slideshow** with the body text as captions, and add prompting text (e.g. *explore the slideshow to see examples of…*).
- **6-activity pattern.** For the 6-activity lesson:
  - **No activity numbers on the clickDrop images**; the pop-out **number is not on the image itself**.
  - **Remove all dropboxes from the activity boxes** — there is **one dropbox at the bottom of the page**.
  - Intro copy: *Below are activities. You can choose the activities you feel will enhance your learning, your knowledge, your wellbeing. When you have completed your chosen activities, you will be able to upload photos, videos or voice recordings to show your kaiako. Click on each image to view the activities.*
  - **Explicit titles:** *Learn about… / Explain why… / Practise… / Compare … versus … / Do you think…? / Create …*
  - Each activity has: text explaining what to do; media (video or image); an invitation to share with kaiako.
  - **Compare** activities: add a Venn-diagram prompt (*You may like to use a Venn diagram to compare*) and a **"What is a Venn diagram?" button** (video `https://www.youtube.com/watch?v=lnalI7eVQsQ&t=16s`), with follow-up text *Here is an example of what your Venn diagram might look like.*
- **Dropbox copy.** Title **Share your learning!**; body: *When you have completed your chosen activities, upload your photos, videos or voice recordings to show your kaiako. If you require a specific media uploaded to the dropbox use the corresponding icon. When there is more than one type of media students can upload, use the generic dropbox button.* Button label: **Upload to Dropbox** (see §14.11).
- **End-of-page "Invitation to move forward" alerts (supplied copy).**
  - **Exploratory:** *Ka pai! You've completed this lesson about \_\_\_\_\_ where we started to explore \_\_learning intention\_\_. Choose which lesson you would like to explore next! Click on the back button below to return to the introduction page and choose your next activity.*
  - **Lesson-by-lesson:** *Ka pai! You've completed lesson \_, where we started to explore \_\_learning intention\_\_. Now let's try lesson \_.*
  - **End of module:** *Ka pai! You have completed this module. We hope you enjoyed your learning. Discuss with your kaiako what topic you might like to explore next!*
- **XLP overviews are unique.** XLP modules are the **Learning Partner Toolkits (for supervisors)**, so they **don't need the full ākonga-facing overview** — XLP modules get a **unique overview**.
- **Standard LS overview (non-XLP).** Overview tab: **UKD, LI and SC**. Information tab: **Planning your time** and **What do I need to get started**. Standards tab: **Assessment for learning** and the standards to be achieved. Whakataukī in **Te Reo and English**. First line: *This module is called …* with an **audio hover trigger over the Te Reo word**. Second body text: purpose of the module. Media: video or photo. Then the move-forward prompt (text prompt if ordered lesson-by-lesson; if exploratory, *Below are options you can select from. You can choose to start anywhere.* then buttons to pages, with the smaller words ("Move", "Eat", etc.) removed).

---

## 14.7 BLL — Blended Literacy
**Scope — (b) Module-series:** **BLL** modules.

- **Template level — split by sub-series (CL-0035, 14 July 2026).** **BLL2xx modules — any code beginning with the literal prefix `BLL2` (BLL253, BLL261, BLL262, BLL263, BLL266, …) — are phase 1 → `template="1-3"`**, a standing designer-directed exception that supersedes the 13 July BLL262-report value of `"4-6"` (CL-0031, now `Reverted`). **All other BLL codes default to Years 4–6 → `template="4-6"`.** **Contrast: BLLR2xx modules are phase 2 → `template="4-6"`** — a `BLLR…` code never matches the `BLL2` prefix (fourth character `R`, not `2`), so the phase-1 exception never applies to BLLR (§14.9). Derive the value from this code→phase mapping; **never mirror `template=` from sibling files** (constraint 21), even where the sibling's value happens to coincide. Full rule: `06_TEMPLATE_RECOGNITION.md` §5 (Detection → Template level).
- **Sassoon "writing font."** Any interactive or text the ākonga must read or interact with uses a **writing font** — use **`refresh_sassoon_font.html`**. Ensure specifically: **`a`** is a single-storey a, **`I`** (capital i) reads as a capital I, **`g`** is a single-storey g. (These ākonga are just learning to read and write, so the letters they read must match the letters they write — `l` and `I` are confusing when identical.)
- **Page-1 animated-person intro.** The **1st page** of each module has an **animated person** introducing what is in the module; the "person" is **different for each set**. Emit the video scaffold with a visible `Designer/Developer To Do:` note (supplied):
  ```html
  <p style="color: red; font-weight: bold;">Designer/Developer To Do: Audiovisual item to be added by designer/developer</p>
  <div class="videoSection ratio ratio-16x9">
    <iframe src="" loading="lazy" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
  </div>
  ```
- **Elkonin boxes for blending.** All "decoding words" activities where sounds are blended go in **elkonin boxes**, with **dots under each sound and an arrow under the dots**; the **vowel is in red**. The image is developer-produced — emit with a visible `Designer/Developer To Do:` note (supplied):
  ```html
  <p style="color: red; font-weight: bold;">Designer/Developer To Do: Designer/developer to create and embed image</p>
  <img class="img-fluid" src="images/.jpg" alt="Blend the sounds diagram">
  ```
- **All activity boxes green** — including dropbox boxes.
- **`.dropbox` is NOT added to `.activity` (BLL exception to constraint 43).** When a dropbox is added to a BLL activity, **do not** append the `dropbox` modifier to the `.activity` class. This is a **BLL-only carve-out** from the universal rule in constraint 43 / `05` → Activities (which otherwise adds `dropbox` to the activity wrapper for every series). The dropbox button itself is still present; only the wrapper modifier is omitted.
- **Button label: "Upload to Dropbox"** (see §14.11).
- **Embedded stories = book-style carousel.** All embedded stories carry **just the story — not the teacher notes or activities — in a carousel** so they read **like a book** (not scrolling down). Supplied pattern (image URLs replaced per story):
  ```html
  <div class="row carousel">
    <div class="col-md-12 col-12 viewer">
      <div class="item"><img class="img-fluid" src="images/SPELDSA_Set_2_Rick-DS_1_Page_1.jpg" alt="Rick cover"></div>
      <div class="item"><img class="img-fluid" src="images/SPELDSA_Set_2_Rick-DS_1_Page_2.jpg" alt="Rick"></div>
      <!-- … one .item per page … -->
    </div>
  </div>
  ```
- **Embedded timer — minutes and seconds only** (no hours). Supplied:
  ```html
  <div class="stopWatch noMilliSeconds noHours"></div>
  ```

---

## 14.8 HPE — Health & PE content lessons
**Scope — Cohort:** all **Health & PE content** modules (content lessons; distinct from the H&PE FUNdamentals of §14.5).

- **Content-page overview = intro page.** Keep the overview the same as the intro page: `[Overview] [Alert]/[Image] [Speech bubble] [Body]` — *In this lesson you are learning…*
- **Lesson summary alert.** `[alert]/[Speech bubble]` → `[H3] Lesson Summary` → `[body] Ka pai! You have been learning about…` → `[checkbox]` → `[Hint Button] [title] Need help?` → `[body] Email or phone the kaiako. You can ring 0800 65 99 88 and ask for them or email them. If you do not know the name of your kaiako click on the words My Te Kura at the top left of your screen. The kaiako can be seen at the right of this page. They may take a minute to upload.` → `[end alert]`.
- **Sticky / floating nav — Fundamentals + Help page only.** Add `<script src="js/stickyNav.js" type="text/javascript" class="stickyNav"></script>` to the `<head>`, with the sticky nav offering **Fundamentals and the Help page**. At the top of the 0.0 content emit a visible `Designer/Developer To Do:` note: *set up the `stickyNav.js` file.*
- **Dropboxes — up to 3, suggest 2.** Up to three dropboxes are allowed; **two is suggested — one Checkpoint and one end-of-module.** Additional activities can be linked to the **checkpoint** dropbox so kaiako know the ākonga is still working through the module.
- **Quiz rules.** `[MTKquiz]` **does not trigger engagement.** `[Multichoice]` is **autograded**; `[Written Response]` is **teacher-marked** (*What do you think about…?*) and lets learners insert images and add attachments. **Max one quiz per every 2–3 lessons.** **Output shape (universal — constraint 65):** an `[MTKquiz]` activity ends in a blank-href **"Go to quiz"** button plus a visible `Designer/Developer To Do:` note (create the quiz in MTK) — never a dropbox button; see `05` → Buttons → MTK Quiz Button.
- **Checkpoint (midway).** `[ActivityDropbox] [H3] [Body]` — midway through the module, for ākonga to upload their learning journal. Phase-specific wording (supplied):
  - **Phase 1 — Checkpoint:** *It's time to show your kaiako what you've been working on! Upload your work to the dropbox so they can see how you're going. They will tell you what you're doing well and give you some ideas to help you with your next steps. If you have any questions or want to say something about your learning, you can write a message in the comment box.*
  - **Phase 2 — Checkpoint:** *Please upload the work you've done so far to the dropbox. This helps your kaiako see how you're going in this module. They'll give you feedback on what you're doing well and share some next steps to help you keep improving. If you have any questions or thoughts about your learning, you can message your kaiako in the comment box.*
  - **Phase 3 — Checkpoint:** *Upload your work so far to the dropbox so your kaiako can check in on your progress. They'll let you know what's going well and give you helpful tips for your next steps. If you have any questions or want to share how you're finding the learning, feel free to message your kaiako in the comment box.*
  - **Phase 4 — Checkpoint:** *It's time to upload the work you've done so far to the dropbox. Your kaiako will let you know what you're doing well and give you helpful tips on what to work on next. If you've got any questions or want to share how you're finding things, just pop a message to your kaiako in the comment box.*
- **End-of-module celebration page.** An **automated celebration** graphic, a congratulation statement, and an SC checklist: `[automated celebration] [H2] Congratulations! [body] Ka pai, you have completed this module about… [dropbox] [H3] Share your learning [body] [button] Go to your journal [button] Upload to dropbox [alert]/[Image] [Speech bubble] [body] If you enjoyed this learning, you may like to explore: … Talk to your kaiako about these and other learning opportunities.`
  - The celebration **.gif has been DELIVERED** (August 2026 — see §14.12, where the same central asset is recorded for Technology). The former "still under development" deferral and its `Designer/Developer To Do:` note are **retired**; emit it as a real asset reference:
    ```html
    <img class="img-fluid imageCentral" loading="lazy" src="congradulations/Congradulations animation.gif" alt="Congradulations animation">
    ```
    > **The misspelling in the path is deliberate — never correct it.** *Congradulations* is misspelt in the delivered folder name, filename and `alt`; modules carrying it are live, the string is never learner-visible, and the design decision is to leave it (§14.12).
  - **Layout note — HPE celebration pages only.** On an **HPE** celebration page the .gif is **1×1 and too large to sit in a `col-8`** — **redesign the layout around the related content** so the graphic fits (do not force it into a `col-8`). **This is HPE's own page composition, not a property of the asset:** §14.12 records a different suggested layout for **Technology** (`col-8` text beside `col-4` gif) using the same shared file. Follow the layout of the family you are converting; neither overrides the other.
  - End-of-module **"Share Your Learning"** phase-specific copy (supplied):
    - **Phase 1:** *You've finished the whole module, ka rawe! Now it's time to share your final work. Upload your learning journal to the dropbox so your kaiako can see all the great learning you've done. If you want to tell your kaiako something about your work, you can say it in the comment box.*
    - **Phase 2:** *You've reached the end of the module, ka pai! Upload your learning journal to the dropbox so your kaiako can see everything you've learned and created. If you'd like to explain your thinking, ask a question, or share what you're most proud of, add a message in the comment box.*
    - **Phase 3:** *Mīharo, you've completed the module! Upload your learning journal to the dropbox so your kaiako can review your full learning journey and see how your ideas have developed. If you want to reflect, explain your choices, or share insights about your learning, you can write in the comment box.*
    - **Phase 4:** *You've reached the end of the module, tau kē! Upload your learning journal to the dropbox so your kaiako can see your full understanding and the thinking behind your completed task. If you'd like to reflect on your learning, discuss your process, or ask questions, feel free to write in the comment box.*
- **"Working toward" dropbox.** A working-toward dropbox uses the **same link as the checkpoint dropbox** unless otherwise stated.
- **Characters (CL-0067).** Characters appear in a `[Speech bubble]` with an `[imageCentral]` image. Character set: **Sura, Afi, Alex, Kai, Leila.**
  - **Folder + filename conventions.** Full-body (pose 1): `health & PE characters/phase #/HP_{Name}_1_phase_#.png`. Head-only (pose 3): `health & PE characters/phase #/head_only/HP_{Name}_3_phase_#.png`. **The folder's phase number and the filename's phase number always match.** All character images carry `class="img-fluid imageCentral"` and `alt=""`. (This corrects the previous `health and PE characters/` folder spelling — the ampersand form is canonical.)
  - **Availability.** **Sura**, **Alex**, and **Kai** — **Kai and Alex are in use** (observed throughout the designer-refined HPRE301 files, 29 July 2026). If a required character is **not yet available**, emit a visible `Designer/Developer To Do:` note in its place. **Developers do not sign off 2nd proof until the missing characters have been created and added.** (Writers have offered to help CS generate characters via a supplied PowerPoint asset.)
  - **Two-character lesson-intro/outro strip (canonical HPE pattern).** Bubble order follows speaker order (the `secondary-light bubble-left` bubble may come first). This full-body strip DOES follow the universal padding rule (left image `paddingR`, right image `paddingL` — CL-0055 / constraint 29):
    ```html
    <div class="row speechBubble" layout="speech">
        <div class="col-md-3 col-12 paddingR">
            <img class="img-fluid imageCentral" alt=""
                 src="health & PE characters/phase 3/HP_Kai_1_phase_3.png" />
        </div>
        <div class="col-md-6 col-6 align-self-center">
            <div class="bubble-basic primary-light no-hover bubble-right"><p>…</p></div>
            <div class="bubble-basic secondary-light no-hover bubble-left"><p>…</p></div>
        </div>
        <div class="col-md-3 col-12 paddingL">
            <img class="img-fluid imageCentral" alt=""
                 src="health & PE characters/phase 3/HP_Alex_1_phase_3.png" />
        </div>
    </div>
    ```
  - **Head-only dialogue strips** (alternating conversation, one bubble per row; image column at `col-md-2 col-12`, bubble column at `col-md-10 col-12 align-self-center`; single closing-bubble variant at `col-md-3` + `col-md-9`):
    ```html
    <div class="row speechBubble" layout="speech">
        <div class="col-md-2 col-12 paddingR">
            <img class="img-fluid imageCentral" alt=""
                 src="health & PE characters/phase 3/head_only/HP_Alex_3_phase_3.png" />
        </div>
        <div class="col-md-10 col-12 align-self-center">
            <div class="bubble-basic primary-light no-hover bubble-right"><p>…</p></div>
        </div>
    </div>
    ```
    Speaker-on-right rows reverse the column order, and the image column **STILL takes `paddingR`** — a **deliberate HPE exception** to CL-0055's universal right-positioned → `paddingL` rule, **scoped to HPE head-only dialogue strips only**.
  - **Bubble colour classes in use:** `primary-light` and `secondary-light` — existing template classes observed in the designer's files (also recorded in `04_COMP_SEGMENTS_OVERLAYS.md` → COMP_09 → Colour Modifier Classes as observed values; nothing is invented beyond these).
  - **Speaker comments are NOT codified.** The `<!-- Alex -->` / `<!-- Kai -->` speaker comments seen in the designer's files are production annotations — the comments policy is unchanged and the Convertor never emits them.
- **Button label: "Upload to Dropbox"** (see §14.11).

---

## 14.9 BLLR — Blended Literacy (Reading)
**Scope — (b) Module-series:** **BLLR** modules. Source: Persephone Samuels → Gavin McGruddy, *"BLLR Global Parameters"*, 9 July 2026.

> **BLLR is a distinct prefix from BLL.** The BLL conventions of §14.7 (Sassoon font, elkonin boxes, `.dropbox` carve-out, etc.) are scoped to the **BLL** series and do **not** automatically bind BLLR. Where a BLLR module needs a BLL convention, it must be recorded here explicitly or raised as a `Red Flag:`.

> **Parameters incomplete.** The source email states *"Most of the parameters still to come."* Treat this section as **current-but-partial**: prefer a built BLLR sibling (Mode B) where one exists, and raise a `Red Flag:` for any BLLR convention this section does not yet cover rather than inferring one from §14.7.

- **Template level = phase 2 → `template="4-6"`.** BLLR2xx modules are **phase 2** and ship `template="4-6"` on every page (designer-confirmed 14 July 2026, CL-0035). The **BLL2xx phase-1 exception (§14.7) never applies here** — a `BLLR…` code does not match the literal `BLL2` prefix (its fourth character is `R`, not `2`). Consistent with the bookworm ranges below (BLLR201–230 → Year suites 4–6). See `06_TEMPLATE_RECOGNITION.md` §5 (Detection → Template level).
- **Bookworm avatar (second avatar).** A cartoon bookworm — plump, brimming with energy and enthusiasm — per the explanation/example in the AVR form. The image varies by **module-code range**, one bookworm per year suite:

  | Image | Module-code range | Year suite |
  |---|---|---|
  | `bookworm_1.jpg` | BLLR201 – BLLR210 | Year 4 |
  | `bookworm_2.jpg` | BLLR211 – BLLR220 | Year 5 |
  | `bookworm_3.jpg` | BLLR221 – BLLR230 | Year 6 |

  Folder: `bookworms/`. Supplied markup (select the image for the module's code range):
  ```html
  <img class="img-fluid imageCentral" loading="lazy" src="bookworms/bookworm_1.jpg" alt="Bookworm" >
  ```
  > The source email writes the first filename capitalised (`Bookworm_1.jpg`) and the other two lower-case (`bookworm_2.jpg`, `bookworm_3.jpg`), while its supplied `<img>` tag uses the lower-case `bookworms/bookworm_1.jpg`. Follow the **supplied `<img>` tag** — lower-case `bookworm_N.jpg` — and emit a `Designer/Developer To Do:` note asking the developer to confirm the exact filename casing when the assets are delivered.

- **Bookworm art + audio are DEFERRED.** The worm characters are **still under development**, and the **audio with audiovisual is yet to be developed**. Emit the `<img>` scaffold above with a visible `Designer/Developer To Do:` note — *bookworm character art still under development; audio/audiovisual to be developed* — never a placeholder silently swapped in and never a hidden comment.

- **"Secret shelf" and "Whispering Archives" map — design under construction.** Both features are **explicitly required to carry a red note**. Emit each in place with a visible note:
  ```html
  <p style="color: red; font-weight: bold;">Designer/Developer To Do: Design is under construction with the development team.</p>
  ```
  This is a **direct instruction from the design authority**, not a Convertor-detected gap — it takes the `Designer/Developer To Do:` prefix (right-but-pending), not `Red Flag:`.

---

## 14.10 MiW — My Te Kura Writing
**Scope — Cohort:** all **MiW (Writing)** FUNdamentals and modules. **Module codes always begin `WJ`.** Source: *"Writing – Global Parameters"* (FUNdamentals and Modules).

- **FUN vs module — trailing-digit test.** Within the `WJ` prefix, a **FUNdamentals templated resource ends in `0`** (e.g. `WJ200`, `WJ210`); a **normal module ends in a non-zero digit** (e.g. `WJ201`, `WJ218`). This is a **naming test only** — structural sub-type recognition (body class `fundamentals container-fluid`, `div.phases` → `div.fundamentalsPanel`, `footer-nav fundamentals-nav`) still comes from `06_TEMPLATE_RECOGNITION.md` §3.3, and Mode B sibling authority still wins where they disagree.

- **NZ map on every intro page.** Each intro page of the FUNs **and** the modules carries an image of **New Zealand on the right-hand side**, with a **star and road sign placed at the town being learned about**. Supplied markup (the label `<p>` carries the placename; `top`/`left`/`pointTop`/`pointLeft` are positioned per town):
  ```html
  <div class="imageLabel" layout="map">
    <img class="img-fluid imageCentral imgLabel" src="New Zealand/iStock-1454804075.png" alt="New zealand map">
    <div class="label" direction="horizontal" top="20%" left="20%" pointTop="50%" pointLeft="50%"><p>Placename</p></div>
  </div>
  ```
  Supplied acknowledgement entry for the map image:
  ```html
  <p>Photo: New Zealand Topographic Relief Map - 3D Render, iStock 1454804075, Getty Images. Used with permission.</p>
  ```
  > The per-town `top` / `left` / `pointTop` / `pointLeft` percentages and the placename are **content-specific** — the supplied values are the reference example, not a default. Where the town's coordinates are not given in the source, emit the pattern with the supplied values and a `Designer/Developer To Do:` note to position the star/road sign for the named town.

- **FUN layout: intro page + clickable lesson tiles, any order.** The FUNs are set out like other FUNs — an **introduction page**, then **images to click** taking the ākonga to specific lessons. **Lessons can be done in any order.** Tile images must be **consistent across each phase** for each FUN topic (Number Sense / Place Value / Operations / Fractions in the supplied example), and **all tiles in a FUN should be the same phase.**

- **Side-navigation tabs inside each lesson.** Each lesson carries **side-nav tabs** so ākonga can work through it as they please — the same pattern as the **Maths 1-10 FUNS**.

- **Kea character, varying by phase.** A character **Kea** features **within each lesson**. The character **varies slightly from phase to phase** (e.g. different medallion placement / wing colours). Folder `kea_characters/`; one image per phase — `kea_1.jpg`, `kea_2.jpg`, `kea_3.jpg`. Supplied markup:
  ```html
  <img class="img-fluid imageCentral" loading="lazy" src="kea_characters/kea_1.jpg" alt="Kea character" >
  ```
- **Kea speech bubble + audio.** When the Kea appears in a module he **also has a speech bubble and audio** (speech-bubble mechanics stay in `04_COMP_SEGMENTS_OVERLAYS.md`).
- **Kea art + audio are DEFERRED.** The **Kea characters are still under development, as well as the audio.** Emit the `<img>` scaffold and the speech bubble/audio slot with a visible `Designer/Developer To Do:` note — *Kea character art and audio still under development.*

---

> **Sections 14.11 and 14.12 continue in `14D_SGP_CROSSCUTTING_AND_TECHNOLOGY.md`** — the cross-cutting notes and the Technology family. The §14.x numbering is ONE continuous sequence across `14A` (14.1-14.5), this part (14.6-14.10) and `14D` (14.11-14.12).
