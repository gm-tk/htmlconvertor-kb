> **Last updated:** Tuesday, 14th July, 2026 5:39 PM
> **Granular part D (4 of 6) of `03_COMP_CORE_INTERACTIVES.md`** — COMP_02 quizzes: graded multi-select, radio, typing.
> All sibling parts live in `03_COMP_CORE_INTERACTIVES/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## Multi Choice Quiz — Graded Multi-Select Variant (multiChoiceQuiz mcqSomeSelected)

**Container class:** `multiChoiceQuiz mcqSomeSelected`
**Required wrapper:** `<div class="activity interactive">`

This is the **graded** form of `multiChoiceQuiz`. Unlike the survey/self-assessment variant (`checkAll`, where every option is valid), the `mcqSomeSelected` variant is a **graded quiz**: each question has one or more **correct** options and one or more **wrong** options, and the student is scored on their selection.

**⚠️ CRITICAL — When to use this, and what NOT to use:**
- Use `multiChoiceQuiz mcqSomeSelected` whenever the content is a **graded multiple-choice / multiple-select quiz** built with the `mcqQuestion` / `mcqQuestionText` / `mcqOptions` / `mcqOption` class family (e.g., a set of scenarios each with selectable answer options where some are right and some are wrong).
- Do **NOT** build a graded quiz of this kind as the standard `multiQuiz` (`question` / `mQContainer` / `mQOption` / `.answer`). The standard `multiQuiz` is a *different* component; mixing the two class families produces a broken, non-functional quiz.
- Do **NOT** use the `checkAll` modifier here. `checkAll` is the self-assessment flag that makes every option count as correct. A graded quiz needs real right/wrong scoring, so `checkAll` must be absent.

**Background — why this variant exists:** A graded quiz was once mistakenly built using the standard `multiQuiz` structure (`mQContainer`/`mQOption`) and had to be rebuilt. The `mcqSomeSelected` variant is the correct, documented component for graded multi-select MCQs. Build it directly from this section — do not improvise from the `multiQuiz` pattern.

### Writer Intent Signals

- A set of **questions or scenarios**, each followed by a list of **answer options**.
- The writer marks one (or more) options as the **correct answer** — e.g. a ✅ tick, "(correct answer)", bold, or a separate answer key.
- The remaining options are plausible but **wrong** distractors.
- Often paired with **per-question explanations / feedback** ("why this is the right answer").
- May be requested inside a **carousel** (one question per slide).

### Class Structure

| Class | Role |
|---|---|
| `multiChoiceQuiz` | Component container (same family as the survey variant) |
| `mcqSomeSelected` | Modifier — marks this as a *graded* multi-select quiz (some options correct, some wrong) |
| `mcqQuestion` | One question block (carries `col-12` when used directly inside a `.row`) |
| `mcqQuestionText` | The `<p>` holding the question/scenario text |
| `mcqOptions` | Container for that question's answer options |
| `mcqOption` | One answer option (`<p>`). Correct options carry `value="correct"`; **wrong options carry NO `value` attribute** |

### Standard Structure (all questions on one page)

```html
<div class="activity interactive" number="3A">
    <div class="row">
        <div class="col-12">
            <h3>Activity heading</h3>
            <p>Instruction text — e.g. "Select the correct answer(s) for each question."</p>

            <div class="multiChoiceQuiz mcqSomeSelected">
                <div class="row">

                    <div class="col-12 mcqQuestion">
                        <p class="mcqQuestionText">Question 1 text?</p>
                        <div class="mcqOptions">
                            <p class="mcqOption">Wrong option</p>
                            <p class="mcqOption" value="correct">Correct option</p>
                            <p class="mcqOption">Wrong option</p>
                            <p class="mcqOption">Wrong option</p>
                        </div>
                    </div>

                    <div class="col-12 mcqQuestion">
                        <p class="mcqQuestionText">Question 2 text?</p>
                        <div class="mcqOptions">
                            <p class="mcqOption" value="correct">Correct option</p>
                            <p class="mcqOption">Wrong option</p>
                            <p class="mcqOption" value="correct">Correct option</p>
                            <p class="mcqOption">Wrong option</p>
                        </div>
                    </div>

                </div>
                <div class="row">
                    <div class="activityButton mcqReset">Reset</div>
                    <div class="activityButton hidden mcqAswers">Check answers</div>
                </div>
            </div>
        </div>
    </div>
</div>
```

### Modifier Classes & Attributes

| Class / Attribute | Purpose |
|---|---|
| `mcqSomeSelected` | **Required.** Marks the quiz as graded multi-select (some options correct, some wrong). |
| `autoCheck` | Optional. Instant feedback as the student selects, instead of waiting for the Check button. |
| `resetAll` | Optional. Reset clears every question at once. |
| `columns="column-N"` | Optional. Lays the options out in N columns (e.g. `column-3`). Omit for a simple stacked list. |

### Structure Rules

1. **Container:** `<div class="multiChoiceQuiz mcqSomeSelected">` — add `autoCheck` / `resetAll` only if the writer's behaviour calls for it. Never add `checkAll`.
2. **All `mcqQuestion` blocks sit inside a single `<div class="row">`.** Each question block is `<div class="col-12 mcqQuestion">`.
3. **Question text** goes in `<p class="mcqQuestionText">…</p>` (NOT a bare `<p>`, NOT a `<div class="question">`).
4. **Options** sit in `<div class="mcqOptions">`, one `<p class="mcqOption">` per option.
5. **Correct options:** `<p class="mcqOption" value="correct">…</p>`. **Wrong options:** `<p class="mcqOption">…</p>` — no `value` attribute at all.
6. A question may have **more than one** correct option (true multi-select) — mark each correct one with `value="correct"`.
7. **Button row:** `mcqReset` (Reset) + `hidden mcqAswers` (Check answers). Note the spelling **`mcqAswers`** (no 'n') — same as the standard MCQ. Never write a leading space in the class attribute.

### Inside a Carousel (one question per slide)

When the writer requests the graded quiz as a carousel (one scenario per slide), keep the `multiChoiceQuiz mcqSomeSelected` wrapper around the whole carousel, and put each `mcqQuestion` inside a carousel `.item`:

```html
<div class="multiChoiceQuiz mcqSomeSelected autoCheck">
    <div class="row carousel">
        <div class="col-md-8 col-12 viewer">
            <div class="item">
                <div class="col-12 mcqQuestion">
                    <p class="mcqQuestionText">Scenario 1?</p>
                    <div class="mcqOptions">
                        <p class="mcqOption">Wrong option</p>
                        <p class="mcqOption" value="correct">Correct option</p>
                    </div>
                </div>
            </div>
            <div class="item">
                <div class="col-12 mcqQuestion">
                    <p class="mcqQuestionText">Scenario 2?</p>
                    <div class="mcqOptions">
                        <p class="mcqOption" value="correct">Correct option</p>
                        <p class="mcqOption">Wrong option</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="activityButton mcqReset">Reset</div>
        <div class="activityButton hidden mcqAswers">Check answers</div>
    </div>
</div>
```

(Carousel viewer column is `col-md-8 col-12` per COMP_07 — see `04_COMP_SEGMENTS_OVERLAYS.md`.)

### Per-Question Explanations (Optional Show-Explanations Pattern)

When the writer supplies an explanation/feedback for each question, the explanations are NOT placed inside the `mcqQuestion` blocks. Instead, gather them into a single `showAnswerContent` block placed BELOW the activity, revealed by a Show/Hide toggle button. The three buttons are wired via the documented cross-component show/hide pattern:

```html
<div class="multiChoiceQuiz mcqSomeSelected">
    <div class="row">
        <!-- mcqQuestion blocks ... -->
    </div>
    <div class="row">
        <div class="activityButton mcqReset hideShowAnswer">Reset</div>
        <div class="activityButton hidden mcqAswers revealShowAnswer">Check answers</div>
        <div class="activityButton hidden showAnswer"><span>Show</span><span>Hide</span> explanations</div>
    </div>
    <div class="showAnswerContent">
        <ol>
            <li>Explanation for question 1.</li>
            <li>Explanation for question 2.</li>
        </ol>
    </div>
</div>
```

- `mcqReset hideShowAnswer` — resetting also collapses the explanations.
- `mcqAswers revealShowAnswer` — clicking "Check answers" reveals the "Show explanations" button.
- `showAnswer` — toggles the `showAnswerContent` panel.

If the writer did not supply per-question explanations, omit this entire pattern and use the simple two-button row from the Standard Structure above.

### Survey vs Graded — Quick Comparison

| | Survey / Self-Assessment | Graded Multi-Select |
|---|---|---|
| Container | `multiChoiceQuiz autoCheck emptyOptions checkAll` | `multiChoiceQuiz mcqSomeSelected` |
| Option marking | EVERY `mcqOption` is `value="correct"` | Correct: `value="correct"`; wrong: no `value` |
| Scoring | None — every choice valid (reflection) | Real right/wrong scoring |
| Layout | Rating columns ("Always / Sometimes / Not yet") | Question + answer options |
| Typical content | "I can…" self-rating statements | Scenario/question quizzes |

---

## Radio Quiz

**Container class:** `radioQuiz`
**Required wrapper:** `<div class="activity interactive">`

**⚠️ CRITICAL — True/False heading row:** Radio quizzes used for True/False activities MUST include a heading row with `T` and `F` column labels plus a `Description` label. This heading row uses the class `headings` on the `.row` div, and contains `<p class="true">T</p>`, `<p class="false">F</p>`, and `<p class="description">Description</p>` in matching column widths. Without this heading row, students cannot see which radio button corresponds to True and which to False.

```html
<div class="radioQuiz">
    <!-- autoCheck -->
    <div class="row headings">
        <div class="col-sm-1 col-2">
            <p class="true">T</p>
        </div>
        <div class="col-sm-1 col-2">
            <p class="false">F</p>
        </div>
        <div class="col-sm-9 offset-sm-1 col-8">
            <p class="description">Description</p>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-2 col-4 radioButtons" answer="true"></div>
        <div class="col-sm-9 offset-sm-1 col-8">
            <p>Statement that is true</p>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-2 col-4 radioButtons" answer="false"></div>
        <div class="col-sm-9 offset-sm-1 col-8">
            <p>Statement that is false</p>
        </div>
    </div>
    <div class="row">
        <div class="activityButton reset">Reset</div>
        <div class="activityButton checkAnswer hidden">Check answers</div>
    </div>
</div>
```

**Key rules for True/False radio quiz:**
- The `<!-- autoCheck -->` comment goes directly inside the `.radioQuiz` div before the heading row
- The heading row uses `class="row headings"` and contains three columns:
  - `<div class="col-sm-1 col-2"><p class="true">T</p></div>` — True column header
  - `<div class="col-sm-1 col-2"><p class="false">F</p></div>` — False column header
  - `<div class="col-sm-9 offset-sm-1 col-8"><p class="description">Description</p></div>` — Description column header
- Each statement row follows the standard pattern with `radioButtons` and the statement text

**With hints:**
```html
<div class="col-sm-9 offset-sm-1 col-8">
    <p>Statement text <span class="hint"></span></p>
    <div class="row">
        <div class="col-12">
            <div class="hintDropContent">
                <p>Explanation of why this is true/false.</p>
            </div>
        </div>
    </div>
</div>
```

---

## Typing Quiz

**Container class:** `typing`
**Required wrapper:** `<div class="activity interactive">`
**Required attribute:** `layout="standardNoBorder"` on the `.typing` container

The student types the missing word(s) into an inline `form-control` input. Every question is a `<div class="row">`, and ALL question rows are wrapped in a single `<div class="typingContainer">`. The button row sits AFTER the `typingContainer` but still inside the `.typing` container.

**Image + sentence form** (image left, sentence-with-blank right — the standard Years 1–3 form):

```html
<div class="typing" layout="standardNoBorder">
    <div class="typingContainer">
        <div class="row">
            <div class="col-md-4 col-12 paddingR">
                <img class="img-fluid" loading="lazy" src="images/iStock-XXXXXXX.jpg" alt="A car driving across a narrow bridge" />
            </div>
            <div class="col-md-8 col-12 paddingL">
                <p class="sassoonI-text">The bridge was narrow, <input class="form-control" type="text" answer="so" placeholder="Type here" caseSensitive="false" /> the car moved slowly.</p>
            </div>
        </div>
        <!-- repeat one <div class="row"> per question, all inside typingContainer -->
    </div>
    <div class="row">
        <div class="activityButton reset">Reset</div>
        <div class="activityButton checkAnswer hidden">Check</div>
        <div class="activityButton showAnswer hidden">Show</div>
    </div>
</div>
```

**Text-only form** (no image — the `<p>` sits directly in the row):

```html
<div class="typing" layout="standardNoBorder">
    <div class="typingContainer">
        <div class="row">
            <p>Question text <input class="form-control" type="text" answer="correct answer" placeholder="Type here" caseSensitive="false" /> more text.</p>
        </div>
        <!-- one <div class="row"> per question, all inside typingContainer -->
    </div>
    <div class="row">
        <div class="activityButton reset">Reset</div>
        <div class="activityButton checkAnswer hidden">Check</div>
        <div class="activityButton showAnswer hidden">Show</div>
    </div>
</div>
```

**Attributes:**
- `layout="standardNoBorder"`: required on the `.typing` container.
- `answer` (on each `<input>`): the correct text. Multiple acceptable answers: `answer="answer1||answer2"`.
- `caseSensitive="false"`: required on each `<input>` — makes the check case-insensitive.
- The input is `class="form-control"` (NOT `typeInput`), `type="text"`, with `placeholder="Type here"` (a visible prompt in the field — NOT an empty `placeholder=""`).
- Optional `accents` on `.typing`: `accents="maori"` (samoan, maori, french, german, spanish).

**Buttons:** three `activityButton`s — `reset`, `checkAnswer hidden`, `showAnswer hidden` — in a `<div class="row">` placed AFTER the `typingContainer`.

**autoCheck:** under the three auto-`autoCheck` templates (see COMP_00 → autoCheck Auto-Application) add `autoCheck` to the container (`<div class="typing autoCheck" layout="standardNoBorder">`). **Unlike every other interactive, the typing quiz KEEPS all three buttons (`reset`, `checkAnswer hidden`, `showAnswer hidden`) even with `autoCheck`** — do NOT drop them.




