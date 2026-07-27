> **Last updated:** Tuesday, 14th July, 2026 5:39 PM
> **Granular part F (6 of 6) of `03_COMP_CORE_INTERACTIVES.md`** — COMP_05 ordering & selecting; COMP_06 sliders.
> All sibling parts live in `03_COMP_CORE_INTERACTIVES/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# COMP_05 — Ordering & Selecting

---

## Reorder

**Container class:** `reorder`
**Required wrapper:** `<div class="activity interactive">`

### re-standard Layout (Sequential Items)

The standard reorder for ordering sequential items (e.g., chronological events, steps in a process). Uses `layout="re-standard"` with the `row` class on the `.reorder` div and `reorderList col-12` as the item wrapper.

**⚠️ CRITICAL — Correct structure:** The `re-standard` layout does NOT use `reorderContent`, does NOT use `item` attributes on `.reorderItem` elements, and does NOT use the `grid` attribute. The correct order is determined by the source order of the items in the HTML — the first `.reorderItem` in the source is position 1, the second is position 2, etc. The JavaScript shuffles them on page load.

```html
<div class="reorder row" layout="re-standard">
    <div class="reorderList col-12">
        <div class="reorderItem"><p>First item (correct position 1)</p></div>
        <div class="reorderItem"><p>Second item (correct position 2)</p></div>
        <div class="reorderItem"><p>Third item (correct position 3)</p></div>
    </div>
    <div class="col-12">
        <div class="reorderReset button activityButton">Reset</div>
        <div class="reorderAnswer button activityButton">Check answer</div>
    </div>
</div>
```

**Key rules for re-standard:**
- `layout="re-standard"` (NOT `layout="standard"`)
- `row` class on the `.reorder` div: `<div class="reorder row" layout="re-standard">`
- Items wrapped in `<div class="reorderList col-12">` (NOT `reorderContent`)
- NO `item` attributes on `.reorderItem` elements — correct order is determined by source order
- NO `grid` attribute on the `.reorder` div
- Buttons use `reorderReset button activityButton` and `reorderAnswer button activityButton` (same as other reorder variants)
- Check answer button text is singular: "Check answer" (NOT "Check answers")
- Items are listed in their CORRECT order in the HTML source — the script shuffles them on page load

**Image variant:**
```html
<div class="reorder row" layout="re-standard">
    <div class="reorderList col-12">
        <div class="reorderItem"><img src="images/first.jpg" class="img-fluid" alt="First"></div>
        <div class="reorderItem"><img src="images/second.jpg" class="img-fluid" alt="Second"></div>
    </div>
    <div class="col-12">
        <div class="reorderReset button activityButton">Reset</div>
        <div class="reorderAnswer button activityButton">Check answer</div>
    </div>
</div>
```

### re-paragraph Layout

For letter-level reordering within words/sentences. Uses `reorderSentence`, `reorderList`, and inline `reorderItem` spans instead of the standard block-level structure.

**⚠️ CRITICAL — `[word drag]` for letter unscrambling:** When the writer specifies `[word drag]` and the task is to unscramble individual letters into a known word or phrase (e.g., "unscramble the letters to form **artificial intelligence**"), ALWAYS use `reorder` with `layout="re-paragraph"` — NOT the `wordDrag` component. The `wordDrag` component is for a different use case (building words by selecting from a shared letter pool). Letter unscrambling — where all necessary letters are presented scrambled and must be dragged into the correct sequential order — is a `reorder re-paragraph` task.

**How to distinguish:**
- Writer provides the exact letters of a known word/phrase to rearrange → `reorder re-paragraph`
- Writer provides a pool of letters to build unknown words from → `wordDrag`

### Single Word

```html
<div class="reorder row" layout="re-paragraph" order="0">
    <p class="reorderSentence">
        <span class="reorderList">
            <span class="reorderItem"><span>a</span></span>
            <span class="reorderItem"><span>r</span></span>
            <span class="reorderItem"><span>t</span></span>
        </span>
    </p>
    <div class="col-12">
        <div class="reorderReset button activityButton hidden">Reset</div>
        <div class="reorderAnswer button activityButton hidden">Check answer</div>
    </div>
</div>
```

### Multi-Word (e.g., "artificial intelligence")

When unscrambling a phrase with multiple words, use a SINGLE `.reorder` div. Each word gets its own `<span class="reorderList">`, and the lists are separated by `<br>` inside one `<p class="reorderSentence">`:

```html
<div class="reorder row" layout="re-paragraph" order="0">
    <p class="reorderSentence">
        <span class="reorderList">
            <span class="reorderItem"><span>t</span></span>
            <span class="reorderItem"><span>a</span></span>
            <span class="reorderItem"><span>i</span></span>
            <span class="reorderItem"><span>a</span></span>
            <span class="reorderItem"><span>c</span></span>
            <span class="reorderItem"><span>i</span></span>
            <span class="reorderItem"><span>r</span></span>
            <span class="reorderItem"><span>l</span></span>
            <span class="reorderItem"><span>f</span></span>
            <span class="reorderItem"><span>i</span></span>
        </span>
        <br>
        <span class="reorderList">
            <span class="reorderItem"><span>g</span></span>
            <span class="reorderItem"><span>c</span></span>
            <span class="reorderItem"><span>i</span></span>
            <span class="reorderItem"><span>n</span></span>
            <span class="reorderItem"><span>n</span></span>
            <span class="reorderItem"><span>t</span></span>
            <span class="reorderItem"><span>e</span></span>
            <span class="reorderItem"><span>l</span></span>
            <span class="reorderItem"><span>i</span></span>
            <span class="reorderItem"><span>e</span></span>
            <span class="reorderItem"><span>l</span></span>
            <span class="reorderItem"><span>e</span></span>
        </span>
    </p>
    <div class="col-12">
        <div class="reorderReset button activityButton hidden">Reset</div>
        <div class="reorderAnswer button activityButton hidden">Check answer</div>
    </div>
</div>
```

**Key rules for re-paragraph:**
- Each letter is a `<span class="reorderItem"><span>letter</span></span>` (double-wrapped)
- All items wrapped in `<span class="reorderList">` inside `<p class="reorderSentence">`
- **Multi-word phrases:** Use ONE `reorder` div with multiple `<span class="reorderList">` groups separated by `<br>` — do NOT create separate reorder components per word
- Uses `row` class on the `.reorder` div
- **`order="0"` attribute:** Add `order="0"` on the `.reorder` div — this tells the JS to present the letters in scrambled order initially
- **⚠️ CRITICAL — Letters must be in CORRECT order in the HTML source.** The script reads the source order as the answer key (i.e., the correct solution), then `order="0"` causes the JS to shuffle/randomise the letter positions on page load to create the challenge. If letters are pre-scrambled in the source, the scrambled order becomes the "correct" answer and the activity will not function properly. Always list letters in the correct spelling order of the target word.
- **Buttons:** Both `reorderReset` and `reorderAnswer` include the `hidden` class (they appear after the user begins interacting): `<div class="reorderReset button activityButton hidden">Reset</div>`
- **⚠️ NEVER use `wordDrag` for letter unscrambling** — always use `reorder` with `layout="re-paragraph"` when the task is rearranging given letters into a known target word or phrase

---

## Clicking Order

**Container class:** `clickingOrder`
**Required wrapper:** `<div class="activity interactive">`

```html
<div class="clickingOrder row" layout="standard" grid="3">
    <div class="cloClicker" item="1"><p>First</p></div>
    <div class="cloClicker" item="2"><p>Second</p></div>
    <div class="cloClicker" item="3"><p>Third</p></div>
    <div class="cloClicker blank" item="0"><p>Not selectable</p></div>
    <div class="row">
        <div class="activityButton cloReset">Reset</div>
        <div class="activityButton cloCheck hidden">Check answers</div>
    </div>
</div>
```

**Attributes:**
- `item`: Order number. `item="0"` + `blank` = not selectable
- `grid`: 3, 4, 5, or 6
- Images: `<img class="cloClicker" item="1" src="...">`

---

## Word Select

**Container class:** `wordSelect`

### Standard Layout

```html
<div class="wordSelect autoCheck row">
    <div class="col-4 wordSelectOptions wSCenter">
        <div class="wordSelectButton" colour="blue" value="noun">Noun</div>
        <div class="wordSelectButton" colour="purple" value="verb">Verb</div>
    </div>
    <div class="col-8">
        <div class="wordSelectContainer">
            <p class="wordSelectText">
                <span>Non-selectable</span> text
                <span spanValue="noun">dog</span> more text
                <span spanValue="verb">runs</span>
            </p>
        </div>
    </div>
    <div class="col-12">
        <div class="activityButton reset">Reset</div>
    </div>
</div>
```

**Colour values:** `blue`, `purple`, `green`, `orange`

### Variants
- **oneSelect:** Add `oneSelect` class to `.wordSelect`
- **Scatter:** `layout="scatter"` — positioned over image
- **Table:** `layout="table"` — words in table cells

---

## Checklist / Selection Box

**Container class:** `selectionBox`

```html
<div class="selectionBox">
    <div class="sBoxItem"><p>Item 1</p></div>
    <div class="sBoxItem"><p>Item 2</p></div>
    <div class="sBoxItem"><p>Item 3</p></div>
</div>
```




# COMP_06 — Sliders

---

## Slider (Scale/Survey)

**Container class:** `slider`
**NOT an activity interactive** — can be standalone or inside activities.

```html
<div class="slider">
    <div class="slideContainer">
        <p class="slideQuestion">1. How do you feel about this?</p>
        <input class="slide" type="range" min="0" max="100" value="50">
        <div class="slidePoints">
            <p>Strongly<br>agree</p>
            <p>Strongly<br>disagree</p>
        </div>
    </div>
</div>
```

**Multiple points:**
```html
<div class="slideContainer">
    <p class="slideQuestion">Rate from 1-5</p>
    <input class="slide" type="range" min="1" max="5" value="1">
    <div class="slidePoints">
        <p>Agree</p>
        <p>Not sure</p>
        <p>Not sure</p>
        <p>Not sure</p>
        <p>Disagree</p>
    </div>
</div>
```

**No thumb variant:** Add `noSlide` class to `.slideContainer`

---

## Slider Chart

**Container class:** `slideChart`
**Required wrapper:** `<div class="activity interactive">`

```html
<div class="slideChart" layout="standard" max="10" xLabel="X Axis" yLabel="Y Axis">
    <div class="slideChartItem" answer="7"><p>Item 1</p></div>
    <div class="slideChartItem" answer="3"><p>Item 2</p></div>
    <div class="slideChartItem" answer="9"><p>Item 3</p></div>
    <div class="row">
        <div class="activityButton reset">Reset</div>
        <div class="activityButton checkAnswer hidden">Check answers</div>
    </div>
</div>
```