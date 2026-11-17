> **Last updated:** Tuesday, 17th November, 2026 7:37 PM
> **Granular part A (1 of 9) of `14_SUBJECT_GLOBAL_PARAMETERS.md`** — Purpose + families 14.1-14.3 (Languages, Pathways, Taonga). CED (14.4) and FUNdamentals (14.5) moved verbatim to `14A2_SGP_FAMILIES_4_5.md` on 17 November 2026 when this part passed the 30 KB soft limit (`CLAUDE.md` §4); renamed from `14A_SGP_PURPOSE_FAMILIES_1_5.md` the same day. The Languages Audiovisual Package asset registry lives in `14C`.
> All sibling parts live in `14_SUBJECT_GLOBAL_PARAMETERS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
> **Last updated:** Monday, 10th August, 2026 10:45 AM

# 14 — Subject Global Parameters

> **When to load:** When converting or advising on a module that belongs to one of the subject **cohorts / series** documented below (Languages Phase 1–4, Pathways, Taonga, CED Phase 5, FUNdamentals H&PE, LS, BLL, BLLR, MiW/WJ, HPE content lessons, Technology, Science, Maths, Social Sciences), and whenever these conventions are changed in Update Mode. These are the design team's per-subject "global parameters" — the standing look-and-feel and structural conventions each subject wants applied to every one of its modules.

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
**Scope — Cohort:** the six Languages prefixes (Chinese, French, Gagana Samoan, German, Japanese, Spanish) at **Phases 1–4**. **Code forms in circulation:** `CHFUN` (Chinese Fundamentals — `CHFUN01`–`CHFUN07` live) and `JPNFUN` (Japanese — `JPNFUN05` named by the designer); record each further prefix as its first module appears (earlier doc-14 drafts used `CHIFUN`/`JAPFUN` — the live codes are the shorter forms). Reference examples: `JAPFUN01_0_0`, `JAPFUN04_0_0` (earlier supplied layout files), and the **final** `20260511_Language_HTML` (supplied 5 August 2026 — the finalised Audiovisual Package asset/tag registry below; a layout/asset reference, never content to copy).

- **Language fonts are mandatory here above all (constraint 92, universal).** Every run of Japanese text carries `jp-text`, every run of Chinese text carries `ch-text`, and every run of pinyin carries `pinyin` — in headings, prose, bold runs, list items, table cells and inside the `<h1><span>` title — not just the first occurrence and not just the vocabulary tables. **Te reo Māori and English are never wrapped**, and a macron alone never identifies pinyin (`ā ē ī ō ū` are shared with te reo). Where Han characters cannot separate Japanese from Chinese, the class comes from the module's language — `JPNFUN`/`JPN` → `jp-text`, `CHFUN`/`CH` → `ch-text` — and a run containing kana is Japanese regardless. Full rules: `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` → **Language Fonts**.
- **Structural reference points (designer instruction, 5 August 2026).** The **CHFUN** modules are the structural reference point for **all** language fundamentals; **`JPNFUN05`** is the reference point for **all language 05 fundamentals**, whose layout is slightly different. Mode B sibling authority (`06_TEMPLATE_RECOGNITION.md`) is unchanged: a built same-language sibling still wins; where none exists, reference the CHFUN set (or JPNFUN05 for an 05 module).
- **Course shape (CL-0150 — *2026 Refreshed 000 Language Global Parameters*).** Each beginning language course has a **Mihi Whakatau**; **5 Novice learning-content modules** (NO901–905) and **5 Novice + (old Emergent) learning-content modules** (NO906–910), **8 lessons each**; and **8 Fundamental modules** (Spanish has **7**). Every learning-content module has an **Introduction page**; Lesson 8 may carry an engagement trigger (MTK quiz or dropbox) — build only what the writer tags.
- **FUN05 is a series of pages.** For every language the FUN05 (*Language Features*) layout differs: it is a **series of pages**, each **linkable from the exact language feature in a Learning Module** — a grid of feature buttons with **Phase 4 / Phase 5** level switches (Phase 4 = *First Steps*, Phase 5 = *Next Steps*). Reference: JPNFUN05.
- **Floating navigation contents.** *Fundamental modules:* the eight Fundamentals as links — Language is Culture · Listening and Speaking · Reading and Writing · Identity and Culture · Language Features · **item 6, the language's own script page (e.g. *Japanese Script*) — different for every language** · Spoken and Written Language Differences · Mistakes Mean Progress — then **The Hub**. *Learning-content modules:* **Fundamentals** and **The Hub**, plus the **Module Word list** (vocabulary list). The `stickyNav` To Do note (below) names these links.
- **Vocabulary quizzes — Learning Systems builds them (decision D5).** Vocabulary quizzes are **MTKQuiz question-pool** quizzes created by **Learning Systems** from the writer's word list, placed in **Lesson 7** (most languages in modules NO906–910; very few in NO901–905). Writer tags: `[Learning systems vocab quiz]` … `[Learning systems quiz end]` around the information for Learning Systems, plus `[quiz – vocab, module]` or `[quiz – vocab, course]` (a module quiz or a whole-course quiz). Build the MTK-quiz activity shell of constraint 65 — title *Vocabulary quiz* unless the writer gives one; the To Do reads *Learning Systems to create this vocabulary quiz (MTKQuiz question pool, \`module\`/\`course\` as tagged) from the writer's word list, then orgunit-link it and insert its quicklink*. Nothing between the two tags is emitted (CL-0082). An engagement trigger is **unlikely** unless the writer specifies it (approved by the Curriculum Liaison).
- **Samoan.** The new Samoan course has its own key communication documents (Creative Services / SMS) — reference only; no conversion rule.
- **All Languages modules are combo.** Every page of every Languages-cohort module ships `template="combo"` on `<html>` — e.g. `<html lang="en" level="" template="combo" class="notranslate" translate="no">`, per the supplied `20260511_Language_HTML` reference ("Languages are all combo — should be reflected in the code"). The sub-type within combo (Fundamentals tiles / Inquiry crumbs / standalone) still comes from the `<body>` class per `06_TEMPLATE_RECOGNITION.md` §2, and `06` §5's Mode B template-level check expects `combo` — not a year-band value — for this cohort. Consequence: `combo` is **not** one of the three autoCheck auto-apply template files (constraint 38 / `03` COMP_00), so `autoCheck` is applied in Languages output only when the writer's intended behaviour calls for it.
- **The Audiovisual Package is FINALISED (5 August 2026).** "All packages have been finalised for each of the languages" — every language panel in the final reference is marked *finalised and will be in use in upcoming modules*. This **supersedes** the former "provisional asset state" and "videos are added manually" bullets **for registry-listed assets**: where a writer's `[Audiovisual package …]` tag names an asset in the registry below, emit the supplied form exactly as the reference shows (Vimeo `videoSection` embed, `audioImage`, `audioButton`, `audioPlayer`, or `imageCentral` image). A tagged Audiovisual asset **not** in the registry still gets the visible `Designer/Developer To Do:` note (*Audiovisual item to be added by designer/developer from Audiovisual*) — and a pending video slot still uses the pending-ID **Vimeo scaffold** of constraint 64 (`05` → Video Embed → Creative Services Videos).
- **The `[Audiovisual package …]` tag family.** Writers reference the finalised assets as `[Audiovisual package <asset name> item N]`. Variants ride in **nested brackets**: `[full body]`, `[headshot]`, `[neutral]`, `[certificate]`, `[holding books]`, `[ice cream]`, `[expression]`. For a character with multiple expressions (Spanish Pablo / María) the writer puts the number in correlation to the expression — e.g. `[Audiovisual package Pablo [expression] item 1]`. Item numbers are per-language (Japanese legitimately starts at item 0); the asset **name** is the primary key, the item number the cross-check.
- **Language icons.** Eight icons — **Reading, Listening, Speaking, Writing, Interact, Think, Idea, Linguist** — tagged `[Audiovisual package Icon <Name>]`; files are **central** — `Language icons/Language icons_<Name>.jpg` with `class="img-fluid imageCentral"`, plus phase-coloured `… P1.jpg` – `P4.jpg` variants (the module-local `images/Icons/…` folders are retired; exact filenames in `14C` §2; CL-0112). **The icons are identical throughout the phases and automatically match the module's phase colour** — the writer never specifies a phase colour and the conversion never asks for one; use the tag as-is.
- **Asset registry (finalised) — the complete registry lives in `14C_LANGUAGES_AV_ASSET_REGISTRY.md`.** Every finalised asset — tag name, item number, delivery form, **full Vimeo URL (including the required `h=` hash)**, `audioName`, `audioImage` id and exact central-asset filename — is absorbed there verbatim from `20260511_Language_HTML`, together with the supplied markup shapes (Vimeo `videoSection` embed, `audioImage`, `audioButton`, `audioPlayer`, headshot + speech-bubble pairing, scene/expression carousels), the eight-icon filename table, the Spanish accents rule (one audio runs Spain → Latin America → Mexico), the iStock-derived-asset rules (the writer still puts an i-Stock link in the WT; "Adapted. Used with permission." acknowledgements per `05C`) and the tag-tolerance notes. **The supplied HTML no longer needs to be consulted** — `14C` is the source of truth for the registry data; this section keeps the rules.
- **Central images — `imageCentral` character/persona assets.** The recurring Languages characters and persona images are **centralised template assets**: they are served from the design team's central per-language asset folders and carry `class="img-fluid imageCentral"` (the class that applies the central-store filepath prefix). Canonical supplied form:
  ```html
  <img class="img-fluid imageCentral" loading="lazy" src="German assets/Salsi_certificate.jpg" alt="pretzel character holding certificate" />
  ```
  Central folders in the final reference: `German assets/`, `Chinese assets/`, `Japanese assets/` (observed in both `Japanese assets/` and `japanese assets/` casings — treat as one folder), `Samoan character assets/`, `Spanish assets/`. **French has no central image folder** — its characters are the Vimeo avatars; scene screenshots (e.g. `images/French/Sophie and Luc podcast.png`, `images/German/Family playing board game.png`) are module-local `images/…` and do **not** take `imageCentral`. **Writer-specified module images are unchanged** — they stay in `images/…` and **never** take `imageCentral` (`01_PIPELINE_EXTRACTION_TAGS.md` → Rules Common to Both Modes); the class is reserved for centralised template assets exactly like these.
- **Two-tile Fundamentals split — the tiles are named *First Steps* and *Next Steps* (CL-0118).** A Fundamentals WT that carries **Novice** content and then **Emergent** content is separated into **two tiles**, one per proficiency level, each leading to that stream's content (per the JAPFUN01 / JAPFUN04 set-up — currently one tile for Phase 4 and one for Phase 5). **From 27 October 2026 the two levels are DISPLAYED as `First Steps` (the former *Novice*) and `Next Steps` (the former *Emergent*)** — the names the curriculum leads confirmed (Stephanie Charles → Kate Scanlon → Persephone Samuels, 16–27 October 2026; example CHFUN08) — **everywhere the level name shows on the page**: the module menu's level tabs (`<li><a>First Steps</a></li>`), the `.phases` strip (`<div phase="1"><p>First Steps</p></div>`), the `phaseLink` tiles' `<h3>` and image `alt`, and the per-level panel heading of the multi-file levels overview. The Global Parameters document was updated to the new names in November 2026 (*"(old Novice) now First Steps Tile and (old Emergent) now Next Steps Tile"* — example: Level 1 Japanese JPN1000's Fundamental set-up, one tile for Phase 4 and one for Phase 5), but older Writers Templates still carry the old words in their markers (`[PAGE 1 Novice]`, `[Novice Page 1]`, `[Novice Content starts here]`, `[Tab 1] Novice Learning Intentions`): **read *Novice* / *Emergent* as the two levels exactly as before, and write the new names** — a template that already types *First Steps* / *Next Steps* is read the same way. Never rename a level word inside the writer's own prose. The eleven finished Language FUN modules (CHFUN01 / 04 / 05 / 06 / 07 / 08, FRFUN06 / 07 / 08, JPFUN01 / 02) were updated to the new names on 27 October 2026 — their menu tabs, level strip, tiles, tile `alt` and level headings only; comments, prose and filenames untouched — so a built sibling now shows the new names too. Use the `phaseContainer` / `choicePage` tile pattern the reference files use; the sub-type width follows constraint 56 (`col-md-11 col-12` for the Fundamentals sub-type, `col-md-8` when paired with an `alertImage`). The CHFUN set is now the structural reference point for this layout (JPNFUN05 for the 05 variant) — see the reference-points bullet.
- **Set characters in red brackets.** Languages define recurring characters written in red brackets (e.g. a named speaker/character tag). **Once a character has been introduced for the first time, that character is added every subsequent time its tag is used** — the tag is never left as bare bracket text (constraint 3) and the character is not dropped on later uses. The Audiovisual Package registry above is the concrete asset set behind this rule.
- **Three-part `[TITLE BAR]` = three titles (target language + English + Te Reo).** A Languages writer may give the module title in **three** languages, `|`-separated — e.g. `[TITLE BAR] HALLO, DEUTSCH! | HELLO, GERMAN! | NAU MAI KI TE REO TIAMANA!` (`GENO901`). **Each part becomes its own `<h1><span>`** on the overview page — three headings, **in the writer's order**: the cohort uses both orders (`GENO901`, `GEFUN01`, `SPA1004`, and the Samoan `1005 Sasa` lead with the target language; `GEFUN06` leads with English), and the conversion never re-orders them. An **empty part, or an unfilled placeholder** such as `TE REO` / `MODULE TITLE TE REO` / `INSERT MODULE TITLE TE REO`, is **skipped** — it is the writer's un-replaced prompt text, not a title. **This three-way split is scoped to this cohort:** outside Languages a second `|` is punctuation inside a title, not a third language (corpus-verified — see `01_PIPELINE_EXTRACTION_TAGS.md` → Template Title Patterns → TITLE BAR PARSING RULE, and constraint 85). Ledger `CL-0085`.
- **Sticky nav on every page.** Add `<script src="js/stickyNav.js" type="text/javascript" class="stickyNav"></script>` to the `<head>` of **every** page. At the **top of the 0.0 content**, emit a visible `Designer/Developer To Do:` note: *set up the `stickyNav.js` file — Fundamentals list + The Hub (Fundamental modules) or Fundamentals + The Hub + Module Word list (learning-content modules).*

---

## 14.2 Pathways
**Scope — (a) Series + level:** **Pathways Level 1** (development focus Terms 2–3). **Level 2 is HELD** — see the note at the end of this section.

- **Course navigation = "Sections", not "Fundamentals" — Te Reo titles DELIVERED (CL-0151).** The course home reveals **Section** tiles, each opening to its modules:

  | Section | Te Reo title | English title | Modules |
  |---|---|---|---|
  | 1 | Ka haere ahau ki hea? | Where am I going? | PWY1001 – PWY1005 |
  | 2 | Me pehea ahau ki reira? | How do I get there? | PWY1006 – PWY1009 |
  | 3 | He aha te heke mai? | What might the future hold? *(the translation table writes "What does the future hold?")* | PWY1010 – PWY1016 |

  Build the wording the Writers Template uses (decision D6). The former *Te Reo translations pending* `Designer/Developer To Do:` is **retired**. (The document's own counts — 5 / 4 / 6 modules — disagree with the table's PWY1010–1016 range for Section 3; the range is recorded as given.)
- **Lesson structure.** Most Level 1 Pathways modules have **three lessons with sub-parts** (`1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 3.1, 3.2, 3.3`). Some modules have fewer sub-parts depending on content. Content is a mixture of refreshed, new, and merged material from the old Pathways course.
- **Persona tagging pattern.** Level 1 Pathways uses rangatahi **personas** that guide the learning, shown with a recognisable **circle image**. The tagging pattern is:
  - `[Persona box]`
  - `[Audioimage]` (with play button)
  - `[Photograph in a circle]` — the persona image
  - `[Audiovisual item N {name}]` — the audio recording (the persona transcripts are **real audio recordings, not AI**)
  - `[Transcript button]` — reveals the transcript
- **Persona details DELIVERED — the `pathwaysPersona` component (CL-0113; `refresh_pathwaysPersonas.html`; gold PWY1001 / PWY1002 / PWY1007).** Section 1: **Whai**; Section 2: **Leilani** and **Bailey**; Section 3: **Māia**. Central images: `pathwaysPersonas/whai.jpg`, `pathwaysPersonas/bailey.jpg`, `pathwaysPersonas/leilani.jpg`, `pathwaysPersonas/māia.jpg` (`pathwaysPersonas/archive/` holds drafts — never reference it). The persona tags above build this markup (copied from the snippet):
  ```html
  <div class="pathwaysPersona" id="whaiIntro">
      <div class="pathwaysPersonaImage">
          <img class="img-fluid imageCentral" src="pathwaysPersonas/whai.jpg" alt="" />
          <div class="pathwaysPersonaText">
              <h5>Whai</h5>
          </div>
      </div>
      <div class="pathwaysPersonaControls">
          <button type="button" class="pathwaysPersonaBtn pathwaysPersonaPlay" aria-label="Play audio" title="Play"></button>
          <button type="button" class="pathwaysPersonaBtn pathwaysPersonaTranscript" aria-label="Show transcript" title="Transcript"></button>
      </div>
      <div class="pathwaysPersonaTranscriptContent">
          <p class="marB0">Transcript text</p>
      </div>
  </div>
  ```
  The **`id` names the audio file** (`id="whaiIntro"` plays `audio/whaiIntro.mp3`); **both buttons stay empty**; the `.pathwaysPersonaText` overlay is optional; the component **must sit inside a `row` and a `col`** (e.g. `col-md-4 col-6` per persona). **`noAudio`** on `.pathwaysPersona` strips it back to just the circular image. The former persona `Designer/Developer To Do:` placeholder is **retired**.
- **Knowledge & Practice (Ks/Ps) statements.** There is **no new Pathways curriculum yet**, so the overview does **not** include new-curriculum K/P statements — the writers' template leaves a placeholder. In the meanwhile, only short **learning intentions and success criteria** are included. **Do NOT add curriculum K/P statements in-module**; this is a **revision request** once the curriculum is announced — emit a `Designer/Developer To Do:` note to that effect at the placeholder.
- **Overview is DEFERRED.** The Pathways overview is **to be set once the first module is complete** — emit the overview scaffold with a `Designer/Developer To Do:` note rather than a finalised overview.
- **Assessments have their own template.** Level 1 Pathways unit-standard assessments are written on the **Pathways Assessment Activities Template** and converted in Assessment Mode by `18_ASSESSMENT_MODE.md` → `18D` (constraint 100, CL-0143) — these module conventions do not apply to them.

> **Pathways Level 2 — HELD (no action this scope).** Level 2 is on pause. Six Level 2 "green" edit-proof modules exist for the refreshed template — **PWO2004, PWO2007, PWO2009, PWO2010, PWO2021, PWO2028** — with an edit-proof sheet set up. Developers revisit these next term when a Level 2 timeline is set and the edits are provided. Recorded here for reference only; no Level 2 conventions are active yet. Level 2's sections, when it resumes: 1. *Where am I going?* (5 modules), 2. *How do I get there?* (8), 3. *How do I thrive moving forward?* (6 or 7).

> **Pathways Fundamentals — space held.** Fundamentals *may* be developed later, once the brief on unit standards and vocational education is confirmed. Nothing to build yet.

---

## 14.3 Taonga (The Arts)
**Scope — Cohort:** all **Taonga** modules (all phases). Taonga modules resemble FUNs but are **Taonga, not FUNs**, because they have **dropboxes attached**.

- **Intro page + clickable lesson images.** Set out like a FUN: an **introduction page**, then **images to click** that take the ākonga to specific lessons. **Lessons can be done in any order** (use the Maths 1-10 FUNS pattern as the model).
- **Side-navigation tabs inside each lesson.** Each lesson has **side-nav tabs** so ākonga work through it in any order, exactly like the Maths 1-10 FUNS.
- **Per-lesson layout (A–E).** Every lesson follows the same layout:
  - **A. Overview** — LI and SC plus a **vocab pull-out box**.
  - **B. Engage (I do)** — a short, simple stimulus to spark interest.
  - **C. Explore (We do)** — a simple online activity or interactive to practise learning.
  - **D. Create (You do)** — a hands-on activity away from the screen, **kaiako-assessed through a dropbox**.
  - **E. Extend (Optional)** — a simple challenge for learners ready to go further.
  - *(The former **F. Links to (Optional)** step is struck through in the November 2026 document — **removed**, CL-0152. A lesson has steps A–E.)*
- **Unique overview.** Taonga modules use a **unique overview** (not the generic pattern).
- **Overview + images are DEFERRED.** The overview is **to be set once the first module is complete**, and images are still to come — **use placeholder images until updated links come through from the first module's Comparison Mode run.** Emit a `Designer/Developer To Do:` note at the overview and at each pending image.
- **Tui character (art DELIVERED — per-phase folders, multiple poses).** A tui character (**Tui Toi**) features in each Taonga module and **varies from phase to phase**. The illustrations are **now in the refresh template** (design-team upload, August 2026), so the tui is no longer a deferred item. The asset convention is a **folder per phase, several poses per folder**:
  - **`tui_characters/phase {N}/`** — **four phase folders**, `phase 1` … `phase 4` — **a space, not an underscore** (the design team's refreshed Centralised Images page, 3 November 2026 — CL-0141; the August reference's `phase_1` form is superseded). `{N}` is the **module's phase**. (The Arts document still shows the superseded `phase_1` path; the space form stands — CL-0141.)
  - **`tui_{P}.jpg`** — the pose. **Poses 1–6** in phases 1–3; **phase 4 has only 4 poses** (`tui_1.jpg` … `tui_4.jpg`).
  - Full path: **`tui_characters/phase {N}/tui_{P}.jpg`**. What each pose shows in each phase (flight / perched / perched singing / default, facing left or right) is tabled in §14.16 (`14F`).

  Supplied markup (phase 1, pose 1 shown):
  ```html
  <img class="img-fluid imageCentral" loading="lazy" src="tui_characters/phase 1/tui_1.jpg" alt="Tui character" >
  ```
  **Phase → folder is derived; the writer's tag names the pose (CL-0141).** Take `{N}` from the module's phase. Where the module's phase is not stated, raise a `Red Flag:` rather than guessing the folder. The refreshed Centralised Images page gives every pose a writer tag, `[Centralised image: tui_<P>]` (§14.16) — where the writer names the pose, build that pose with no note. **Only where no pose is named**, emit **`tui_1.jpg`** (the supplied example) as the scaffold and carry a visible `Designer/Developer To Do:` note (*Tui pose is a designer choice — confirm which pose belongs at this placement*). Never invent a pose beyond the phase's ceiling: a pose above **6** (or above **4** in phase 4) does not exist — raise a `Red Flag:` rather than emitting a path to a missing file.

  Reference: the design team's central-images snippet file, `Z:\Development\Online\Templates\Refresh Template - modules\refresh_template_HTML\tools snippets\refresh_imageCentral.html`, carried the full worked examples (updated in the same August 2026 delivery); its refreshed version (3 November 2026) is absorbed as **§14.16 (`14F`)** — read the registry there.

---

> **Sections 14.4 (CED Phase 5) and 14.5 (FUNdamentals H&PE) continue in `14A2_SGP_FAMILIES_4_5.md`** (split from this part on 17 November 2026 when it passed the 30 KB soft limit, `CLAUDE.md` §4; content moved verbatim). The §14.x numbering is ONE continuous sequence across this part (14.1-14.3), `14A2` (14.4-14.5), `14B` (14.6-14.8), `14B2` (14.9-14.10), `14D` (14.11-14.12), `14E` (14.13-14.15), `14F` (14.16) and `14G` (14.17).
