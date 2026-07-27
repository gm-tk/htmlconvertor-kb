> **Last updated:** Tuesday, 14th July, 2026 5:39 PM
> **Granular part E (5 of 6) of `03_COMP_CORE_INTERACTIVES.md`** — COMP_03 self check & reflection; COMP_04 games & word components.
> All sibling parts live in `03_COMP_CORE_INTERACTIVES/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# COMP_03 — Self Check & Reflection

---

## Self Check

**Container class:** `selfCheck`
**Required wrapper:** `<div class="activity interactive">`

Freeform text — no exact correct answer. Model answer shown after student types.

```html
<div class="selfCheck" accents="samoan">
    <p class="sCQuestion">What is the best advice?</p>
    <div class="sCText" checkOn="9">
        <textarea rows="2" placeholder="Type here"></textarea>
    </div>
    <p class="sCQuestion">Another question?</p>
    <div class="sCText" checkOn="12">
        <textarea rows="2" placeholder="Type here"></textarea>
    </div>
    <div class="sCAnswerContainer">
        <p>Model answer text here.</p>
        <p>Another model answer here.</p>
    </div>
</div>
```

**Attributes:**
- `checkOn`: Characters typed before answer revealed. Empty (`checkOn=""`) = auto (default 10)
- `accents`: Optional (samoan, maori, french, german, spanish)
- Can use `<input type="text">` instead of `<textarea>` for single-line

**Behaviour:** `.sCAnswerContainer` appears AFTER student types specified characters. Data does NOT save.

---

## Self Reflection

**Container class:** `selfReflection`

```html
<div class="selfReflection"></div>
```

**Variants:**
- Custom start: `<div class="selfReflection" startValue="0"></div>`
- Custom images: `<div class="selfReflection customImages" imageURL="images/beA" imageType="png" customImages="be_a_communicator||be_a_learner||be_a_thinker"></div>`
- Custom text: `<div class="selfReflection customText" customText="Very hard||Kinda hard||Kinda easy||Very easy"></div>`
- No images: `<div class="selfReflection noImages"></div>`
- No text: `<div class="selfReflection noText"></div>`

---

## Reflection Slider

Legacy slider with emoji images:

```html
<div class="row justify-content-center slider margB2">
    <div class="col-11">
        <div class="row justify-content-between">
            <div class="col-1"><img loading="lazy" src="self-reflection-emoji/sad.png" alt="" class="img-fluid imageCentral"></div>
            <div class="col-1"><img loading="lazy" src="self-reflection-emoji/neutral.png" alt="" class="img-fluid imageCentral"></div>
            <div class="col-1"><img loading="lazy" src="self-reflection-emoji/happy.png" alt="" class="img-fluid imageCentral"></div>
        </div>
        <div class="slideContainer">
            <input class="slide" type="range" min="0" max="100" value="50">
        </div>
    </div>
    <div class="col-12">
        <div class="row justify-content-between">
            <div class="col-3"><h5 class="text-center float-start">Not fun.<br>Too Hard.</h5></div>
            <div class="col-3"><h5 class="text-center">Ok. I had to work hard to do this.</h5></div>
            <div class="col-3"><h5 class="text-center float-end">Loved it!<br>Easy and fun.</h5></div>
        </div>
    </div>
</div>
```




# COMP_04 — Games & Word Components

---

## Memory Game

**Container class:** `memoryGame`
**Required wrapper:** `<div class="activity interactive">`

Cards come in MATCHING PAIRS. Each card is a `<div class="memCard">` carrying a `match="N"` attribute — the two cards sharing the same `match` value are the pair (e.g. a word card and its picture card both carry `match="1"`). Each card has a face-down `cardFace` (showing `<h3>?</h3>`) and a hidden `cardHidden` holding the actual content (text or image).

```html
<div class="memoryGame" memCardSize="lg">
    <div class="memCard" match="1">
        <div class="cardFace"><h3>?</h3></div>
        <div class="cardHidden">
            <p class="memText sassoonIB-text">Meerkat</p>
        </div>
    </div>
    <div class="memCard" match="1">
        <div class="cardFace"><h3>?</h3></div>
        <div class="cardHidden">
            <img class="img-fluid" loading="lazy" src="images/iStock-2224188967.jpg" alt="A meerkat" />
        </div>
    </div>
    <!-- each pair shares the same match="N"; continue for every pair -->
    <div class="clearDiv"></div>
    <div class="activityButton memGameReset">Reset</div>
</div>
```

**Attributes:**
- `memCardSize`: card size on the `.memoryGame` container — `"lg"` is the production value used for Years 1–3 word/picture matching. There is NO `grid` attribute — sizing is the named `memCardSize` attribute.
- `match="N"`: numeric pair id on each `.memCard`. The two cards with the same `match` value form the matching pair. Matching is by this attribute — NOT by identical hidden content.
- Text cards: `<p class="memText sassoonIB-text">…</p>` inside `.cardHidden`. Note the bold infant font class is `sassoonIB-text` (not `sassoonI-text`).
- Image cards: `<img class="img-fluid" loading="lazy" src="…" alt="…" />` inside `.cardHidden`.

**Card structure:** every `.memCard` has exactly two children — `<div class="cardFace"><h3>?</h3></div>` (the face-down "?" the student sees first) and `<div class="cardHidden">…</div>` (revealed on click).

**Reset:** a `<div class="clearDiv"></div>` separator followed by a bare `<div class="activityButton memGameReset">Reset</div>` — both placed directly inside the `.memoryGame` container (NOT wrapped in a `<div class="row">`).

> **Inline-style boundary note (constraint #2).** Production module files have historically also carried an inline `style="font-family: SassoonInfantStd, Sassoon, sans-serif; font-size: 22px; font-weight: bold; line-height: 1.2;"` on every `memText` text card. The `memText sassoonIB-text` **class** is the supported, constraint-#2-compliant styling hook and is what this project emits. The inline font block is a known boundary item: do NOT auto-emit it — constraint #2 forbids invented inline CSS. If a specific module requires it, treat it as an explicit per-module / one-off designer instruction (see `08` → One-Off Module Overrides); it is not a standing rule.

---

## Puzzle

**Container class:** `puzzle`
**Required wrapper:** `<div class="activity interactive">`

```html
<div class="row puzzle showGrid" image="template-example-dino" activated="4"></div>
```

**Attributes:**
- `image`: Puzzle piece set name (from `central-images/puzzle-pieces/`)
- `activated`: Complexity — `4`, `12`, or `20` pieces
- `showGrid`: Shows grid lines

---

## Crossword

**Container class:** `crossword`
**Requires:** `<script type="text/javascript" src="../js/crossword.js"></script>`

```html
<div class="crossword row" layout="standard" accents="maori" crosswordData="crossword"></div>
```

**Attributes:**
- `accents`: samoan, maori, french, german, spanish (leave empty if not needed)
- `crosswordData`: Data file name
- Optional classes: `jpnFont`, `chiFont`, `sassoon-text`, `sassoonI-text`, `secondary`, `tertiary`, `echSize`, `prmSize`

---

## Word Find

**Container class:** `wordFind`
**Requires:** `<script type="text/javascript" src="../js/wordFind.js"></script>`

```html
<div id="WF" class="col-12 wordFind" layout="standard" wordFindData="wordFind"></div>
<div class="clearDiv"></div>
```

**Attributes:**
- `wordFindData`: Data file name
- Optional classes: `jpnFont`, `chiFont`, `sassoonI-text`

---

## Bingo

**Container class:** `bingo`
**Required wrapper:** `<div class="activity interactive">`

```html
<div class="bingo col-12">
    <h4>Card 1</h4>
    <div class="bingoContainer" grid="4">
        <div class="number" value="correct"><p>24</p></div>
        <div class="number" value="correct"><p>3</p></div>
        <div class="number"><p>7</p></div>
        <div class="number" value="correct"><p>19</p></div>
    </div>
    <div class="row">
        <div class="activityButton reset-btn">Reset</div>
        <div class="activityButton hidden check-btn">Check</div>
    </div>
</div>
```

**Attributes:**
- `grid`: Columns (typically `"4"`)
- `value="correct"`: Marks correct selection

---

## Word Drag

**Container class:** `wordDrag`
**Required wrapper:** `<div class="activity">`

```html
<div class="row wordDrag" layout="standard" letters="a|b|c|t|m|o" wordLength="3">
    <div class="col-12">
        <div class="wordDragContainer"></div>
    </div>
    <div class="col-12">
        <div class="wordDropContainer"></div>
    </div>
    <div class="col-12 wordDragList">
        <div class="word" word="cat||bat||mat"></div>
    </div>
    <div class="col-12 wordDragButtons">
        <div class="activityButton reset">Reset</div>
        <div class="activityButton undo hidden">Undo</div>
        <div class="activityButton checkAnswer hidden">Check answers</div>
    </div>
</div>
```

**Attributes:**
- `letters`: Pipe-delimited available letters
- `wordLength`: Number of positions
- `word`: Correct word(s), `||` for alternatives
- Optional `audioName` on `.word`
- `lockedLetters` + `lockedPos`: Lock letters in position
- Layouts: `standard`, `standardAudio`
- Optional classes: `elk` (early literacy), `circle` (circular tiles)

**⚠️ CRITICAL — Do NOT use wordDrag for letter unscrambling:** When the writer specifies `[word drag]` but the task is to unscramble/rearrange all the letters of a known word or phrase (e.g., "unscramble the letters to form **artificial intelligence**"), use `reorder` with `layout="re-paragraph"` instead — see COMP_05 Reorder. The `wordDrag` component is ONLY for building words by selecting letters from a shared pool where multiple words can be formed (e.g., given letters a, b, c, t, m, o — form "cat", "bat", or "mat").




