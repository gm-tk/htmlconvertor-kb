> **Last updated:** Friday, 18th September, 2026 3:30 PM
> **Granular part B (2 of 3) of `18_ASSESSMENT_MODE.md`** — Content rules inside the accordions (text, headings, the nesting rule, tables, alerts, links, dropbox), the acknowledgements block (6.8), the `Designer/Developer To Do:` list, workflow, never-does list.
> All sibling parts live in `18_ASSESSMENT_MODE/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# 18B — Assessment Mode: content rules, acknowledgements, To Do list, workflow

> **When to load:** with `18A`, whenever Assessment Mode runs. Section numbers continue from `18A` (which ends at Section 5).

---

## 6. CONTENT RULES INSIDE AN ACCORDION

### 6.1 Text and inline formatting
Paragraphs → `<p>`. Bold → `<b>`, italic → `<i>`, underline → `<u>`, a line break inside a paragraph → `<br>` — exactly as the writer has them, using the same tags the example uses (`<b>`, not `<strong>`). Writer text is never reworded (constraint 1); the writer's punctuation quirks (`Requirement 1:` with a colon, `Behaviour 1` without) are kept as written. The writer's own colouring/highlighting of filled-in text (Te Kura writers often type their content in a coloured or italic style to distinguish it from the template) is **formatting of the template, not content** — ignore run-level colour; carry bold/italic/underline only where they are applied to specific words or phrases within a paragraph, not where an entire section is uniformly styled.

### 6.2 Headings
The accordion title already uses `<h4>`, so writer headings inside a section step down one level:

| Word style | Output |
|---|---|
| Heading 2 (e.g. `Task 1 – Personal Presentation`) | `<h4>` |
| Heading 3, **un-numbered** (e.g. `In order of preference:`) | `<h5>` |
| Heading 3 (or any heading) whose text **starts with a number** (`1. Time management and punctuality`, `2. Use of devices`, …) | **not a heading** — the run of numbered headings becomes ONE `<ol>`, each heading an `<li>` whose text is wrapped in `<b>` with the leading number and dot removed (the list supplies the numbers), and everything that followed the heading in Word nested inside that `<li>` (Section 6.3). The template's stylesheet does not style `<h5>`, so numbered sub-sections left as headings render as plain text; the example page (AS91956 → Getting started) shows the intended styled numbered list. |

Never use `<h1>`–`<h3>` inside an accordion (`<h3>` is reserved for the header bar and the dropbox standard number). Never add a `<span>` to any heading (constraint 6).

### 6.3 Lists and the hierarchy rule
Bulleted lists → `<ul>`; numbered lists → `<ol>`. The ordinary conversion rules apply, plus one rule specific to assessment documents, where writers routinely number the big questions and then put sub-points, explanatory paragraphs and answer tables under each one:

**Everything that follows a numbered item — up to the next item of the same list — is nested inside that item's `<li>`.** Paragraphs, sub-lists and tables go inside the `<li>`, after the item's own text; the `<li>` closes only when the next numbered item (or the next Heading) begins. Never restart the list with `start="2"`, never leave the sub-material sitting beside the list, and never let two `1.`s appear at different levels of the same block.

A list nested inside a numbered item is **lettered, never numbered**: `<ol type="a" style="list-style-type: lower-alpha;">`. The inline style is mandatory because the D2L stylesheet overrides the `type` attribute and would otherwise force `1. 2.` again (Section 6.4). A bulleted sub-list stays `<ul>`. A second nesting level (rare) uses lower-roman: `style="list-style-type: lower-roman;"`.

Worked shape (from US4249, Task 1):

```html
<h4>Task 1 – Personal Presentation</h4>
<ol>
<li><b>Describe your workplace context.</b><br>This must be a workplace you are <b>familiar with…</b> (…).
<p>In your description, include:</p>
<ol type="a" style="list-style-type: lower-alpha;">
<li>The type of workplace</li>
<li>The work that employees do</li>
</ol>
</li>
<li><b>Describe the personal presentation requirements for this workplace (including safety).</b>
<p>Include at least <b>five requirements</b>, such as …</p>
<p><b>For each</b> requirement:</p>
<ol type="a" style="list-style-type: lower-alpha;">
<li>Describe what is expected</li>
<li>Explain why it is important in this workplace</li>
</ol>
<table class="table table-bordered" style="margin-bottom: 30px;">…</table>
</li>
</ol>
```

A numbered heading run (Section 6.2) follows the same shape — each `<li>` opens with the heading text in `<b>`, then holds its paragraphs, prompts and any bullet list:

```html
<h4>Task 4 – Time and Organisation</h4>
<p>Describe how an employee shows responsibility in the workplace:</p>
<ol>
<li><b>Time management and punctuality</b>
<p><i>I would manage my time by…</i></p>
</li>
<li><b>Care of equipment</b>
<ul>
<li>I would take care of equipment by…</li>
</ul>
</li>
</ol>
```

### 6.4 Tables — the constraint-2 exception for this mode
The assessment template's CSS was written without tables in mind: an unclassed `<table>` renders as bare text with no borders and no gap before the next heading. Two fixed inline styles are therefore **permitted in Assessment Mode only** (recorded at `00` constraint 2) and are the **only** inline CSS this mode may emit besides the red-note style:

1. every content table: `<table class="table table-bordered" style="margin-bottom: 30px;">` — Bootstrap's table classes (the page already uses Bootstrap's grid) plus a 30-pixel gap below the table;
2. every lettered sub-list: `<ol type="a" style="list-style-type: lower-alpha;">` (or `lower-roman` at the next level).

Nothing else — no widths, no colours, no cell styles, no `<style>` block. Table structure: the writer's header row → `<thead><tr><th>…</th></tr></thead>`; data rows → `<tbody><tr><td>…</td></tr></tbody>`; empty cells stay as empty `<td></td>` (they are the student's answer spaces, and the row labels — `Requirement 1:`, `Behaviour 2` — are content).

Three table shapes need interpretation, all seen in US4249:

| Word table | Treatment |
|---|---|
| **Answer table** — a header row plus labelled rows with empty cells (`Requirement`, `What is expected?`, …) | keep as a table per the rule above. |
| **Empty writing box** — a one-column table with no text at all (a lined answer space) | **dropped**; it carries no content. |
| **Layout box** — a one-column table whose cells hold headings, questions and italic prompt sentences (US4249 Task 4) | the table is only a visual frame in Word: **flatten it** — its headings and paragraphs are converted as if they were not in a table, so a numbered-heading run inside it becomes the `<ol>` of Section 6.2/6.3. |

> Answer tables and prompts are on the page for now. Persephone has indicated that the parts students write into may eventually be built as a separate **journal** template with a "Go to assessment" link instead; until an Update Mode / Admin Mode change says so, keep them on the assessment page as above and do not build a journal.

### 6.5 Alert boxes
The example's coloured "Before you begin" box (`<div class="alert"><div class="row"><div class="col-12">…</div></div></div>`) is used **only** when the writer marks a block for it (a Word callout/shaded box, or an explicit `[ALERT]` / "Before you begin" heading). A plain paragraph such as `Conditions:` followed by text is **not** an alert — render it as paragraphs. Never invent an alert to make the page look like the example.

### 6.6 Links, buttons and files
A hyperlink in the Word text → `<a href="…" target="_blank" rel="noopener">`. A cover-sheet or resource PDF the writer names becomes the example's button pattern — `<a href="{URL}" target="_blank" rel="noopener"><div class="button">{label}</div></a>` — inside the accordion where the writer placed it, its `{URL}` built on the server convention in Section 7.2 (`…/{CODE}/pdf/{file}.pdf`) and paired with the Section 7.2 upload To Do. Module codes the writer cites (e.g. `PWY1001`) are plain text, not links.

### 6.7 The dropbox accordion
The `Dropbox` section always produces the `dropBox` accordion pair from the skeleton, even when the writer left `[H3]` and `[body]` empty:

- `<h3>` = the writer's `[H3]` text; if empty, the **standard code** (`US4249`).
- `<p>` = the writer's `[body]` text; if empty, the stock sentence `When you have completed your assessment, upload your final work to the dropbox below.` (with a `Designer/Developer To Do:` saying the writer left it blank).
- `[Button] Upload to dropbox.` → the quickLink button; the trailing full stop is dropped (the button label is fixed).
- `rcode=` is the assessment's dropbox code. It is never in the Word document: use the code if the user supplied one, otherwise emit `rcode=TCS-XXXXXX` **and** a `Designer/Developer To Do:` directly under the button (Section 7.1).

External template, two groups filled in: emit **two** `dropBox` accordion pairs in order. The group whose `[H3]` is the standard number is titled `Final Dropbox`; the formative `Activities` group is titled `Formative Dropbox`, with a `Designer/Developer To Do:` to confirm that label (it is not in the example).

---

### 6.8 The acknowledgements block — always, even with no media

Every assessment page ends with the standard acknowledgements accordion, placed **after the closing `</div>` of `#footer`** exactly as the `18A` skeleton shows, inside `row → col-md-8 col-12`, wrapper **`<div class="acks acksTemplate">`**. It is emitted **on every page without exception**: the `acksTemplate` class makes the template render Te Kura's generic statements — the *Every effort has been made…* apology and the *Copyright © [year] Board of Trustees of Te Aho o Te Kura Pounamu…* line — so a page with no media still carries the full copyright block. Those generated statements are **never typed as `<p>` text** (constraint 90 — typing them doubles them up on the published page); the **one** boilerplate line that IS typed is the closing `<div class="acksLesson"><p>All other images © Te Aho o Te Kura Pounamu, Wellington, New Zealand.</p></div>`. Add `acksAI` to the wrapper (`<div class="acks acksTemplate acksAI">`) when the document uses or requests an AI-generated asset, with the pending-asset `Designer/Developer To Do:` from `05C` (constraint 72). The block follows the four-space indentation rule like the rest of the page.

**Structure inside `accContent`:** an assessment is one page, so the media entries go in **one** `acksLesson` div with **no** `<!-- Lesson N.N -->` label (the label names a page in a multi-page module and has no meaning here), followed by the unlabelled "All other images" div. With no media at all, the "All other images" div is the only child. Entry wording, italics, URL wrapping (`<a href="…" target="_blank">URL</a>`, punctuation outside the anchor), the `retrieved d/m/y` conversion date for videos and every other entry rule are exactly those in `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` → Acknowledgements (`05C`); nothing is re-invented here.

**Isolating the media — there is never a Media List.** The document itself is the only inventory, so sweep the whole `.docx` (every section, the details table, table cells, hyperlinks and embedded objects) and classify each item:

| Found in the document | Acknowledgement |
|---|---|
| An embedded or linked **stock image** (iStock / Getty / Shutterstock — recognised by an ID in the filename, alt text, caption or URL) | `Photo:` / `Illustration:` entry per `05C`, ID cited as in constraint 61. Title or ID unconfirmable → `Red Flag:` for the developer, never an invented entry. |
| A **video** link or embed (YouTube or another platform) | `Video:` entry — full published title and channel/author, wrapped URL, `retrieved d/m/y` = the conversion date, `Used in online learning within the exception for education.` Title or author unconfirmable → `Red Flag:`. |
| **Third-party text or a document reproduced on the page** (a story, an article excerpt, a scanned page, a journal or book cover) | `Story:` / `Image:` entry per `05C`, with byline and licence; unconfirmable byline → `Red Flag:`. |
| A **Te Kura-owned asset** — the rubric, the assessment cover sheet, a PWY/JPN module reference, a Te Kura diagram, the writer's own photo | **No entry** — the typed "All other images © Te Aho o Te Kura Pounamu…" line covers it. |
| The **NZQA standard link**, a **plain hyperlink** the student visits (a website, a government page, a dropbox), a module code, an email address | **Not media** — no entry. |
| A picture the document **names but does not contain** (the broken `[Merged content: …]` rubric link, an asset the writer asks CS to create) | No entry yet; the Section 7.3 `Designer/Developer To Do:` already says the asset is pending and where to upload it — extend it with "and add its acknowledgement entry if it is not Te Kura's own". |

Order the entries as the items appear on the page. A `Red Flag:` inside the acks block is a visible red `<p>` in the media `acksLesson` div, exactly as in a module.

**Worked shape — a page with one video and nothing else external:**

```html
                        <div class="acksLesson">
                            <p>Video: How volcanoes work, GNS Science, <a href="https://www.youtube.com/watch?v=XXXXXXXXXXX" target="_blank">https://www.youtube.com/watch?v=XXXXXXXXXXX</a>, retrieved 18/9/2026. Used in online learning within the exception for education.</p>
                        </div>
                        <div class="acksLesson">
                            <p>All other images © Te Aho o Te Kura Pounamu, Wellington, New Zealand.</p>
                        </div>
```

**Worked shape — no media (US4249):** the `accContent` holds only the "All other images" div.

---

## 7. WHAT THE DOCUMENT CANNOT TELL YOU — visible `Designer/Developer To Do:` notes

Every gap is a **visible** red, bold `<p style="color: red; font-weight: bold;">Designer/Developer To Do: …</p>` at the exact spot (constraint 5 — never an HTML comment), and is listed in the Designer Summary. The page is always produced in full around them.

1. **Dropbox code** — always, unless supplied: placeholder `TCS-XXXXXX` in the link + a To Do under the button. (No footer-path question rides along with it — the footer links are always blank.)
2. **Media files — where they live on the server, how they are named, and the To Do that says so.** Every assessment page is published in D2L's public files area at `https://tekura.desire2learn.com/shared/assessment/NCEA%20Level%20{n}/{COURSE}/{CODE}/{CODE}.html`, and its media sit in two fixed sub-folders beside it: **`images/`** for pictures and **`pdf/`** for PDFs and other documents (e.g. `…/NCEA%20Level%201/AGH1000/AS91929/images/climate.jpg`, `…/AS91929/pdf/Cover Sheet.pdf`). `{n}` is the NCEA level; `{COURSE}` is the subject's course-folder code — the subject's three-letter code followed by the level digit and `000` (`AGH1000`, `JPN1000`, `PWY1000`), derived from the module code the writer cites (`PWY1001` → `PWY1000`) or from the subject family in `14`; `{CODE}` is the standard code (`AS91929`, `US4249`). Spaces in the path are written `%20`. **File names** are lowercase, descriptive, hyphenated, without spaces or special characters, keeping the original extension — `us4249-assessment-rubric.jpg`, `nzmap.jpg`, `climate.jpg`. An `<img>` therefore reads `<img src="https://tekura.desire2learn.com/shared/assessment/NCEA%20Level%201/PWY1000/US4249/images/us4249-assessment-rubric.jpg" alt="{writer's alt text or caption}">`. Because the developer must physically put the file there, **every media item gets a To Do that names the exact destination**, in this form:

   `Designer/Developer To Do: export this image from the Word document, save it as us4249-assessment-rubric.jpg, and upload it in D2L → Manage Files → shared › assessment › NCEA Level 1 › PWY1000 › US4249 › images. If the US4249 folder does not exist yet, create it there with images and pdf sub-folders. Confirm PWY1000 is the correct course folder for this subject; the link above assumes it.`

   The Designer Summary repeats the list: one line per media file → its destination folder. The footer links are **not** part of this — they stay blank (`18A` Section 5.1) and get no To Do.
3. **Images that are not in the file** — the assessment `.docx` has typically been saved out of SharePoint/Teams, so a picture the writer merged in (usually the rubric) is often a broken link with no image inside the file. Where the writer's placeholder sentence exists (`[Merged content: The assessment rubric on … – page 2]`) it is **not** rendered; emit a To Do at that spot asking for the image, quoting the writer's placeholder and naming the destination folder per item 2. Where the image **is** embedded, emit the `<img>` per item 2 with the writer's alt text, the item-2 To Do, and an acknowledgement per Section 6.8 unless it is Te Kura's own.
4. **Writer left a required field empty** (`Title:`, `Credits:`, the Standard row) — build the bar with what exists and a To Do naming the missing field. Never guess a credit count or a standard title.
5. **Anything the Convertor cannot interpret** (a table shape not in 6.4, a heading level that cannot be placed) → `Red Flag:` with a visible fallback, per the universal rule.

---

## 8. WORKFLOW (pseudo-code)

```
1. TRIAGE     phrase ASSESSMENT MODE (any case) OR .docx passes fingerprint (§2) → Mode 9
              (ADMIN / PAGEFORGE COMPARE / COMPARISON / UPDATE phrases still win)
2. READ       the details table → header-bar fields (§4.1); standard code → NZQA link (§4.2), <title>, filename
3. SECTIONS   split the body at the bold template headings (§4.3); strip [body] [H3] [Button] DROPBOX
4. CONVERT    each section's content (§6): headings step down; numbered items nest their sub-material;
              lettered sub-lists; tables classed + padded; layout boxes flattened; empty boxes dropped
5. DROPBOX    always emit the dropBox pair (§6.7); rcode from the user or TCS-XXXXXX + To Do
5a. ACKS      always emit the acknowledgements block after #footer (§6.8): sweep the document for media,
              one unlabelled acksLesson of entries (or none) + the typed "All other images" div; acksAI if AI media
6. GAPS       one visible Designer/Developer To Do per §7 item, at its spot — media To Dos name the exact
              D2L destination (shared › assessment › NCEA Level {n} › {COURSE} › {CODE} › images | pdf); footer hrefs stay ""
6a. REPEAT    steps 2–5a for every fingerprinted .docx in the upload; all pages emitted in ONE response
7. VERIFY     skeleton matches `18A` §5 apart from the placeholders — live `tekura.` scripts, `<div id="body">`, four-space
              indentation throughout (§5.1); all writer text present and unchanged;
              no <h1>–<h3> in accordions; no inline CSS beyond §6.4 + the red-note style; no HTML comments
              other than the skeleton's own next-lesson line; file named {CODE}.html
8. DELIVER    the file(s) + the Designer Summary (constraint 88): departures first, then To Dos, then anything
              guessed or owed — or "No red flags; nothing outstanding."
```

---

## 9. WHAT THIS MODE NEVER DOES

- Never emits a module page, menu, lesson delimiters, `stickyNav` or acknowledgements; never offers Split Mode.
- Never copies the example's `tekuradev` script host, its bare `<div>` after the header, or its unindented body; never names the file `Assessment-{CODE}.html`.
- Never rewords, reorders or summarises writer text; never drops a filled-in section; never renders `Brief description:` or the 3rd-party row.
- Never invents an alert box, a journal, a rubric table, a dropbox code or an acknowledgement entry; never omits the acknowledgements block or types the statements `acksTemplate` generates.
- Never adds CSS/JS beyond the two §6.4 styles and the red-note style; never uses `<strong>`/`<em>` where the example uses `<b>`/`<i>`.
- Never asks for the dropbox code or images before converting — it converts first and flags them, naming the exact D2L folder each media file must be uploaded to.
- Never fills in the footer links, never guesses them, never raises a To Do for them — they are always `href=""`.
- Never emits a batch of pages one per turn, and never asks for a Media List.
