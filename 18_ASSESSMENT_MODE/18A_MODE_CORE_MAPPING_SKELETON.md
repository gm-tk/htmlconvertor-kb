> **Last updated:** Friday, 18th September, 2026 1:00 PM
> **Granular part A (1 of 3) of `18_ASSESSMENT_MODE.md`** — Mode 9 core: trigger, fingerprint, inputs (incl. multi-document uploads), the details-table → header-bar mapping, NZQA links, section → accordion mapping, the corrected skeleton (with the acknowledgements block).
> All sibling parts live in `18_ASSESSMENT_MODE/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# 18 — Assessment Mode (Mode 9)

> **When to load:** Whenever a message contains the trigger phrase **`ASSESSMENT MODE`** (case-insensitive), **or** an uploaded `.docx` matches the **Assessment Activity fingerprint** in Section 2 — whatever the user typed, including nothing at all, or a plain-English request such as "please convert this word doc" / "convert this assessment content". This is **Mode 9 — Assessment** (see `00_MASTER_INSTRUCTIONS.md` → Operating Modes). It is a **conversion variant with its own output**: one single-page assessment HTML file per document, not a module. This topic is split into three parts: **18A** (this part — trigger, fingerprint, inputs, mapping, skeleton), **18B** (content rules inside the accordions, the acknowledgements block, the `Designer/Developer To Do:` list, workflow) and **18C** (the assessment variant of Comparison Mode). `ADMIN MODE`, `PAGEFORGE COMPARE MODE`, `COMPARISON MODE` (which, in a chat that ran this mode, is the assessment variant in `18C`) and `UPDATE MODE` still outrank it; it outranks the ordinary Conversion / Support / Advisory signals and the "ambiguous `.docx` → ask" rule, because the fingerprint is unambiguous.

---

## PURPOSE

Te Kura's NCEA assessment activities (internal and external, achievement standards and unit standards) are written by writers in one of two Word templates — **"Blank Assessment Activities Template.docx"** and **"Blank External Assessment Activities Template.docx"** — and published as a **single HTML page** hosted in D2L's public files area (`/shared/assessment/…`), not inside a module. The page has a coloured header bar naming the activity and linking to the standard on NZQA, and an accordion for each section of the template, ending with the dropbox. This mode turns the filled-in Word template into that page. It builds nothing else, never edits student content, and never adds CSS or JavaScript beyond the two fixed inline styles in `18B` Section 6.4 (constraint 2 exception). Every page ends with the acknowledgements block (`18B` Section 6.8) — always, even with no media.

The authoritative example of the finished output is `Assessment-AS91956-example.html` (NCEA Level 1 Japanese, AS91956). The skeleton in Section 5 is taken from it with **three corrections the example itself gets wrong** (live script host, `<div id="body">`, and indentation — Section 5.1) — plus the acknowledgements block the example lacks — and must be reproduced exactly as printed there, never as printed in the example.

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

The two blank templates differ only in the **Dropbox** section: the ordinary template has one `[H3]` / `[body]` / `[Button]` group; the External template offers two — one "for non-exam external assessments" (`[H3]` = the standard number) and an optional "formative dropbox for exam activities" (`[H3]` = *Activities*). `18B` Section 6.7 covers both.

---

## 3. INPUTS

- **Required:** the filled-in assessment `.docx`. Nothing else is needed to produce the page. There is **never a Media List** for an assessment — every acknowledgement is derived from the document's own content (`18B` Section 6.8).
- **Several `.docx` files at once.** Every upload is fingerprinted on its own; each one that passes becomes its own `{CODE}.html`, and **all of the pages are emitted in the same response** — never one per turn, never "say next" (the Mode 6 discipline, not the Mode 5 cadence) — each page followed by its own Designer Summary headed with the file name. An upload that does not pass the fingerprint is named in one line and handled by the normal triage after the assessment pages, never silently dropped. Two documents carrying the same standard code → build both, name the second `{CODE}-2.html`, and raise a `Designer/Developer To Do:` on each saying so.
- **Optional:** the dropbox code (`TCS-nnnnnn`), the D2L folder path for the footer links, and any image the writer merged in (typically the rubric). When these are not supplied the page is still produced in full, with a visible `Designer/Developer To Do:` note at each spot (`18B` Section 7) — **never ask for them first, never stall the conversion on them.**
- No image-mode prompt (constraint 9 does not apply): the assessment page carries no module images; a writer-supplied picture is handled by `18B` Section 7.3, and credited per `18B` Section 6.8.

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
    <div class="row">
        <div class="col-md-8 col-12">
            <div class="acks acksTemplate">
                <div class="accordion">
                    <div class="accHead"><h4>Acknowledgements</h4></div>
                    <div class="accContent">
                        {acksLesson div holding the media entries — omitted entirely when the page has no media}
                        <div class="acksLesson">
                            <p>All other images © Te Aho o Te Kura Pounamu, Wellington, New Zealand.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

### 5.1 The three corrections to the example — and the indentation rule

`Assessment-AS91956-example.html` is the structural authority, but it was captured from the **dev** server and hand-edited, so three things in it are **not** to be copied (designer feedback, 16 September 2026):

1. **Script host — live, never dev.** Both `<script>` lines point at `https://tekura.desire2learn.com/…` (the example's `tekuradev.desire2learn.com` is the dev domain — a mistake in the training files, never reproduced). The two paths (`/shared/refresh_template/js/idoc_scripts.js` and `/shared/Assessment/assessmentLinker.js`) are unchanged.
2. **`<div id="body">`.** The wrapper that follows the closing `</div>` of `#header` is `<div id="body">`, not a bare `<div>` — the template's padding depends on the id (the example has the bare `<div>` and gets the padding wrong).
3. **Indentation.** The page is indented — **four spaces per nesting level**, one block-level element per line, closing tags on their own line — from `<head>` down to the last `</div>`. Inline elements (`<b>`, `<i>`, `<u>`, `<br>`, `<a>` around running text, the `<i class="fa-solid …">` icon) stay inside their line; `<li>`, `<th>`, `<td>`, `<p>`, `<h4>`, `<h5>` each take one line, and a `<li>` that holds nested paragraphs, lists or a table opens on its own line, indents its children one level, and closes on its own line. Section content in `{section content}` is indented to the level of its `accContent` div's children (six levels, 24 spaces). The example's unindented body is **not** the standard.

Everything else in the skeleton is **verbatim**: the `{{orgUnitId}}` token, the `&amp;` entities, the commented-out `next-lesson` line, `level=""` (stays empty) and `template="NCEA"`. No `stickyNav`, no lesson menu, no `<!-- N -->` delimiters — this is not a module page. The acknowledgements block after the footer **is** part of every page (`18B` Section 6.8). Output is **one file**, named **`{CODE}.html`** (e.g. `US4249.html`, `AS91956.html` — never `Assessment-{CODE}.html`), delivered as a downloadable file.

---
