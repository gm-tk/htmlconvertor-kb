> **Last updated:** Wednesday, 29th July, 2026 5:36 PM
> **Granular part B (2 of 3) of `05_COMP_LANGUAGE_MEDIA_LAYOUT.md`** — COMP_14 layout & structure (activities, alerts, buttons, tables, columns).
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

<!-- Interactive activity (circle icon) — heading/intro row, then interactive row -->
<div class="activity interactive" number="1B">
    <div class="row"><div class="col-md-8 col-12">
        <h3>Activity heading</h3>
        <p>Intro / instructions</p>
    </div></div>
    <div class="row"><div class="col-12">
        <!-- Interactive component here -->
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

**MTK quiz activities (constraint 65).** An activity whose writer source carries the `[MTKquiz]` tag (with any modifiers, e.g. `[engage]`, `[type the answer]`, `[Teacher marked …]`) ends in a **"Go to quiz" button**, never a dropbox button — see Buttons → MTK Quiz Button below. Because the activity does not end in a dropbox button, the `dropbox` wrapper modifier of constraint 43 does **not** attach.

**Text and interactive sit in SEPARATE inner rows — always (constraint 63).** Inside **every** activity wrapper, the activity's plain text content (the `<h3>` heading, intro/instruction prose, lists) sits at **`col-md-8 col-12`** — reading width — in its **own inner `row`**, and the interactive follows in a **separate inner `row`** at the wrapper's own width:

```html
<div class="activity interactive" number="1A">
    <div class="row">
        <div class="col-md-8 col-12">
            <h3>Which scam is it?</h3>
            <p>Match the example to the correct scam type.</p>
        </div>
    </div>
    <div class="row">
        <div class="col-12">
            <div class="dragAndDrop" layout="standard">
                ...
            </div>
        </div>
    </div>
</div>
```

This holds **whether or not the wrapper is widened**: prose is read, so it keeps reading width; the interactive takes whatever width its wrapper allows (`col-md-8 col-12` default, or the widened `col-12` / `col-md-11 col-12` / `col-md-12 col-12` of constraint 56). A **text-only** activity (no interactive) needs no split — its single `row`/`col-md-8 col-12` carries the heading and prose. See `02_DATA_CONTENT_VERIFICATION.md` → Interactive Wrapper Width.

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

## Buttons

```html
<!-- Internal -->
<a href="URL" target="_blank"><div class="button">Button text</div></a>

<!-- External -->
<a href="URL" target="_blank"><div class="externalButton">Button text</div></a>
```

**⚠️ CRITICAL — A STANDALONE external link is a button; an INLINE one is an anchor (constraint 75).** Whether an `[external link]` renders as an `externalButton` or as a plain inline `<a>` is decided by **where the link sits**, not by which tag the writer used. Writers use `[external link]` and `[external link button]` interchangeably, so the tag alone is not a reliable signal — **position is**:

| The link… | Renders as |
|---|---|
| **stands alone** — the writer gave it its own line/paragraph, as a call to action | `<a href="URL" target="_blank"><div class="externalButton">Text</div></a>` |
| **sits inline** — inside a sentence of prose, a list item, or a table cell | `<a href="URL" target="_blank">Text</a>` |

`[external link button]` **always** renders as a button regardless of position — an explicit request is honoured. The `external link` / `external link button` **tag distinction is retained** in the taxonomy (`01` → Tag Taxonomy → Link/Button Tags); it is the *rendering* of a standalone `[external link]` that now matches `[external link button]`.

```html
<!-- Standalone: own line, call to action → button -->
<a href="https://report.netsafe.org.nz/hc/en-au/requests/new" target="_blank"><div class="externalButton">Report a scam to Netsafe online</div></a>

<!-- Inline: inside prose → anchor -->
<p>You can also <a href="https://www.snopes.com/" target="_blank">check a claim on Snopes</a> before you share it.</p>

<!-- Inline: inside a table cell → anchor -->
<td><a href="https://report.netsafe.org.nz/hc/en-au/requests/new" target="_blank">Netsafe report form</a></td>
```

**The test:** would removing the link leave a grammatically incomplete sentence? If yes, it is inline (anchor). If the link occupies its own line with nothing depending on it grammatically, it is standalone (button). A link inside an `alert`, an accordion panel, or a speech bubble follows the same test — it is the **prose relationship** that decides, not the containing component. Where a link is genuinely borderline, render the **anchor** and raise a `Red Flag:` — an anchor inside prose always reads correctly, whereas a button mid-sentence breaks the line.

**Submission button labels — keep the "Go to" prefix.** A button that sends the student to the **dropbox** or to their **portfolio** keeps its full label: **"Go to dropbox"** and **"Go to portfolio"**. Do **not** drop the leading "Go to" to a bare "Dropbox" / "Portfolio" — the full "Go to …" wording is the standard and is what students expect. **Series exception (BLL / LS / HPE):** these three families label the dropbox button **"Upload to Dropbox"** — a series-scoped label that sits **alongside** (does not overturn) this universal "Go to …" default; see `14_SUBJECT_GLOBAL_PARAMETERS.md` §14.11 / `00` constraint 55. (In the HPE end-of-module celebration, a **"Go to your journal"** button also sits beside the "Upload to dropbox" button.)

```html
<a href="URL" target="_blank"><div class="button">Go to dropbox</div></a>
<a href="URL" target="_blank"><div class="button">Go to portfolio</div></a>
```

This is the button **label** convention. It is separate from — and additional to — the `dropbox` modifier on the activity *wrapper* (see Activities, above, and constraint 43): an activity that ends in a "Go to dropbox" button both carries the `dropbox` wrapper modifier **and** keeps the full "Go to dropbox" label on the button itself.

### MTK Quiz Button — `[MTKquiz]` (constraint 65)

When the writer's template uses the **`[MTKquiz]`** tag (any variant/modifier combination — `[MTKquiz] [engage]`, `[type the answer]`, `[Teacher marked …]`, etc.), **do NOT generate a dropbox button.** Generate a **"Go to quiz"** button with a **blank href**, plus a visible `Designer/Developer To Do:` note telling the developer to create the new quiz within MTK (My Te Kura) and wire its D2L quicklink URL into the href:

```html
<p style="color: red; font-weight: bold;">Designer/Developer To Do: create a new quiz within MTK for this activity and insert its D2L quicklink URL into the "Go to quiz" button href below.</p>
<a href="#" target="_blank"><div class="button">Go to quiz</div></a>
```

- **Tag precedence — WJ series.** In WJ-series modules, when `[MTK Quiz]` co-occurs with an in-page quiz tag on the same activity (e.g. `[Multichoice quiz]`, `[Radio quiz]`), `[MTK Quiz]` wins: emit this section's "Go to quiz" button pattern, NOT the in-page quiz component. An in-page quiz tag with no co-occurring `[MTK Quiz]` still builds the in-page component as normal. (WJFUN107 finalized report, Difference 1, scope (b), 29 July 2026.)
- The finished production form is a D2L quiz quicklink (`/d2l/common/dialogs/quickLink/quickLink.d2l?ou={orgUnitId}&type=quiz&rcode=…`) — the developer supplies it; the Convertor never invents an `rcode`.
- **Writer-supplied quiz content stays visible.** Any question/sentence material the writer attached to the `[MTKquiz]` activity (e.g. the incorrect sentences a quiz will ask students to fix) is writer content: render it on the page as normal so the developer has the data to build the quiz from — never silently delete it (constraint 1; the developer removes it from the page once the quiz is created).
- The activity wrapper's classes follow the normal rules — the `dropbox` modifier does **not** attach (the activity no longer ends in a dropbox button). A `dropbox` token observed on a designer-refined MTKquiz activity is a leftover, not a rule.
- `MTK` here means **My Te Kura** (the D2L quiz tool) — not the MTK (Te Reo Rangatira) Writers Template pathway of `07_MTK_DOCX_CONVERSION.md`.

---

## Supervisor Button (constraint 68)

> **⚠️ The legacy `supervisorContainer` / `supervisorButton` / `supervisorContent` trio is RETIRED — never emit it.** It survives in only 2 files corpus-wide (`CEDR101`, `HPRE301`) and the designer replaces it on sight. The live convention is the **`super-content-button` family** below (recognise the trio in old references; do not generate it).

**Triggers (what produces a supervisor button):** the bracketed tags `[supervisor note]` (dominant), `[supervisor button]`, `[supervisor]`; or a red-text prose lead-in whose case-folded lead matches `^supervisor('s)?( note[s]?)?\s*:` (`Supervisor:` / `Supervisor's Notes:` / `Supervisors notes:` — writers frequently type the note as red text after an `[Activity]` rather than bracketing a tag; this is a supervisor trigger, NOT a `Writers Note:` — see `01_PIPELINE_EXTRACTION_TAGS.md` → Red Text Handling). A companion `[side alert]` in the same paragraph selects side-column **placement** only — resolve the side-alert placement per the existing side-alert rule, then render the supervisor box with the panel structure below inside it; it never changes the supervisor component's internal HTML. The note's **text content** is whatever prose the writer attached to the trigger, passed through **verbatim** — only the wrapper structure is templated.

**THE HEADLINE RULE:** whenever a supervisor button is placed inside an activity (it belongs to a numbered activity box), the **topmost `.row` that wraps the whole block carries the class `supervisor`** → `<div class="row supervisor">` (corpus: 484/506 = 95.6%; the only legitimate exception is §Nested below). Shapes B and C use the same `row supervisor` outer.

**Decision tree — which shape to emit:**

1. **Is the note bound to an ACTIVITY** (a red `Supervisor:` note directly under an `[Activity N]` tag, or a `[supervisor note]`/`[supervisor button]` inside the activity's content run)? → **Shape A**.
2. Otherwise it is a page/section-level note: does it sit **beside** a block of ordinary section content? → **Shape C**. Does it **stand alone**? → **Shape B**.

*Page-type heuristic (sanity check, not the sole decider):* overview pages overwhelmingly use the section shapes (82 section vs 7 activity); lesson pages mostly use the activity-integrated shape (153 activity vs 81 section).

### Shape A — Activity-integrated

The activity div gains the `super-content-button` modifier (keep whatever modifiers the activity already required — `interactive`, `dropbox`, `alertPadding` combine freely; token order is not significant) and keeps its existing `number="{lesson}{letter}"`. The **reveal panel is ALWAYS the first child of the activity**, with the activity's ordinary content following as sibling `.row`(s). Content column default: `col-md-8 col-12` (follow the enclosing context where the surrounding layout already dictates a wider column).

```html
<div class="row supervisor">
    <div class="col-md-8 col-12">
        <div class="activity super-content-button" number="1A">

            <!-- reveal panel: ALWAYS the first child of the activity -->
            <div class="super-content row">
                <div class="row">
                    <div class="col-12">
                        <h3>Supervisor note</h3>
                    </div>
                    <div class="col-12">
                        <p>{supervisor note text, verbatim}</p>
                    </div>
                </div>
            </div>

            <!-- the activity's own content follows as normal sibling row(s) -->
            <div class="row">
                <div class="col-12">
                    <h3>{activity title}</h3>
                    <!-- … activity body / interactive / media … -->
                </div>
            </div>

        </div>
    </div>
</div>
```

### Shape B — Section standalone, single column

A page/section-level note that is not part of an activity and has no paired content column (most overview-page supervisor notes). `super-content-button` moves onto the **column** — there is no `.activity` div and no `number`. Any section prose the writer placed after the note renders inside the same button column, after the panel.

```html
<div class="row supervisor">
    <div class="col-md-8 col-12 super-content-button">

        <div class="super-content row">
            <div class="row">
                <div class="col-12">
                    <h3>Supervisor note</h3>
                </div>
                <div class="col-12">
                    <p>{supervisor note text, verbatim}</p>
                </div>
            </div>
        </div>

        <!-- optional: any ordinary section prose the writer put after the note -->
        <p>{following section body text, if any}</p>

    </div>
</div>
```

### Shape C — Section standalone, paired 2-column

A section-level note that sits **beside** a block of ordinary section content (common on BLL/phonics overview pages). The `paddingL`/`paddingR` pair is the discriminator between Shapes B and C: the button column takes `paddingL`, the content column takes `paddingR`.

```html
<div class="row supervisor">

    <div class="col-md-8 col-12 paddingL super-content-button">
        <div class="super-content row">
            <div class="row">
                <div class="col-12">
                    <h3>Supervisor note</h3>
                </div>
                <div class="col-12">
                    <p>{supervisor note text, verbatim}</p>
                </div>
            </div>
        </div>
    </div>

    <div class="col-md-8 col-12 paddingR">
        <p>{accompanying section content}</p>
    </div>

</div>
```

### The reveal panel — invariant internal structure

Every supervisor reveal panel — in all three shapes — has the same **four levels of nesting**, and the reveal JavaScript relies on it; do not flatten or reorder it:

```
div.super-content.row              ← the panel wrapper (prefer "super-content row" order)
  └─ div.row
       ├─ div.col-12
       │    └─ <h3>Supervisor note</h3>
       └─ div.col-12               ← content col (also seen as col-md-12 col-12)
            └─ <p>…note text…</p>
```

The `<h3>` heading defaults to **"Supervisor note"**; a heading the writer explicitly gave wins (it is a text field and never affects the wrapper structure).

### Edge cases

- **Nested inside another interactive** (accordion panel, clickDrop content block, inquiryPanel — ~21 corpus cases): the immediate wrapper is that widget's own row, so the outer row is **not** re-classed `supervisor` — keep the widget's row and place the `super-content-button` col inside it. This is the only legitimate exception to the headline rule.
- **Alternate `activity supervisor` gold form** (minority, ~16 cases — CEDT101, CEDT207, MXEX101): `supervisor` on the activity div with the button on an inner col. **Recognise-only, never generate** — a Mode B sibling showing this form is not a licence to emit it; Shape A is canonical (~15× more common and designer-designated correct).
- **Summary:** activity-bound → Shape A (`row supervisor`, class on `.activity`, `number` yes); section alone → Shape B (class on `.col`); section beside content → Shape C (class on `.col` + `paddingL`/`paddingR` pair); nested in widget → widget's own row; legacy trio → retired, never emit.

---

## Tables

```html
<div class="table-responsive">
    <table class="table table-bordered">
        <tr><th>Header 1</th><th>Header 2</th></tr>
        <tr><td>Cell 1</td><td>Cell 2</td></tr>
    </table>
</div>
```

**Optional classes:** `tableFixed`, `noHover`, `center-text`

**Table class selection guidance:**
- **`table-bordered`**: General default for most table types
- **`tableFixed`**: Prefer for two-column comparison tables (e.g., "Can" vs "Cannot", "Pros" vs "Cons", "Advantages" vs "Disadvantages") where equal column widths are desirable. Use `tableFixed` WITHOUT `table-bordered` for these cases.

```html
<!-- Comparison table — use tableFixed -->
<div class="table-responsive">
    <table class="table tableFixed">
        <tr><th>AI Can</th><th>AI Cannot</th></tr>
        <tr><td>Process data quickly</td><td>Feel emotions</td></tr>
    </table>
</div>
```

---

## Columns & Floating Columns

### Standard Grid
```html
<div class="row">
    <div class="col-md-8 col-12">Content</div>
    <div class="col-md-4 col-12">Sidebar</div>
</div>
```

**Sectioning widths.** For laying out a **section of content**, the column is `col-md-8 col-12` (standard) or `col-12` / `col-md-12 col-12` (full width). **Activity/interactive wrappers never use `col-md-10`** — a wide interactive uses `col-12` (Standard) or `col-md-11 col-12` (Inquiry & Fundamentals), or `col-md-8 col-12` with an `alertImage` at `col-md-4` (see constraint 56). `col-md-10` is no longer an activity-wrapper width. A plain, non-activity *narrowed* content block is outside this rule and may still use `col-md-10`. This is forward-only — existing `col-md-10` activity wrappers are pre-rule and are not retro-flagged. **Inside ANY activity wrapper, plain text stays at `col-md-8` in its own inner row (constraint 63):** the activity's prose (headings, instructions, paragraphs, lists) sits in its own inner `row` → `col-md-8 col-12` column, and the interactive follows in a separate inner `row` at the wrapper's width — whether that width is the default `col-md-8 col-12` or a widened `col-12` / `col-md-11 col-12` / `col-md-12 col-12`. See `02_DATA_CONTENT_VERIFICATION.md` → Interactive Wrapper Width.

### Floating (clearfix)
```html
<div class="clearfix">
    <div class="col-md-8 col-xs-12 float-md-start">Main content</div>
    <div class="col-md-4 col-12 float-md-end">
        <div class="alert"><p>Sidebar content</p></div>
    </div>
    <div class="col-md-8 col-xs-12 float-md-start">More content</div>
</div>
```

**No `col-8` directly inside a `col-8` (constraint 77).** An inner `row` placed inside a `col-md-8 col-12` column must not use a `col-8`-family class (`col-md-8`, `col-8`) for its own column(s) — use `col-md-12 col-12` (or a documented inner pattern such as the `col-md-6` pair). A `col-md-8` inside a `col-md-12`, and a `col-md-12` inside a `col-md-8`, are both fine. This applies inside activities too: an `.activity` whose outer wrapper is `col-md-8 col-12` keeps its inner columns at `col-12`; an activity that genuinely needs an inner `col-8` takes a `col-md-12 col-12` outer wrapper instead.

```html
<!-- WRONG: col-md-8 nested directly inside col-md-8 -->
<div class="row"><div class="col-md-8 col-12">
    <div class="row"><div class="col-md-8 col-12">…</div></div>
</div></div>

<!-- CORRECT: col-12 inside col-8, or col-8 inside col-12 -->
<div class="row"><div class="col-md-8 col-12">
    <div class="row"><div class="col-md-12 col-12">…</div></div>
</div></div>
<div class="row"><div class="col-md-12 col-12">
    <div class="row"><div class="col-md-8 col-12">…</div></div>
</div></div>
```

---

## Quote Text

```html
<p class="quoteText">"Quote text here."</p>
<p class="quoteAck">— Attribution</p>
```

---

## Whakatauki

```html
<div class="whakatauki">
    <p>Māori proverb text</p>
    <p>English translation</p>
</div>
```

---

## Rhetorical Question

```html
<div class="rhetoricalQuestion">
    <p>What if we could change the world?</p>
</div>
```

---

