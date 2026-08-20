> **Last updated:** Friday, 21st August, 2026
> **Granular part E (5 of 5) of `01_PIPELINE_EXTRACTION_TAGS.md`** — Tag interpretation: structural, headings, body, media, styling, activities, links.
> All sibling parts live in `01_PIPELINE_EXTRACTION_TAGS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# 05 — Tag Interpretation

> **When to load:** During Phase 5, when mapping normalised tags to HTML components.
> **For interactive components:** Also load the relevant component section from `03_COMP_CORE_INTERACTIVES.md` (COMP_00–COMP_06), `04_COMP_SEGMENTS_OVERLAYS.md` (COMP_07–COMP_11), or `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` (COMP_12–COMP_14).

---

## Structural & Page Tags

| Normalised Tag | HTML Action |
|---|---|
| `title_bar` | Header section: `<div id="header">` with module code + title |
| `module_introduction` | Module intro content inside `<div id="body">` |
| `lesson` + number | New lesson page with its own header |
| `lesson_overview` | Module menu content for the lesson page (use simplified or full tabs — see section 01) |
| `lesson_content` | Signals start of body content (no HTML output for tag itself) |
| `end_page` | End of current page — apply Page Boundary Validation first |

---

## Headings

| Normalised | HTML |
|---|---|
| `heading` level 1 | `<h1>` in header; `<h2>` in body context |
| `heading` level 2 | `<h2>` (no span — spans only used in `<h1>` header titles) |
| `heading` level 3 | `<h3>` (no span) |
| `heading` level 4 | `<h4>` (no span) |
| `heading` level 5 | `<h5>` (no span) |

**⚠️ Drop a body heading that duplicates the `<h1>` header title.** On a lesson page the **lesson's own title** already appears in the header `<h1><span>` (constraint 79), so the heading this normally drops is the lesson's opening `[H2]` — compare ignoring any leading `Lesson N` / `Lesson N:` prefix, and note that dropping the duplicate is **never** a reason to leave the header title empty or fall back to the module title. If the writer's body heading (typically an `[H2]` or `[H3]`) repeats that same title text — e.g. header `<h1><span>Inside animal cells</span></h1>` followed by a body `<h3>Inside animal cells</h3>` — **omit the redundant body heading entirely** and let the first body `<p>` follow directly. This is a documented *casing/format* normalisation, not a wording change: it removes a duplicate, it does not alter any writer text. Only drop the body heading when its text is **identical** (ignoring case/punctuation) to the h1 header title; a body heading that introduces a *different* sub-topic is kept as a normal `<h3>`.

---

## Body Text

| Normalised | HTML |
|---|---|
| `body` | `<p>` paragraph |

---

## Media

### Video
Extract video ID from any YouTube URL, embed using:
```html
<div class="videoSection ratio ratio-16x9">
    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/VIDEO_ID" loading="lazy" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
```

YouTube Shorts:
```html
<div class="videoSection youtubeShort ratio ratio-1x1">
    <iframe src="https://www.youtube.com/embed/SHORT_ID" frameborder="0" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>
```

Vimeo:
```html
<div class="videoSection ratio ratio-16x9">
    <iframe src="https://player.vimeo.com/video/VIDEO_ID" frameborder="0" allowfullscreen></iframe>
</div>
```

**Creative Services videos are Vimeo (constraint 64).** Any video produced by Creative Services (a Te Kura in-house / Audiovisual production, as opposed to an external YouTube source) is embedded as a **Vimeo** `videoSection` scaffold with the video ID left pending, accompanied by a visible `Designer/Developer To Do:` note identifying the audiovisual item — never a YouTube embed and never a bare placeholder. Full scaffold and rules: `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` → Video Embed → Creative Services Videos (Vimeo).

TikTok embeds are **no longer allowed**.

### Images

**⚠️ IMAGE OUTPUT MODE — ALWAYS determine before generating any HTML.**

Different designers have different preferences for how writer-referenced images are represented in the output HTML. Before generating any HTML, determine which of the two modes applies for this conversion:

- **Mode P — Placeholder Mode:** Generate a visible `placehold.co` placeholder AND include the real `images/iStock-XXXXXXXXX.jpg` reference as a commented-out `<img>` tag for CS to swap in later.
- **Mode D — Direct Link Mode:** Skip the `placehold.co` placeholder entirely. Emit a single clean `<img>` tag pointing directly to the anticipated `images/iStock-XXXXXXXXX.jpg` filename. No HTML comment block is needed — the actual filename in `src` is sufficient.

**How to select the mode:**
- If the user has stated a preference in their initial message or at any point during the conversation (e.g., "use placeholders", "I'm a direct-link designer", "skip placeholders", "just link the images directly"), use that mode silently.
- If the user has NOT stated a preference, **ALWAYS prompt before proceeding.** Ask once at the start of the conversion:

  *"Which image output mode would you like?*
  *• **Placeholder Mode** — visible placehold.co placeholders with the real image references commented out for CS to swap in later.*
  *• **Direct Link Mode** — direct image filenames (e.g., images/iStock-XXXXXXXXX.jpg) with no placeholder or comment block."*

- Do NOT silently default to either mode. The prompt is mandatory when no preference has been stated.

The mode applies uniformly to ALL images in the conversion. Do NOT mix modes within a single output file.

---

#### Mode P — Placeholder Mode

Default fallback placeholder (when writer gives no image reference at all): `<img class="img-fluid" loading="lazy" src="https://placehold.co/600x400?text=Image+Placeholder" alt="">`

When the writer provides an image reference (e.g., iStock URL, filename, or description), generate a **visible** placeholder using the placehold.co service AND retain the original iStock reference as a **commented-out** `<img>` tag for CS to replace later.

**Placeholder pattern:**
```html
<img class="img-fluid" loading="lazy" src="https://placehold.co/600x400?text=AI+Robot+Image" alt="">
<!-- <img class="img-fluid" loading="lazy" src="images/iStock-957693546.jpg" alt="AI robot image — https://www.istockphoto.com/photo/..."> -->
```

**placehold.co service rules:**
- **Base URL:** `https://placehold.co/{width}x{height}`
- Use `+` for spaces in the `text` parameter, e.g., `?text=AI+Robot+Image`
- Use `\n` for new lines in the `text` parameter
- Keep text brief (2–4 words summarising what the image should be)
- Default format is SVG (no extension needed)
- Colour can be customised: `https://placehold.co/600x400/EEE/999?text=...`

**Intelligent dimension selection:**
| Context | Dimensions | Reasoning |
|---|---|---|
| Standard content image | `600x400` | Standard 3:2 landscape in body column |
| Sidebar image | `400x300` | Smaller 4:3 for `col-md-4` sidebars |
| Full-width image (col-12) | `800x400` | Wide 2:1 for full-width contexts |
| Square image (character, avatar, icon) | `300x300` | 1:1 for character assets or profile images |
| Speech bubble character | `200x200` | Small 1:1 for `col-2` character images |
| Carousel/slide image | `700x400` | 7:4 landscape for slider/carousel contexts |
| Scatter/label background | `800x500` | Large landscape for image label or scatter D&D |
| Flip card / memory card | `300x200` | Compact 3:2 for card-based components |
| Activity sidebar image (`alertImage`) | `400x400` | Square or near-square for `alertImage` |
| Info trigger image background | `800x500` | Large landscape for `infoImage` overlay |

**Commented-out iStock tag rules (Mode P):**
- The commented-out `<img>` tag MUST follow the syntax `images/iStock-XXXXXXXXX.jpg`
- Extract the iStock ID from the writer's URL if available: the ID is the number **immediately following `gm`** in the URL slug (constraint 61)
  - **Dual-ID URLs** (the current iStock format) carry two hyphen-separated numbers after `gm` — `gm{A}-{B}` (e.g. `gm2194652495-612793002`). The ID is **`A`**, the first number (→ `iStock-2194652495`). The trailing number `B` is a secondary catalogue identifier and is **NEVER** used — not for filenames, not for acknowledgements, not for acks-file matching. The correct ID always matches the asset page's **"Stock photo ID"** field.
  - **Single-ID URLs** (the legacy format) carry one number — `gm{A}` (e.g. `gm957693546` → `iStock-957693546`)
- Include the full iStock URL in the `alt` attribute of the commented-out tag for CS reference
- If no iStock ID can be extracted, use a descriptive filename: `images/iStock-DESCRIPTION.jpg`
- The comment is for CS to later download and link the correct stock image

Always include `class="img-fluid"` and `alt=""` on the visible placeholder, plus `loading="lazy"` — **except** where the placeholder sits inside a **moving-or-draggable interactive**, which carries no `loading` attribute at all (see *No `loading="lazy"` inside moving interactives* under Rules Common to Both Modes below; constraint 83). Placeholders follow the same rule as real images.

---

#### Mode D — Direct Link Mode

Emit a single clean `<img>` tag pointing at the anticipated final filename in the `images/` directory. No `placehold.co` URL is produced in this mode. **No HTML comment block is needed** — since the actual image filename is already in the `src` attribute, there is no need to duplicate image details in a comment.

**Direct-link pattern (iStock source):**
```html
<img class="img-fluid" loading="lazy" src="images/iStock-957693546.jpg" alt="AI robot hand reaching out">
```

**Filename construction rules (Mode D):**

1. **iStock images (preferred, most common):**
   - Filename MUST follow the exact syntax `iStock-XXXXXXXXX.jpg` (capital `i`, capital `S`, hyphen, numeric ID, `.jpg` extension)
   - Extract the numeric ID from the writer's URL: the ID is the number **immediately following `gm`** in the URL slug (extraction aid: `gm(\d+)(?:-\d+)?` — capture group 1 is the ID; constraint 61)
     - **Dual-ID URLs** (the current iStock format) carry two hyphen-separated numbers after `gm` — `gm{A}-{B}` (e.g. `gm2194652495-612793002`). The ID is **`A`**, the first number (→ `iStock-2194652495.jpg`). The trailing number `B` is a secondary catalogue identifier and is **NEVER** used — not for filenames, not for acknowledgements citations, not for acks-file matching. The correct ID always matches the asset page's **"Stock photo ID"** field (and the preview-image watermark ID).
     - **Single-ID URLs** (the legacy format) carry one number — `gm{A}` (e.g. `gm957693546` → `iStock-957693546.jpg`)
   - Path is always `images/iStock-XXXXXXXXX.jpg` (lower-case `images/` directory)
   - Do NOT invent an ID if none is given — see fallback rules below

2. **Non-iStock images (Unsplash, Pexels, Pixabay, Shutterstock, Adobe Stock, writer-supplied photos, etc.):**
   - Structure the filename logically based on the source and available identifiers
   - Common patterns by source:
     | Source | Filename pattern | Example |
     |---|---|---|
     | Unsplash | `unsplash-{photo-id}.jpg` | `unsplash-abc123xyz.jpg` |
     | Pexels | `pexels-{photo-id}.jpg` | `pexels-1234567.jpg` |
     | Pixabay | `pixabay-{photo-id}.jpg` | `pixabay-5678910.jpg` |
     | Shutterstock | `shutterstock-{photo-id}.jpg` | `shutterstock-2345678901.jpg` |
     | Adobe Stock | `adobestock-{photo-id}.jpg` | `adobestock-123456789.jpg` |
     | Flickr | `flickr-{photo-id}.jpg` | `flickr-49876543210.jpg` |
     | Wikimedia / Creative Commons | `wiki-{short-descriptor}.jpg` | `wiki-mount-cook.jpg` |
     | Writer-supplied / custom photo | `{short-kebab-case-description}.jpg` | `principal-headshot.jpg`, `school-library-view.jpg` |
     | Unknown / source not identifiable | `{short-kebab-case-description}.jpg` | `ai-robot-illustration.jpg` |
   - Use lowercase kebab-case for descriptive portions (words separated by hyphens, no spaces, no underscores)
   - Keep descriptors short — 2 to 5 words maximum
   - Default extension is `.jpg`; use `.png` only when transparency is clearly implied (e.g., character cut-outs, icons, logos) and `.gif`/`.svg` only when the writer explicitly specifies

3. **Fallback — no identifiable source or ID:**
   - Use a descriptive iStock-style filename: `iStock-DESCRIPTION.jpg` where `DESCRIPTION` is a short UPPER-CASE-OR-KEBAB-CASE tag (e.g., `iStock-AI-ROBOT.jpg`)
   - This signals to the designer that the ID still needs to be sourced

**`alt` attribute (Mode D):**
- Populate the `alt` attribute on the live `<img>` with a short descriptive value — not an empty string
- Keep alt text concise (under ~125 characters), descriptive, and free of the phrases "image of", "picture of", and **"stock photo"** (the words *stock photo* must never appear in alt text)
- For an **iStock** image, prefer the **iStock/Getty API image name** as the alt value — see *Alt text content* under Rules Common to Both Modes below
- If the image is purely decorative (e.g., a divider, a background flourish with no informational content), use `alt=""`

**Attributes (Mode D) — same as Mode P except for `src` and `alt`:**
- `class="img-fluid"` — always
- `loading="lazy"` — always, **except inside a moving-or-draggable interactive** (see *No `loading="lazy"` inside moving interactives* under Rules Common to Both Modes below)
- Any component-specific classes required by the surrounding structure (e.g., `canvasImage` inside sketcher, `bubble-img` inside speech bubble) apply equally in Mode D

**Worked example — non-iStock, Unsplash source:**
```html
<img class="img-fluid" loading="lazy" src="images/unsplash-abc123xyz.jpg" alt="Students working together on a laptop">
```

**Worked example — fallback, no source identifiable:**
```html
<img class="img-fluid" loading="lazy" src="images/iStock-WATER-CYCLE-DIAGRAM.jpg" alt="Diagram of the water cycle">
```

---

#### Rules Common to Both Modes

**⚠️ CRITICAL — No imageCentral:** Do NOT add the `imageCentral` class to any writer-specified images, in either mode. This class is reserved for centralised template assets only (e.g., self-reflection emoji). Adding it to writer images causes a filepath prefix that breaks the image path. See COMP_09 in `04_COMP_SEGMENTS_OVERLAYS.md` for details.

**⚠️ CRITICAL — No `loading="lazy"` inside moving interactives (constraint 83).** `loading="lazy"` defers an image until the browser decides it is near the viewport. That is right for ordinary page images and **wrong** for an image the student drags, flips, or watches slide past: a deferred image can arrive late, arrive mid-animation, or arrive with the wrong measured size, which breaks the interactive's positioning and hit-detection. **Omit `loading="lazy"` from EVERY `<img>` inside these components** — in both image output modes, for real images and placeholders alike:

| Component | Container class | Why |
|---|---|---|
| **Rotating banner** | `.rotateBanner` / `.bannerContainer` / `.bannerItem` | Images move continuously; a late image breaks the rotation |
| **Carousel** | `.carousel` / `.viewer` / `.item` | Off-screen slides are lazily deferred and arrive blank when swiped to |
| **Drag and drop** | `.dragAndDrop` (`.drag`, `.drop`, `.ddContainer`, `.ddColumn`) | The student physically moves the image; drag positioning needs its real dimensions up front |
| **Click drop** | `.clickDrop` / `.clickDropContent` | Panel images sit hidden until revealed, so they are never "near the viewport" |
| **Flip card** | `.flipCard` (`.front`, `.front flipImage`, `.back`) | Card faces animate; a deferred face flips blank |
| **Memory game** | `.memoryGame` (`.memCard`, `.cardHidden`) | Hidden card faces must be loaded before the first reveal, or a card turns up empty |
| **Sketcher** | `.canvasContainer` | Lazy loading breaks canvas overlay alignment and event handling (the original case — see COMP_11) |

**Everything else keeps `loading="lazy"`.** Static content images, `alertImage` images, speech-bubble character images, accordion and tab-panel images, self-reflection emoji, and images the student only *clicks* without any movement (e.g. `infoImage` / `infoTrigger` hotspots, `imageLabel` diagrams) are unaffected — they carry `loading="lazy"` exactly as before. **The test when a new component appears:** does an image inside it *move*, animate, or get dragged by the student? If yes, drop `loading="lazy"`. If the image only sits still while something is drawn on top of or beside it, keep it.

**⚠️ CRITICAL — Sketcher images:** Inside `.canvasContainer` the image MUST also have the `canvasImage` class (in addition to carrying no `loading="lazy"`), regardless of image output mode. See COMP_11 in `04_COMP_SEGMENTS_OVERLAYS.md`.

**⚠️ CRITICAL — Component-specific structural rules take precedence:** If a component section in `03_COMP_CORE_INTERACTIVES.md`, `04_COMP_SEGMENTS_OVERLAYS.md`, or `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` specifies required classes, attributes, or wrappers on an image, those requirements apply in both modes. The image output mode only governs the `src`, the `alt`, and whether a placeholder is used — not the component structure around the image.

**⚠️ CRITICAL — Missing image references:** If the writer template references an image position but provides no URL, filename, or usable description, still emit an image tag per the active mode:
- Mode P → `placehold.co` placeholder with generic descriptive text + empty commented-out reference
- Mode D → fallback filename (`images/iStock-DESCRIPTION.jpg`) with no comment block

Never silently omit the `<img>` tag — downstream CS/design workflows rely on seeing every intended image position in the output.

---

**Alt text content (both modes):**

The descriptive `alt` value — written on the **Mode D** live `<img>` and on the **Mode P** commented-out reference `<img>` alike — follows the same rules:

- Keep it concise (under ~125 characters) and descriptive.
- **Never** use the phrases "image of", "picture of", or **"stock photo"** — the words *stock photo* must not appear in any alt text. (This is an **alt-text-only** prohibition: an acknowledgements entry title that officially ends in ". stock photo" keeps that suffix in the acks block — constraint 66 — because the acks cite the published title verbatim, while alt text is a brief description for screen readers and drops platform-title suffixes.)
- **For an iStock image, prioritise the iStock/Getty API image name** as the alt value. When a developer has supplied an **iStock acknowledgements file** (see iStock Acknowledgements File in Section 02), use the descriptive name from the matching line — the text between `Photo:` and `, iStock [ID]` (e.g. *"Confident boy sitting on bicycle in the forest"*). Otherwise recover the descriptive name from the iStock link / asset slug. Only when no API name is available, fall back to a short writer-derived description.
- Purely decorative images use `alt=""` in both modes.

---

**Caption text under an image (`captionText`):**
 
When a paragraph's only job is to **describe or caption an image** — a short line sitting directly under an image that names or explains it (e.g. "Kuirau Park, Rotorua", "This is Robert Hooke's drawing of cork cells.") — give that `<p>` the `captionText` class:
 
```html
<img class="img-fluid" loading="lazy" src="images/iStock-XXXXXXXXX.jpg" alt="Kuirau Park, Rotorua">
<p class="captionText">Kuirau Park, Rotorua</p>
```
 
This applies **universally and in every context** — standalone images, images inside columns, and images inside an **accordion** or other component content — wherever a caption `<p>` accompanies an image. It is the plain-`<p>` caption that follows an image; it is distinct from the hover-overlay `captionImage` component below (which is only used when the writer asks for a caption that appears *on* the image on hover). Body paragraphs that are ordinary prose (not captions for a specific adjacent image) stay as plain `<p>`.
 
**Caption images:**

*Mode P:*
```html
<div class="captionImage">
    <div class="captionTrigger">
        <img class="img-fluid" loading="lazy" src="https://placehold.co/600x400?text=Caption+Image" alt="">
        <!-- <img class="img-fluid" loading="lazy" src="images/iStock-XXXXXXXXX.jpg" alt="Description — URL"> -->
        <div class="caption" type="dark"><p>Caption text</p></div>
    </div>
</div>
```

*Mode D:*
```html
<div class="captionImage">
    <div class="captionTrigger">
        <img class="img-fluid" loading="lazy" src="images/iStock-957693546.jpg" alt="Short descriptive alt">
        <div class="caption" type="dark"><p>Caption text</p></div>
    </div>
</div>
```

### Audio
```html
<audio preload="none" src="audio/FILENAME.mp3" class="audioPlayer icon" title="max-width:300px"></audio>
```

**⚠️ CRITICAL:** Audio filenames must NOT contain spaces — this causes a known bug. Use underscores or camelCase (e.g., `loremFull.mp3`, `track_one.mp3`).

Inline audio trigger:
```html
<span class="audioTrigger" audioName="AUDIO_FILENAME">trigger word</span>
```

**Audio in table cells:** When `[audio trigger]` appears inside table cells, implement as `<div class="audioButton" audioName="FILENAME"></div>` (compact play button) rather than `<span class="audioTrigger">` (inline trigger). The `audioButton` is more appropriate for tabular contexts where a distinct play icon is needed rather than inline text. CS may add a `_01` suffix to processed audio filenames — use the writer's original filename as the base but note that CS will update during production.

### Audio Image
Clickable image that plays associated audio. See COMP_08 in `04_COMP_SEGMENTS_OVERLAYS.md` for full HTML structure.

```html
<div class="audioImage">
    <div id="AUDIO_FILENAME" class="audioImageOption">
        <img class="img-fluid" src="images/image.jpg">
    </div>
</div>
```

---

## Content Styling

| Normalised | HTML |
|---|---|
| `alert` | `<div class="alert"><div class="row"><div class="col-12"><p>content</p></div></div></div>` |
| `important` | `<div class="alert solid"><div class="row"><div class="col-12"><p>content</p></div></div></div>` |
| `alert_cultural_wananga` | `<div class="alert cultural" layout="wananga"><div class="row"><div class="col-12"><p>content</p></div></div></div>` |
| `alert_cultural_talanoa` | `<div class="alert cultural" layout="talanoa"><div class="row"><div class="col-12"><p>content</p></div></div></div>` |
| `alert_cultural_combined` | `<div class="alert cultural" layout="combined"><div class="row"><div class="col-12"><p>content</p></div></div></div>` |
| `whakatauki` | `<div class="whakatauki"><p>Māori text</p><p>English text</p></div>` |
| `quote` | `<p class="quoteText">"Quote"</p><p class="quoteAck">Attribution</p>` |
| `rhetorical_question` | `<div class="rhetoricalQuestion"><p>Question text</p></div>` |
| `reo_translate` | Body class `reoTranslate` + `language`/`translation` attributes. See COMP_12 in `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` |

---

## Activities

| Normalised | HTML |
|---|---|
| `activity` + ID (interactive) | `<div class="activity interactive" number="ID">` |
| `activity` + ID (text/workbook) | `<div class="activity alertPadding" number="ID">` |
| `activity` + ID (dropbox) | `<div class="activity alertPadding dropbox" number="ID">` |
| `activity_heading` | `<h3>Activity heading text</h3>` within activity |
| `end_activity` | Closing `</div>` for activity container |

**Dropbox trigger — BLL series:** *for BLL-series modules,* append the `dropbox` modifier to any activity that ends in an **Upload to dropbox** button (or carries `[trigger engagement]` on it) — e.g. `activity dropbox` (no interactive) or `activity interactive dropbox` (with an interactive). Applies to BLL modules only; see `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` → Activities for the full condition.

Activity sidebar:
```html
<div class="col-md-4 offset-md-0 col-12">
    <div class="alertActivity"><h4>Note</h4><p>Text</p></div>
</div>
```

---

## Links & Buttons

| Normalised | HTML |
|---|---|
| `button` | `<a href="URL" target="_blank"><div class="button">Text</div></a>` |
| `external_link_button` | `<a href="URL" target="_blank"><div class="externalButton">Text</div></a>` |
| `external_link` — **standalone** (own line/paragraph) | `<a href="URL" target="_blank"><div class="externalButton">Text</div></a>` (constraint 75) |
| `external_link` — **inline** (inside prose, a list item, or a table cell) | `<a href="URL" target="_blank">Text</a>` |
| `engagement_quiz_button` | External quiz link button |
| `mtk_quiz` | **A numbered `activity` box (next consecutive number, even where the writer assigned none) holding ONLY these children, in order:** `<h3>` quiz title (default `Quiz`, or the writer's own title verbatim) → the writer's quiz instructions as normal `<p>` text (**omitted where the writer supplied none**) → a visible `Designer/Developer To Do:` note (create the quiz in MTK DEV and orgunit link it to the module) → `<a href="#" target="_blank"><div class="button">Go to quiz</div></a>`. **NEVER the quiz's own questions, options or answers** — silently omitted, no `Red Flag:` (constraint 65 / CL-0082). **NEVER a dropbox button.** See `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` → Buttons → MTK Quiz |
| `supervisor_button` | The **`super-content-button` family** (Shape A activity-integrated / Shape B section standalone / Shape C section paired — outer `<div class="row supervisor">`); the legacy `supervisorContainer`/`supervisorButton`/`supervisorContent` trio is **RETIRED — never emit it** (constraint 68). See `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` → Supervisor Button for the full decision tree and templates |
| `modal_button` | `<div class="button TKmodalButton">Text</div>` + `<div class="TKmodal" size="S"><p>Content</p></div>` |
| `audio_button` | `<div class="audioButton" audioName="">` |

---

## Interactive Components

**For every interactive, consult the relevant component section from `03_COMP_CORE_INTERACTIVES.md`, `04_COMP_SEGMENTS_OVERLAYS.md`, or `05_COMP_LANGUAGE_MEDIA_LAYOUT.md`.**

The normalised tag tells you which component; the data pattern (see section 06 in `02_DATA_CONTENT_VERIFICATION.md`) tells you how to extract the data; the component section gives you the exact HTML structure.

### Info Trigger Image

| Normalised | HTML |
|---|---|
| `info_trigger_image` | `infoImage` container with positioned `infoTrigger` elements. See COMP_08 in `04_COMP_SEGMENTS_OVERLAYS.md` for full structure. |

**⚠️ CRITICAL:** This is a DOCUMENTED component. Do NOT fall back to flip cards, accordions, or other alternatives. Use the `infoImage` pattern with `infoTrigger` elements positioned over the image using percentage-based `top` and `left` inline styles. See Pattern 12 in section 06 of `02_DATA_CONTENT_VERIFICATION.md` for data extraction and COMP_08 in `04_COMP_SEGMENTS_OVERLAYS.md` for the HTML structure.