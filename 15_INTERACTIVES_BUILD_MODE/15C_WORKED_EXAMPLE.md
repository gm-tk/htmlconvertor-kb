> **Last updated:** Thursday, 30th July, 2026 2:02 PM
> **Granular part C (3 of 3) of `15_INTERACTIVES_BUILD_MODE.md`** — One worklist entry taken end to end: input, reading, output, and why it is right.
> All sibling parts live in `15_INTERACTIVES_BUILD_MODE/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# 15C — Worked example: one worklist entry → one finished build

A real entry from `XDLS908_interactives.txt`, taken end to end. The output matches the documented
`dragAndDrop` column-layout pattern **and** matches, structure for structure, what the human
developer shipped for this exact activity in the finished module.

## The input entry

```
INTERACTIVE 1 of 65
-------------------------------------
REFERENCE CODE:  XDLS908-INT-01-01-dragAndDrop
   ↳ search this exact code in XDLS908-01.html to place the finished interactive

File: XDLS908-01.html
Placeholder marker: data-cv2-index="1" (the placeholder div to replace)
Activity: 1A
Type: dragAndDrop

Content:
🔴[RED TEXT] [Interactive activity – drag and drop] Answers are placed in the correct columns –
please place outside the table for this activity for learners to drag to the correct place. [/RED TEXT]🔴
┌─── TABLE ───
│ Writing ║ Speaking ║ Visual Communication
│ 🔴[RED TEXT] [Image]  [/RED TEXT]🔴Texting (https://www.istockphoto.com/photo/texting-gm1358386001-…) ║ Waiata (https://www.istockphoto.com/photo/waiata-gm1180972216-…) ║ Road signs (https://www.istockphoto.com/photo/road-signs-gm172206037-…)
│ Letter (https://www.istockphoto.com/photo/letter-gm1210162574-…) ║ Kōrero (https://www.istockphoto.com/photo/korero-gm1345678901-…) ║ Emoji (https://www.istockphoto.com/photo/emoji-gm1298765432-…)
└─── END TABLE ───

-------------------------------------
```

## Reading it

- The red instruction says the table's items are ANSWERS shown in their correct columns, to be
  placed OUTSIDE the columns for learners to drag in — i.e. a **column-layout dragAndDrop**, with
  the three category columns coming from the header row. It is a note about the drag mechanic,
  **not** a request for instant feedback — so no `autoCheck`, and the standard three-button row
  ships.
- The header row (`Writing ║ Speaking ║ Visual Communication`) gives the three column headings.
- Each body cell is one draggable item. The `[Image]` tag + iStock URL means the drag items are
  images — in **column** layout that is simply an `<img class="img-fluid">` inside each `.drag`
  (the `images` modifier class belongs to the standard layout).
- The `option` value is the **column number**: column-1 items get `option="1"`, column 2
  `option="2"`, column 3 `option="3"` — the two drops in a column share that column's option.
- Every `.ddColumn` must exist in **both** containers: all the drags sit in the first drag-column,
  followed by two empty padding `ddColumn` divs.
- iStock IDs are the number after `gm` (constraint 61) → `images/iStock-1358386001.jpg` etc.

## The output (as it appears inside the built file)

```html
<section class="cv2-built" data-cv2-ref="XDLS908-INT-01-01-dragAndDrop">
<div class="dragAndDrop" layout="column">
    <div class="row dropContainer">
        <div class="ddColumn">
            <p>Writing</p>
            <div class="drop" option="1"></div>
            <div class="drop" option="1"></div>
        </div>
        <div class="ddColumn">
            <p>Speaking</p>
            <div class="drop" option="2"></div>
            <div class="drop" option="2"></div>
        </div>
        <div class="ddColumn">
            <p>Visual Communication</p>
            <div class="drop" option="3"></div>
            <div class="drop" option="3"></div>
        </div>
    </div>
    <div class="row dragContainer">
        <div class="ddColumn">
            <div class="drag" option="1">
                <img src="images/iStock-1358386001.jpg" alt="Texting" class="img-fluid" />
            </div>
            <div class="drag" option="1">
                <img src="images/iStock-1210162574.jpg" alt="Letter" class="img-fluid" />
            </div>
            <div class="drag" option="2">
                <img src="images/iStock-1180972216.jpg" alt="Waiata" class="img-fluid" />
            </div>
            <div class="drag" option="2">
                <img src="images/iStock-1345678901.jpg" alt="Kōrero" class="img-fluid" />
            </div>
            <div class="drag" option="3">
                <img src="images/iStock-172206037.jpg" alt="Road signs" class="img-fluid" />
            </div>
            <div class="drag" option="3">
                <img src="images/iStock-1298765432.jpg" alt="Emoji" class="img-fluid" />
            </div>
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
</section>
```

## Why this is right

- **The reference code is untouched** — the stitcher finds `XDLS908-INT-01-01-dragAndDrop`,
  splices the `<div class="dragAndDrop" …>` into `XDLS908-01.html` where the marker sits (inside
  activity 1A, which the page already renders), and deletes both anchors.
- **It matches the documented component pattern and the shipped human build of this exact
  activity**: a plain `dragAndDrop layout="column"` wrapper, drops paired to columns by shared
  `option` number, image drags without the `images` class, all drags in the first drag-column with
  empty padding columns after it, and the three-button row. Had the writer asked for instant
  feedback the wrapper would gain `autoCheck` and the buttons row would shrink to Reset only.
- **No `blanks` attribute** — that is only for pre-filled slots, which this activity does not
  have.
- **The red instruction was obeyed and dropped** — no `🔴`, no `[tags]`, no ASCII table lines
  survive in the output.
- iStock IDs became `images/iStock-{ID}.jpg` placeholders with the writer's own item names as alt
  text; the macron in Kōrero is intact.
- **No activity box, no page rows, no scripts** — the widget starts at its own wrapper, exactly
  what the marker's spot expects.
