> **Last updated:** Wednesday, 29th July, 2026 5:36 PM
> **Granular part B (2 of 3) of `04_COMP_SEGMENTS_OVERLAYS.md`** — COMP_08 triggers & overlays (infoTrigger, audio, image label/zoom, word highlighter).
> All sibling parts live in `04_COMP_SEGMENTS_OVERLAYS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# COMP_08 — Triggers & Overlays
 
---
 
## Info Trigger / Hover Trigger
 
**Container class:** `infoTrigger`
 
```html
<span class="infoTrigger" info="Tooltip/definition text">trigger word</span>
```
 
---
 
## Info Trigger Image
 
**Container class:** `infoImage`
 
Interactive overlay where hoverable trigger labels are positioned over an image using percentage-based `top` and `left` inline styles. When hovered/clicked, each trigger reveals its `info` text in a popup.
 
**⚠️ CRITICAL:** This is a DOCUMENTED component — do NOT fall back to flip cards or other alternatives when encountering `[info trigger image]` or `[info trigger] image` tags. Use the `infoImage` pattern below.
 
**↪ But for a labelled DIAGRAM** — labels that point to specific **parts** of the image with leader lines and reveal text **on click** (cell/anatomical/equipment diagrams, map features) — use **`imageLabel` with `layout="labelLine"`** and `<div class="label infoTrigger">` children instead (see *Image Label → Clickable Labelled Diagram*). `infoImage` is for simple hotspot overlays **without** leader lines pointing to parts.
 
### Standard Layout
 
```html
<div class="row">
    <div class="col-md-12 col-12 infoImage">
        <img src="images/image.jpg" alt="Description" class="img-fluid">
        <p class="infoTrigger" info="Popup text for trigger 1" style="top:15%; left:25%;">Trigger label 1</p>
        <p class="infoTrigger" info="Popup text for trigger 2" style="top:40%; left:25%;">Trigger label 2</p>
        <p class="infoTrigger" info="Popup text for trigger 3" style="top:65%; left:25%;">Trigger label 3</p>
        <p class="infoTrigger" info="Popup text for trigger 4" style="top:90%; left:25%;">Trigger label 4</p>
    </div>
</div>
```
 
### Positioning Rules
 
The `.infoTrigger` elements use inline `style` attributes with percentage-based `top` and `left` values to position them over the image. Calculate positions to evenly distribute the triggers across the image area:
 
**Vertical distribution (top %):** Divide the available vertical space evenly among the number of triggers. For N triggers in a single column, use approximately `top` values from ~10–15% to ~85–90%, spaced evenly.
 
**Horizontal distribution (left %):** If triggers are in a single column, use a consistent `left` value (e.g., `25%` for left-aligned, `50%` for centred, `75%` for right-aligned). For two-column layouts, use two `left` values (e.g., `25%` and `75%`).
 
**Example — 5 triggers in single column:**
```
top: 10%, 30%, 50%, 70%, 90%  (each at left: 25%)
```
 
**Example — 8 triggers in two columns of 4:**
```
Left column:  top: 10%, 30%, 60%, 80%  (each at left: 25%)
Right column: top: 10%, 30%, 60%, 80%  (each at left: 78%)
```
 
### With Placeholder Image
 
```html
<div class="row">
    <div class="col-md-12 col-12 infoImage">
        <img class="img-fluid" loading="lazy" src="https://placehold.co/800x500?text=Interactive+Image" alt="">
        <!-- <img class="img-fluid" loading="lazy" src="images/iStock-XXXXXXXXX.jpg" alt="Description — URL"> -->
        <p class="infoTrigger" info="AI can't feel happy, sad, or excited like people do." style="top:15%; left:25%;">No feelings</p>
        <p class="infoTrigger" info="AI learns from lots of pictures, words, or data." style="top:35%; left:25%;">Needs examples</p>
        <p class="infoTrigger" info="AI sometimes gives wrong answers or guesses." style="top:55%; left:25%;">Makes mistakes</p>
        <p class="infoTrigger" info="AI follows rules and patterns. It doesn't imagine new things by itself." style="top:75%; left:25%;">No original ideas</p>
        <p class="infoTrigger" info="AI uses huge amounts of power. It is bad for the environment." style="top:90%; left:25%;">Uses lots of power</p>
    </div>
</div>
```
 
**Key rules:**
- The `.infoImage` div contains the image AND all `.infoTrigger` elements as siblings
- Triggers use `<p class="infoTrigger">` (paragraph tags, not spans) when inside `.infoImage`
- The `info` attribute holds the popup/tooltip text
- The text content of the `<p>` tag is the visible label shown on the image
- Inline `style` with percentage `top` and `left` is the ONLY permitted inline style (this is a documented pattern, NOT an invented style)
- The image should use `col-md-12 col-12` since triggers need space across the full width
---
 
## Audio Trigger
 
**Container class:** `audioTrigger`
 
```html
<span class="audioTrigger" audioName="AUDIO_FILENAME">trigger word</span>
```
 
**⚠️ CRITICAL:** Audio filenames must NOT contain spaces — this causes a known bug. Use underscores or camelCase (e.g., `loremFull`, `track_one`).
 
---
 
## Audio Image
 
**Container class:** `audioImage`
 
Clickable image that plays an associated audio file. The `id` attribute on `.audioImageOption` maps to the audio filename (without extension).
 
### Standard
```html
<div class="audioImage">
    <div id="AUDIO_FILENAME" class="audioImageOption">
        <img class="img-fluid" src="images/image.jpg">
    </div>
</div>
```
 
### With Play Button Visible
```html
<div class="audioImage">
    <div id="AUDIO_FILENAME" class="audioImageOption playVisible">
        <img class="img-fluid" src="images/image.jpg">
    </div>
</div>
```
 
### With Caption Popup
```html
<div class="audioImage">
    <div id="AUDIO_FILENAME" class="audioImageOption">
        <img class="img-fluid" src="images/image.jpg">
        <p class="popCaption">Caption text</p>
    </div>
</div>
```
 
**Key rules:**
- `id` on `.audioImageOption` = audio filename (no extension, no spaces). E.g., `id="loremFull"` → plays `audio/loremFull.mp3`
- **⚠️ CRITICAL:** Audio filenames must NOT contain spaces — causes a known bug
- `playVisible` class: Makes play button always visible (default: appears on hover)
- `popCaption`: Shows caption text on hover/click
- Typical column sizing: `col-md-4 col-6`
 
**WJFUN series — mandatory component.** In WJFUN modules a writer's `[Audio image]` grid (click-the-picture-to-hear-the-word) MUST be built with this `audioImage` / `audioImageOption` component — the audio filename goes on the `id` of `.audioImageOption` — never as `audioTrigger` spans wrapping the images. (WJFUN108 finalized report, Difference 3, scope (b), 29 July 2026.)
 
---
 
## Image Label
 
**Container class:** `imageLabel`
 
> **WHEN TO USE `imageLabel layout="labelLine"` vs `infoImage` (clickable labelled diagrams).** When the writer asks for a **labelled diagram** — labels that identify or point to specific **parts** of an image and reveal a description **on click** (cell diagrams, anatomical diagrams, equipment diagrams, map features) — build it with **`imageLabel` + `layout="labelLine"`** using `<div class="label infoTrigger" …><p>…</p></div>` children (see *Clickable Labelled Diagram* below). This is the preferred pattern for "make text drop down when students click on the labels" requests on a diagram. Reserve **`infoImage`** (positioned `<p class="infoTrigger" style="top/left">` hotspots) for **simple hotspot overlays** where labels float over an image **without leader lines** pointing to parts. Positioning in `imageLabel` uses element **attributes** (`top` / `left` / `pointTop` / `pointLeft` / `direction`), never inline `style`.
 
### Basic Label
 
```html
<div class="row imageLabel" layout="label">
    <div class="col-12">
        <img class="img-fluid imgLabel" src="images/image.jpg" alt="">
    </div>
    <div class="col-2 label" top="50%" left="30%"><p>Label 1</p></div>
    <div class="label col-4 outline" top="55%" left="50%"><p>Label 2</p></div>
</div>
```
 
### With Info Trigger
 
```html
<div class="label infoTrigger" top="40%" left="65%" info="Definition text"><p>Label</p></div>
```
 
### Map Pin Layout
 
```html
<div class="imageLabel" layout="map">
    <img class="img-fluid imgLabel" src="images/image.jpg" alt="">
    <div class="label" direction="horizontal" top="25%" left="50%" pointTop="30%" pointLeft="80%"><p>Label</p></div>
</div>
```
 
### Label Line Layout
 
```html
<div class="imageLabel" layout="labelLine">
    <img class="img-fluid imgLabel" src="images/image.jpg" alt="">
    <div class="label" direction="horizontal" top="10%" left="40%" pointTop="20%" pointLeft="20%"><p>Label</p></div>
    <div class="label" direction="vertical" top="70%" left="70%" pointTop="90%" pointLeft="50%"><p>Label</p></div>
</div>
```
 
### Clickable Labelled Diagram (label + infoTrigger)
 
Use this when each label must **reveal a description on click** (the "drop down text when students click the labels" request on a diagram). Each label is a `<div class="label infoTrigger">` carrying the description in its `info` attribute, positioned with `top`/`left`, with the leader-line endpoint set by `pointTop`/`pointLeft`. The label text is wrapped in `<p>`. The whole block sits inside the standard `col-md-8 col-12` content column.
 
```html
<div class="imageLabel" layout="labelLine">
    <img class="img-fluid imgLabel" src="images/animal-cell-diagram.png" alt="Simple diagram of animal cell">
    <div class="label infoTrigger" info="The cell membrane is a thin layer that surrounds the cell and holds it together." direction="horizontal" top="10%" left="10%" pointTop="20%" pointLeft="30%"><p>Cell membrane</p></div>
    <div class="label infoTrigger" info="The nucleus has DNA inside it, which carries the instructions for how the cell works." direction="horizontal" top="90%" left="90%" pointTop="50%" pointLeft="50%"><p>Nucleus</p></div>
</div>
```
 
- Wrapper is `imageLabel` (NOT `infoImage`); image carries `imgLabel`.
- Labels are `<div class="label infoTrigger">` (NOT `<span class="infoTrigger">` / `<p class="infoTrigger">`), with the label text inside a `<p>`.
- Positioning is by **attributes** (`top` / `left` / `pointTop` / `pointLeft` / `direction`) — never inline `style`.
- The `info` attribute holds the click-reveal description.
### Relative Label Line
 
```html
<div class="imageLabel relative" layout="labelLine">
    <div class="row">
        <div class="col-10 paddingR">
            <img class="img-fluid imgLabel" src="images/image.jpg" alt="">
        </div>
        <div class="col-2 paddingL">
            <div class="label" direction="horizontal" pointTop="20%" pointLeft="20%"><p>Label</p></div>
        </div>
    </div>
</div>
```
 
### Combined with Drag & Drop (Scatter)
 
```html
<div class="dragAndDrop" layout="scatter">
    <div class="row dropContainer">
        <div class="imageLabel" layout="labelLine">
            <div class="label drop col-2 secDrop" option="1" direction="horizontal" top="10%" left="40%" pointTop="20%" pointLeft="20%"><p class="white-text">Test</p></div>
            <img class="img-fluid imgLabel" src="images/image.jpg" alt="">
        </div>
    </div>
    <div class="row">
        <div class="drag dragLabel col-2" option="1"><p>Answer</p></div>
    </div>
</div>
```
 
**Modifier classes:** `outline`, `diagonal`, `white-text`
**Direction values:** `horizontal`, `vertical`
 
---
 
## Image Zoom
 
**Container class:** `imageZoom`
 
```html
<div class="imageZoom" layout="hoverFollow" scale="1.5">
    <img src="images/image.jpg" alt="" class="img-fluid">
</div>
```
 
**Layout:** Only `hoverFollow` is active (hover/hoverContained are deprecated).
**Scale:** Zoom multiplier (e.g., `"1.5"`, `"2"`)
 
---
 
## Word Highlighter
 
**Container class:** `wordHighlighter`
 
The `wordHighlighter` wrapper has two forms.
 
### Static colour-coded analysis (reference layout)
 
A `wordHighlighter` wrapper around a table whose cells carry bare `<span colour="primary-N">` elements. Used for fixed, pre-coloured analysis (e.g. labelling subject / verb / object). The colours are presentational only — the student does not click them.
 
```html
<div class="table-responsive wordHighlighter">
    <table class="table table-bordered">
        <tr>
            <th></th>
            <th>Pattern description</th>
        </tr>
        <tr>
            <th>English structure</th>
            <td><span colour="primary-1">Subject</span> <span colour="primary-2">verb</span> <span colour="primary-3">object</span></td>
        </tr>
    </table>
</div>
```
 
### Interactive in-text highlighter
 
When the writer marks words inside running prose for the student to click and colour-highlight (the `✅word [word highlighter]` pattern in the source), use the interactive form:
 
- **Wrap the section that contains the highlightable text in a `wordHighlighter` container.** This can be a standalone `<div class="wordHighlighter">` around the paragraph(s), OR — when the text lives inside an accordion — the class is added to the accordion's content div: `<div class="accContent wordHighlighter">`. The wrapper is what activates the click-to-highlight behaviour for everything inside it.
- **Each clickable word is a `<span class="highlightBtn" colour="primary-N">word</span>`.** The `highlightBtn` class is what makes the span clickable / interactive.
Standalone wrapper:
 
```html
<div class="wordHighlighter">
    <p>These parts are the <span class="highlightBtn" colour="primary-1">beginning</span>, the <span class="highlightBtn" colour="primary-2">middle</span> and the <span class="highlightBtn" colour="primary-3">end</span>.</p>
</div>
```
 
Inside an accordion (wrapper added to `accContent`):
 
```html
<div class="accContent wordHighlighter">
    <p>Rachel and Alex's favourite holiday activity was going to the local swimming pool. <span class="highlightBtn" colour="primary-2">It</span> was usually a little crowded, but that didn't matter. <span class="highlightBtn" colour="primary-1">They</span> loved jumping in the water and playing with everyone else.</p>
</div>
```
 
**Colour attributes:** `colour="primary-1"`, `colour="primary-2"`, `colour="primary-3"`
 
**`highlightBtn` vs bare `colour` span:**
- `<span class="highlightBtn" colour="primary-N">word</span>` → an **interactive** highlight the student clicks. Only valid inside a `wordHighlighter` wrapper.
- `<span colour="primary-N">word</span>` (NO `highlightBtn`) → a **static** colour reference — e.g. when re-citing a previously-highlighted word inside a later quiz question or sentence. Keep it bare; do NOT add `highlightBtn`.
