> **Last updated:** Wednesday, 1st July, 2026 12:39 AM

# 13 — Split Mode (Mode 5)

> **When to load:** Whenever a message contains the trigger phrase **`SPLIT MODE`** (case-insensitive), and whenever the conversion pipeline identifies a **single-page** module and you are deciding whether to offer Split Mode. This is **Mode 5 — Split** (see `00_MASTER_INSTRUCTIONS.md` → Operating Modes). Together with `COMPARISON MODE` and `UPDATE MODE`, the `SPLIT MODE` trigger takes precedence over the ordinary Conversion / Advisory / Support mode signals.

---

## PURPOSE — what Split Mode is, and the problem it solves

Most modules are built as **one single-page HTML file**: the whole module lives in one `#body`, and each lesson is delimited by its own `<!-- 1 -->`, `<!-- 2 -->`, … HTML comment (a structural delimiter, **not** a page break). When such a module is **very long**, generating the entire page in a single pass can exceed one response and the conversion **truncates or aborts**.

**Split Mode** lets the converter emit that long single-page module **in pieces** — a small **base homepage** plus **one section file per lesson** — so each generation stays within limits. The pieces are emitted **one file per response** (the first response returns the base; each subsequent designer prompt returns the next single section, in order), and each file carries highly detailed **`PAGEFORGE-GUIDE`** comment blocks so a developer can also stitch the pieces together **by hand**. PageForge's **Page Stitcher** then recombines the pieces into **one single-page file that is byte-identical to a normally-built single-page module**. The split is a **generation-time convenience only**; it must leave **no trace** in the final stitched output.

Split Mode is a **packaging variant of Conversion Mode (Mode 1)**, not a separate kind of conversion. It runs the **entire Conversion Pipeline unchanged** — same content fidelity, same skeleton derivation from the structural reference, same tag mapping, same component rules, same red flags for ambiguities, same image-mode prompt, same acknowledgements placement, same captured-reviewer-comment rendering (`02_DATA_CONTENT_VERIFICATION.md` → Captured Reviewer Comments). **Split Mode changes only how the output is packaged, not what it contains.**

---

## 1. SPLIT MODE ≠ THE PAGE BOUNDARY SYSTEM (read first)

This is the single most important distinction in this file. **Do not conflate the two systems.**

| | **Page Boundary System** (`01` Section 03) | **Split Mode** (this file) |
|---|---|---|
| Applies to | **Multi-page** modules — delimited by `[LESSON]` / `[End page]` | **Single-page** modules — too long to emit in one pass |
| Produces | **Separate** lesson *pages* (`-00.html`, `-01.html`, …) | A **base homepage** + per-lesson **section files**, stitched back into **one** page |
| Final result | Several distinct pages | **One** single-page file, byte-identical to a one-pass build |
| Lesson delimiter | A genuine page break | The lesson's own `<!-- N -->` comment carried inside `#body` |

- A genuinely **multi-page** module (`[LESSON]` / `[End page]` boundaries present) uses the **Page Boundary System** and is **never** split.
- A **single-page** module is **never** broken into separate `-NN` pages — if it is too long, it is **Split Mode**.

---

## 2. PROACTIVE SINGLE-PAGE IDENTIFICATION + OFFERING SPLIT MODE

The converter already determines page structure during triage/extraction (Phase 3 — see `01_PIPELINE_EXTRACTION_TAGS.md` → Multi-Page vs Single-Page Modules). Split Mode adds a proactive offer:

- When the converter determines a module is **single-page** — i.e. it has **no** `[LESSON]` / `[End page]` page boundaries, or it is a module type that ships as one page — **say so**, and **proactively offer Split Mode** as an option the user may invoke, explaining in one line what it does: *emit the page in stitchable pieces that PageForge's Page Stitcher recombines into one file.*
- Make the offer **especially prominent when the single-page output is large** (many lessons / heavy interactive content) and therefore at real risk of exceeding one response.
- The suggestion is an **offer, not an automatic action.** Split Mode runs **only** when the user explicitly invokes `SPLIT MODE` (Section 3). If the user does nothing, continue producing the normal single-page file in one pass.

The intent: a user who asks for a single-page module is told, up front, *"this is a single-page module; if it's too long to build in one go, you can run `SPLIT MODE` and stitch it back together in PageForge."*

---

## 3. TRIGGER, TRIAGE & APPLICABILITY

- **Trigger phrase:** `SPLIT MODE` — an explicit, user-invoked precedence mode, in the same family as `COMPARISON MODE` and `UPDATE MODE`.
- **Applicability:** **only** for a **single-page** module whose full output is too long to emit in one pass. If the module is genuinely multi-page (`[LESSON]` / `[End page]`), use the **Page Boundary System** instead — **do not** split.
- **All other conversion rules are unchanged** while in Split Mode: never modify writer text, never invent structure, never render `[tags]` as visible text, raise visible red flags for ambiguities, render captured reviewer comments as visible red designer messages, omit `stickyNav` (see Section 9), prompt for image mode, place acknowledgements at the bottom of the base, etc. Split Mode changes only **how the output is packaged**, not what it contains.

---

## 4. OUTPUT #1 — THE BASE HOMEPAGE (`<CODE>-base.html`)

The base is the **complete single-page scaffold**, exactly as a normal single-page module, **except** that `#body` contains **only an ordered list of splice markers — one per lesson/section — and no lesson content.**

```html
<!DOCTYPE html>
<html lang="en" template="<phase>" class="notranslate" translate="no">
<head>
    <meta charset="utf-8">
    <meta content="IE=edge" http-equiv="X-UA-Compatible">
    <meta content="width=device-width, initial-scale=1" name="viewport">
    <title><CODE></title>
    <script type="text/javascript" src="https://tekura.desire2learn.com/shared/refresh_template/js/idoc_scripts.js"></script>
</head>
<body class="<body-class>">
    <div id="header"> … module-code, title h1(s), menu button, full #module-menu-content … </div>
    <!-- colourlevel="<phase>" -->
    <div id="body">
        <!-- PAGEFORGE-GUIDE-START -->
        <!-- SPLICE POINT 1 — id="intro". Replace the marker below with the slot content from
             <CODE>-lesson-intro.html (between its PAGEFORGE-SECTION markers). First slot in #body. -->
        <!-- PAGEFORGE-GUIDE-END -->
        <!-- PAGEFORGE-SPLICE id="intro" -->
        <!-- PAGEFORGE-GUIDE-START -->
        <!-- SPLICE POINT 2 — id="01". Replace the marker below with the slot content from
             <CODE>-lesson-01.html. -->
        <!-- PAGEFORGE-GUIDE-END -->
        <!-- PAGEFORGE-SPLICE id="01" -->
        <!-- …one PAGEFORGE-GUIDE block + PAGEFORGE-SPLICE marker per remaining slot, in order… -->
        <!-- PAGEFORGE-SPLICE id="02" -->
        <!-- PAGEFORGE-SPLICE id="03" -->
    </div>
    <div id="footer"> … footer nav … </div>
    <div class="row"><div class="col-md-8 col-12"><div class="acks"> … Acknowledgements … </div></div></div>
</body>
</html>
```

**Rules for the base:**

- The **header, menu, footer, and acknowledgements are fully built** in the base. They are short and shared, so they are produced once, here — not split. Build them by the normal scaffold rules (`01_PIPELINE_EXTRACTION_TAGS.md` for head/header/menu/footer; `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` → Acknowledgements for the acks block, which stays at the bottom of the page exactly as in a one-pass build).
- `#body` holds **only** the `PAGEFORGE-SPLICE` markers (each preceded by its `PAGEFORGE-GUIDE` block — see below), **in the exact order the lessons must appear** in the finished page — and **no lesson content**.
- There is **one splice marker per lesson/section** that the module contains.
- **Place a `PAGEFORGE-GUIDE` block at every splice point** naming which section file fills it and in what order (Section 5B). These blocks are machine-stripped by the Page Stitcher.
- **Do not emit `stickyNav`** anywhere in the base (Section 9).
- All scaffold attributes (`<html template>`, `<body class>`, the `colourlevel` comment, `level`, etc.) are produced **exactly** as for a normal single-page build — the stitched output inherits them verbatim from the base.

> The `<phase>`, `<body-class>`, `<CODE>`, and `idoc_scripts.js` URL are resolved exactly as in a normal conversion (from the structural reference and content source) — the template above shows placeholders only.

---

## 5. OUTPUT #2 — ONE SECTION FILE PER SLOT (`<CODE>-lesson-<id>.html`)

Each section file carries the **raw `#body` content for exactly one slot**, wrapped in section markers. The content between the markers is **exactly what belongs inside `#body`** for that one lesson — **including that lesson's own `<!-- N -->` comment** — at the normal indentation:

```html
<!-- PAGEFORGE-GUIDE-START -->
<!-- MANUAL STITCH — this file fills SPLICE POINT id="01" in <CODE>-base.html.
     Copy everything between the PAGEFORGE-SECTION markers below (NOT the markers themselves) and
     paste it in place of the matching <!-- PAGEFORGE-SPLICE id="01" --> marker in the base #body.
     Keep the <!-- 1 --> lesson delimiter as the first line of the pasted content. -->
<!-- PAGEFORGE-GUIDE-END -->
<!-- PAGEFORGE-SECTION id="01" -->
<!-- 1 -->
<div class="row"> … lesson 1 content … </div>
<div class="activity"> … </div>
<!-- /PAGEFORGE-SECTION -->
```

The `PAGEFORGE-GUIDE` block sits **outside** the `PAGEFORGE-SECTION` markers (immediately before the opening marker) so that copying just the slot content does not carry the guidance along (Section 5B).

**Rules for a section file:**

- The `id` on the section **must match** a `PAGEFORGE-SPLICE id` in the base.
- Put **only** that slot's `#body` content between the markers — **no** `<html>`, `<head>`, `<body>`, `#header`, or `#footer`.
- Include the lesson's `<!-- N -->` delimiter comment as the **first line** of the slot content (this is what makes the stitched `#body` identical to a one-pass build).
- **One file per slot.** Every base slot needs exactly one section file, and every section file must correspond to a base slot.
- **Place a `PAGEFORGE-GUIDE` block outside the `PAGEFORGE-SECTION` markers** (immediately before the opening marker) naming the base splice point this section fills (Section 5B). It is machine-stripped by the Page Stitcher.
- The section content is the writer's converted HTML, produced by the normal conversion rules, **unchanged**.

---

## 5A. EMISSION CADENCE — ONE FILE PER RESPONSE

Split Mode emits **exactly one HTML file per response** — never more than one file in a single turn.

- **First response:** the **base** file (`<CODE>-base.html`) **only**. Nothing else — no section files alongside it.
- **Each subsequent response** (on the designer's next prompt): the **next single section file**, one at a time, **in slot order** (`intro`, then `01`, `02`, …).
- **Never emit more than one file in a single turn**, and never jump ahead or batch several sections together.

**Worked cadence** — a single-page module with four embedded lessons:

| Turn | Designer prompt | File emitted |
| --- | --- | --- |
| 1 | invoke `SPLIT MODE` | `<CODE>-base.html` |
| 2 | next prompt | `<CODE>-lesson-01.html` |
| 3 | next prompt | `<CODE>-lesson-02.html` |
| 4 | next prompt | `<CODE>-lesson-03.html` |
| 5 | next prompt | `<CODE>-lesson-04.html` |

Each section file still contains **only** the exact `#body` content for that one slot (wrapped in its section markers, with the lesson's `<!-- N -->` delimiter first), exactly as Section 5 requires — and nothing else. The cadence changes **only** how many files are emitted per turn; it does **not** change what any file contains, the marker contract, the ids, or the round-trip guarantee.

> Why one-at-a-time: the whole reason Split Mode exists is that the full single-page output is too long to emit in one pass (Purpose). Emitting one file per response keeps every generation within limits and lets the designer pace the run.

---

## 5B. MANUAL-STITCH GUIDANCE BLOCKS (`PAGEFORGE-GUIDE`)

So a developer can assemble the files **by hand** (without PageForge's web app), the base and every section file carry **highly detailed manual-stitch guidance**, wrapped in a clearly delimited block:

```html
<!-- PAGEFORGE-GUIDE-START -->
<!-- …highly detailed manual-stitch instructions… -->
<!-- PAGEFORGE-GUIDE-END -->
```

**In the base file** — place a `PAGEFORGE-GUIDE` block **at each splice point**, telling the developer which section file fills that splice point and in what order:

```html
<div id="body">
    <!-- PAGEFORGE-GUIDE-START -->
    <!-- SPLICE POINT 1 of 2 — id="01".
         Replace the PAGEFORGE-SPLICE marker immediately below with the slot content from
         DEMO101-lesson-01.html (the HTML between that file's PAGEFORGE-SECTION markers,
         excluding the markers themselves). This is the FIRST lesson in #body. -->
    <!-- PAGEFORGE-GUIDE-END -->
    <!-- PAGEFORGE-SPLICE id="01" -->
    <!-- PAGEFORGE-GUIDE-START -->
    <!-- SPLICE POINT 2 of 2 — id="02".
         Replace the PAGEFORGE-SPLICE marker immediately below with the slot content from
         DEMO101-lesson-02.html. This is the SECOND lesson in #body. -->
    <!-- PAGEFORGE-GUIDE-END -->
    <!-- PAGEFORGE-SPLICE id="02" -->
</div>
```

**In each section file** — place a `PAGEFORGE-GUIDE` block **outside** the `PAGEFORGE-SECTION` content markers (so a manual copy of just the slot content does **not** drag the guidance along), naming the base splice point this section fills:

```html
<!-- PAGEFORGE-GUIDE-START -->
<!-- MANUAL STITCH — this file fills SPLICE POINT id="01" in DEMO101-base.html.
     Copy everything between the PAGEFORGE-SECTION markers below (NOT the markers) and paste it
     in place of the matching <!-- PAGEFORGE-SPLICE id="01" --> marker in the base #body.
     Keep the <!-- 1 --> lesson delimiter as the first line of the pasted content. -->
<!-- PAGEFORGE-GUIDE-END -->
<!-- PAGEFORGE-SECTION id="01" -->
<!-- 1 -->
<div class="row"> … lesson 1 content … </div>
<!-- /PAGEFORGE-SECTION -->
```

**Rules for guide blocks:**

- The guidance must be **very clear and highly detailed** — which splice point each section replaces, the order the sections go in, and where each section's insertable content begins and ends.
- In the base, a guide block sits at **every** splice point. In a section file, the guide block sits **outside** the `PAGEFORGE-SECTION` markers (ideally immediately before the opening section marker).
- Guide blocks carry **no student content, no designer-action notes, and no interactive answers** — purely manual-stitch instructions for a human developer.
- **PageForge's Page Stitcher strips every `PAGEFORGE-GUIDE` block** during automated stitching, exactly as it strips the splice/section markers — so the finalised unified HTML contains **none** of these manual instructions. They exist purely to help a developer assembling the files by hand.
- `PAGEFORGE-GUIDE` blocks are a **permitted Split-Mode-only comment exception** (see `02_DATA_CONTENT_VERIFICATION.md` → Comment & Red Flag Policy → permitted comment exceptions, and `00` constraint 37) — machine-stripped, not a designer communication channel.

---

## 6. ID AND FILENAME CONVENTIONS

- **Id values:** use the lesson identity as the id — `intro` for the module-introduction section, then zero-padded lesson numbers `01`, `02`, … matching the `<!-- N -->` lesson comments.
- **Ids are case-insensitive and must be unique** within the module.
- **The marker id is authoritative; the filename is a human-readable convenience.** Name the base `<CODE>-base.html` and each section `<CODE>-lesson-<id>.html` (e.g. `BLL210-lesson-01.html`), but PageForge identifies the base by the presence of `PAGEFORGE-SPLICE` markers and matches sections by their `PAGEFORGE-SECTION id` — so the suffixes are an aid, not a requirement.

---

## 7. KEYWORD / MARKER REFERENCE (reproduce these EXACTLY)

The marker spelling, the `id="…"` attribute syntax, the `PAGEFORGE-SPLICE` / `PAGEFORGE-SECTION` / `/PAGEFORGE-SECTION` names, and the one-marker-per-lesson-in-order rule are all **load-bearing**. Any deviation (different casing, missing closing marker, mismatched id, extra `#body` wrapper in a section) breaks the stitch.

| Purpose | Exact token | Where it goes |
| --- | --- | --- |
| Base body slot (one per lesson, in order) | `<!-- PAGEFORGE-SPLICE id="X" -->` | Inside `<div id="body">` of `<CODE>-base.html`, nothing else in `#body` |
| Section start | `<!-- PAGEFORGE-SECTION id="X" -->` | First line of each section file |
| Section end | `<!-- /PAGEFORGE-SECTION -->` | Last line of each section file (the guide block, if any, sits before the section start) |
| Manual-stitch guide — open | `<!-- PAGEFORGE-GUIDE-START -->` | Base: before each `PAGEFORGE-SPLICE` marker. Section: before the `PAGEFORGE-SECTION` start marker |
| Manual-stitch guide — close | `<!-- PAGEFORGE-GUIDE-END -->` | Closes each `PAGEFORGE-GUIDE` block |
| Lesson delimiter (carried inside the section) | `<!-- N -->` (the lesson's own number) | First line of the section's slot content, between the section markers |
| Base filename (aid) | `<CODE>-base.html` | — |
| Section filename (aid) | `<CODE>-lesson-<id>.html` | — |
| Id values | `intro`, then `01`, `02`, … (case-insensitive, unique) | The `id="…"` of each splice/section marker |

> These splice/section markers **and the `PAGEFORGE-GUIDE` blocks** are a **permitted Split-Mode-only comment exception** (see `02_DATA_CONTENT_VERIFICATION.md` → Comment & Red Flag Policy → The permitted comment exceptions, and `00` constraint 37). They are machine tokens / manual-stitch instructions, not a designer communication channel, and they are all removed by the Page Stitcher before any human reads the final file.

---

## 8. THE ROUND-TRIP GUARANTEE (why the exactness matters)

Stitching the base + all section files must yield a single file whose `#body` is **the section contents concatenated in slot order** — **byte-for-byte** the same `#body` a one-pass single-page build would have produced (lessons delimited by their `<!-- N -->` comments). **No `PAGEFORGE-*` markers survive** in the stitched output — neither the `PAGEFORGE-SPLICE` / `PAGEFORGE-SECTION` markers **nor any `PAGEFORGE-GUIDE` manual-stitch block**. The header, menu, footer, acknowledgements, and all scaffold attributes come straight from the base, untouched. Split Mode is correct **only** if this holds; the marker contract exists precisely to make it hold.

---

## 9. HOW PAGEFORGE'S PAGE STITCHER CONSUMES THE OUTPUT (so the split is valid)

So you understand what must be true for a successful stitch, this is what PageForge does at the other end (single upload container; files auto-classified):

1. It reads the **base** (the file carrying `PAGEFORGE-SPLICE` markers, or named `<CODE>-base.html`) and collects every `<!-- PAGEFORGE-SPLICE id="X" -->` marker **in document order**.
2. For each other (section) file it determines an `id` and `content`, in this precedence: the text between `<!-- PAGEFORGE-SECTION id="X" -->` … `<!-- /PAGEFORGE-SECTION -->` (**authoritative**); else the inner HTML of a `#body` if the file is a full page; else the whole file, with the id taken from the `-lesson-NN` / `-NN` filename.
3. It **validates before emitting anything** (it never produces a broken file): every base slot has exactly one matching section; every section matches a base slot (no orphans/extras); no duplicate ids; at least one slot. Any mismatch is reported and nothing is downloaded.
4. It replaces each splice marker with its section's content, preserving order and leaving the surrounding scaffold untouched, and **strips every `PAGEFORGE-GUIDE` block** (in both the base and the section content) so none survive into the unified file.
5. It offers the unified `<CODE>.html` for download, plus a placement summary.

**Practical implications for the converter's Split Mode output:** ids must line up **one-to-one** between base and sections; **every lesson must have both** a base slot and a section file; **no id may repeat**; and **the base must contain at least one slot**. If you cannot produce a given section, still emit that section file with a **visible red flag inside it** rather than omitting the slot (an omitted slot fails validation; a red-flagged slot stitches and tells the designer what is missing).

### Carried-over hard rule on `stickyNav`

Do **not** emit the `stickyNav` script in the base or any section file. (This is a Split-Mode output requirement. Note: project-wide, `stickyNav.js` is treated as **non-universal** — see `01_PIPELINE_EXTRACTION_TAGS.md` → Template Head Sections and `00` constraint 22; in Split Mode it is omitted from the base/sections regardless.)

---

## 10. VALIDATION AND FAILURE HANDLING THE CONVERTER MUST HONOUR

- Emit **exactly one section file per base slot**, and one base slot per section — keep them in agreement.
- Emit **exactly one HTML file per response** — the base first, then one section file per subsequent designer prompt, in slot order; never more than one file in a single turn (Section 5A).
- **Never emit an empty slot.** If a lesson's content cannot be produced, emit the section file with a **visible red flag** (`<p style="color: red; font-weight: bold;">Red Flag: …</p>`) describing what is missing — visible content always wins over a silent gap.
- Keep **ids unique and consistent** between the base and the sections.
- Include the **`PAGEFORGE-GUIDE` blocks** — at every splice point in the base, and outside the section markers in each section file (Section 5B). They are machine-stripped by the Page Stitcher and must carry no student content or answers.
- Do **not** place `PAGEFORGE-*` markers anywhere except as specified (no stray markers in section content, none left in any human-facing place).
- The base must contain **at least one slot**.

---

## 11. HARD RULES CARRIED OVER FROM THE CONVERTER'S CONSTRAINTS

- **Content fidelity** — section content is the writer's converted HTML, unchanged (`00` constraint 1).
- **No invented structure** — the base scaffold and the section content are produced by the normal conversion rules; Split Mode only changes *packaging* (`00` constraints 2–3).
- **Visible content always wins** — a missing section becomes a red flag in that section file, never an empty slot (Core Philosophy).
- **Captured reviewer-comment rendering still applies** inside section content — a reviewer comment led by `Note from {author}:` renders as a visible red **and bold** designer message, in position (`02` → Captured Reviewer Comments; `00` constraint 57).
- **No `stickyNav`** in the base or any section (Section 9).
- The splice/section markers **and the `PAGEFORGE-GUIDE` manual-stitch blocks** are the **only** comments Split Mode adds, and they are a permitted, machine-consumed exception (`00` constraint 37; `02` → permitted comment exceptions).
- **One file per response** — base first, then one section per prompt, in order (Section 5A).

---

## 12. WORKED MINI-EXAMPLE

**Base — `DEMO101-base.html`:**

```html
<div id="body">
    <!-- PAGEFORGE-GUIDE-START -->
    <!-- SPLICE POINT 1 of 2 — id="01". Replace the marker below with the slot content from
         DEMO101-lesson-01.html (between its PAGEFORGE-SECTION markers). First lesson. -->
    <!-- PAGEFORGE-GUIDE-END -->
    <!-- PAGEFORGE-SPLICE id="01" -->
    <!-- PAGEFORGE-GUIDE-START -->
    <!-- SPLICE POINT 2 of 2 — id="02". Replace the marker below with the slot content from
         DEMO101-lesson-02.html. Second lesson. -->
    <!-- PAGEFORGE-GUIDE-END -->
    <!-- PAGEFORGE-SPLICE id="02" -->
</div>
```

**`DEMO101-lesson-01.html`:**

```html
<!-- PAGEFORGE-GUIDE-START -->
<!-- MANUAL STITCH — this file fills SPLICE POINT id="01" in DEMO101-base.html. Copy everything
     between the PAGEFORGE-SECTION markers below (not the markers) in place of the matching
     <!-- PAGEFORGE-SPLICE id="01" --> marker. Keep <!-- 1 --> as the first line. -->
<!-- PAGEFORGE-GUIDE-END -->
<!-- PAGEFORGE-SECTION id="01" -->
<!-- 1 -->
<div class="row"><p>Lesson one.</p></div>
<!-- /PAGEFORGE-SECTION -->
```

**`DEMO101-lesson-02.html`:** likewise for lesson two (`id="02"`, `<!-- 2 -->`), with its own guide block naming splice point `id="02"`.

> Emitted across responses: turn 1 → `DEMO101-base.html`; turn 2 → `DEMO101-lesson-01.html`; turn 3 → `DEMO101-lesson-02.html` (Section 5A).

**Stitched `#body` (what PageForge produces):**

```html
<div id="body">
    <!-- 1 -->
<div class="row"><p>Lesson one.</p></div>
    <!-- 2 -->
<div class="row"><p>Lesson two.</p></div>
</div>
```

> The Page Stitcher strips both the `PAGEFORGE-SPLICE`/`PAGEFORGE-SECTION` markers **and** every `PAGEFORGE-GUIDE` block, so the unified `#body` is byte-identical to a one-pass build.

---

## 13. ACCEPTANCE CRITERIA

- On a single-page module, the converter proactively identifies it as single-page and offers Split Mode (with a one-line explanation), more prominently when the output is large.
- When the user invokes `SPLIT MODE`, the converter emits one `<CODE>-base.html` (full scaffold; `#body` = ordered `PAGEFORGE-SPLICE` markers, each preceded by a `PAGEFORGE-GUIDE` block; no `stickyNav`) and one `<CODE>-lesson-<id>.html` per slot (a `PAGEFORGE-GUIDE` block outside the section markers, then section-marker-wrapped raw `#body` content including the `<!-- N -->` comment; nothing else).
- Files are emitted **one per response** — the base first, then one section file per subsequent prompt, in slot order; never more than one file in a single turn.
- Ids line up one-to-one between base and sections; none repeat; there is at least one slot.
- Dropping all emitted files into PageForge's Page Stitcher validates cleanly and produces a `<CODE>.html` whose `#body` equals a one-pass single-page build, with no `PAGEFORGE-*` markers remaining (splice/section markers and `PAGEFORGE-GUIDE` blocks all stripped).
- A multi-page module is **not** split — it continues to use the Page Boundary System.

---

## 14. WHAT SPLIT MODE DOES NOT DO

- It does **not** change what the module contains — only how the single-page output is packaged.
- It does **not** apply to multi-page modules (`[LESSON]` / `[End page]`) — those use the Page Boundary System.
- It does **not** run automatically — it runs only when the user explicitly invokes `SPLIT MODE`.
- It does **not** emit more than one file per response — the base comes first, then one section file per subsequent prompt, in order.
- It does **not** modify writer content, invent structure, or relax any conversion constraint.
- It does **not** leave `PAGEFORGE-*` markers — splice/section markers or `PAGEFORGE-GUIDE` manual-stitch blocks — in any human-facing final file; they exist only in the intermediate split files and are removed by the Page Stitcher.
- The `PAGEFORGE-GUIDE` blocks do **not** carry student content, designer-action notes, or interactive answers — only manual-stitch instructions for a developer assembling the files by hand.

---

## 15. RELATIONSHIP TO THE OTHER MODES

- **Conversion Mode (Mode 1)** is the parent: Split Mode runs the full Conversion Pipeline and differs only in packaging. The single-page identification + offer lives in the conversion pipeline's page-structure step (`00` → Conversion Pipeline → Phase 3; `01` Section 03).
- **Comparison / Update Modes (Modes 3–4)** are unrelated processes (refinement capture and project-file maintenance) and are not invoked by Split Mode.
- **The Page Boundary System** is the multi-page counterpart Split Mode must never be confused with (Section 1).
