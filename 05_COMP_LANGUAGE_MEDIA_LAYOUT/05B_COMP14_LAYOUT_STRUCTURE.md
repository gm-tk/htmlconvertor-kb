> **Last updated:** Friday, 21st August, 2026
> **Granular part B (2 of 4) of `05_COMP_LANGUAGE_MEDIA_LAYOUT.md`** — COMP_14 Layout & Structure, first half: Activities and Alerts. Buttons onward (Buttons, Supervisor Button, Tables, Columns, Quote/Whakatauki/Rhetorical) live in `05D`.
> All sibling parts live in `05_COMP_LANGUAGE_MEDIA_LAYOUT/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# COMP_14 — Layout & Structure

---

## Activities

```html
<!-- Standard activity (triangle icon) -->
<div class="activity" number="1A">
    <div class="row"><div class="col-12">
        <h3>Activity heading</h3>
        <p>Instructions</p>
    </div></div>
</div>

<!-- Interactive activity (circle icon) — DEFAULT wrapper width: ONE inner row, col-12 (constraint 63) -->
<div class="activity interactive" number="1B">
    <div class="row"><div class="col-12">
        <h3>Activity heading</h3>
        <p>Intro / instructions</p>
        <!-- Interactive component here, in the same column -->
    </div></div>
</div>

<!-- Dropbox activity (square orange icon) -->
<div class="activity alertPadding dropbox" number="1C">
    <div class="row"><div class="col-12">
        <h3>Activity heading</h3>
        <p>Upload instructions</p>
    </div></div>
</div>

<!-- Standard text activity -->
<div class="activity alertPadding" number="1D">
    <div class="row"><div class="col-12">
        <h3>Activity heading</h3>
    </div></div>
</div>
```

**Dropbox trigger condition — ALL modules except BLL.** Add the `dropbox` modifier class to **any** activity that ends in an **Upload to dropbox** button (equivalently, whose writer source carries `[trigger engagement]` / a "Go to dropbox" or "Upload to dropbox" button). This applies to **every module series except the BLL series**. **BLL carve-out:** BLL activities add the dropbox **button** but do **not** append the `dropbox` modifier to the `.activity` wrapper (see `14_SUBJECT_GLOBAL_PARAMETERS.md` §14.7 / `00` constraint 43). For every non-BLL series, keep the activity's existing classes and append `dropbox`:
- An activity with no interactive that ends in an upload → `<div class="activity dropbox" number="ID">`.
- An activity that contains an interactive AND ends in an upload → `<div class="activity interactive dropbox" number="ID">`.

Do not force `alertPadding` onto a dropbox activity — follow the activity's own class set and simply append `dropbox`. The "square orange dropbox icon" example above (`activity alertPadding dropbox`) keeps `alertPadding` only because that specific source activity already carried it.

**One interactive per activity (constraint 62).** Each activity wrapper holds **at most one interactive component**. When a writer's single activity heading carries two or more interactives, split them into separate sequential activities and renumber the following activities, flagging the split with a visible `Red Flag:` note — full rule in `03_COMP_CORE_INTERACTIVES.md` → COMP_00 (Universal Rules).

**MTK quiz activities (constraint 65).** An `[MTKquiz]` tag (with any modifiers, e.g. `[engage]`, `[type the answer]`, `[Teacher marked …]`) builds its **own activity box, carrying the next consecutive activity number even where the writer assigned none**, holding only these children in order — quiz title `<h3>` (default `Quiz`), the writer's quiz instructions where supplied, a `Designer/Developer To Do:` note, and a **"Go to quiz" button** — and **never the quiz's own questions or answers**. See Buttons → MTK Quiz in `05D` for the full shell. Because the activity does not end in a dropbox button, the `dropbox` wrapper modifier of constraint 43 does **not** attach.

**The inner text column is `col-12`, and the split is conditional on the wrapper's width (constraint 63).** Two linked rules, both inside the activity wrapper:

**1. The inner text column is `col-12` — never `col-md-8 col-12`.** The wrapper already sets the reading width; an inner `col-md-8` narrows the prose a second time.

**2. At the DEFAULT wrapper width, text and interactive share ONE inner row.** There is no width difference to express, so there is nothing to split:

```html
<div class="activity interactive" number="1A">
    <div class="row">
        <div class="col-12">
            <h3>Which scam is it?</h3>
            <p>Match the example to the correct scam type.</p>
            <div class="dragAndDrop" layout="standard">
                ...
            </div>
        </div>
    </div>
</div>
```

**The two-row split is retained ONLY where the wrapper is widened** (`col-12` Standard / `col-md-11 col-12` Inquiry & Fundamentals / `col-md-12 col-12` full width — constraint 56). There the text sits in its own inner `row` > `col-12` and the interactive follows in a **separate** inner `row` at the wrapper's own width:

```html
<div class="row">
    <div class="col-12"><!-- widened activity wrapper (Standard) -->
        <div class="activity interactive" number="3C">
            <div class="row">
                <div class="col-12">
                    <h3>Activity heading</h3>
                    <p>Instructions</p>
                </div>
            </div>
            <div class="row">
                <div class="col-12"><!-- interactive spans the widened width -->
                    <!-- wide interactive component here -->
                </div>
            </div>
        </div>
    </div>
</div>
```

A **text-only** activity (no interactive) needs no split at either width — its single `row` > `col-12` carries the heading and prose. **This supersedes the former "always separate rows, prose stays at `col-md-8`" rule** (`CL-0036` → `CL-0048`, corrected by `CL-0077`). See `02_DATA_CONTENT_VERIFICATION.md` → Interactive Wrapper Width.

**Activity sidebar:**
```html
<div class="col-md-4 offset-md-0 col-12">
    <div class="alertActivity">
        <h4>Note</h4>
        <p>Sidebar content</p>
    </div>
</div>
```

---

## Alerts

```html
<!-- Standard (coloured left border) -->
<div class="alert"><div class="row"><div class="col-12"><p>Content</p></div></div></div>

<!-- Solid (full background — [Important]) -->
<div class="alert solid"><div class="row"><div class="col-12"><p>Content</p></div></div></div>

<!-- Top (sidebar) -->
<div class="alert top"><h4>Heading</h4><p>Text</p></div>

<!-- Blank -->
<div class="alert blank"><div class="row"><div class="col-md-12"><p><span class="highlight">Text</span></p></div></div></div>

<!-- Teacher (CS/developer — NOT student-facing) -->
<div class="alert teacher"><div class="row"><div class="col-12"><p>Instructions</p></div></div></div>
```

**Alert heading label — "Key points" (SCBI series).** *For SCBI-series modules,* when a lesson's alert presents a "Key points" summary, render the label as a heading with **no trailing colon** — `<h4>Key points</h4>` — not as a paragraph (`<p>Key points:</p>`):

```html
<div class="alert">
    <div class="row">
        <div class="col-12">
            <h4>Key points</h4>
            <ul>
                <li>…</li>
            </ul>
        </div>
    </div>
</div>
```

This is a **SCBI-series convention** (applies to every SCBI module across all year levels). For other series, follow that series' own reference; do not assume the `<h4>` form unless its reference shows it.

### Cultural Alert (Wānanga / Talanoa)

Cultural-themed alerts for content relating to Māori and Pasifika culture. Uses `layout` attribute to set the visual variant.

```html
<!-- Wānanga layout -->
<div class="alert cultural" layout="wananga">
    <div class="row">
        <div class="col-12">
            <h4>Heading</h4>
            <p class="margB0">Content about wānanga.</p>
        </div>
    </div>
</div>

<!-- Talanoa layout -->
<div class="alert cultural" layout="talanoa">
    <div class="row">
        <div class="col-12">
            <h4>Heading</h4>
            <p class="margB0">Content about talanoa.</p>
        </div>
    </div>
</div>

<!-- Combined layout (both wānanga and talanoa) -->
<div class="alert cultural" layout="combined">
    <div class="row">
        <div class="col-12">
            <h4>Heading</h4>
            <p class="margB0">Content about both wānanga and talanoa.</p>
        </div>
    </div>
</div>
```

**Layout values:** `wananga`, `talanoa`, `combined`

**Acknowledgement requirement:** When using cultural alerts, the acknowledgements block (at the bottom of the overview page, lesson 0.0) MUST include: `Wānanga/Talanoa cultural alert: Polynesian tattoo tribal band design, iStock 2161774427, 2159637722 and 1821541617, Getty Images. Adapted. Used with permission.`

### Translate Section in Alert Solid

Variant where a translate section is embedded inside an `alert solid` container:

```html
<div class="col-md-8 col-12 translateSection">
    <div class="alert solid translateSectionButton">
        <div class="translate">
            <h4>Te Reo heading</h4>
            <p>Te Reo content</p>
        </div>
        <div class="translate">
            <h4>English heading</h4>
            <p>English content</p>
        </div>
    </div>
</div>
```

### Activity Image Sidebar

Image sidebar for activities (alternative to `alertActivity` text sidebar):

```html
<div class="col-md-4 offset-md-0 col-6 offset-3">
    <div class="alertImage">
        <img alt="" class="img-fluid" src="images/image.jpg" />
    </div>
</div>
```

### Activity + AlertImage Pairing (Wide Interactive Layout)

When an interactive activity (e.g., a dropQuiz list layout) needs more room than the default `col-md-8` and an `alertImage` accompanies it, the activity takes `col-md-8 col-12` and the `alertImage` sits **beside** it at `col-md-4` (8 + 4 = 12). This is the dominant convention across the module library and applies in **every** module type — an Inquiry/Fundamentals activity paired with an alertImage is still `col-md-8`, not `col-md-11`, so the image has room. `col-md-10` is no longer used for activity wrappers (see constraint 56). Use the following pattern:

```html
<div class="row">
    <div class="col-md-8 col-12">
        <div class="activity interactive" number="2A">
            <div class="row">
                <div class="col-12">
                    <!-- Interactive component here (e.g., dropQuiz list layout) -->
                </div>
            </div>
        </div>
    </div>
    <div class="col-md-4 offset-md-0 col-12">
        <div class="alertImage">
            <div class="row">
                <div class="col-12">
                    <img class="img-fluid" loading="lazy" src="images/image.jpg" alt="Description" />
                </div>
            </div>
        </div>
    </div>
</div>
```

**Key rules for activity + alertImage pairing:**
- The outer row contains the activity at `col-md-8 col-12` and the `alertImage` at `col-md-4 offset-md-0 col-12`, side by side (8 + 4 = 12)
- The activity and the `alertImage` div are siblings in the same outer `row`
- The `alertImage` container uses `col-md-4 offset-md-0 col-12`
- The `alertImage` contains an inner `<div class="row"><div class="col-12">` wrapping the image
- Use `loading="lazy"` on the image
- Use actual image paths (not placehold.co URLs) when the writer has specified the image
- This pairing width applies whenever an interactive sits beside an alertImage and **overrides** the module-type wrapper default (`col-12` Standard / `col-md-11 col-12` Inquiry & Fundamentals). Activity wrappers never use `col-md-10` (see constraint 56)

---

> **COMP_14 continues in `05D_COMP14_BUTTONS_TABLES_COLUMNS.md`** — Buttons (incl. the external-link default label and the MTK Quiz activity shell), the Supervisor Button, Tables, Columns & Floating Columns, Quote Text, Whakatauki and Rhetorical Question. COMP_14 is ONE section split across `05B` and `05D`.
