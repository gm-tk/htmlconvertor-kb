> **Last updated:** Wednesday, 1st July, 2026 12:39 AM
> **Granular part A (1 of 3) of `04_COMP_SEGMENTS_OVERLAYS.md`** — COMP_07 content segmentation (accordion, carousel, banner, clickDrop, flipCard, tabs, hint, modal).
> All sibling parts live in `04_COMP_SEGMENTS_OVERLAYS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
> **Last updated:** Wednesday, 1st July, 2026 12:39 AM

# COMP_07 — Content Segmentation
 
---
 
## Accordion
 
**Container class:** `accordion`
 
```html
<div class="accordion">
    <div class="accHead"><h4>Section 1</h4></div>
    <div class="accContent"><p>Content 1</p></div>
    <div class="accHead"><h4>Section 2</h4></div>
    <div class="accContent"><p>Content 2</p></div>
</div>
```
 
**Modifier classes on `.accHead`:** `secondary`, `tertiary`
 
**Keep all open:** `<div class="accordion accKeepOpen">`
 
**With layout:** `<div class="accordion" layout>`
 
**Rule:** Each term/item MUST be its own accHead/accContent pair.
 
---
 
## Carousel
 
**Container class:** `carousel`
 
Carousels have multiple sub-types — **image carousels**, **video carousels**, and **carousels with external navigation buttons** — which use different `.viewer` column widths and item structures.
 
### Image Carousel
 
```html
<div class="row carousel">
    <div class="col-md-8 col-12 viewer">
        <div class="item image">
            <img src="images/slide1.jpg" class="img-fluid" alt="">
            <div class="carousel-caption"><p>Caption text</p></div>
        </div>
        <div class="item image">
            <img src="images/slide2.jpg" class="img-fluid" alt="">
            <div class="carousel-caption"><p>Caption text 2</p></div>
        </div>
    </div>
</div>
```
 
**Image carousel rules:**
- Use `col-md-8 col-12` for the `.viewer` column — this constrains images to a reasonable width and prevents them from stretching to fill the entire screen width
- When carousel items contain images, add the `image` class to the `.item` div: `<div class="item image">`
- Caption optional: `<div class="carousel-caption"><p>text</p></div>`
- **⚠️ CRITICAL:** Do NOT use `col-md-12 col-12` for basic image carousels — images will scale to full page width and take up the entire screen
### Video Carousel
 
**⚠️ CRITICAL — Video carousels use different markup from image carousels.** The `.viewer` column is narrower, item titles use `<h5>`, and the description paragraph is placed ABOVE the video embed (not below it).
 
```html
<div class="row carousel">
    <div class="col-md-8 col-12 viewer">
        <div class="item">
            <h5>Video Title Here</h5>
            <p>Description of the video content.</p>
            <div class="videoSection ratio ratio-16x9">
                <iframe src="https://www.youtube-nocookie.com/embed/VIDEO_ID" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
            </div>
        </div>
        <div class="item">
            <h5>Second Video Title</h5>
            <p>Description of the second video.</p>
            <div class="videoSection ratio ratio-16x9">
                <iframe src="https://www.youtube-nocookie.com/embed/VIDEO_ID_2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
            </div>
        </div>
    </div>
</div>
```
 
**Video carousel rules:**
- Use `col-md-8 col-12` for the `.viewer` column (NOT `col-md-12`)
- Item titles use `<h5>` headings (NOT `<p><i>` or other markup)
- Description `<p>` goes directly UNDER the `<h5>` title and ABOVE the `<div class="videoSection">` — never below the video
- Do NOT add the `image` class to video carousel items
- Each item contains: `<h5>` title → `<p>` description → `<div class="videoSection">` video embed
### Carousel with External Navigation Buttons
 
When a carousel needs labeled navigation buttons (e.g., year dates, category names) that appear OUTSIDE the carousel as a separate row of clickable buttons, use the `exSlideBtns` attribute to link the buttons to the carousel.
 
**⚠️ CRITICAL:** Like all carousel types, this variant uses `col-md-8 col-12` for the `.viewer` column. The carousel items use the `video` class when containing video embeds, and the description paragraph is placed BELOW the video embed.
 
```html
<div class="row">
    <div class="col-md-8 col-12">
        <div class="carousel-btns" exSlideBtns="dates">
            <div class="button">1888</div>
            <div class="button">1895</div>
            <div class="button">1902</div>
            <div class="button">Present Day</div>
        </div>
    </div>
</div>
<div class="row carousel" exSlideBtns="dates">
    <div class="col-md-8 col-12 viewer">
        <div class="item video">
            <div class="videoSection ratio ratio-16x9">
                <iframe src="https://www.youtube.com/embed/VIDEO_ID?si=XXXXX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
            </div>
            <p>Description text goes BELOW the video for this variant.</p>
        </div>
        <div class="item video">
            <div class="videoSection ratio ratio-16x9">
                <iframe src="https://www.youtube.com/embed/VIDEO_ID_2?si=XXXXX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
            </div>
            <p>Description of the second video.</p>
        </div>
    </div>
</div>
```
 
**External navigation button rules:**
- The `carousel-btns` div is a separate element that goes ABOVE the carousel, typically wrapped in its own `<div class="row"><div class="col-md-8 col-12">`
- Both the `carousel-btns` div and the `carousel` row MUST share the same `exSlideBtns` attribute value (e.g., `exSlideBtns="dates"`) — this is what links the buttons to the carousel
- Each `<div class="button">` inside `carousel-btns` corresponds to one carousel item (first button → first item, etc.)
- The number of buttons MUST equal the number of `.item` elements in the carousel
- Carousel items use `<div class="item video">` when containing video embeds (note the `video` class)
- For this variant, the description `<p>` goes BELOW the `<div class="videoSection">` (not above)
- The `.viewer` column uses `col-md-8 col-12` (same as all carousel types)
- Items do NOT use `<h5>` headings — the external buttons serve as the navigation labels instead
- When a carousel item has no video available, leave the `<div class="videoSection ratio ratio-16x9"></div>` empty (no iframe)
- YouTube URLs in external nav carousels may use the standard `youtube.com/embed/` format (with `?si=` sharing parameter) rather than `youtube-nocookie.com` — preserve the URL format provided by the writer
- YouTube timestamp parameters (`&start=` and `&end=`) can be appended directly to the iframe `src` URL
### General Carousel Rules
 
- **⚠️ CRITICAL:** ALL carousel types (image, video, and external nav button) use `col-md-8 col-12` for the `.viewer` column. NEVER use `col-md-12 col-12` for ANY carousel viewer — content will display too large and take up the full screen width.
- Each `<div class="item">` = one slide
- Text-only slides (no image, no video) can use either column width as appropriate
- Determine carousel sub-type by content: if items contain `<div class="videoSection">` video embeds → video carousel; if items contain `<img>` images → image carousel; if the writer provides labeled navigation buttons (dates, categories) → external nav button carousel
---
 
## Rotating Banner
 
**Container class:** `rotateBanner`
 
**⚠️ CRITICAL:** The `[rotating banner]` tag maps to the `rotateBanner` component, NOT the `carousel` component. These are distinct components with different class structures.
 
**⚠️ CRITICAL — Scrolling marquee requests:** When a writer requests a "scrolling marquee", "scrolling banner", "marquee of images", or similar scrolling/sliding image display, this MUST be interpreted as a `rotateBanner` component. NEVER hide or comment out such a request — always implement it as a `rotateBanner` with placeholder images. If the writer specifies images, use placeholder images with descriptive text and raise a VISIBLE red flag (`<p style="color: red; font-weight: bold;">Red Flag: ...</p>`) recording the writer's image descriptions so the designer can source them — do NOT bury the description in an HTML comment. (This is a Convertor-detected sourcing gap, so it takes the `Red Flag:` prefix; see `02_DATA_CONTENT_VERIFICATION.md` → Source-Specific Red-Note Prefixes.)
 
```html
<div class="row">
    <div class="col-md-8 col-12">
        <div class="rotateBanner">
            <div class="bannerContainer">
                <div class="bannerItem">
                    <img class="img-fluid" src="images/image1.jpg" alt="Description">
                </div>
                <div class="bannerItem">
                    <img class="img-fluid" src="images/image2.jpg" alt="Description">
                </div>
                <div class="bannerItem">
                    <img class="img-fluid" src="images/image3.jpg" alt="Description">
                </div>
            </div>
        </div>
    </div>
</div>
```
 
**With placeholder images (when writer describes desired images but no files exist yet)** — pair the placeholders with a single VISIBLE red flag listing each image the writer described, so the designer sources them before go-live:
```html
<div class="row">
    <div class="col-md-8 col-12">
        <div class="rotateBanner">
            <div class="bannerContainer">
                <div class="bannerItem">
                    <img class="img-fluid" src="https://placehold.co/600x400?text=Image+1+Description" alt="Description">
                </div>
                <div class="bannerItem">
                    <img class="img-fluid" src="https://placehold.co/600x400?text=Image+2+Description" alt="Description">
                </div>
            </div>
        </div>
    </div>
</div>
```
 
**Key rules:**
- Each `<div class="bannerItem">` contains an image and an optional `<span>` caption
- Captions use `<span>` (not `<div class="carousel-caption"><p>`)
- No `.viewer` column wrapper needed — the `bannerContainer` handles layout
- Data comes from the same numbered slides pattern as carousel (Pattern 5 in section 06)
- The `rotateBanner` should be wrapped in a `<div class="row"><div class="col-md-8 col-12">` container
- Writer requests for "scrolling marquee", "scrolling images", "image marquee", "banner of images" etc. → implement as `rotateBanner`
---
 
## Click Drop
 
**Container class:** `clickDrop` / `clickDropContent`
 
**⚠️ CRITICAL STRUCTURE RULE:** All `.clickDrop` button elements MUST be grouped together FIRST, followed by all `.clickDropContent` divs AFTER. Do NOT interleave them (i.e., do NOT place a `.clickDropContent` immediately after each `.clickDrop`).
 
**⚠️ CRITICAL:** Number of `clickDrop` triggers MUST equal number of `clickDropContent` divs.
 
**⚠️ `rel` IS AUTO-CALCULATED — OMIT IT BY DEFAULT.** The engine automatically pairs each `.clickDrop` button with its `.clickDropContent` panel **in document order**, so do NOT emit a `rel` attribute as a matter of course. A **single** clickDrop pair never needs `rel`. Only add explicit `rel="N"` (0-indexed) in the rare case where multiple pairs are authored **out of document order** and must be disambiguated. The examples below are shown without `rel`; that is the default form to generate.
 
### Standard Layout (Buttons Stacked)
 
```html
<div class="button clickDrop">Click to reveal 1</div>
<div class="button clickDrop">Click to reveal 2</div>
<div class="button clickDrop">Click to reveal 3</div>
<div class="clickDropContent"><p>Content 1</p></div>
<div class="clickDropContent"><p>Content 2</p></div>
<div class="clickDropContent"><p>Content 3</p></div>
```
 
### Optimal Layout (Buttons Side-by-Side)
 
When multiple clickDrop items exist, wrap all buttons in a `.row` with column classes so they display side-by-side. The `.clickDropContent` divs remain OUTSIDE this row wrapper. This keeps the buttons static when clicked while the correct content panel expands below.
 
```html
<div class="row">
    <div class="col-md-4 offset-md-0 col-12">
        <div class="button clickDrop">Click to reveal 1</div>
    </div>
    <div class="col-md-4 offset-md-0 col-12">
        <div class="button clickDrop">Click to reveal 2</div>
    </div>
    <div class="col-md-4 offset-md-0 col-12">
        <div class="button clickDrop">Click to reveal 3</div>
    </div>
</div>
<div class="clickDropContent"><p>Content 1</p></div>
<div class="clickDropContent"><p>Content 2</p></div>
<div class="clickDropContent"><p>Content 3</p></div>
```
 
**Column sizing for side-by-side buttons:** Adjust based on number of items:
- 2 items: `col-md-6`
- 3 items: `col-md-4`
- 4 items: `col-md-3`
### Attributes
 
| Attribute | Purpose |
|---|---|
| `rel="N"` | **Optional — omit by default.** Pairing is auto-calculated from document order. Only supply `rel` (0-indexed) to override that order when multiple pairs are authored out of sequence. Never needed for a single pair. |
 
**⚠️ CRITICAL — No initial state attributes:** Do NOT add an `active` class to any `.clickDrop` button, and do NOT add inline `style` attributes (such as `style=""` or `style="display: none;"`) to any `.clickDropContent` div. The JavaScript handles the initial active/visible state automatically. Adding these attributes manually causes the interactive to malfunction.
 
### In Activity with Accordion
 
```html
<div class="activity" number="1A">
    <div class="row"><div class="col-md-8 col-12">
        <div class="accordion" layout>
            <div class="accHead"><h4>Section</h4></div>
            <div class="accContent">
                <div class="button clickDrop">Reveal</div>
                <div class="clickDropContent"><p>Content</p></div>
            </div>
        </div>
    </div></div>
</div>
```
 
---
 
## Flip Card
 
**Container class:** `flipCard`
 
### Text-Only Flip Cards
 
```html
<div class="col-md-4 col-12 paddingLR">
    <div class="flipCard">
        <div class="front"><h5>Front heading</h5><p>Front text</p></div>
        <div class="back"><p>Back content</p></div>
    </div>
</div>
```
 
### Image Flip Cards
 
When flip cards contain images:
1. Wrap all cards in `<div class="row flipCardsContainer">`
2. Add the `flipImage` class to the `.front` div
3. Place the image BEFORE the heading text in the `.front` div
4. Use `<h5>` for card titles (not `<h4>`)
```html
<div class="row flipCardsContainer">
    <div class="col-md-4 col-12 paddingLR">
        <div class="flipCard">
            <div class="front flipImage">
                <img class="img-fluid" loading="lazy" src="images/image1.jpg" alt="">
                <h5>Card Title 1</h5>
            </div>
            <div class="back">
                <p>Back content 1</p>
            </div>
        </div>
    </div>
    <div class="col-md-4 col-12 paddingLR">
        <div class="flipCard">
            <div class="front flipImage">
                <img class="img-fluid" loading="lazy" src="images/image2.jpg" alt="">
                <h5>Card Title 2</h5>
            </div>
            <div class="back">
                <p>Back content 2</p>
            </div>
        </div>
    </div>
</div>
```
 
**Key rules:**
- `flipCardsContainer`: Add to the wrapping `.row` when multiple flip cards appear together
- `flipImage`: Add to `.front` when it contains an image — this triggers appropriate image styling
- Image-before-text: In `.front` with images, the `<img>` comes before the `<h5>` heading
- Use `<h5>` for card titles within flip cards (not `<h4>`)
---
 
## Tabs
 
**Container class:** `tabs`
 
```html
<div class="tabs col-md-8 col-12">
    <ul class="nav nav-tabs">
        <li><a>Tab 1</a></li>
        <li><a>Tab 2</a></li>
    </ul>
    <div class="tab-content">
        <div class="tab-pane"><p>Tab 1 content</p></div>
        <div class="tab-pane"><p>Tab 2 content</p></div>
    </div>
</div>
```
 
**⚠️ CRITICAL:** Number of `<li>` = number of `<div class="tab-pane">`.
 
---
 
## Hint
 
**Container class:** `hint` / `hintDropContent`
 
```html
<p class="hintLink">Text content <span class="hint"></span></p>
<div class="hintDropContent">
    <p>Hint explanation text</p>
</div>
```
 
**In columns:**
```html
<div class="row">
    <div class="col-md-9 col-12 paddingR">
        <p class="hintLink">Text with <span class="hint"></span></p>
    </div>
    <div class="col-md-3 col-12 paddingL">
        <div class="hintDropContent"><p>Hint text</p></div>
    </div>
</div>
```
 
---
 
## Hint Slider
 
**Container class:** `hintSlider`
 
```html
<div class="hintSlider" hintCssFile="standard">
    <div class="hintRow">
        <div class="infoContainer">
            <div class="frontInfo"><p>Front text</p></div>
            <div class="backInfo"><p>Back text</p></div>
        </div>
    </div>
</div>
```
 
**Multiple rows:**
```html
<div class="hintSlider" hintCssFile="standard">
    <div class="hintRow">
        <div class="infoContainer">
            <div class="frontInfo"><p>Item 1</p></div>
            <div class="backInfo"><p>Back 1</p></div>
        </div>
    </div>
    <div class="hintRow">
        <div class="infoContainer">
            <div class="frontInfo"><p>Item 2</p></div>
            <div class="backInfo"><p>Back 2</p></div>
        </div>
    </div>
</div>
```
 
**Audio triggers:**
- On row: `<div class="hintRow audioTrigger" audioName="filename">`
- On front: `<div class="frontInfo audioTrigger" audioName="filename">`
- On back: `<div class="backInfo audioTrigger" audioName="filename">`
**Dark variant:** `<div class="hintRow dark">`
 
**Grid layout:**
```html
<div class="col-md-6 col-lg-4 col-12 paddingR">
    <div class="hintSlider" hintCssFile="standard">
        <div class="hintRow dark">
            <div class="infoContainer">
                <div class="frontInfo"><p>Term</p></div>
                <div class="backInfo"><p>Definition</p></div>
            </div>
        </div>
    </div>
</div>
```
 
---
 
## Modal
 
**Container class:** `TKmodalButton` / `TKmodal`
 
```html
<div class="button TKmodalButton">Open Modal</div>
<div class="TKmodal" size="S">
    <p>Modal content here</p>
</div>
```
 
**Size values:** `S`, `M`, `L`, `XL`
 
**Inline trigger:**
```html
<p><span class="TKmodalButton">Click here</span> to learn more.</p>
<div class="TKmodal" size="M"><p>Modal content</p></div>
```
 
**⚠️ CRITICAL:** Each `TKmodalButton` MUST have corresponding `TKmodal` immediately following.
 
**Limitation:** Modals cannot contain packages requiring offline access.
 
 
 
 
