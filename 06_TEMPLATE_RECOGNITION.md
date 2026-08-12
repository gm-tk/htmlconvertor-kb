> **Last updated:** Thursday, 13th August, 2026

# 06 — Template Recognition & Structural Validation

> **When to load:** At the start of EVERY Mode B conversion (reference module files), and whenever you need to validate structural patterns in uploaded HTML files. Also consult when a user asks about template differences or why a particular file looks "different."

---

## PURPOSE

This file provides the structural knowledge needed to **correctly identify, classify, and validate** HTML files uploaded as reference modules (Mode B). Without this reference, an uploaded file is a black box — you can see its markup but cannot distinguish between:
- Intentional structural patterns (safe to replicate)
- Module-specific quirks or one-off variants (should NOT be replicated)
- Legacy template markup (incompatible with Refresh conversions)
- Dev-domain URLs that should be swapped for production

This file answers three questions during Mode B:
1. **What sub-type is this file?** (detection)
2. **What patterns are normal for that sub-type?** (validation)
3. **What should I watch out for?** (known quirks and pitfalls)

---

## 1. TEMPLATE SYSTEM DETECTION — Legacy vs Refresh

**This is the first check on any uploaded HTML file.** Legacy and Refresh templates are structurally incompatible. If a user uploads Legacy files for a Refresh conversion (or vice versa), flag it immediately.

### Quick Detection

| Signal | Legacy (ECHP) | Refresh |
|--------|---------------|---------|
| `<html>` attribute | `level="prm"` (or `level="prinq"`) | `level=""` + `template="..."` |
| JS pipeline | `jquery-2.0.2.min.js` + `script.js` | `idoc_scripts.js` (no jQuery) |
| Bootstrap grid | `col-xs-*`, `col-md-offset-*` | `col-*` (bare), `offset-md-*` |
| Image class | `otleImage img-responsive` | `img-fluid` |
| Page container | `<div id="container"><lesson>` | `<div id="body">` |
| Header tag | `<nav id="module-head">` | `<div id="header">` |
| Footer tag | `<nav id="module-foot">` with `<button>` + FA icons | `<div id="footer">` with `<ul class="footer-nav">` |
| Content wrapper | `<div class="content">` around each section | None — rows sit directly in `#body` |
| Button markup | `<button class="btn btn1">` | `<div class="button">` |
| Video wrapper | `embed-responsive embed-responsive-16by9` | `ratio ratio-16x9` |
| Menu button | Contains `<p><i class="fa fa-bars"></i></p>` | Empty `<div>` |
| Menu content class | `class="bg row"` | `class="moduleMenu"` |
| Activity class | `content activity activity-bg` | `activity` |
| Caption | `div.captionTrigger` → `div.caption` | `<p class="captionText">` |

**If the reference files are Legacy:** Tell the user these are Legacy (ECHP) template files. Ask whether the new module should also be Legacy, or whether they want a Refresh conversion (in which case they need Refresh reference files or a dedicated template).

---

## 2. REFRESH SUB-TYPE IDENTIFICATION

Once confirmed as Refresh, determine which sub-type the reference files represent. This drives structural decisions about navigation, footer classes, and body layout.

### Quick Identifier Table

| Check | Standard | Bilingual | Fundamentals | Inquiry | Combo |
|-------|----------|-----------|-------------|---------|-------|
| `template=` | `1-3` / `4-6` / `7-8` / `9-10` | `1-3` | `combo` | `combo` | `combo` |
| `<body>` class | `container-fluid` | `container-fluid reoTranslate` | `fundamentals container-fluid` | `inquiry container-fluid` | `container-fluid` |
| Navigation system | None | None | `div.phases` → `div.fundamentalsPanel` | `div.crumbs` → `div.inquiryPanel` | None |
| Footer `<ul>` class | `footer-nav` | `footer-nav` | `footer-nav fundamentals-nav` | `footer-nav inquiry-nav` | `footer-nav` |
| `language`/`translation` on `<body>` | No | Yes | Sometimes | No | No |
| `eng`/`reo` on content elements | No | Yes (every element duplicated) | No | No | No |

### Detection Flow

```
1. Check <html> template attribute:
   ├─ "1-3"/"4-6"/"7-8"/"9-10" → Check <body> class:
   │   ├─ Has "reoTranslate" → BILINGUAL
   │   └─ No "reoTranslate" → STANDARD LESSON
   └─ "combo" → Check <body> class:
       ├─ Has "fundamentals" → FUNDAMENTALS
       ├─ Has "inquiry" → INQUIRY
       └─ Neither → COMBO (Standalone)

2. Cross-cutting modifier check:
   └─ <html> has "learningSupport" class → note it (CSS hook, not a separate sub-type)
```

---

## 3. STRUCTURAL NORMS BY SUB-TYPE

Use these to validate reference files and distinguish intentional patterns from quirks.

### 3.1 Standard Lesson — Expected Structure

**Header:** `#module-code` → `<h1>` (module code or lesson number), then `<h1><span>Title</span></h1>`, then `#module-head-buttons` → `#module-menu-button.circle-button.btn1`, then `#module-menu-content.moduleMenu`.

**Module menu labels (expected patterns by level — LESSON PAGES):**

| Template Level | Expected Pattern |
|----------------|------------------|
| 1-3, 4-6 | `<h5>We are learning:</h5>` + `<h5>You will show your understanding by:</h5>` |
| 7-8, 9-10 | `<h5>We are learning:</h5>` + `<h5>I can:</h5>` |

**⚠️ CRITICAL:** These `<h5>` headings serve AS the label text on lesson pages. Do NOT add separate section titles (e.g., "Learning intentions", "Success criteria") above these headings. Do NOT add intermediate `<p>` elements between the heading and the list (e.g., no `<p>We are learning:</p>` after an `<h5>Learning intentions</h5>`). The `<h5>` text IS the complete label. List items must NOT be wrapped in `<i>` tags, must begin lowercase, and must use verb forms matching the heading context. See `01_PIPELINE_EXTRACTION_TAGS.md` for full formatting rules.

**⚠️ Known quirks in existing files (do NOT replicate unless user explicitly requests):**
- ENGI302/401 use `<h3><span>` instead of `<h5>` in module menu — non-standard
- OSAI/OSBY use `<h4>Lesson Overview</h4>` then `<p><b>` for labels — non-standard
- XMES/XTAS use bare `<p>` for labels (no heading tags) — non-standard
- **Corpus-measured scope of these deviations (across all 376 finalized modules):** the `<p><b>` bold lead-ins recur as a *series* convention in **OSBY (Phases 1-3, 7-8, 9-10), OSAI (7-8), MXEO (1-3), and XDLS (NCEA)**; a leading title heading appears as **`Overview`** (OSBY 7-8, ENG NCEA) or **`Lesson Overview`** (OSAI 7-8). Everywhere else the standard plain `<h5>` labels dominate. These are therefore **series/phase-specific** deviations (a Series-Anchor convention), NOT level-wide rules: when a NEW module joins one of those existing series (e.g. a future OSBY302), match that series' menu styling; for any other module, use the standard `<h5>` rules. (See the corpus reference `10_CORPUS_VALIDATED_SCAFFOLDING.md`.)
- For new modules, follow the project's documented heading rules in `01_PIPELINE_EXTRACTION_TAGS.md` (Section 01)

**Body:** Sequential rows directly inside `#body`. No `.content` wrapper. Standard content column: `col-md-8 col-12`.

**Footer:** `<ul class="footer-nav">` with prev + next + home links.

### 3.2 Bilingual Lesson — Expected Structure

**Body class:** `container-fluid reoTranslate` with `language` and `translation` attributes.

**Content duplication:** Every content element is duplicated with `eng` and `reo` bare attributes:
```html
<h3 eng>English heading</h3>
<h3 reo>Te reo heading</h3>
<p eng>English paragraph</p>
<p reo>Te reo paragraph</p>
```

Container-level elements (rows, lists) are also duplicated with language attributes.

**Header:** Always has dual `<h1>` titles (English + te reo).

**Module menu:** Bilingual — full content duplicated with `eng`/`reo` attributes on each element.

**⚠️ Known quirks:**
- TRR104 and TRR108 have no menu button — check whether the new module needs one
- PRIINQ-07 is bilingual with inquiry crumbs — a hybrid, treat carefully

### 3.3 Fundamentals — Expected Structure

> **Subject cohort refinement.** The **Health & PE FUNdamentals** cohort (16 FUNs) adds content conventions on top of this recognised structure — 5–6 tabs down the RHS, first tab an introduction, last tab a reflection, each tab a short lesson, inline interactives plus one engagement quiz in the reflection tab. The **recognition** rules (body class, `div.phases` → `div.fundamentalsPanel`, `footer-nav fundamentals-nav`) stay here; the H&PE content conventions live in `14_SUBJECT_GLOBAL_PARAMETERS.md` §14.5.

**Body class:** `fundamentals container-fluid` (usually with `language="eng" translation="reo"`).

**Navigation:** Phase-based — `div.phases` containing phase tabs, then `div.fundamentalsPanel[phase]` content panels. First panel usually has class `introduction fundamentalsPanel`.

**Phase link cards:**
```html
<div class="row phaseContainer">
  <div class="col-md-3 col-6">
    <div class="phaseLink" phase="2">
      <h3>Phase title</h3>
      <img src="..." alt="..." class="phaseImg">
    </div>
  </div>
</div>
```

**Module menu:** Two-column layout (`col-md-6 col-12 paddingR` + `col-md-6 col-12 paddingL`).

**Footer:** `footer-nav fundamentals-nav` — typically home-nav only (no prev/next).

**⚠️ Known quirks:**
- MXFUN304 has `template="7-8"` but uses `fundamentals` body class — hybrid, unusual
- XFUN01 omits language attributes on `<body>`, has home + next (no `fundamentals-nav`), and places acks after footer
- Most fundamentals files use `tekuradev` domain — check and swap to production if needed

### 3.4 Inquiry — Expected Structure

**Body class:** `inquiry container-fluid`.

**Navigation:** Breadcrumb/tab-based — `div.crumbs` containing crumb tabs, then `div.inquiryPanel[rel]` content panels. First panel has `class="inquiryPanel showing"` and first crumb has `class="showing"`.

**Module menu:** Two-column layout. Left column: `<h4><span>Understand / Know / Do</span></h4>` headings. Right column: `<h5>Learning intentions</h5>` + `<h5>How will I know if I've learned it?</h5>`.

**Footer:** `footer-nav inquiry-nav` with prev + next + home.

**⚠️ Known quirks:**
- SSWHA has no menu button in header
- TWHA902–904 use `choicePage` activity grids and dual titles + `whakatauki` — these are content patterns, safe to use if the new module needs them
- BLL110 uses `super-content-button` inside inquiry panels

### 3.5 Combo (Standalone) — Expected Structure

**Body class:** `container-fluid` (no `fundamentals` or `inquiry` modifier).

Structurally identical to a Standard Lesson but uses `template="combo"`. No phase or crumb navigation. Content flows as sequential rows.

**⚠️ Known quirks:**
- XGF9003 has no menu button and no module menu — check if intentional
- XDLS9004 has `learningSupport` on `<html>`, `choicePage` grid, `supervisor` row, `iconCentral`
- XLP05 lacks `learningSupport` despite being a learning support module

---

## 4. KNOWN PITFALLS IN REFERENCE FILES

When analyzing uploaded reference files, watch for these issues. Do NOT carry them into new modules unless the user explicitly confirms they are intentional.

### 4.1 Dev Domain URLs

Some existing files use the **dev** domain for `idoc_scripts.js`:
```
tekuradev.desire2learn.com/shared/refresh_template/js/idoc_scripts.js
```

**Production domain:**
```
tekura.desire2learn.com/shared/refresh_template/js/idoc_scripts.js
```

**Known dev-domain files:** ARFUN01–05, ENGC101, ENGC201, MXFL204, HPFUN101, HPFUN201, HPFUN902, TEFUN01, OSAI101, OSAI301, OSBY101.

**Action:** If reference files use `tekuradev`, flag it to the user. Default to using whichever domain the reference files use (per Mode B rules: preserve exact script URLs from reference), but note it in the verification summary.

### 4.2 Missing or Malformed Structural Elements

These have been observed in existing files:
- **Missing `<body>` tag:** MXFU401, XTAS101 — causes rendering issues
- **stickyNav.js pointing to wrong module path:** MXEX302 has absolute URL pointing to MXEX301 path
- **stickyNav.js commented out:** Various files — check whether it should be active for the new module
- **CSS links commented out (Legacy):** Several Legacy files have `css/css.css` commented out — this is handled by `script.js` injecting styles dynamically
- **`level="1-3"` on `<html>` instead of `template`:** XTAS101, XTAS102 — use `level` attribute with a template value; non-standard

**Action:** Never carry missing `<body>` tags or malformed paths into new modules. If the reference has these issues, fix them silently in the output.

> **⚠️ THE OPENING `<body class="…">` TAG IS MANDATORY IN THE OUTPUT — constraint 82.** The rule
> above is about not *inheriting* the defect; this is about not *producing* it. A generated page
> whose `</head>` runs straight into `<div id="header">` has been observed in delivered modules,
> and it is a **hard fault**, not a cosmetic one: the browser opens an implicit `<body>` with **no
> class**, so every rule that hangs off `container-fluid` / `fundamentals` / `inquiry` /
> `reoTranslate` silently stops applying and the page renders wrongly while the source still looks
> plausible. Emit the tag on **every** whole-page build, with the class **derived** from the
> sub-type (Quick Identifier Table above; Document Shell in §6). Where the sub-type cannot be
> resolved, emit the Standard `container-fluid` default **plus** a visible
> `Designer/Developer To Do:` note — never a class-less `<body>`, and never none.
> *(Fragments are out of scope by design: Interactives Build Mode sections and Split Mode section
> files carry no shell — constraint 78 / `13_SPLIT_MODE.md`.)*

### 4.3 Non-Standard Module Menu Heading Levels

The project's documented standard (see `01_PIPELINE_EXTRACTION_TAGS.md`, Section 01) specifies: **lesson pages** — plain `<h5>` labels; **overview (`-00`) tabbed menus** — the canonical heading table (constraint 67: `<h4><span>` for the Overview/Knowledge/Practices titles; `<h5>` no-span for the We-are-learning:/I-can: labels and all Information/Standards headings). The overview menu's TAB SET is also canonical and content-driven — never copied from a reference's own tab selection. However, existing reference files use various non-standard patterns:

| Pattern | Files | Standard? |
|---------|-------|-----------|
| `<h5>We are learning:</h5>` | Most standard lessons | Common but differs from documented `<h4>` standard |
| `<h3><span>We are learning:</span></h3>` | ENGI302, ENGI401 | Non-standard |
| `<h4>Lesson Overview</h4>` + `<p><b>` | OSAI, OSBY files | Non-standard |
| `<p>We are learning:</p>` (no heading) | XMES, XTAS files | Non-standard |

**Action:** For new modules, ALWAYS follow the documented project standard: `<h5>` labels on lesson pages (per the table above), `<h4>` headings on overview pages. Do NOT replicate non-standard heading patterns from reference files even if the user does not explicitly request standardisation. Always note in the verification summary which heading pattern was used and why.

### 4.4 `learningSupport` Modifier

This is a CSS class on `<html>`, not a separate template sub-type. It can appear on any sub-type. Currently observed on:
- XFUN01_00 (fundamentals)
- XDLS9004_03_0 (combo)
- XWHA01-02 (standard 1-3, but also has `inquiry-nav` on footer)

**Action:** If the new module is a learning support module, add `learningSupport` to the `<html>` class list. The reference files should indicate whether this is needed. **The LS module-series carries `learningSupport` as standard** — for LS look-and-feel and structural conventions (larger font, terminology/brackets, no tab navs, clickDrop activity layout, speech-bubble prompts, the 6-activity pattern, XLP unique overviews) see `14_SUBJECT_GLOBAL_PARAMETERS.md` §14.6.

---

## 5. VALIDATION CHECKLIST — Mode B Reference Files

Run this checklist when analyzing uploaded reference files, BEFORE starting the conversion:

### Detection
- [ ] **Template system:** Legacy or Refresh? If Legacy, confirm with user.
- [ ] **Sub-type:** Standard / Bilingual / Fundamentals / Inquiry / Combo?
- [ ] **Template level:** Does `template="..."` match the expected year level for the new module code? The value is **derived from the new module's code**, never mirrored from the sibling files (constraint 21). Series-scoped corrections:
  - **BLL series — level split by sub-series (designer-corrected 14 July 2026, CL-0035).** Derive the value from the module code's sub-series:
    - **BLL2xx → phase 1 → `template="1-3"`.** Any module whose code begins with the literal prefix **`BLL2`** (BLL253, BLL261, BLL262, BLL263, BLL266, …) is **phase 1** and ships `template="1-3"` on every page. A standing, designer-directed exception that **supersedes, for the BLL2xx sub-series, the 13 July BLL262-report correction to `"4-6"`** (CL-0031, now `Reverted`); it re-settles BLL263 Difference 1 as `"1-3"`, and BLL266's shipped `"1-3"` was correct all along.
    - **All other BLL codes → Years 4–6 → `template="4-6"`** (the series default).
    - **BLLR is NOT BLL2.** BLLR2xx modules are **phase 2 → `template="4-6"`**. A `BLLR…` code never matches the `BLL2` prefix — its fourth character is `R`, not `2` — so the phase-1 exception never applies to BLLR (see `14` §14.9). Beware sloppy pattern tests (`BLL` plus "contains a 2") that would wrongly catch BLLR codes; the test is the literal four-character prefix `BLL2`.
    - Mirroring a sibling's `template=` value remains prohibited (constraint 21) even where the sibling's value happens to coincide — the value comes from this code→phase mapping only. (Cross-referenced from `14_SUBJECT_GLOBAL_PARAMETERS.md` §14.7.)
  - **Languages Phase 1–4 — all combo.** Every Languages-cohort module ships `template="combo"` (the sub-type — Fundamentals / Inquiry / standalone Combo — then comes from the `<body>` class per §2 above), so the expected value for this cohort is `combo`, not a year-band value. See `14_SUBJECT_GLOBAL_PARAMETERS.md` §14.1.
- [ ] **Cross-cutting modifiers:** `learningSupport` on `<html>`? `reoTranslate` on `<body>`?

### Structural Integrity
- [ ] **`<body>` tag present in the REFERENCE?** (MXFU401 and XTAS101 are known to be missing it — never inherit the omission)
- [ ] **`<body class="…">` present in MY OUTPUT, with the correct derived class?** (constraint 82 — `</head>` must never be followed straight by `<div id="header">`)
- [ ] **Script domain:** `tekura` (prod) or `tekuradev` (dev)? Flag if dev.
- [ ] **`stickyNav.js`:** Present, commented out, or absent? If present, does the path reference the correct module?
- [ ] **Module menu heading levels:** Standard (canonical `-00` heading table / lesson-page `<h5>` labels — see `01` Module Menu Structures) or variant? Note which. The `-00` tab set for the NEW module always follows the canonical set (constraint 67) regardless of the reference's tab selection.
- [ ] **Footer class:** Matches expected sub-type pattern?

### Content Patterns to Catalogue
- [ ] **Navigation system:** Phases, crumbs, or none?
- [ ] **Title pattern:** Single or dual `<h1>`?
- [ ] **Activity wrappers:** What modifier classes are used? (`interactive`, `dropbox`, etc.)
- [ ] **Components observed:** Speech bubbles, flip cards, carousel, choice page, etc.?
- [ ] **Acknowledgements:** Accordion style, flat style, or absent? Where positioned?

### Output Decisions
- [ ] **What to replicate:** Skeleton structure, grid patterns, script URLs, footer pattern
- [ ] **What to fix:** Missing `<body>`, malformed paths, dev domain (if flagged)
- [ ] **What to standardise:** Module menu headings (use project standard unless told otherwise)
- [ ] **What to adapt:** Page count, titles, module code, content

---

## 6. ELEMENT REFERENCE — Refresh Baseline

These are the standard structural patterns consistent across ALL Refresh files. Use this as the ground truth when a reference file deviates.

### Document Shell
```html
<!doctype html>
<html lang="en" level="" template="..." class="notranslate" translate="no">
<head>
  <meta charset="utf-8" />
  <meta content="IE=edge" http-equiv="X-UA-Compatible" />
  <meta content="width=device-width, initial-scale=1" name="viewport" />
  <title>...</title>
  <script type="text/javascript" src="https://tekura.desire2learn.com/shared/refresh_template/js/idoc_scripts.js"></script>
</head>
<body class="container-fluid">
  <div id="header">...</div>
  <div id="body">...</div>
  <div id="footer">...</div>
</body>
</html>
```

### Standard Content Column
```html
<div class="row">
  <div class="col-md-8 col-12">
    <!-- content here -->
  </div>
</div>
```

### Content with Sidebar
```html
<div class="row">
  <div class="col-md-8 col-12"><!-- main --></div>
  <div class="col-md-4 col-12">
    <div class="alert top"><p>Sidebar note</p></div>
  </div>
</div>
```

### Activity Block
```html
<div class="activity" number="1A">
  <div class="row">
    <div class="col-12">
      <h3>Activity title</h3>
      <p>Instructions...</p>
    </div>
  </div>
</div>
```

### Images
```html
<img class="img-fluid" src="images/..." alt="Description">
```

### Buttons
```html
<a href="..." target="_blank">
  <div class="button">Button text</div>
</a>
```

### Video
```html
<div class="videoSection ratio ratio-16x9">
  <iframe src="..." frameborder="0" allowfullscreen></iframe>
</div>
```

### Audio
```html
<audio preload="none" class="audioPlayer" title="...">
  <source src="..." type="audio/mpeg">
</audio>
```

### Footer
```html
<div id="footer">
  <ul class="footer-nav">
    <li><a href="" id="prev-lesson" target="_self"></a></li>
    <li><a href="" id="next-lesson" target="_self"></a></li>
    <li><a href="" class="home-nav" target="_parent"></a></li>
  </ul>
</div>
```

### Text Elements
- **Section heading:** `<h3>Title</h3>` (bare)
- **Sub-heading:** `<h4>Subtitle</h4>` (bare)
- **Paragraph:** `<p>Text</p>` (no class)
- **Lists:** `<ul>` / `<ol>` (no class)
- **Bold:** `<b>Text</b>`
- **Image caption:** `<p class="captionText">Caption text</p>`

### Tables
```html
<div class="table-responsive">
  <table class="table noHover tableFixed">
    <tr><th>Header</th></tr>
    <tr><td>Data</td></tr>
  </table>
</div>
```

### Utility Classes
| Class | Purpose |
|-------|---------|
| `paddingR` | Right padding on column div |
| `paddingL` | Left padding on column div |
| `paddingLR` | Left + right padding |
| `margB0` | Zero bottom margin |
| `margB2` | Small bottom margin |
| `margB3` | Medium bottom margin |
| `marg0` | Zero margin (used on lists) |
| `noBorder` | Remove border (on `clickDropContent`) |