> **Last updated:** Wednesday, 29th July, 2026 6:41 PM
> **Granular part C (3 of 3) of `04_COMP_SEGMENTS_OVERLAYS.md`** — COMP_09 speech bubbles; COMP_10 diagrams & timelines; COMP_11 drawing tools.
> All sibling parts live in `04_COMP_SEGMENTS_OVERLAYS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# COMP_09 — Speech Bubbles
 
**Container class:** `speechBubble`
 
---
 
## Basic Conversation Layout
 
```html
<div class="row speechBubble" layout="speech">
    <div class="col-2">
        <img class="img-fluid bubble-img" alt="" src="images/character1.png">
    </div>
    <div class="col-md-4 col-10">
        <div class="bubble-right no-hover">
            <p>Character 1 speaks</p>
        </div>
    </div>
    <div class="col-md-4 col-10">
        <div class="bubble-left primary-4 no-hover">
            <p>Character 2 responds</p>
        </div>
    </div>
    <div class="col-2">
        <img class="img-fluid bubble-img" alt="" src="images/character2.png">
    </div>
</div>
```
 
---
 
## No-Hover Rule
 
**⚠️ CRITICAL:** When a speech bubble displays static text (no interactive functionality such as audio triggers or clickable elements), the bubble div MUST include the `no-hover` class. This prevents unwanted hover interactivity on display-only bubbles.
 
- **Text-only bubble → ALWAYS add `no-hover`**
- **Bubble with audio trigger / audioButton → `no-hover` is already shown in audio examples (standard pattern)**
- **Bubble used as interactive clickable element → do NOT add `no-hover`**
```html
<!-- CORRECT: Display-only bubble with no-hover -->
<div class="bubble-left no-hover">
    <p>Static text content here.</p>
</div>
 
<!-- CORRECT: Audio bubble (also uses no-hover) -->
<div class="bubble-right no-hover">
    <div class="audioButton" audioName="filename"></div>
</div>
 
<!-- CORRECT: Interactive/clickable bubble — NO no-hover -->
<div class="bubble-right">
    <p>Click me for something interactive</p>
</div>
```
 
---
 
## imageCentral Rule
 
**⚠️ CRITICAL:** The `imageCentral` class MUST NOT be added to any images that are specified within the Writers Template. This class causes a filepath prefix to be added which assumes the images are part of a predetermined centralised repository (e.g., `Character_assets/`). Since writer-specified images use the standard `images/` directory (or placeholder URLs), adding `imageCentral` will break the image path.
 
**Use `imageCentral` ONLY for:** Pre-existing centralised assets such as self-reflection emoji images (`self-reflection-emoji/`) that are part of the template system itself — NOT for any content images from the writer.
 
```html
<!-- CORRECT: Writer-specified character image — NO imageCentral -->
<img class="img-fluid bubble-img" alt="" src="images/character.png">
 
<!-- CORRECT: Placeholder character image — NO imageCentral -->
<img class="img-fluid bubble-img" alt="" loading="lazy" src="https://placehold.co/200x200?text=Character">
 
<!-- CORRECT: System emoji (centralised asset) — imageCentral is OK -->
<img loading="lazy" src="self-reflection-emoji/happy.png" alt="" class="img-fluid imageCentral">
```
 
---
 
## Bubble Direction Classes
 
| Class | Use |
|-------|-----|
| `bubble-right` | Points right (speaker on left) |
| `bubble-left` | Points left (speaker on right) |
| `bubble-top` | Points up |
| `bubble-bottom` | Points down |
| `bubble-basic` | No directional pointer |
 
---
 
## Colour Modifier Classes
 
Apply to bubble div: `primary-1`, `primary-2`, `primary-3`, `primary-4`, `secondary-1`, `secondary-2`, `tertiary-1`, `tertiary-2`
 
**Observed values (HPE, CL-0067):** `primary-light` and `secondary-light` — existing template classes recorded from the designer-refined HPRE301 files (see `14` §14.8). Not invented; use within the HPE patterns that document them.
 
---
 
## Other Modifier Classes
 
| Class | Effect |
|-------|--------|
| `no-hover` | Disables hover colour change — **REQUIRED for all display-only bubbles** |
| `left` | Additional left alignment (bubble-top/bottom) |
| `right` | Additional right alignment (bubble-top/bottom) |
 
---
 
## With Audio
 
```html
<div class="bubble-right no-hover">
    <div class="audioButton" audioName="filename"></div>
</div>
```
 
**Hover-to-play:** `<div class="audioButton" hover audioName="filename"></div>`
 
**Full audio player:**
```html
<div class="bubble-right no-hover">
    <audio preload="none" src="audio/file.mp3" class="audioPlayer" title="Track title"></audio>
</div>
```
 
### WJFUN series — inline audio button inside the sentence `<p>` (CL-0063)
 
**In WJFUN modules, a speech-bubble audio button is emitted INSIDE the sentence's `<p>`, as an inline span after a line break — never as a separate block `<div class="audioButton">` sibling:**
 
```html
<p>Today are travelling to the Pancake Rocks. <br><span class="audioButton" audioName="kea-sentences-1"></span></p>
```
 
Never `<p>…</p><div class="audioButton" audioName="…"></div>` in WJFUN. This applies to **all Kea speech bubbles and any other WJFUN bubble audio button**. Outside WJFUN, the generic block-`div` forms above remain correct.
 
> **No style attribute.** The designer's refined WJFUN108 file carried a malformed inline `style` attribute (`style="vertical-align:bottom;top;left;right;"`) on this span. That attribute is **NOT** part of the codified pattern and is never emitted — the structural change only is recorded, preserving constraint 2 with no new exception. (WJFUN108 finalized report, Difference 1, designer decision (c), 29 July 2026.)
 
---
 
## Height Equalisation
 
Add `bubbleHeight` class to the `speechBubble` row:
```html
<div class="row speechBubble bubbleHeight" layout="speech">
```
 
---
 
## Single Character Speech Bubble
 
When there is only one character (common pattern: a character introducing themselves, text on one side, character image on the other). This is NOT a conversation — use `bubble-basic` combined with a positional class.
 
**⚠️ CRITICAL:** Single-character speech bubbles use `bubble-basic` COMBINED with a positional class (`bubble-left`, `bubble-right`, `bubble-top`, or `bubble-bottom`) on the same element. The positional class is determined by the layout in the Writers Template. The character image does NOT need `bubble-img` class when using wider column sizing.
 
### Positional Class Selection
 
| Writers Template Layout | Positional Class | Reasoning |
|---|---|---|
| Text on LEFT, image on RIGHT | `bubble-left` | Character/speaker is on the right; tail points left toward speaker |
| Image on LEFT, text on RIGHT | `bubble-right` | Character/speaker is on the left; tail points right toward speaker |
| Writer specifies "above" the image | `bubble-top` | Bubble appears above the character; image moves to separate row below |
| Writer specifies "below" the image | `bubble-bottom` | Bubble appears below the character; image moves to separate row above |
 
**⚠️ CRITICAL — Writer positional instructions override default layout.** If a writer includes a CS instruction specifying where the speech bubble should appear relative to the character image (e.g., "CS: can the speech bubble come out above the cat's head"), that instruction takes precedence over the default left/right positioning derived from the table layout. Apply the corresponding positional class (`bubble-top`, `bubble-bottom`, etc.) as instructed.
 
### Standard Layout — Text Left, Image Right (bubble-left)
 
When the Writers Template has the speech bubble text on the left and the image on the right (and no other positional instructions from the writer):
 
```html
<div class="row speechBubble" layout="speech">
    <div class="col-md-8 col-6">
        <div class="bubble-basic no-hover bubble-left">
            <p>Character speaks here.</p>
        </div>
    </div>
    <div class="col-md-4 offset-md-0 col-12 paddingL">
        <img class="img-fluid" alt="" loading="lazy" src="https://placehold.co/300x300?text=Character">
        <!-- <img class="img-fluid" alt="Character description — URL" loading="lazy" src="images/iStock-XXXXXXXXX.jpg"> -->
    </div>
</div>
```
 
### Standard Layout — Image Left, Text Right (bubble-right)
 
When the Writers Template has the image on the left and the speech bubble text on the right:
 
```html
<div class="row speechBubble" layout="speech">
    <div class="col-md-4 offset-md-0 col-12 paddingR">
        <img class="img-fluid" alt="" loading="lazy" src="https://placehold.co/300x300?text=Character">
        <!-- <img class="img-fluid" alt="Character description — URL" loading="lazy" src="images/iStock-XXXXXXXXX.jpg"> -->
    </div>
    <div class="col-md-8 col-6">
        <div class="bubble-basic no-hover bubble-right">
            <p>Character speaks here.</p>
        </div>
    </div>
</div>
```
 
### Vertical Layout — Bubble Above Image (bubble-top)
 
When the writer explicitly specifies that the speech bubble should appear above the character image. The bubble and image are placed in **separate rows** because they are stacked vertically:
 
```html
<div class="row speechBubble" layout="speech">
    <div class="col-4">
        <div class="bubble-basic no-hover bubble-top">
            <p>Character speaks here.</p>
        </div>
    </div>
</div>
<div class="row">
    <div class="col-md-2 offset-md-1">
        <img class="img-fluid" loading="lazy" src="https://placehold.co/300x300?text=Character" alt="" />
        <!-- <img class="img-fluid" loading="lazy" src="images/iStock-XXXXXXXXX.jpg" alt="Character description — URL" /> -->
    </div>
</div>
```
 
**⚠️ CRITICAL — Separate rows for vertical layouts:** When using `bubble-top` or `bubble-bottom`, the bubble and the character image MUST be in separate `<div class="row">` elements (not in the same row), because the image is positioned vertically relative to the bubble rather than side-by-side.
 
### Multi-Paragraph Content Wrapping
 
**⚠️ CRITICAL:** When a speech bubble contains multiple `<p>` elements (multiple paragraphs), the paragraphs MUST be wrapped in an additional `<div>` inside the bubble element. Single-paragraph bubbles do not need this wrapper.
 
```html
<!-- CORRECT: Multiple paragraphs — wrapping <div> required -->
<div class="bubble-basic no-hover bubble-left">
    <div>
        <p>First paragraph of speech.</p>
        <p>Second paragraph of speech.</p>
    </div>
</div>
 
<!-- CORRECT: Single paragraph — no wrapping <div> needed -->
<div class="bubble-basic no-hover bubble-left">
    <p>Single paragraph of speech.</p>
</div>
```
 
### Image Column Padding
 
When the character image column is adjacent to the bubble in a horizontal layout, apply padding classes to the image column:
 
| Image Position | Padding Class |
|---|---|
| Image on RIGHT (text-left layout) | `paddingL` |
| Image on LEFT (text-right layout) | `paddingR` |
 
**Do not mirror a sibling that pads both sides the same.** Some reference files (e.g. HPRE301) apply `paddingR` to both the left- and right-hand image columns; that is a known sibling deviation, not the rule. The right-positioned image column takes `paddingL` even when the Mode B sibling shows otherwise. (HPRE203 finalized report, Difference 4, 29 July 2026.) **Scoped exception (CL-0067):** HPE **head-only dialogue strips** deliberately take `paddingR` on both the left- and right-positioned image columns — see `14_SUBJECT_GLOBAL_PARAMETERS.md` §14.8; HPE full-body strips and every other module follow the universal rule above.
 
### Key Differences from Conversation Speech Bubbles
 
- Uses `bubble-basic` combined with a positional class (e.g., `bubble-basic bubble-left`) — conversation bubbles use directional classes alone (e.g., `bubble-right`)
- Image column uses `col-md-4 offset-md-0 col-12` with `paddingL` or `paddingR` (wider, no `bubble-img` class)
- Text column uses `col-md-8 col-6` for horizontal layouts, `col-4` for vertical layouts
- Character image is a standard `img-fluid` without `bubble-img` class
- Multi-paragraph content requires a wrapping `<div>` inside the bubble
---
 
## Writer Tag Variants
 
| Tag | Implementation |
|-----|---------------|
| `[speech bubble]` | Single character: `bubble-basic` + positional class from layout + `no-hover` on text-only bubbles. Conversation: alternating `bubble-right`/`bubble-left` + `no-hover` |
| `[speech bubble front]` | Same as standard `[speech bubble]` |
| `[speech bubble tiles]` | Multiple bubbles with `bubble-basic no-hover` in grid |
| `[speech bubble two people]` | Two characters, alternating bubble-right/bubble-left + `no-hover` on text-only bubbles |
| `[thinking speech bubble]` | Standard bubble + `no-hover` + **RED FLAG** for thought bubble CSS |
 
 
 
 
# COMP_10 — Diagrams & Timelines
 
---
 
## Shape Hover
 
**Container class:** `shapeHover`
 
```html
<div class="shapeHover" layout="clockwise">
    <div class="outerContent">
        <div class="shape"><h4>Shape 1</h4></div>
        <div class="shape"><h4>Shape 2</h4></div>
        <div class="shape"><h4>Shape 3</h4></div>
    </div>
    <div class="hoverContent">
        <div class="shapeContent"><p>Content for shape 1</p></div>
        <div class="shapeContent"><p>Content for shape 2</p></div>
        <div class="shapeContent"><p>Content for shape 3</p></div>
    </div>
</div>
```
 
**Layout values:**
- `clockwise` — arrows clockwise (use when content represents sequential steps)
- `counterClockwise` — arrows counter-clockwise
- `bothClockwise` — arrows both directions
- No layout — no arrows
**⚠️ CRITICAL — Layout selection:** When the shape hover represents sequential steps (step 1, step 2, etc.), ALWAYS use `layout="clockwise"` to show directional arrows between shapes. Omitting the layout attribute when steps are sequential is incorrect.
 
**With image in shape:**
```html
<div class="shape image">
    <img class="img-fluid" src="images/image.jpg" alt="">
    <h4>Shape Title</h4>
</div>
```
 
**Standard shapeContent (text reveal — most common):**
```html
<div class="shapeContent">
    <div><p>Description text</p></div>
</div>
```
 
**shapeContent with image (only for dedicated image reveal panels):**
The `image` class and image duplication should ONLY appear in `.shapeContent` when the hovered panel is specifically designed to show a different or larger version of the shape image. For standard text reveal, use plain `<div class="shapeContent"><div><p>content</p></div></div>` WITHOUT the `image` class. Do NOT duplicate images from `.shape` into `.shapeContent` by default.
 
```html
<div class="shapeContent image">
    <img class="img-fluid" src="images/different_image.jpg" alt="">
    <div><p>Description text</p></div>
</div>
```
 
**⚠️ CRITICAL:** Number of `.shape` = number of `.shapeContent`.
 
---
 
## Timeline
 
**Container class:** `timeline`
 
```html
<div class="timeline" direction="horizontal" layout="basic">
    <div class="flag clickDrop"><p>1840s</p></div>
    <div class="flag clickDrop"><p>1860s</p></div>
    <div class="flag clickDrop"><p>1880s</p></div>
</div>
<div class="col-md-8 offset-md-2 col-12">
    <div class="clickDropContent"><p>Content for 1840s</p></div>
    <div class="clickDropContent"><p>Content for 1860s</p></div>
    <div class="clickDropContent"><p>Content for 1880s</p></div>
</div>
```
 
**Attributes:**
- `direction="horizontal"`
- `layout="basic"`
- Uses `clickDrop`/`clickDropContent` pattern for reveals
---
 
## Venn Diagram
 
**Container class:** `vennDiagram`
 
### Two Circle (Static)
 
```html
<div class="vennDiagram twoCircle"
     left-circle-label="Tomato"
     right-circle-label="Strawberry"
     intersection-label="Both">
    <svg class="vennSVG"></svg>
    <div class="left-circle-content"><p>Savory</p></div>
    <div class="right-circle-content"><p>Sweet</p></div>
    <div class="intersection-content"><p>Red</p></div>
</div>
```
 
### Two Circle (Drag and Drop)
 
See COMP_01 in `03_COMP_CORE_INTERACTIVES.md` — Venn Layout section.
 
### Three Circle (Static)
 
```html
<div class="vennDiagram threeCircle"
     top-circle-label="Set A"
     left-circle-label="Set B"
     right-circle-label="Set C"
     center-intersection-label="All Three">
    <svg class="vennSVG"></svg>
    <div class="top-circle-content"><p>Top only</p></div>
    <div class="left-circle-content"><p>Left only</p></div>
    <div class="right-circle-content"><p>Right only</p></div>
    <div class="center-intersection-content"><p>All three</p></div>
    <div class="top-left-intersection-content"><p>Top & Left</p></div>
    <div class="top-right-intersection-content"><p>Top & Right</p></div>
    <div class="left-right-intersection-content"><p>Left & Right</p></div>
</div>
```
 
 
 
 
# COMP_11 — Drawing Tools & Utilities
 
---
 
## Sketcher
 
**Container class:** `sketcher`
**Required wrapper:** `<div class="activity">`
 
```html
<div class="sketcher" lineWidth="10" imageName="sketch.png">
    <div class="canvasContainer">
        <canvas class="canvasWindow"></canvas>
        <img src="images/image.jpg" class="canvasImage img-fluid">
    </div>
    <div class="colorOptions">
        <div color="#000000"></div>
        <div color="#0000ff"></div>
        <div color="#00ffff"></div>
        <div color="#00ff00"></div>
        <div color="#ffff00"></div>
        <div color="#ff00ff"></div>
        <div color="#ff0000"></div>
        <div color="#ffffff"></div>
    </div>
    <div class="activityButton skResetButton">Reset</div>
</div>
```
 
**⚠️ CRITICAL — canvasImage class:** The image inside `.canvasContainer` MUST have the `canvasImage` class in addition to `img-fluid`. Without `canvasImage`, the sketcher interactive will not function correctly — the drawing canvas will not align with the background image. This applies to both real images and placeholder images.
 
**⚠️ CRITICAL — No loading="lazy" on canvasContainer images:** Images inside `.canvasContainer` MUST NOT have the `loading="lazy"` attribute. Adding `loading="lazy"` to a canvas background image breaks the sketcher functionality — the image becomes unresponsive to drawing interactions because lazy loading interferes with the canvas overlay alignment and event handling. This overrides the general rule that all images should have `loading="lazy"`. The prohibition applies to ALL images that are children of `.canvasContainer`, whether real images or placeholders.
 
```html
<!-- CORRECT — canvasImage class present, NO loading="lazy" -->
<img src="images/image.jpg" class="canvasImage img-fluid">
<img class="img-fluid canvasImage" src="https://placehold.co/800x500?text=Sketch+Image" alt="">
 
<!-- WRONG — missing canvasImage class -->
<img class="img-fluid" src="https://placehold.co/800x500?text=Sketch+Image" alt="">
 
<!-- WRONG — loading="lazy" breaks sketcher functionality -->
<img class="img-fluid canvasImage" loading="lazy" src="https://placehold.co/800x500?text=Sketch+Image" alt="">
```
 
**Note:** Drawings disappear on page reload. Freeform drawing only.
 
---
 
## Number Line
 
**Container class:** `numberLine`
 
```html
<div class="numberLine">-10 10||-3 3 4 8||3 8||3 8</div>
```
 
**Format:** `RANGE || DOT-POSITIONS || LOOPLINE || DIRECTIONLINE`
- Range: start and end numbers (`-10 10`)
- Dot positions: space-separated (`-3 3 4 8`)
- Loopline: start and end of loop arc
- Directionline: start and end of direction arrow
---
 
## Stop Watch
 
**Container class:** `stopWatch`
 
```html
<div class="stopWatch"></div>
```
 
**Variants:**
- No milliseconds: `<div class="stopWatch noMilliSeconds"></div>`
- No milliseconds + no hours: `<div class="stopWatch noMilliSeconds noHours"></div>`
Commonly placed inside `<div class="alertActivity">` sidebars.