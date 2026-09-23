> **Last updated:** Wednesday, 23rd September, 2026 11:36 AM
> **Granular part B2 (3 of 5) of `14_SUBJECT_GLOBAL_PARAMETERS.md`** — Families 14.9 (BLLR) and 14.10 (MiW/WJ). Split from `14B` on 23 September 2026 when it passed the 30 KB soft limit (`CLAUDE.md` §4); content moved verbatim.
> All sibling parts live in `14_SUBJECT_GLOBAL_PARAMETERS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## 14.9 BLLR — Blended Literacy (Reading)
**Scope — (b) Module-series:** **BLLR** modules. Source: Persephone Samuels → Gavin McGruddy, *"BLLR Global Parameters"*, 9 July 2026.

> **BLLR is a distinct prefix from BLL.** The BLL conventions of §14.7 (writing font, elkonin boxes, `.dropbox` carve-out, etc.) are scoped to the **BLL** series and do **not** automatically bind BLLR. Where a BLLR module needs a BLL convention, it must be recorded here explicitly or raised as a `Red Flag:`.

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
  > The source email writes the first filename capitalised (`Bookworm_1.jpg`) and the other two lower-case (`bookworm_2.jpg`, `bookworm_3.jpg`), while its supplied `<img>` tag uses the lower-case `bookworms/bookworm_1.jpg`. Follow the **supplied `<img>` tag** — lower-case `bookworm_N.jpg` — and emit a `Designer/Developer To Do:` note asking the developer to confirm the exact filename casing when the assets are delivered. **Settled (CL-0113):** the delivered files are lower-case, so the confirm-the-casing note is retired.

- **Bookworm art DELIVERED (CL-0113, September 2026 server list); audio still to be developed.** The central `bookworms/` folder now holds `bookworms/bookworm_1.jpg`, `bookworms/bookworm_1a.jpg`, `bookworms/bookworm_2.jpg` and `bookworms/bookworm_3.jpg` (lower-case — which settles the casing question above: follow the lower-case `<img>` tag and **drop** the confirm-the-casing To Do note). Emit the real `<img>` for the module's code range — no art To Do note (gold: BLLR201–203 carry `bookworms/bookworm_1.jpg`). The **audio with audiovisual is still to be developed**: where the Writers Template calls for the bookworm's audio, emit a visible `Designer/Developer To Do:` note for the audio only. (`bookworms/archive/` and `bookworms/idk/` are the design team's working files — never reference them.)

- **"Secret shelf" — BUILT: the `bookshelf` component (CL-0113; `bookshelf.html`; gold BLLR202 / BLLR203).** Book covers sit on a shelf (each cover styled 20 % wide); clicking a cover opens that book's carousel. Supplied markup (copied from the snippet):
  ```html
  <div class="bookshelf row">
      <div class="shelf col-md-8 col-12">
          <div class="bookCover">
              <img src="images/detective-beans/Cover.jpg" alt="" class="img-fluid">
          </div>
          <div class="bookCover blank">
              <h4>Wild Robot</h4>
              <h5>Peter Brown</h5>
          </div>
      </div>
      <div class="bookContainer col-md-8 col-12">
          <div class="bookContent">
              <div class="row carousel">
                  <div class="col-md-12 col-12 viewer">
                      <div class="item image">
                          <div class="row">
                              <div class="col-md-8 offset-md-2 col-12">
                                  <img src="images/detective-beans/Cover.jpg" alt="" class="img-fluid">
                              </div>
                          </div>
                      </div>
                      <!-- one item image per page: Cover, First-page, Mid-book, Blurb … -->
                  </div>
              </div>
          </div>
          <!-- one bookContent per bookCover, in the same order -->
      </div>
  </div>
  ```
  One `bookCover` per book (a cover image, or `bookCover blank` with the title `<h4>` and author `<h5>` where there is no cover image), and one `bookContent` carousel per cover in the same order. Shelf acknowledgement (supplied): `Photo: Bookshelves with books for children, iStock 1423266435, Getty Images. Used with permission.` The former "design under construction" red note for the secret shelf is **retired**.
- **"Whispering Archives" map — design under construction.** Still **explicitly required to carry a red note**. Emit it in place with a visible note:
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
- **Kea art DELIVERED (CL-0113); audio still pending.** The central store now holds `kea_characters/kea_1.jpg`, `kea_2.jpg`, `kea_3.jpg`, `kea_4.jpg`, `Kea_5.jpg`, `kea_6.jpg`, plus the custom pair `kea_characters/customKea/kea_formal.jpg`, `kea_formal_text.jpg`, `kea_informal.jpg`, `kea_informal_text.jpg` (gold: 21 WJFUN modules). **Unresolved filename mismatch:** the server lists `Kea_5.jpg` with a **capital K**, while the built modules write `kea_characters/kea_5.jpg` (WJFUN108 / 205 / 210 / 212) — record both; until the design team confirms, follow the built modules (`kea_5.jpg`) and raise a `Red Flag:` naming the mismatch where kea 5 is used. The server does not say which image belongs to which phase — follow a same-phase sibling module. No art To Do note; the **audio** is still pending, so the speech bubble's audio slot keeps a visible `Designer/Developer To Do:` note.
- **Writing process (CL-0113; `writingProcess.html`; gold ENGC206 / ENGC403 / ENGS404).** The writing-process graphic is centralised and generated by the template from one empty div: `<div class="writingProcess" phase="1-yr-1"></div>` — `phase` values `1-yr-1`, `1-yr-23`, `2-yr-456`, `3-yr-78`, `4-yr9-10`, `5-NCEA1`. A single stage: `<div class="writingProcess singleStage" stage="Plan"></div>` — `stage` values `Plan` / `Draft` / `Revise` / `Edit` / `Publish` / `Reflect` / `Checkpoint` / `Checkpoint_1` / `Checkpoint_2` / `Checkpoint_3`. **The div must sit in its own row (inside a `col`) or it will bug.** The stage images live centrally under `writing process/phase N/` (e.g. `writing process/phase 2/plan.png`); never copy them into the module.

---

> **Sections 14.11 and 14.12 continue in `14D_SGP_CROSSCUTTING_AND_TECHNOLOGY.md`** — the cross-cutting notes and the Technology family. The §14.x numbering is ONE continuous sequence across `14A` (14.1-14.5), `14B` (14.6-14.8), this part (14.9-14.10) and `14D` (14.11-14.12).
