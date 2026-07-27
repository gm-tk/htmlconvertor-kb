> **Last updated:** Tuesday, 14th July, 2026 5:39 PM
> **Granular part C (3 of 6) of `03_COMP_CORE_INTERACTIVES.md`** — COMP_02 quizzes: dropdown, MCQ, survey variant.
> All sibling parts live in `03_COMP_CORE_INTERACTIVES/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# COMP_02 — Quizzes

---

## Dropdown Quiz

**Container class:** `dropQuiz`
**Required wrapper:** `<div class="activity interactive">`

### Standard (Grid) Layout

```html
<div class="dropQuiz" layout="standard">
    <div class="row questionContainer">
        <div class="question"><p>Question 1</p></div>
        <div class="question"><p>Question 2</p></div>
    </div>
    <div class="row dropContainer">
        <div class="drop" answer="1" options="Option A||Option B||Option C"></div>
        <div class="drop" answer="2" options="Option A||Option B||Option C"></div>
    </div>
    <div class="row">
        <div class="activityButton reset">Reset</div>
        <div class="activityButton checkAnswer hidden">Check answers</div>
    </div>
</div>
```

**Attributes:**
- `answer`: 1-based index of correct option
- `options`: `||` separated choices
- Multiple correct: `answer="1 3"` (space-separated)

### Paragraph Layout

**⚠️ CRITICAL:** The paragraph layout uses `dropParaContainer` (NOT `dropContainer`) and a different inner structure from the standard/scatter/list layouts. Each dropdown is built with `dropQuestion` > `dropDown` > `placeholder` + `options` divs. Use this layout ONLY when dropdowns are embedded inline within continuous paragraph text (fill-in-the-blank style).

```html
<div class="dropQuiz" layout="paragraph">
    <div class="dropParaContainer">
        <p>The capital of France is
            <div class="dropQuestion">
                <div class="dropDown" answer="2">
                    <p class="placeholder">Select one</p>
                    <div class="options">
                        <p>London</p>
                        <p>Paris</p>
                        <p>Berlin</p>
                    </div>
                </div>
            </div>
            and it is known for the
            <div class="dropQuestion">
                <div class="dropDown" answer="2">
                    <p class="placeholder">Select one</p>
                    <div class="options">
                        <p>Colosseum</p>
                        <p>Eiffel Tower</p>
                        <p>Big Ben</p>
                    </div>
                </div>
            </div>.
        </p>
    </div>
    <div class="row">
        <div class="activityButton reset">Reset</div>
        <div class="activityButton checkAnswer hidden">Check answers</div>
    </div>
</div>
```

**With numbered items (ordered list) — paragraph style (dropdowns inline within sentences):**
When the writer provides numbered sentences/questions where dropdowns replace blanks WITHIN the sentence text, wrap them in `<ol><li>` inside `dropParaContainer`:

```html
<div class="dropQuiz autoCheck" layout="paragraph">
    <div class="dropParaContainer">
        <ol>
            <li>
                Sentence text
                <div class="dropQuestion">
                    <div class="dropDown" answer="1 2 3">
                        <p class="placeholder">Select one</p>
                        <div class="options">
                            <p>option 1</p>
                            <p>option 2</p>
                            <p>option 3</p>
                        </div>
                    </div>
                </div>
                more sentence text.
            </li>
            <li>
                Another sentence
                <div class="dropQuestion">
                    <div class="dropDown" answer="1 2 3">
                        <p class="placeholder">Select one</p>
                        <div class="options">
                            <p>option A</p>
                            <p>option B</p>
                            <p>option C</p>
                        </div>
                    </div>
                </div>.
            </li>
        </ol>
    </div>
    <div class="row">
        <div class="activityButton reset">Reset</div>
        <div class="activityButton checkAnswer hidden">Check answers</div>
    </div>
</div>
```

**Key rules for paragraph layout:**
- Use `dropParaContainer` (NOT `dropContainer`)
- Each dropdown: `<div class="dropQuestion"><div class="dropDown" answer="..."><p class="placeholder">Select one</p><div class="options"><p>option</p>...</div></div></div>`
- `answer` attribute: 1-based index of correct option(s). Space-separated for multiple correct (e.g., `answer="1 2 3"`)
- For exploratory dropdowns where ALL options are correct, add `autoCheck` to the `dropQuiz` div and set `answer="1 2 3"` (all indices)
- Use `<ol><li>` when writer provides numbered items

### List Layout (Question-Answer Pairs)

**⚠️ CRITICAL — When to use list layout vs paragraph layout:** Use list layout when each numbered item is a **standalone question** with its own separate dropdown answer (question on the left, dropdown on the right). Use paragraph layout when dropdowns are **embedded inline within continuous sentence text** (fill-in-the-blank style). These are structurally different and must NOT be confused.

The list layout presents questions as numbered items with the question text on the left and a dropdown answer selector on the right. There is NO `layout` attribute on the `dropQuiz` div (it uses the default/no-layout variant). Each question uses a row with two columns.

```html
<div class="dropQuiz">
    <ol>
        <li>
            <div class="row">
                <div class="col-md-6 offset-md-0 col-12 paddingR">
                    <p>Question text goes here?</p>
                </div>
                <div class="col-md-6 offset-md-0 col-12 dropQuestion">
                    <div class="dropDown" answer="2">
                        <p class="placeholder">Select one</p>
                        <div class="options">
                            <p>Option A.</p>
                            <p>Option B (correct).</p>
                            <p>Option C.</p>
                            <p>Option D.</p>
                        </div>
                    </div>
                </div>
            </div>
        </li>
        <li>
            <div class="row">
                <div class="col-md-6 offset-md-0 col-12 paddingR">
                    <p>Another question text?</p>
                </div>
                <div class="col-md-6 offset-md-0 col-12 dropQuestion">
                    <div class="dropDown" answer="1">
                        <p class="placeholder">Select one</p>
                        <div class="options">
                            <p>Option A (correct).</p>
                            <p>Option B.</p>
                            <p>Option C.</p>
                        </div>
                    </div>
                </div>
            </div>
        </li>
    </ol>
    <div class="row">
        <div class="activityButton reset">Reset</div>
        <div class="activityButton checkAnswer hidden">Check answers</div>
    </div>
</div>
```

**Key rules for list layout:**
- NO `layout` attribute on the `.dropQuiz` div (do NOT use `layout="paragraph"` or `layout="standard"`)
- NO `dropParaContainer` wrapper — the `<ol>` sits directly inside `.dropQuiz`
- Each `<li>` contains a `<div class="row">` with two columns:
  - Left: `<div class="col-md-6 offset-md-0 col-12 paddingR">` containing the question in a `<p>` tag
  - Right: `<div class="col-md-6 offset-md-0 col-12 dropQuestion">` containing the dropdown
- Each dropdown uses the same inner structure: `<div class="dropDown" answer="..."><p class="placeholder">Select one</p><div class="options"><p>option</p>...</div></div>`
- `answer` attribute: 1-based index of correct option(s)
- This layout needs more room than the default `col-md-8 col-12` for its two-column question/answer rows. When it is paired with an `alertImage`, the activity container is `col-md-8 col-12` with the `alertImage` at `col-md-4` (8 + 4 = 12) — see the alertImage pairing pattern in COMP_14 of `05_COMP_LANGUAGE_MEDIA_LAYOUT.md`. A standalone wide instance uses `col-12` (Standard) or `col-md-11 col-12` (Inquiry & Fundamentals); activity wrappers never use `col-md-10` (see constraint 56).
- Inline formatting (e.g., `<i>` for quoted text within questions) is preserved as normal

### Scatter Layout

```html
<div class="dropQuiz" layout="scatter">
    <div class="dropScatterContainer">
        <div class="drop" top="10%" left="30%" answer="1" options="A||B||C"></div>
        <img src="images/image.jpg" alt="" class="img-fluid">
    </div>
    <div class="row">
        <div class="activityButton reset">Reset</div>
        <div class="activityButton checkAnswer hidden">Check answers</div>
    </div>
</div>
```

---

## Multiple Choice Quiz (MCQ)

**Container class:** `multiQuiz`
**Required wrapper:** `<div class="activity interactive">`

> **⚠️ DO NOT USE `multiQuiz` FOR A GRADED QUIZ — use the `multiChoiceQuiz` family instead.** Any multiple-choice activity where an answer is **right or wrong** (including a simple **single-answer, two-option** question such as "Is this a plant cell or an animal cell?") must be built with the `multiChoiceQuiz` class family (`mcqQuestion` / `mcqQuestionText` / `mcqOptions` / `mcqOption`), NOT the legacy `multiQuiz` / `question` / `mQContainer` / `mQOption` / `.answer` structure. The correct option carries `value="correct"`; wrong options carry no `value` attribute (for multi-correct quizzes add `mcqSomeSelected` on the container). Do NOT add a typed question number to `mcqQuestionText` — the component numbers its own questions. See **Multi Choice Quiz — Graded Multi-Select Variant** below and hard constraint 36. The `multiQuiz` structure documented here is retained only for legacy reference; new graded conversions should not reach for it.

### Standard MCQ

```html
<div class="multiQuiz" layout="standard">
    <div class="question"><p>Question text</p></div>
    <div class="mQContainer">
        <div class="mQOption"><p>Wrong answer</p></div>
        <div class="mQOption answer"><p>Correct answer</p></div>
        <div class="mQOption"><p>Wrong answer</p></div>
    </div>
    <div class="row">
        <div class="activityButton mcqReset">Reset</div>
        <div class="activityButton hidden mcqAswers">Show answers</div>
    </div>
</div>
```

**⚠️ CRITICAL:** Standard MCQ uses `mcqAswers` (NO 'n').

### Image MCQ

```html
<div class="multiQuiz" layout="image">
    <div class="question"><p>Question text</p></div>
    <div class="mQContainer">
        <div class="mQOption"><img src="images/wrong.jpg" class="img-fluid" alt=""></div>
        <div class="mQOption answer"><img src="images/correct.jpg" class="img-fluid" alt=""></div>
    </div>
    <div class="row">
        <div class="activityButton mcqReset">Reset</div>
        <div class="activityButton mcqAnswers hidden">Show answers</div>
    </div>
</div>
```

**⚠️ CRITICAL:** Image MCQ uses `mcqAnswers` (WITH 'n').

### Multiple Questions MCQ

```html
<div class="multiQuiz" layout="standard">
    <div class="question"><p>Q1?</p></div>
    <div class="mQContainer">
        <div class="mQOption answer"><p>Correct</p></div>
        <div class="mQOption"><p>Wrong</p></div>
    </div>
    <div class="question"><p>Q2?</p></div>
    <div class="mQContainer">
        <div class="mQOption"><p>Wrong</p></div>
        <div class="mQOption answer"><p>Correct</p></div>
    </div>
    <div class="row">
        <div class="activityButton mcqReset">Reset</div>
        <div class="activityButton hidden mcqAswers">Show answers</div>
    </div>
</div>
```

---

## Multi Choice Quiz — Survey/Self-Assessment Variant (multiChoiceQuiz)

**Container class:** `multiChoiceQuiz`
**Required wrapper:** `<div class="activity">` (or `<div class="activity interactive">`)

This is a distinct component from the standard `multiQuiz` MCQ. It is used for **self-assessment / survey-style** activities where students rate themselves against a set of statements using columns (e.g., "Always / Sometimes / Not yet"). All options are marked `value="correct"` because any choice is valid — this is a reflection tool, not a graded quiz.

**⚠️ CRITICAL — Do NOT confuse with `multiQuiz`:** The `multiChoiceQuiz` uses a completely different class structure (`multiChoiceQuiz`, `mcqQuestion`, `mcqOptions`, `mcqOption`) from the standard MCQ (`multiQuiz`, `question`, `mQContainer`, `mQOption`). They are separate components.

### Writer Intent Signals

Writers may request this component using various terms. Look for these signals:
- **Explicit keywords:** "tick box", "tickbox", "tick boxes", "checkbox", "check box", "check boxes"
- **Contextual signals:** A table/list of self-assessment statements with rating columns (e.g., "Always / Sometimes / Not yet", "Yes / No / Sometimes", "Confident / Developing / Not yet", "Can do / Learning / Need help")
- **Writer instructions:** Phrases like "create columns where ākonga can click what column they're in" or "students select which level they are at"
- **Content pattern:** A set of "I can..." or "I do..." statements paired with rating/frequency categories

**When the content is a self-assessment rubric or self-rating checklist, use `multiChoiceQuiz` — NOT a plain HTML table, NOT a standard MCQ, and NOT a radio quiz.**

### Standard Structure

```html
<div class="multiChoiceQuiz autoCheck emptyOptions checkAll" columns="column-4">
    <div class="row"></div>
    <div class="row">
        <div class="col-md-9 offset-md-0 col-12">
            <p><b>Section heading</b></p>
        </div>
        <div class="col-md-1 offset-md-0 col-12 center-text">
            <p><b>Always</b></p>
        </div>
        <div class="col-md-1 offset-md-0 col-12 center-text">
            <p><b>Sometimes</b></p>
        </div>
        <div class="col-md-1 offset-md-0 col-12 center-text">
            <p><b>Not yet</b></p>
        </div>
    </div>
    <div class="col-12 mcqQuestion">
        <div class="row">
            <div class="col-9">
                <p>I take turns and let others have a go.</p>
            </div>
            <div class="col-3">
                <div class="mcqOptions">
                    <p class="mcqOption" value="correct"></p>
                    <p class="mcqOption" value="correct"></p>
                    <p class="mcqOption" value="correct"></p>
                </div>
            </div>
        </div>
    </div>
    <div class="col-12 mcqQuestion">
        <div class="row">
            <div class="col-9">
                <p>I show respect when others are speaking.</p>
            </div>
            <div class="col-3">
                <div class="mcqOptions">
                    <p class="mcqOption" value="correct"></p>
                    <p class="mcqOption" value="correct"></p>
                    <p class="mcqOption" value="correct"></p>
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="activityButton mcqReset">Reset</div>
        <div class="activityButton undo hidden">Undo</div>
    </div>
</div>
```

### Modifier Classes

| Class | Purpose |
|---|---|
| `autoCheck` | Instant feedback on selection |
| `emptyOptions` | Option buttons have no visible text labels (the column headers serve as labels) |
| `checkAll` | All options are valid selections (self-assessment — no wrong answers) |

### Attributes

| Attribute | Purpose |
|---|---|
| `columns="column-N"` | Total number of columns in the layout. Count = 1 (statement column) + number of rating options. E.g., 3 rating options → `columns="column-4"` |

### Structure Rules

1. **First row:** Empty `<div class="row"></div>` (required spacer)
2. **Header row:** Contains the section heading in `col-md-9` and each rating column header in `col-md-1 center-text` with bold text
3. **Question rows:** Each `<div class="col-12 mcqQuestion">` contains a `.row` with:
   - `col-9` for the statement text
   - `col-3` containing `<div class="mcqOptions">` with one `<p class="mcqOption" value="correct"></p>` per rating column
4. **Button row:** `mcqReset` + `undo hidden`
5. **Number of `mcqOption` elements per question MUST equal the number of rating columns**
6. **All `mcqOption` elements use `value="correct"`** because every choice is valid in a self-assessment

### Column Sizing by Number of Options

| Rating Options | `columns` Attribute | Header Column | Option Columns |
|---|---|---|---|
| 2 options | `column-3` | `col-md-10` | 2 × `col-md-1` |
| 3 options | `column-4` | `col-md-9` | 3 × `col-md-1` |
| 4 options | `column-5` | `col-md-8` | 4 × `col-md-1` |

### With Section Image (Optional)

When the writer provides an image for a section heading (e.g., above the section title), include it in the header row:

```html
<div class="row">
    <div class="col-md-9 offset-md-0 col-12">
        <img class="img-fluid" loading="lazy" src="https://placehold.co/600x400?text=Image+Placeholder" alt="">
        <p><b>Section heading</b></p>
    </div>
    <!-- rating column headers... -->
</div>
```

---

