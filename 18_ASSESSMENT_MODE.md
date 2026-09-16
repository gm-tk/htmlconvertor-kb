> **Last updated:** Wednesday, 16th September, 2026 8:30 PM

# 18 — Assessment Mode (Mode 9)

> **When to load:** Whenever a message contains the trigger phrase **`ASSESSMENT MODE`** (case-insensitive), **or** an uploaded `.docx` matches the **Assessment Activity fingerprint** in Section 2 — whatever the user typed, including nothing at all, or a plain-English request such as "please convert this word doc" / "convert this assessment content". This is **Mode 9 — Assessment** (see `00_MASTER_INSTRUCTIONS.md` → Operating Modes). It is a **conversion variant with its own output**: one single-page assessment HTML file, not a module. `ADMIN MODE`, `PAGEFORGE COMPARE MODE`, `COMPARISON MODE` and `UPDATE MODE` still outrank it; it outranks the ordinary Conversion / Support / Advisory signals and the "ambiguous `.docx` → ask" rule, because the fingerprint is unambiguous.

---

## PURPOSE

Te Kura's NCEA assessment activities (internal and external, achievement standards and unit standards) are written by writers in one of two Word templates — **"Blank Assessment Activities Template.docx"** and **"Blank External Assessment Activities Template.docx"** — and published as a **single HTML page** hosted in D2L's public files area (`/shared/assessment/…`), not inside a module. The page has a coloured header bar naming the activity and linking to the standard on NZQA, and an accordion for each section of the template, ending with the dropbox. This mode turns the filled-in Word template into that page. It builds nothing else, never edits student content, and never adds CSS or JavaScript beyond the two fixed inline styles in Section 6.4 (constraint 2 exception).

The authoritative example of the finished output is `Assessment-AS91956-example.html` (NCEA Level 1 Japanese, AS91956). The skeleton in Section 5 is taken from it with **three corrections the example itself gets wrong** (live script host, `<div id="body">`, and indentation — Section 5.1) and must be reproduced exactly as printed there, never as printed in the example.

---

## 1. THE TRIGGER

Any of the following starts Assessment Mode:

1. The phrase **`ASSESSMENT MODE`** in any capitalisation (`assessment mode`, `Assessment Mode`, …) with a `.docx` attached in the same or the next message.
2. A `.docx` upload that passes the **fingerprint** in Section 2, with **no** mode phrase and any wording — "please convert this word doc", "convert this assessment content", "can you make the HTML for this", or no words at all. The document identifies itself; the user must not have to remember the phrase.
3. A plain-English request mentioning an assessment, a standard (`AS9…`, `US…`) or "assessment activity" together with a matching `.docx`.

Precedence: `ADMIN MODE` → `PAGEFORGE COMPARE MODE` → `COMPARISON MODE` → `UPDATE MODE` all still win if their phrase is present. `SPLIT MODE` and `INTERACTIVES MODE` do not apply to an assessment document; if either phrase arrives with a fingerprinted `.docx`, run Assessment Mode and say so in one line. A `.docx` that does **not** pass the fingerprint is handled by the normal triage (a Writers Template → Conversion Mode; an MTK docx → `07`; otherwise ask).

---

## 2. THE FINGERPRINT — recognising an assessment document

A `.docx` is an Assessment Activity document when **both** hold:

1. It opens with a **two-column details table** whose left-hand cells are labels drawn from: `Activity name:`, `Subject:`, `Achievement Standard:` **or** `Unit Standard:`, `Method of Assessment:`, `Credits:`, `Title:`, `Brief description:`, and (newer template only) `Are any 3rd Party Items required?`. The bold line above the table normally reads **"NCEA External Assessment Activity"** — note that **both** writers' templates carry this title, even for an internal assessment, so the word "External" in it means nothing; the `Method of Assessment:` row is what decides internal vs external.
2. Below the table, at least three of these **bold section headings** appear in this order: **What to do**, **How to present your learning**, **Timeframe**, **Getting started**, **Student Resources**, **Dropbox**.

Template scaffolding markers such as `[body]`, `[H3]`, `[Button]` and the trailing `DROPBOX` title line confirm the match but are not required (a writer may have deleted them). A Writers Template for a module (`[TITLE BAR]`, `[LESSON]`, `--- CONTENT START ---`) never passes this fingerprint.

The two blank templates differ only in the **Dropbox** section: the ordinary template has one `[H3]` / `[body]` / `[Button]` group; the External template offers two — one "for non-exam external assessments" (`[H3]` = the standard number) and an optional "formative dropbox for exam activities" (`[H3]` = *Activities*). Section 6.7 covers both.

---

## 3. INPUTS

- **Required:** the filled-in assessment `.docx`. Nothing else is needed to produce the page.
- **Optional:** the dropbox code (`TCS-nnnnnn`), the D2L folder path for the footer links, and any image the writer merged in (typically the rubric). When these are not supplied the page is still produced in full, with a visible `Designer/Developer To Do:` note at each spot (Section 7) — **never ask for them first, never stall the conversion on them.**
- No image-mode prompt (constraint 9 does not apply): the assessment page carries no module images; a writer-supplied picture is handled by Section 7.3.

---

## 4. THE MAPPING — Word template → page

### 4.1 The details table → the header bar (`#header` → `.alertAssessment`)

| Word row | Goes to |
|---|---|
| `Title:` | `<h3>` in `.col-md-8 .assessment` — the big heading on the bar |
| `Activity name:` | the `<p>` directly under that `<h3>` |
| `Achievement Standard:` / `Unit Standard:` — the part **before** the dash (e.g. `US4249 (Version 10)`, `AS91956`) **+** `Subject:` with any `(Level n)` suffix removed | `<p class="standard"><b>{code}, {subject}</b></p>` — e.g. `AS91956, Japanese 1.1` / `US4249 (Version 10), Pathways Education` |
| the part **after** the dash in the Standard row (the standard's own title) | `<p class="description">` |
| level (from `(Level n)` in `Subject:`, or the standard's level) **+** `Method of Assessment:` (first word: Internal / External) **+** `Credits:` | `<p class="credits">Level {n} {Internal\|External} Assessment <br>{n} Credits <i class="fa-solid fa-arrow-up-right-from-square"></i></p>` |
| the standard code | the NZQA link wrapping the right-hand box (Section 4.2) and the `<title>`: `NCEA Level {n} {code}` — code only, e.g. `NCEA Level 1 US4249` |
| `Brief description:` | **not rendered** — it is catalogue metadata, not student content. |
| `Are any 3rd Party Items required?` | **not rendered**; if the writer ticked **Yes**, raise a `Designer/Developer To Do:` at the top of the **Student Resources** accordion noting that third-party items were declared. |

Everything after `Method of Assessment:`'s dash (e.g. "– Written responses") is dropped from the credits line; the page shows only Internal or External.

### 4.2 The NZQA link

| Standard type | Link |
|---|---|
| Achievement standard `AS9nnnn` | `https://www.nzqa.govt.nz/nqfdocs/ncea-resource/achievements/{year}/as9nnnn.pdf` — copy the `{year}` from an earlier assessment for the same subject if one is in the chat; otherwise use the current year and raise a `Designer/Developer To Do:` to confirm the year. |
| Unit standard `USnnnn` | `https://www.nzqa.govt.nz/nqfdocs/units/pdf/{nnnn}.pdf` — the bare number, no `US` prefix (verified: `4249.pdf`). |

The link keeps `target="_blank" rel="noopener"` exactly as in the skeleton.

### 4.3 Section headings → accordions

Every **bold section heading** of the template becomes one accordion pair inside `<div class="accordion assessment">`, **in the order the writer has them**, and only if the writer filled it in (an empty `[body]` section is dropped, except Dropbox — Section 6.7):

| Word heading | `accHead` `<h4>` |
|---|---|
| What to do | What to do |
| How to present your learning | How to present your learning |
| Timeframe | Timeframe |
| Getting started | Getting started |
| Student Resources | Student Resources |
| Dropbox | **Final Dropbox** — with `class="accHead dropBox"` / `class="accContent dropBox"` (Section 6.7) |

Everything between one section heading and the next is that accordion's content. The scaffolding tokens `[body]`, `[H3]`, `[Button]` and the closing `DROPBOX` title line are **stripped**, never rendered (constraint 3 applies to these square-bracket markers exactly as to writer tags). Where `[body]` runs on into the writer's first sentence on the same line (`[body] You will complete four tasks…`), remove the token and keep the sentence.

---

## 5. THE SKELETON (reproduce exactly — placeholders in `{braces}`)

```html
<!DOCTYPE html>
<html lang="en" level="" template="NCEA" class="notranslate" translate="no">
<head>
    <meta charset="utf-8">
    <meta content="IE=edge" http-equiv="X-UA-Compatible">
    <meta content="width=device-width, initial-scale=1" name="viewport">
    <title>NCEA Level {n} {CODE}</title>
    <script type="text/javascript" src="https://tekura.desire2learn.com/shared/refresh_template/js/idoc_scripts.js"></script>
    <script type="text/javascript" src="https://tekura.desire2learn.com/shared/Assessment/assessmentLinker.js"></script>
</head>
<body class="container-fluid">
    <div id="header">
        <div class="alertAssessment">
            <div class="row">
                <div class="col-md-8 col-12 assessment">
                    <h3>{Title}</h3>
                    <p>{Activity name}</p>
                </div>
                <div class="col-md-4 col-12 achievement">
                    <a href="{NZQA link}" target="_blank" rel="noopener">
                        <p class="standard"><b>{code}, {subject}</b></p>
                        <p class="description">{standard title}</p>
                        <p class="credits">Level {n} {Internal|External} Assessment <br>{n} Credits <i class="fa-solid fa-arrow-up-right-from-square"></i></p>
                    </a>
                </div>
            </div>
        </div>
    </div>
    <div id="body">
        <div class="row">
            <div class="col-md-8 col-12 assessment">
                <div class="accordion assessment">
                    <div class="accHead">
                        <h4>{section heading}</h4>
                    </div>
                    <div class="accContent">
                        {section content}
                    </div>
                    … one accHead/accContent pair per filled-in section, in template order …
                    <div class="accHead dropBox">
                        <h4>Final Dropbox</h4>
                    </div>
                    <div class="accContent dropBox">
                        <div class="col-12">
                            <div class="row">
                                <div class="col-12">
                                    <h3>{CODE}</h3>
                                    <p>{dropbox body}</p>
                                    <a href="/d2l/common/dialogs/quickLink/quickLink.d2l?ou={{orgUnitId}}&amp;type=dropbox&amp;rcode={TCS-nnnnnn}" target="_blank" rel="noopener">
                                        <div class="button">Upload to dropbox</div>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div id="footer">
        <ul class="footer-nav">
            <li><a href="/shared/assessment/NCEA Level {n}/{COURSE}/{CODE}/" id="prev-lesson" target="_self"></a></li>
            <!-- <li><a href="" id="next-lesson" target="_self"></a></li> -->
            <li><a href="/shared/assessment/NCEA Level {n}/{COURSE}/{CODE}/" class="home-nav" target="_parent"></a></li>
        </ul>
    </div>
</body>
</html>
```

### 5.1 The three corrections to the example — and the indentation rule

`Assessment-AS91956-example.html` is the structural authority, but it was captured from the **dev** server and hand-edited, so three things in it are **not** to be copied (designer feedback, 16 September 2026):

1. **Script host — live, never dev.** Both `<script>` lines point at `https://tekura.desire2learn.com/…` (the example's `tekuradev.desire2learn.com` is the dev domain — a mistake in the training files, never reproduced). The two paths (`/shared/refresh_template/js/idoc_scripts.js` and `/shared/Assessment/assessmentLinker.js`) are unchanged.
2. **`<div id="body">`.** The wrapper that follows the closing `</div>` of `#header` is `<div id="body">`, not a bare `<div>` — the template's padding depends on the id (the example has the bare `<div>` and gets the padding wrong).
3. **Indentation.** The page is indented — **four spaces per nesting level**, one block-level element per line, closing tags on their own line — from `<head>` down to the last `</div>`. Inline elements (`<b>`, `<i>`, `<u>`, `<br>`, `<a>` around running text, the `<i class="fa-solid …">` icon) stay inside their line; `<li>`, `<th>`, `<td>`, `<p>`, `<h4>`, `<h5>` each take one line, and a `<li>` that holds nested paragraphs, lists or a table opens on its own line, indents its children one level, and closes on its own line. Section content in `{section content}` is indented to the level of its `accContent` div's children (six levels, 24 spaces). The example's unindented body is **not** the standard.

Everything else in the skeleton is **verbatim**: the `{{orgUnitId}}` token, the `&amp;` entities, the commented-out `next-lesson` line, `level=""` (stays empty) and `template="NCEA"`. No `stickyNav`, no lesson menu, no acknowledgements block, no `<!-- N -->` delimiters — this is not a module page. Output is **one file**, named **`{CODE}.html`** (e.g. `US4249.html`, `AS91956.html` — never `Assessment-{CODE}.html`), delivered as a downloadable file.

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
A hyperlink in the Word text → `<a href="…" target="_blank" rel="noopener">`. A cover-sheet or resource PDF the writer names becomes the example's button pattern — `<a href="{path}" target="_blank" rel="noopener"><div class="button">{label}</div></a>` — inside the accordion where the writer placed it, with a `Designer/Developer To Do:` if the file path is not known. Module codes the writer cites (e.g. `PWY1001`) are plain text, not links.

### 6.7 The dropbox accordion
The `Dropbox` section always produces the `dropBox` accordion pair from the skeleton, even when the writer left `[H3]` and `[body]` empty:

- `<h3>` = the writer's `[H3]` text; if empty, the **standard code** (`US4249`).
- `<p>` = the writer's `[body]` text; if empty, the stock sentence `When you have completed your assessment, upload your final work to the dropbox below.` (with a `Designer/Developer To Do:` saying the writer left it blank).
- `[Button] Upload to dropbox.` → the quickLink button; the trailing full stop is dropped (the button label is fixed).
- `rcode=` is the assessment's dropbox code. It is never in the Word document: use the code if the user supplied one, otherwise emit `rcode=TCS-XXXXXX` **and** a `Designer/Developer To Do:` directly under the button (Section 7.1).

External template, two groups filled in: emit **two** `dropBox` accordion pairs in order. The group whose `[H3]` is the standard number is titled `Final Dropbox`; the formative `Activities` group is titled `Formative Dropbox`, with a `Designer/Developer To Do:` to confirm that label (it is not in the example).

---

## 7. WHAT THE DOCUMENT CANNOT TELL YOU — visible `Designer/Developer To Do:` notes

Every gap is a **visible** red, bold `<p style="color: red; font-weight: bold;">Designer/Developer To Do: …</p>` at the exact spot (constraint 5 — never an HTML comment), and is listed in the Designer Summary. The page is always produced in full around them.

1. **Dropbox code** — always, unless supplied: placeholder `TCS-XXXXXX` in the link + a To Do under the button.
2. **Footer folder path** — `/shared/assessment/NCEA Level {n}/{COURSE}/{CODE}/`, where `{COURSE}` is the subject's course-folder code (the example uses `JPN1000` for Japanese). Derive it from the first module code the writer cites (`PWY1001` → `PWY1000`), or from the subject's Languages/Pathways code in `14`; state the assumption in the same To Do as the dropbox code.
3. **Images** — the assessment `.docx` has typically been saved out of SharePoint/Teams, so a picture the writer merged in (usually the rubric) is often a broken link with no image inside the file. Where the writer's placeholder sentence exists (`[Merged content: The assessment rubric on … – page 2]`) it is **not rendered**; emit a To Do at that spot asking for the image, quoting the writer's placeholder. Where the image **is** embedded, emit `<img>` per the Mode D rules in `01` with the writer's alt text and a To Do to confirm the hosted path.
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
6. GAPS       one visible Designer/Developer To Do per §7 item, at its spot
7. VERIFY     skeleton matches §5 apart from the placeholders — live `tekura.` scripts, `<div id="body">`, four-space
              indentation throughout (§5.1); all writer text present and unchanged;
              no <h1>–<h3> in accordions; no inline CSS beyond §6.4 + the red-note style; no HTML comments
              other than the skeleton's own next-lesson line; file named {CODE}.html
8. DELIVER    the file + the Designer Summary (constraint 88): departures first, then To Dos, then anything
              guessed or owed — or "No red flags; nothing outstanding."
```

---

## 9. WHAT THIS MODE NEVER DOES

- Never emits a module page, menu, lesson delimiters, `stickyNav` or acknowledgements; never offers Split Mode.
- Never copies the example's `tekuradev` script host, its bare `<div>` after the header, or its unindented body; never names the file `Assessment-{CODE}.html`.
- Never rewords, reorders or summarises writer text; never drops a filled-in section; never renders `Brief description:` or the 3rd-party row.
- Never invents an alert box, a journal, a rubric table or a dropbox code.
- Never adds CSS/JS beyond the two §6.4 styles and the red-note style; never uses `<strong>`/`<em>` where the example uses `<b>`/`<i>`.
- Never asks for the dropbox code, folder path or images before converting — it converts first and flags them.
