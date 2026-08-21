> **Last updated:** Friday, 21st August, 2026 6:30 PM
> **Granular part A (1 of 4) of `05_COMP_LANGUAGE_MEDIA_LAYOUT.md`** — COMP_12 language & specialist; COMP_13 media & embeds.
> All sibling parts live in `05_COMP_LANGUAGE_MEDIA_LAYOUT/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
> **Last updated:** Thursday, 16th July, 2026 9:30 PM

# COMP_12 — Language & Specialist

---

## Glossary

**Container class:** `glossary`

Searchable table for vocabulary/terminology:

```html
<div class="col-md-8 col-12 glossary">
    <h3 class="glossaryTitle"><span>Glossary</span></h3>
    <div class="table-responsive">
        <table class="table table-fixed search-table">
            <tr class="title-g">
                <th>Term</th>
                <th>Reading</th>
                <th>Meaning</th>
            </tr>
            <tbody>
                <tr class="title-g">
                    <th scope="row" colspan="3" class="title-g"><b>Section heading</b></th>
                </tr>
                <tr>
                    <td>Term 1</td>
                    <td></td>
                    <td>Definition 1</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
```

**Key elements:**
- `title-g` class: Makes row unsearchable (section headers)
- `search-table` class: Enables search
- Can include `audioTrigger` spans in cells

---

## Kanji Cards / Language Letter

**Container class:** `languageLetter`

```html
<div class="row languageLetter">
    <div class="col-md-8 col-12">
        <div class="row">
            <div class="letterDrop"><span class="jp-text">日</span></div>
            <div class="letterDrop"><span class="jp-text">本</span></div>
        </div>
        <div class="row">
            <div class="col-12">
                <div class="letterDropContent" letterType="video">
                    <div class="row">
                        <div class="col-6 paddingLR">
                            <p><b>on:</b> <span class="jp-text">にち</span></p>
                            <p><b>kun:</b> <span class="jp-text">ひ</span></p>
                        </div>
                        <div class="col-6 paddingLR">
                            <video class="letterVideo" muted>
                                <source src="videos/kanji.mp4" type="video/mp4">
                            </video>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

**letterType:** `video` or `iframe`

---

## Language Fonts

| Class | Language |
|-------|----------|
| `jp-text` | Japanese |
| `ch-text` | Chinese |
| `pinyin` | Pinyin |
| `sassoon-text` | Sassoon font |
| `sassoonI-text` | Sassoon Infant font |

---

## Translate Section

**Container class:** `translateSection` / `translateSectionButton`

```html
<div class="row translateSection">
    <div class="col-12 translateSectionButton"></div>
    <div class="col-12">
        <div class="translate">
            <h3>Te Reo heading</h3>
            <p>Te Reo content</p>
        </div>
        <div class="translate">
            <h3>English heading</h3>
            <p>English content</p>
        </div>
    </div>
</div>
```

Pairs of `.translate` divs toggle between languages.

---

## Reo Translate (Full Page Translate)

**Body class:** `reoTranslate`

Full-page bilingual toggle. Applies to the `<body>` element, not an inner container. Content tagged with language attributes toggles between the two languages.

```html
<body class="container-fluid reoTranslate" language="reo" translation="eng">
```

**Attributes on `<body>`:**
- `language`: Primary language code (e.g., `"reo"`)
- `translation`: Secondary language code (e.g., `"eng"`)

**Content tagging:**
```html
<!-- Bilingual headings -->
<h3 eng>English Heading</h3>
<h3 reo>Te Reo Heading</h3>

<!-- Bilingual paragraphs -->
<p eng>English content here.</p>
<p reo>Te Reo content here.</p>

<!-- Bilingual row blocks -->
<div class="row" eng>
    <div class="col-md-8 col-12">
        <div class="alert"><h4>English Alert</h4><p>Content</p></div>
    </div>
</div>
<div class="row" reo>
    <div class="col-md-8 col-12">
        <div class="alert"><h4>Te Reo Alert</h4><p>Content</p></div>
    </div>
</div>
```

**Key rules:**
- The `eng` / `reo` attributes can be applied to any element: `<p>`, `<h3>`, `<div>`, etc.
- Paired elements toggle visibility — one shows while the other hides
- Content without a language attribute is always visible (shared content)
- Activities can contain mixed language content within the same activity wrapper
- This is different from `translateSection` (inline section toggle) — reoTranslate toggles the entire page

---

## MathJax / Equations

Standard LaTeX syntax. Inline: `\( \)`. Block: `\[ \]`.

```html
<p>The quadratic formula is \(x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}\)</p>
```




# COMP_13 — Media & Embeds

---

## Video Embed

### YouTube (standard)
```html
<div class="videoSection ratio ratio-16x9">
    <iframe src="https://www.youtube-nocookie.com/embed/VIDEO_ID" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>
```

### YouTube Shorts
```html
<div class="videoSection youtubeShort ratio ratio-1x1">
    <iframe src="https://www.youtube.com/embed/SHORT_ID" frameborder="0" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>
```

### Vimeo
```html
<div class="videoSection ratio ratio-16x9">
    <iframe src="https://player.vimeo.com/video/VIDEO_ID" frameborder="0" allowfullscreen></iframe>
</div>
```

### Creative Services Videos (Vimeo) — constraint 64

**All Creative Services videos are Vimeo links.** Any video produced by Creative Services (a Te Kura in-house / Audiovisual production — e.g. an animated intro, a kaiako video, an Audiovisual item — as opposed to an external YouTube source) is embedded as a **Vimeo** `videoSection` scaffold with the video ID left **pending**, and is always accompanied by a visible `Designer/Developer To Do:` note identifying the audiovisual item the developer must embed. Emit exactly this (designer-supplied scaffold):

```html
<p style="color: red; font-weight: bold;">Designer/Developer To Do: add vimeo embed for [audiovisual item x]</p>

<div class="videoSection ratio ratio-16x9">
   <iframe src="https://player.vimeo.com/video/" loading="lazy" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe> <!-- &amp;start=0 --> <!-- &amp;end=0 -->
</div>
```

- Replace `[audiovisual item x]` with the item's actual identifier/description from the writer source or Media List (e.g. *audiovisual item 3 — module introduction video*).
- The `src` stays `https://player.vimeo.com/video/` with **no ID** — the developer appends the Vimeo ID during production. Never guess or invent a Vimeo ID.
- The scaffold's attribute set (including its `title` value) and the trailing `<!-- &amp;start=0 --> <!-- &amp;end=0 -->` time-parameter placeholders are emitted **exactly as supplied by the design team** — the two placeholders are a designer-supplied scaffold mechanism (a narrow permitted comment exception; see `02_DATA_CONTENT_VERIFICATION.md` → Comment & Red Flag Policy, exception 5) and carry no content, note, or answer.
- The deferred note takes the standard **`Designer/Developer To Do:`** prefix (red + bold) per the Source-Specific Red-Note Prefixes scheme.
- Ordinary **external YouTube** videos are unchanged (YouTube patterns above); this rule governs videos whose producer is Creative Services. Where the producer is genuinely unclear, raise a visible `Red Flag:` asking which pathway applies rather than guessing.

**TikTok embeds are no longer allowed.**

---

## Audio Player

### Standard
```html
<audio preload="none" src="audio/FILENAME.mp3" class="audioPlayer" title="Track title"></audio>
```

### With Icon
```html
<audio preload="none" src="audio/FILENAME.mp3" class="audioPlayer icon" title="max-width:300px"></audio>
```

### Audio Button (compact)
```html
<div class="audioButton" audioName="FILENAME"></div>
```

**⚠️ CRITICAL:** Audio filenames must NOT contain spaces — this causes a known bug. Use underscores or camelCase for all audio file references (e.g., `loremFull.mp3`, `track_one.mp3`, NOT `lorem full.mp3`).

---

## Embed PDF

```html
<div class="embed-responsive embed-responsive-4by3">
    <embed class="embed-responsive-item" src="pdf/filename.pdf" type="application/pdf">
</div>
```

> **Scope — this generic shape is for ordinary writer-supplied PDFs only.** It stays in force for every PDF embed that is *not* an AI Guidelines document. The eight **AI Guidelines** PDFs are a delivered central asset set with their **own** markup and their **own** eight writer tags — see *AI Guidelines PDFs (the eight teacher tags)* immediately below. **Whenever the embedded PDF is an AI Guidelines document, that block applies and this one does not.**

---

## AI Guidelines PDFs (the eight teacher tags)

**Container class:** `embedPDF` · **Object class:** `centralFile` · **Asset folder:** `AI-guidelines/`

Eight **delivered** central PDFs — Te Kura's AI use guidelines for ākonga and kaimahi. Each has its **own writer tag**. When any of the eight tags appears in a Writers Template, emit the block below with that tag's filename substituted — **never** the generic `embed-responsive` shape above, and never a placeholder, a link-only fallback or a `Designer/Developer To Do:` note: these assets exist and resolve.

**The block (Traffic Light shown — the only thing that changes between the eight is the filename):**

```html
<div class="embedPDF" layout="portrait">
<object class="centralFile" data="AI-guidelines/AI Use Guidelines Traffic Light.pdf#view=fit&amp;toolbar=0" type="application/pdf">
<p>Unable to display PDF file. <a href="AI-guidelines/AI Use Guidelines Traffic Light.pdf" target="_blank" class="centralFile">Download</a> here</p>
</object>
</div>
```

### The tag → filename registry

Copy the filename **character-for-character** from the right-hand column. Note that the tag spells the year ranges with a plain hyphen (`11-13`) while the **filename uses an en dash** (`11–13`) — that mismatch is real and deliberate; the file on the server carries the en dash.

| Writer tag (as the WT types it) | PDF filename — exact, copy verbatim |
|---|---|
| `[AI Use Guidelines Traffic Light PDF]` | `AI Use Guidelines Traffic Light.pdf` |
| `[Ākonga AI Use Guide Years 11-13 and NCEA PDF]` | `Ākonga AI Use Guide Years 11–13 and NCEA.pdf` |
| `[Ākonga AI Use Guide Years 1-6 PDF]` | `Ākonga AI Use Guide Years 1–6.pdf` |
| `[Ākonga AI Use Guide Years 7-10 PDF]` | `Ākonga AI Use Guide Years 7–10.pdf` |
| `[Kaimahi AI Guidelines - Authenticity Guidelines for Years 11-13 and NCEA PDF]` | `Kaimahi AI Guidelines - Authenticity Guidelines for Years 11–13 and NCEA.pdf` |
| `[Kaimahi AI Guidelines - Responding to Suspected use in Assessments for Years 11-13 and NCEA PDF]` | `Kaimahi AI Guidelines - Responding to Suspected use in Assessments for Years 11–13 and NCEA.pdf` |
| `[Kaimahi AI Use Guidelines Years 1-6 PDF]` | `Kaimahi AI Use Guidelines Years 1–6.pdf` |
| `[Kaimahi AI Use Guidelines Years 7-10 PDF]` | `Kaimahi AI Use Guidelines Years 7–10.pdf` |

### Build rules (all eight)

- **The filename appears TWICE** in the block and the two forms differ: in `data=` it carries the viewer fragment `#view=fit&amp;toolbar=0`; in the fallback `href=` it is **bare** — no fragment.
- **`&amp;` is an entity, not a bare `&`.** `#view=fit&amp;toolbar=0` is copied exactly.
- **`layout="portrait"` on all eight.** No landscape variant exists (designer decision, Chris, 21 August 2026).
- **Path is `AI-guidelines/` + the filename** — hyphen, lower-case `g`, no `pdf/` directory. **Spaces in the path are NOT URL-encoded** — the path is written with real spaces exactly as shown.
- **The fallback paragraph is verbatim:** `Unable to display PDF file. <a …>Download</a> here` — the word *here* sits **outside** the anchor, and `class="centralFile"` sits on the anchor as well as the `<object>`.
- **Never "correct" a filename.** The en dashes, the macron on `Ākonga`, the spaced hyphen in `Kaimahi AI Guidelines - Authenticity …`, and the lower-case `use` in `Responding to Suspected use in Assessments` are the real strings on the server. A tidied path is a broken path — the same rule that governs `congradulations/` (`14_SUBJECT_GLOBAL_PARAMETERS.md` §14.12).
- **Tolerant tag matching, exact filename out.** Recognise the tag **case-insensitively**, treat a hyphen / en dash / em dash in the year range as the **same** tag, and accept `Akonga` without the macron. Whatever form the writer typed, the emitted filename is the exact string in the table above. A near-miss is matched, never flagged.
- **These tags are DELIVERED assets and are never deferred.** Where a family rule defers PDF resources — CED Phase 5, `14_SUBJECT_GLOBAL_PARAMETERS.md` §14.4 — that deferral does **not** apply to these eight; build the block.
- **Never render the tag as visible text** (`02_DATA_CONTENT_VERIFICATION.md` → Square-Bracket Tags).

---

## Embed Padlet

```html
<div class="padletContainer" style="max-width:100%">
    <div class="padlet-embed" style="border:1px solid rgba(0,0,0,0.1);border-radius:2px;box-sizing:border-box;overflow:hidden;position:relative;width:100%;background:#F4F4F4">
        <p style="padding:0;margin:0">
            <iframe src="https://padlet.com/embed/PADLET_ID" frameborder="0" allow="camera;microphone;clipboard-read;clipboard-write" style="width:100%;height:608px;display:block;padding:0;margin:0"></iframe>
        </p>
    </div>
</div>
```

---

## Embed Desmos Graph

```html
<div class="desmosContainer">
    <iframe src="https://www.desmos.com/calculator/GRAPH_ID" style="border:0;width:100%;height:400px;" frameborder="0"></iframe>
</div>
```




