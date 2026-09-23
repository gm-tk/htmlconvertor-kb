> **Last updated:** Wednesday, 23rd September, 2026 11:36 AM
> **Granular part B (2 of 5) of `14_SUBJECT_GLOBAL_PARAMETERS.md`** — Families 14.6-14.8 (LS, BLL, HPE). BLLR (14.9) and MiW/WJ (14.10) live in `14B2`; cross-cutting notes (14.11) and Technology (14.12) live in `14D`.
> All sibling parts live in `14_SUBJECT_GLOBAL_PARAMETERS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## 14.6 LS — Learning Support
**Scope — (b) Module-series:** **LS** modules (including the **XLP** Learning Partner Toolkits and **XDLS** exemplars). Reference exemplar: `XDLS501`.

> **Two different scopes live in this section.** The **`.learningSupport` class** bullet below is **cohort-scoped to every `X`-prefixed module code** (constraint 89) — wider than this section's series scope. **Every other convention in § 14.6** — terminology and brackets, removed tab navs, the clickDrop layout, speech-bubble prompts, the 6-activity pattern, dropbox copy, move-forward alerts, XLP overviews — stays scoped to **LS / XLP / XDLS** and is never inferred for another X-prefixed series. Where an X-prefixed module outside LS appears to want an LS convention, raise a `Red Flag:` rather than applying it.

- **`.learningSupport` on `<html>` — required by the `X` code prefix (constraint 89).** Add the `learningSupport` class to the root tag, e.g. `<html lang="en" level="" template="NCEA" class="notranslate learningSupport" translate="no">`. **The test is the module code:** any module whose code begins with `X` is a learning support module and carries the class on every page — which covers LS, XLP and XDLS, and equally `XFUN`, `XWHA`, `XMES`, `XTAS` and any other X-prefixed series. The `template=` value is unaffected and is still derived from the module code (constraint 21); the example above shows `NCEA` only because `XDLS501` is an NCEA module. Full rule: `06_TEMPLATE_RECOGNITION.md` § 4.4.
- **Larger font — delivered BY the class.** The bigger module font (the same font as the LS Whakatau) is the stylesheet's response to `learningSupport`. Applying the class is the whole of the Convertor's job here: **never** write font-size CSS, and never add an inline style to achieve it (constraint 2).
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
- **Writing font.** Any text the ākonga must read or interact with uses **`writeFont`** (`writeFont.html`, Playwrite NZ Basic — `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` → Writing Font; constraint 93; CL-0109). The sassoon classes of the earlier `refresh_sassoon_font.html` are legacy — never emitted in a new build. The letterform check still applies: **`a`** is a single-storey a, **`I`** (capital i) reads as a capital I, **`g`** is a single-storey g. (These ākonga are just learning to read and write, so the letters they read must match the letters they write — `l` and `I` are confusing when identical.)
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
- **Quiz rules.** `[MTKquiz]` **does not trigger engagement.** `[Multichoice]` is **autograded**; `[Written Response]` is **teacher-marked** (*What do you think about…?*) and lets learners insert images and add attachments. **Max one quiz per every 2–3 lessons.** **Output shape (universal — constraint 65):** an `[MTKquiz]` builds its own numbered activity box holding only these in order — quiz-title `<h3>`, the writer's quiz instructions where supplied, a `Designer/Developer To Do:` note (create the quiz in MTK DEV + orgunit link it), and a blank-href **"Go to quiz"** button — never a dropbox button, and **never the quiz's own questions or answers**; see `05` → Buttons → MTK Quiz.
- **Health and Safety — the supervisor guidance block (CL-0111).** Where an activity carries a health-and-safety consideration, the writer supplies a supervisor block (Global Edits HPE, September 2026):
  `[Supervisor Button RHS activity] [H4] Guidance for supervisors [Body] This activity… (state the risk / what they are asked to do) As a supervisor, you can: • support your ākonga to choose an option that aligns with their values, beliefs, and level of comfort • guide learning in a way that reflects your context • select resources or approaches that feel age-appropriate and respectful. Some ākonga may prefer: • general or science-based learning • discussion with a trusted adult • private or reflective approaches. You are encouraged to work alongside your ākonga … [End supervisor button]`
  It renders with the **supervisor-button component, Shape A (activity-bound)** — `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` → Supervisor Button (constraint 68): `<h4>Guidance for supervisors</h4>`, the body paragraphs, and each `•` run as a `<ul>` list. The writer's wording is copied verbatim; nothing is added to it.
  - **WATER — health-and-safety content is forefronted in an alert box, never in a supervisor note.** Safety content about water goes in a visible `alert` in the lesson body, not behind the supervisor button.
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
  - **Availability — all five characters are DELIVERED for phases 1–4 (CL-0111; server list, September 2026).** Full body, poses 1 and 2, for every character in every phase: `health & PE characters/phase #/HP_{Sura|Afi|Alex|Kai|Leila}_{1|2}_phase_#.png`. Head-only: `health & PE characters/phase #/head_only/HP_{Name}_3_phase_#.png` (pose 3) and, for most characters, pose 4 (`HP_{Name}_4_phase_#.png`) — **the head-only set is not uniform, so copy the exact filename from the server list, never construct it**: phase 4 Sura has pose 4 only (`head_only/HP_Sura_4_phase_4.png`), and phase 3 also holds `HP_Afi_3_phase_3.png` in the full-body folder. Pairs: `health & PE characters/phase 1/combination/Kai and Afi phase 1.png` and `health & PE characters/phase 1/combination/Sura and Leila phase 1.png` (phase 1 only on the server today). **The missing-character `Designer/Developer To Do:` note is RETIRED** — every character is available, so the former "developers do not sign off 2nd proof until the missing characters are added" hold no longer applies.
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
  - **Beyond two speech bubbles: faces only (CL-0111).** A strip carries at most two speech bubbles; beyond that the characters are shown as faces only (the head-only images), and **a conversation longer than two bubbles goes into a slideshow (carousel)** — `04_COMP_SEGMENTS_OVERLAYS.md` → COMP_07 → Carousel.
  - **Speaker comments are NOT codified.** The `<!-- Alex -->` / `<!-- Kai -->` speaker comments seen in the designer's files are production annotations — the comments policy is unchanged and the Convertor never emits them.
- **Button label: "Upload to Dropbox"** (see §14.11).

---

> **Sections 14.9 and 14.10 continue in `14B2_SGP_FAMILIES_BLLR_MIW.md`** (split from this part on 23 September 2026 when it passed the 30 KB soft limit, `CLAUDE.md` §4; content moved verbatim), and 14.11-14.12 in `14D_SGP_CROSSCUTTING_AND_TECHNOLOGY.md`. The §14.x numbering is ONE continuous sequence across `14A` (14.1-14.5), this part (14.6-14.8), `14B2` (14.9-14.10) and `14D` (14.11-14.12).
