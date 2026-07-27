> **Last updated:** Tuesday, 14th July, 2026 5:39 PM
> **Granular part B (2 of 6) of `03_COMP_CORE_INTERACTIVES.md`** — COMP_01 drag and drop (all layouts).
> All sibling parts live in `03_COMP_CORE_INTERACTIVES/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# COMP_01 — Drag and Drop

**Container class:** `dragAndDrop`
**Required wrapper:** `<div class="activity interactive">`

---

## Available Layouts

| Layout | Attribute | Use Case |
|--------|-----------|----------|
| Standard | `layout="standard"` | Question-answer matching side by side |
| Column | `layout="column"` | Sort items into category columns |
| FIB | `layout="FIB"` | Drop words into inline blanks |
| Scatter | `layout="scatter"` | Label positions on an image |
| Area | `layout="area"` | Free-form placement (no correct answer) |
| Venn | `layout="venn"` | Drop into Venn diagram zones |

## Modifier Classes (on `dragAndDrop` div)

| Class | Effect |
|-------|--------|
| `autoCheck` | Instant feedback (remove undo + checkAnswer buttons) |
| `noShuffle` | Prevents randomisation |
| `images` | Drag items are images |
| `noBG` | Removes background styling |
| `hoverBoxes` | Drag items show alternate text on hover |
| `row` | Side-by-side drop/drag areas (column/area) |

---

## Standard Layout

```html
<div class="dragAndDrop" layout="standard">
    <div class="row">
        <div class="col-6 questionContainer">
            <div class="question"><p>Question 1</p></div>
            <div class="question"><p>Question 2</p></div>
        </div>
        <div class="col-6 ddContainer">
            <div class="dropContainer">
                <div class="drop" option="1"></div>
                <div class="drop" option="2"></div>
            </div>
            <div class="dragContainer">
                <div class="drag" option="1"><p>Answer 1</p></div>
                <div class="drag" option="2"><p>Answer 2</p></div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="activityButton reset">Reset</div>
        <div class="activityButton undo hidden">Undo</div>
        <div class="activityButton checkAnswer hidden">Check answers</div>
    </div>
</div>
```

**With autoCheck** (only Reset needed):
```html
<div class="dragAndDrop autoCheck noShuffle" layout="standard">
    <!-- same inner structure -->
    <div class="row">
        <div class="activityButton reset">Reset</div>
    </div>
</div>
```

**With images:**

**⚠️ CRITICAL — D&D Standard with Images — Content Placement Rule:** When a D&D standard layout uses the `images` modifier class, the **text descriptions** go in the `questionContainer` (the static/fixed side) and the **images** go as the draggable items in the `dragContainer`. This is the opposite of what might seem intuitive but is essential for usability:
- Images in the `questionContainer` stretch vertically and make the interactive unusably tall (requiring users to drag items across multiple screen heights)
- Text naturally compresses better and keeps the interactive compact
- Column widths should be `col-7` for the text questions and `col-5` for the image drag items (not the default `col-6`/`col-6`)
- Add `margB0` class to images inside drag items to remove bottom margin

```html
<div class="dragAndDrop images" layout="standard">
    <div class="row">
        <div class="col-7 questionContainer">
            <div class="question"><p>Text description of item 1</p></div>
            <div class="question"><p>Text description of item 2</p></div>
            <div class="question"><p>Text description of item 3</p></div>
        </div>
        <div class="col-5 ddContainer">
            <div class="dropContainer">
                <div class="drop" option="1"></div>
                <div class="drop" option="2"></div>
                <div class="drop" option="3"></div>
            </div>
            <div class="dragContainer">
                <div class="drag" option="1">
                    <img class="img-fluid margB0" loading="lazy" src="images/image1.jpg" alt="Dnd image" />
                </div>
                <div class="drag" option="2">
                    <img class="img-fluid margB0" loading="lazy" src="images/image2.jpg" alt="Dnd image" />
                </div>
                <div class="drag" option="3">
                    <img class="img-fluid margB0" loading="lazy" src="images/image3.jpg" alt="Dnd image" />
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="activityButton reset">Reset</div>
        <div class="activityButton undo hidden">Undo</div>
        <div class="activityButton checkAnswer hidden">Check answers</div>
    </div>
</div>
```

**Key rules for D&D standard with `images` class:**
- Text descriptions = `questionContainer` (LEFT, `col-7`)
- Images = `dragContainer` items (RIGHT, `col-5`)
- Use `margB0` on images inside `.drag` items
- Use `loading="lazy"` on all images
- Use descriptive `alt` text (e.g., `alt="Dnd image"`)
- This ensures the interactive remains compact and fully usable

**Pre-filled slots:**
- Blank: `<div class="blank"><p>blank text</p></div>`
- Pre-answered: `<div class="blank answered" option="X"><p>answered text</p></div>`

**With d-flex alignment:**
```html
<div class="col-6 ddContainer d-flex">
    <div class="dropContainer align-self-center">
```

**With Show/Hide answers:**
```html
<div class="row">
    <div class="activityButton reset hideShowAnswer">Reset</div>
    <div class="activityButton hidden checkAnswer revealShowAnswer">Check answers</div>
    <div class="activityButton hidden showAnswer">
        <span>Show</span><span>Hide</span> answers
    </div>
</div>
<div class="showAnswerContent">
    <p>Explanation of correct answers.</p>
</div>
```

---

## Column Layout

```html
<div class="dragAndDrop" layout="column">
    <div class="row dropContainer" blanks="3">
        <div class="ddColumn">
            <p>Column 1 heading</p>
            <div class="drop" option="1"></div>
            <div class="drop" option="1"></div>
        </div>
        <div class="ddColumn">
            <p>Column 2 heading</p>
            <div class="drop" option="2"></div>
            <div class="drop" option="2"></div>
        </div>
    </div>
    <div class="row dragContainer">
        <div class="ddColumn">
            <div class="drag" option="1"><p>Goes to Col 1</p></div>
            <div class="drag" option="2"><p>Goes to Col 2</p></div>
        </div>
        <div class="ddColumn"></div>
    </div>
    <div class="row">
        <div class="activityButton reset">Reset</div>
        <div class="activityButton undo hidden">Undo</div>
        <div class="activityButton checkAnswer hidden">Check answers</div>
    </div>
</div>
```

**Key rules:**
- `option` on drags matches column number
- Empty `<div class="ddColumn"></div>` pads to match drop column count
- Optional `blanks` attribute specifies pre-filled slot count

**⚠️ CRITICAL — Image distribution for many drag items:** When a D&D column layout uses images (`class="dragAndDrop images"`) and has a large number of drag items (6+), the images can become unwieldy if all placed in a single `.ddColumn` within the `dragContainer`. To solve this:

1. **Use `col-12` (Standard) or `col-md-11 col-12` (Inquiry & Fundamentals) as the outer content wrapper** (instead of `col-md-12`) — **never `col-md-10`** (activity wrappers no longer use it; see constraint 56). Distributing the images across multiple `.ddColumn` elements (step 2) is what keeps them manageable.

2. **Add empty `.ddColumn` elements** after the main `.ddColumn` containing all the drag items. The underlying script will automatically distribute the images evenly across all available columns. For example, with 9 images and 3 `.ddColumn` elements, the script distributes 3 images per column.

3. **Maximum of 3 `.ddColumn` elements total** in the `dragContainer` — having 4 or more causes the fourth column to wrap below the others, recreating the original problem.

```html
<!-- CORRECT: Many images distributed across 3 columns; col-12 wrapper (Standard) — never col-md-10 -->
<div class="row">
    <div class="col-12">
        <div class="activity interactive" number="3A">
            <div class="row"><div class="col-12">
                <div class="dragAndDrop images" layout="column">
                    <div class="row dropContainer" blanks="3">
                        <!-- drop columns here -->
                    </div>
                    <div class="row dragContainer">
                        <div class="ddColumn">
                            <!-- ALL drag items go in this first ddColumn -->
                            <div class="drag" option="1"><img src="..." alt="" class="img-fluid"></div>
                            <div class="drag" option="2"><img src="..." alt="" class="img-fluid"></div>
                            <!-- ... more items ... -->
                        </div>
                        <div class="ddColumn"></div>
                        <div class="ddColumn"></div>
                    </div>
                    <div class="row">
                        <div class="activityButton reset">Reset</div>
                        <div class="activityButton undo hidden">Undo</div>
                        <div class="activityButton checkAnswer hidden">Check answers</div>
                    </div>
                </div>
            </div></div>
        </div>
    </div>
</div>
```

**Choosing the number of empty `.ddColumn` elements:**
- 4–6 drag items: Add **1** empty `.ddColumn` (2 columns total) — images split into 2 groups
- 7+ drag items: Add **2** empty `.ddColumn` elements (3 columns total) — images split into 3 groups
- NEVER exceed 3 `.ddColumn` elements total in the `dragContainer`

**Side-by-side variant:**
```html
<div class="dragAndDrop row" layout="column">
    <div class="col-6"><div class="row dropContainer"><!-- ddColumns --></div></div>
    <div class="col-6 align-self-end"><div class="row dragContainer"><!-- ddColumns --></div></div>
</div>
```

**With hoverBoxes:** Each `.drag` has two `<p>` — second revealed on hover:
```html
<div class="drag" option="1">
    <p>Default text</p>
    <p>Hover reveal text</p>
</div>
```

**With images as column headers:** When images are used as column headings in `ddColumn`, wrap them in a sizing column for better proportions:
```html
<div class="ddColumn">
    <div class="col-md-6 offset-md-3 col-12">
        <img class="img-fluid" loading="lazy" src="images/column_header.jpg" alt="">
    </div>
    <div class="drop" option="1"></div>
    <div class="drop" option="1"></div>
</div>
```

**⚠️ CRITICAL — Outer container width:** D&D column layout activities should use `col-md-12 col-12` as their outer content wrapper (not the standard `col-md-8`) to accommodate multiple drop columns plus the drag container without cramping. **EXCEPTION:** When the D&D column uses images and has many drag items (6+), use `col-12` (Standard) or `col-md-11 col-12` (Inquiry & Fundamentals) instead — **never `col-md-10`** (see constraint 56 and the image distribution guidance above).

---

## FIB (Fill in Blank) Layout

Drop zones are inline `<span>` elements:

```html
<div class="dragAndDrop" layout="FIB">
    <div class="row dropContainer">
        <p>This is an <span class="drop" option="1"></span> sentence with <span class="drop" option="2"></span> blanks.</p>
    </div>
    <div class="row">
        <div class="drag" option="1"><p>example</p></div>
        <div class="drag" option="2"><p>inline</p></div>
    </div>
    <div class="row">
        <div class="activityButton reset">Reset</div>
        <div class="activityButton undo hidden">Undo</div>
        <div class="activityButton checkAnswer hidden">Check answers</div>
    </div>
</div>
```

**Two-column parallel text (translation exercises):**
```html
<div class="row dropContainer">
    <div class="row dropBorder">
        <div class="col-6 paddingR"><p>English sentence</p></div>
        <div class="col-6 paddingL"><p><span class="drop" option="1"></span> translated text.</p></div>
    </div>
</div>
```

---

## Scatter Layout

Drop zones positioned absolutely over an image:

```html
<div class="dragAndDrop" layout="scatter">
    <div class="row dropContainer">
        <div class="drop col-2" top="0%" left="0%" option="1"></div>
        <div class="drop col-2" top="26.66%" left="16.66%" option="2"></div>
        <img src="images/image.jpg" alt="" class="img-fluid">
    </div>
    <div class="row">
        <div class="drag col-2" option="1"><p>Label 1</p></div>
        <div class="drag col-2" option="2"><p>Label 2</p></div>
    </div>
    <div class="row">
        <div class="activityButton reset">Reset</div>
        <div class="activityButton undo hidden">Undo</div>
        <div class="activityButton checkAnswer hidden">Check answers</div>
    </div>
</div>
```

**With bubble/pointer positions:**
```html
<div class="drop col-2" top="13.33%" left="0%" option="1" bubble="top-center"></div>
<div class="drop col-2" top="13.33%" left="0%" option="1" pointer="top-center"></div>
```
Bubble values: `top-center`, `bot-center`, `left`, `right`, `bot-left`, `top-right`

---

## Area Layout (Free-form, no correct answer)

```html
<div class="dragAndDrop" layout="area">
    <div class="drop">
        <img src="images/World_Map.svg" alt="World Map" class="img-fluid">
        <div class="drag" option="1" style="width:50px">
            <img class="dragImage" src="images/map_pin.svg" alt="Map pin">
        </div>
    </div>
    <div class="row">
        <div class="col">
            <div class="activityButton reset">Reset</div>
            <div class="activityButton undo hidden">Undo</div>
        </div>
    </div>
</div>
```

**External drag container:**
```html
<div class="dragAndDrop row" layout="area">
    <div class="dragContainer col-12">
        <div class="drag" option="1" style="width:50px">
            <img class="dragImage" src="images/map_pin.svg" alt="Map pin">
        </div>
    </div>
    <div class="drop">
        <img src="images/World_Map.svg" alt="World Map" class="img-fluid">
    </div>
</div>
```

**Clone (reusable):** `<div class="drag clone" option="1">`

**Grouped:** `<div class="dragContainer group col-1">`

---

## Venn Layout

See also COMP_10 in `04_COMP_SEGMENTS_OVERLAYS.md` for standalone Venn diagrams.

```html
<div class="dragAndDrop" layout="venn" venn-type="twoCircle"
     left-circle-label="A's" right-circle-label="B's" intersection-label="Both">
    <div class="questionContainer"><p>Instructions</p></div>
    <div class="vennContainer">
        <svg class="vennSVG"></svg>
        <div class="drop venn-drop" option="left-circle"></div>
        <div class="drop venn-drop" option="intersection"></div>
        <div class="drop venn-drop" option="right-circle"></div>
    </div>
    <div class="row dragContainer">
        <div class="drag" option="left-circle"><p>A</p></div>
        <div class="drag" option="intersection"><p>AB</p></div>
        <div class="drag" option="right-circle"><p>B</p></div>
    </div>
    <div class="row">
        <div class="activityButton reset">Reset</div>
        <div class="activityButton undo hidden">Undo</div>
        <div class="activityButton checkAnswer hidden">Check answers</div>
    </div>
</div>
```




