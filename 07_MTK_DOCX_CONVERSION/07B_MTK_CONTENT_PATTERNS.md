> **Last updated:** Thursday, 16th July, 2026 9:30 PM
> **Granular part B (2 of 4) of `07_MTK_DOCX_CONVERSION.md`** — MTK: body content, alerts, interactive mapping, media, bilingual buttons (SS7-11).
> All sibling parts live in `07_MTK_DOCX_CONVERSION/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## 7. BODY CONTENT PATTERNS

### Module Introduction (Page 0.0 Body)

The module introduction section appears after the overview menu and contains:
1. Course code heading: `<h1 reo>TRR900</h1>` / `<h1 eng>TRR900</h1>`
2. Introduction heading: `<h2 reo>Kōwae Ako Whakataki</h2>` / `<h2 eng>Module Introduction</h2>`
3. Body paragraphs (bilingual pairs)
4. Optional whakatauki (proverb) section
5. Optional karakia (prayer) with image/audio/video

Some modules (TRR107) place the karakia BEFORE the intro text. Others (TRR104/105) place only intro text + video. TRR108 places the whakatauki and karakia on the overview page. Follow the writer's content order.

### Whakatauki / Proverb

Uses a dedicated component:

```html
<div class="whakatauki">
    <p reo>Māori proverb text</p>
    <p eng>English translation</p>
    <!-- <p></p> --> <!-- Author, if provided -->
</div>
```

**Placement varies by module:** TRR104 places it on lesson page 1.0; TRR108 places it on the overview page 0.0. Follow the writer's document structure.

**TRR107 variation:** The whakatauki may use `<h3 reo>` / `<h3 eng>` for the proverb text itself.

### Activity Structure

Activities follow a consistent pattern in the writer's template:

```
| Activity 1A: | Ngohe 1A: |
| [H2] Activity Title | [H2] Māori Title |
| [Body] ... | [Body] ... |
```

This maps to:
```html
<div class="activity" number="1.1">
    <div class="row">
        <div class="col-12">
            <h3 reo>Ngohe 1A: Māori Title</h3>
            <h3 eng>Activity 1A: English Title</h3>
            <p reo>...</p>
            <p eng>...</p>
        </div>
    </div>
</div>
```

**Activity number format:** The writer uses letter suffixes (1A, 1B, 1C, then 1E, 1I for vowel-specific modules). Map these to decimal format for the `number` attribute: A→.1, B→.2, C→.3, E→.4, I→.5 etc. However, note that some finalized modules (TRR108) retain the writer's letter format in the `number` attribute (e.g., `number="1A"`). **Preferred approach: use decimal format** (1.1, 1.2, 1.3) for consistency with TRR104/TRR105 precedent.

**Activity classes:** Add `interactive` class when the activity contains an interactive component (MCQ, D&D, word select, etc.). Add `dropbox` class for activities with a file upload dropbox. Add `alertPadding` when a side alert sits adjacent.

### "What will we be learning?" Checklist

The writer includes a checklist like:
```
**What will we be learning?**
☒ Read ☒ Speak ☒ Listen ☒ Watch
```

**Developer variation exists.** TRR104 skips this section entirely; TRR108 renders it as a visible bilingual `<ul>` list within each activity. **Preferred approach: render it as visible content** within the activity, as bilingual `<ul>` lists:

```html
<p reo><b>He aha tā tātou ako ai?</b></p>
<ul reo>
    <li><span>Pānui</span></li>
    <li><span>Kōrero</span></li>
    <li><span>Whakarongo</span></li>
</ul>
<p eng><b>What will we be learning?</b></p>
<ul eng>
    <li><span>Read</span></li>
    <li><span>Speak</span></li>
    <li><span>Listen</span></li>
</ul>
```

Only include items marked with ☒ (ticked). Items marked with ☐ (unticked) are excluded.

### Activity Instructions

The writer's `[H3] Activity Instructions:` / `[H3] Ngā Tohutohu Hei Mahi` maps to `<h4>` headings within the activity:

```html
<h4 reo>Ngā Tohutohu Hei Mahi</h4>
<h4 eng>Activity Instructions:</h4>
```

### "Finished!" / "What have I learned?" Sections

Each lesson in the writer's template ends with:
1. `[H3] Finished!` / `[H3] Kua oti!` — completion heading
2. Summary text
3. `[H3] What have I learned?` / `[H3] He aha tāku i ako ai?` — reflection heading
4. Reflection/summary text

These map to `<h4>` headings with `<p>` body text in the finalized HTML:

```html
<h4 reo>Kua oti!</h4>
<h4 eng>Finished!</h4>
<p reo>Completion text...</p>
<p eng>Completion text...</p>

<h4 reo>He aha tāku i ako ai?</h4>
<h4 eng>What have I learned?</h4>
<p reo>Reflection text...</p>
<p eng>Reflection text...</p>
```

On the FINAL lesson page, the "What have I learned?" may become a self-check with a `selectionBox` component if the writer provides selectable items.

### Self-Check / Selection Box (Final Page)

When present, the final lesson page wraps the self-check in an `alert` container:
```html
<div class="alert">
    <div class="row">
        <div class="col-12">
            <p reo style="color:#56d19e; font-size: 2em;">He aha tāku i ako ai?</p>
            <h3 eng>What have I learned?</h3>
            ...
            <div class="row selectionBox">
                <div class="col-md-12 col-12">
                    <ol reo>
                        <li select="tick" reo>Item text</li>
                        ...
                    </ol>
                    <ol eng>
                        <li select="tick" eng>Item text</li>
                        ...
                    </ol>
                </div>
            </div>
        </div>
    </div>
</div>
```

**Note the Māori heading workaround:** The Māori "He aha tāku i ako ai?" uses a `<p>` tag with inline green colour styling instead of `<h3>` — this is a known workaround for a language-toggle glitch in the template system.

---

## 8. ALERT AND SIDEBAR PATTERNS

### Inline Alert (Standard)

Writer's `[Alert]` or `[Alert Solid]` with heading text like `**Remember**` / `**Kia maumahara koe**`:

```html
<div class="alert">
    <div class="row">
        <div class="col-12">
            <p reo><b>Kia maumahara koe</b></p>
            <p eng><b>Remember</b></p>
            <p reo>Māori alert text</p>
            <p eng>English alert text</p>
        </div>
    </div>
</div>
```

**Note:** The heading is rendered as a bold `<p>`, not as an `<h3>` or `<h4>`. This is consistent across TRR104, TRR105, TRR107, and TRR108.

### Side Alert

Writer's `[Side Alert]` tag or a table row with alert content placed separately:

```html
<div class="col-md-4 offset-md-0 col-12">
    <div class="alertActivity">
        <p reo>Māori alert text</p>
        <p eng>English alert text</p>
        <img class="img-fluid" loading="lazy" src="images/..." alt="..." />
    </div>
</div>
```

Side alerts sit beside the main content column, changing it from `col-md-8` default to accommodate both.

---

## 9. INTERACTIVE COMPONENT MAPPING

### Writer's Descriptions → Component Selection

MTK writers often describe interactives in natural language rather than using formal tags. Map as follows:

| Writer Description | Component | Notes |
|---|---|---|
| `[Activity: Embedded] Multi Choice Quiz with Image` | `multiChoiceQuiz` | With `<img>` in each `mcqQuestion` |
| `[Activity: Embedded] Multiple choice with audio` | `dropQuiz` with `audioButton` | Table layout with audio + dropdown |
| `[Activity: Embedded] [Word Select]` | `wordSelect` | Standard or `oneSelect` |
| `[Activity: Embedded] Drag and Drop` | `dragAndDrop` | Check for `layout` variant |
| `[Activity: Embedded] [Memory Game]` | Memory game | `memCard` pairs |
| `[Activity: Embedded] [Radio Quiz]` | `multiChoiceQuiz` | Despite the name, TRR104 used MCQ for this |
| `[Carousel Slideshow]` or `[Carousel]` | `carousel` with `carouselBorder` | Items with images and captions |
| `[Interactive] [AudioImage Hover]` | `audioImage` | `audioImageOption` with `id` = audio filename |
| `[Interactive] [Audio Hover Image]` | `audioImage` | Same as above (variant naming) |
| `[Interactive] Stopwatch` | `stopWatch` | `<div class="stopWatch reo"></div>` |
| `[Speech Bubble]` | `speechBubble` | See COMP_09 |
| `[Modal]` | `TKmodalButton` + `TKmodal` | Recipe/instructions popup |
| `[Voice recorder dropbox]` | Dropbox placeholder | Button with `activityButton` link |
| `Please created N Accordions` | `accordion` | One `accHead` + `accContent` per item |
| `Drag a line to match` | `dragAndDrop layout="standard"` | Standard matching D&D |
| `[Flip Card]` | `flipCard` | Front image, back text |
| `Memory Card Match` (natural language) | `dragAndDrop` or `wordSelect` | Context-dependent; check writer's intent |

### MCQ Answer Marking

In the writer's tables, correct answers are marked with `✔` after the option text. Map the `✔` option to `value="correct"` on the `<p class="mcqOption">` element.

### D&D Data Tables

The writer provides D&D data as tables showing correct pairings. The HTML must shuffle the drag items but keep the correct `option` attribute mapping intact.

### D&D with Audio (Sound-to-Letter Matching)

When the writer describes matching sounds to letters (e.g., "Drag the sound to the matching consonant"), use `dragAndDrop layout="standard"` with `audioButton` elements in the `questionContainer`:

```html
<div class="dragAndDrop autoCheck" layout="standard">
    <div class="row">
        <div class="col-1 questionContainer">
            <div class="question">
                <div class="audioButton" audioName="consonant_p"></div>
            </div>
            <!-- repeat for each sound -->
        </div>
        <div class="col-11 ddContainer">
            <div class="dropContainer">
                <div class="drop" option="1"></div>
                <!-- repeat -->
            </div>
            <div class="dragContainer">
                <div class="drag" option="1"><p>Pp</p></div>
                <!-- repeat -->
            </div>
        </div>
    </div>
</div>
```

### D&D with Images (Picture-to-Letter Matching)

When the writer describes matching pictures to letters, use `dragAndDrop layout="standard"` with images in the `questionContainer`:

```html
<div class="dragAndDrop" layout="standard">
    <div class="row">
        <div class="col-3 questionContainer">
            <div class="question">
                <img class="img-fluid margB0" loading="lazy" src="images/item.jpg" alt="Description" />
            </div>
            <!-- repeat -->
        </div>
        <div class="col-9 ddContainer">
            <!-- dropContainer + dragContainer as above -->
        </div>
    </div>
</div>
```

---

## 10. MEDIA ASSET HANDLING

### Image References

Writer provides: `[Item N] [Image] [Description](SharePoint URL)`

**⚠️ Image output mode applies to MTK conversions.** Before generating any HTML, determine the image output mode (Mode P or Mode D) using the same rules documented in the Images section of `01_PIPELINE_EXTRACTION_TAGS.md`. If the user has not stated a preference, prompt them before proceeding.

**Mode P (Placeholder):** Use placehold.co placeholders with the real image path commented out, plus a `<!-- CS: Item N — description -->` comment above for media catalogue reference:
```html
<!-- CS: Item N — description -->
<img class="img-fluid" loading="lazy" src="https://placehold.co/600x400?text=Description" alt="" />
<!-- <img class="img-fluid" loading="lazy" src="images/descriptive_name.jpg" alt="Description"> -->
```

**Mode D (Direct Link):** Use direct image filenames with a `<!-- CS: Item N — description -->` comment above for media catalogue reference only (no additional image detail comment block):
```html
<!-- CS: Item N — description -->
<img class="img-fluid" loading="lazy" src="images/descriptive_name.jpg" alt="Description" />
```

**Common rules for both modes:**
- Use underscores instead of spaces in filenames
- Always add `<!-- CS: Item N — description -->` comment above each image (this is for media catalogue tracking, not image detail duplication). This Item-N annotation is a deliberate, documented exception to the project-wide "no designer-facing comments" rule — it is a stable catalogue key, not a note to action. Anything a designer must actually action still goes in a VISIBLE red flag — see `02_DATA_CONTENT_VERIFICATION.md` → Comment & Red Flag Policy
- Use `class="img-fluid"` on all images
- Add `loading="lazy"` on images below the fold

### Audio References

Writer provides: `[Item N] [Audio] [Description](SharePoint URL)`

For `audioImage` components, the audio filename is set via the `id` attribute on `.audioImageOption`:
```html
<div id="audio_filename_no_spaces" class="audioImageOption">
```

For `audioButton` components:
```html
<div class="audioButton" audioName="audio_filename_no_spaces"></div>
```

**⚠️ CRITICAL:** Never use spaces in audio filenames. Replace spaces with underscores.

### Video References

Writer provides: `[Item N] [Video] [Description](URL)`

For YouTube videos:
```html
<div class="videoSection ratio ratio-16x9">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/VIDEO_ID" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
```

For local/Vimeo videos:
```html
<div class="videoSection ratio ratio-16x9">
    <video controls src="video/filename.mp4" title="Description"></video>
</div>
```

**Creative Services videos are Vimeo (constraint 64).** A video produced by Creative Services (a Te Kura in-house / Audiovisual production) — in any pathway, including MTK — embeds as the pending-ID Vimeo `videoSection` scaffold with a visible `Designer/Developer To Do:` note per audiovisual item. See `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` → Video Embed → Creative Services Videos (Vimeo).

---

## 11. BILINGUAL BUTTON PATTERNS

All buttons should have both `reo` and `eng` variants:

### Activity Buttons (MCQ)
```html
<div eng class="activityButton mcqReset">Reset</div>
<div reo class="activityButton mcqReset">Tautuhi anō</div>
<div eng class="activityButton hidden mcqAswers">Check answers</div>
<div reo class="activityButton hidden mcqAswers">Tirohia ngā whakautu</div>
```

### Activity Buttons (D&D / DropQuiz)
```html
<div eng class="activityButton reset">Reset</div>
<div reo class="activityButton reset">Tautuhi anō</div>
<div eng class="activityButton checkAnswer hidden">Check answers</div>
<div reo class="activityButton checkAnswer hidden">Tirohia ngā whakautu</div>
```

### Memory Game Buttons
```html
<div eng class="activityButton memGameReset">Reset</div>
<div reo class="activityButton memGameReset">Tautuhi anō</div>
```

### Navigation/Content Buttons
```html
<a eng href="URL" target="_blank"><div class="button">English label</div></a>
<a reo href="URL" target="_blank"><div class="button">Māori label</div></a>
```

---

