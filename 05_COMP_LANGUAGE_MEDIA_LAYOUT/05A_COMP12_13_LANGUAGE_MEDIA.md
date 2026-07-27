> **Last updated:** Thursday, 16th July, 2026 9:30 PM
> **Granular part A (1 of 3) of `05_COMP_LANGUAGE_MEDIA_LAYOUT.md`** — COMP_12 language & specialist; COMP_13 media & embeds.
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




