> **Last updated:** Tuesday, 27th October, 2026 2:43 PM
> **Granular part E (6 of 6) of `14_SUBJECT_GLOBAL_PARAMETERS.md`** — Families 14.13 (Science) and 14.14 (Maths): the centralised character images. Opened 27 October 2026 (CL-0117) as a new part rather than growing `14D`.
> All sibling parts live in `14_SUBJECT_GLOBAL_PARAMETERS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## 14.13 Science — the four characters + the comic scenes
**Scope — Cohort:** all **Science** modules. *(The module-code prefix was not stated in the source; identify these modules by subject until a prefix is recorded here. Do not guess one.)* Source: Meredith Lees → Gavin McGruddy, *"New template items"*, 23 October 2026 — `Global Edits Science.docx`, the template's Centralised Images page (`refresh_imageCentral.html` → *Science Characters*) and the server folder `imageCentral\Science Characters`. Actioned through the authorised channel 27 October 2026 (CL-0117; constraint 95).

- **Four characters — Aroha, Lani, Max, Quinn.** Each has **three full-body poses, numbered 1–3**, and **two head shots, numbered 4–5**. **Quinn is the exception with FOUR head shots:** 4–5 with her safety goggles **on**, 6–7 with them **on her head**. Every image is a `.jpg`.
- **Folder and filename — copy verbatim.** `science characters/<Name>-<n>.jpg` — the folder **lower-case** exactly as the template page writes it, the name capitalised, a hyphen, the pose number: `science characters/Aroha-1.jpg`, `science characters/Quinn-6.jpg`. *(The server folder itself is listed as `Science Characters`; the template page — the design team's own working reference — writes `science characters/`, and that is the form to emit. A `draft/` sub-folder exists on the server and is never referenced.)*
- **Supplied markup** (the Global Edits document's form — the `alt` is the character's name; the template page leaves it empty, use the name):
  ```html
  <img class="img-fluid imageCentral" loading="lazy" src="science characters/Quinn-1.jpg" alt="Quinn" >
  ```
- **Writer tag.** `[Centralised image: Quinn 4]`, `[Image centralised Quinn 4]`, `[Central image: Quinn]` — the centralised-image tag in any of its forms (`01` → Tag Taxonomy) plus the character's name and, optionally, the pose number. **No number → pose 1** (the full-body image the Global Edits document shows first). A name or number that does not exist in the set (`Aroha-6`, `Max-7`) is a `Red Flag:` naming the request, never a guessed file. The characters appear in `[Speech bubble]`s like every other character set — mechanics stay in `04_COMP_SEGMENTS_OVERLAYS.md` → COMP_09 (its `imageCentral` rule already covers central characters).
- **Comic scenes — designer-made, always `.png`.** `science characters/comic scenes/clubhouse_1.png` (*Clubhouse*) and `science characters/comic scenes/kowhai_reserve_1.png` (*Kōwhai Reserve*). Writer tag `[Centralised image: clubhouse]` / `[Centralised image: kowhai reserve]`. **A scene not in this list must be created by a designer** — emit a visible `Designer/Developer To Do:` naming the scene the writer asked for; never compose one from the character images.
  ```html
  <img class="img-fluid imageCentral" loading="lazy" src="science characters/comic scenes/clubhouse_1.png" alt="Clubhouse" >
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
- **The rest of the Global Edits Maths document is NOT folded in by this change.** The same document also sets out a three-part overview tab (Learning intentions / *Maths No Problem* links / Curriculum content), phase-by-phase checkpoint and end-of-module dropbox copy, a lesson-summary alert and the `[Math]` fraction rule. Only the characters were in the authorised change; where a Maths module needs one of those conventions, follow a built Maths sibling (Mode B) and raise a `Red Flag:` rather than inferring the rule from the document. *(The `[Math]` fraction rule is already governed by CL-0115 — `05A` → Equations.)*
