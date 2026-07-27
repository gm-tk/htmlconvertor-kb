> **Last updated:** Tuesday, 14th July, 2026 5:39 PM
> **Granular part A (1 of 6) of `03_COMP_CORE_INTERACTIVES.md`** — COMP_00 component index & universal rules.
> All sibling parts live in `03_COMP_CORE_INTERACTIVES/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
> **Last updated:** Tuesday, 14th July, 2026 5:39 PM

# COMP_00 — Component Index & Universal Rules

> **When to load:** Before generating ANY interactive component HTML.

---

## Universal Rules

- All interactives MUST be inside `<div class="activity">` wrapper (typically `class="activity interactive"`)
- **⚠️ CRITICAL — One interactive per activity (UNIVERSAL, constraint 62):** Each `activity` wrapper contains **at most ONE interactive component**. When the writer places two or more interactives under a single activity heading, **split them into separate sequential activities** — the first interactive keeps the writer's activity number; each subsequent interactive becomes the next activity letter — and **renumber the following activities accordingly** (e.g. two drag-and-drops under a writer's "Activity 1D" become Activities 1D and 1E, and a trailing 1E Word Find becomes 1F). Flag the split with a visible red note at the head of each newly created activity, e.g. `<p style="color: red; font-weight: bold;">Red Flag: Writer placed two interactives under Activity 1D — split into 1D and 1E (one interactive per activity); subsequent activities renumbered.</p>`, so the renumbering is auditable against the writer's source. Supporting elements inside the activity — audio buttons/triggers, images, hover translations, instructional text and lists — are NOT counted as interactives; the count applies to the whitelisted interactive components that form the activity's task (D&D, quizzes, self check, games, ordering, sliders, etc.). See `02_DATA_CONTENT_VERIFICATION.md` → Verification Checklist.
- Activity wrapper goes inside: `<div class="row"><div class="col-12">`
- **⚠️ CRITICAL — No leading spaces in class attributes:** Class attribute values must NEVER begin with a leading space. Always write `class="activityButton reset"` (no space before `activityButton`), never `class=" activityButton reset"`
- Commented-out sections in source (wrapped in `<!-- -->`) are deprecated — do NOT use
- **⚠️ CRITICAL — Never comment interactive answers:** NEVER add an HTML comment that records the correct answer(s) of an interactive (e.g. `<!-- correct: 2, 4 -->`). Correct answers belong ONLY in the functional markup attributes the engine reads (`option`, `answer`, `value="correct"`, etc.). A human-readable answer comment is a security leak — code-savvy students can read it with browser inspect tools. Anything a designer needs to know goes in a VISIBLE red flag instead. See `02_DATA_CONTENT_VERIFICATION.md` → Comment & Red Flag Policy.
- **⚠️ CRITICAL — Numbered instructions use `<ol><li>`, never manual numbering (UNIVERSAL):** When the writer numbers the instructions, steps, or sub-questions of an activity/interactive (e.g. "1. Drag and drop the labels…", "2. Drag these images…"), render them as a semantic ordered list (`<ol><li>…</li></ol>`) — NEVER as paragraphs with a typed-in number (`<p>1. …</p>`). This applies to **every interactive, everywhere** (D&D sub-questions, quiz instruction lists, ordering tasks, etc.). When numbered items are split by other content (an interactive between step 1 and step 2), continue the count with the `start` attribute: `<ol start="2"><li>…</li></ol>`. Do NOT carry a leading number inside an MCQ/quiz **question** string either — strip the typed number; the component supplies its own numbering. See `02_DATA_CONTENT_VERIFICATION.md` → Numbered Instructions in Activities.

---

## autoCheck Auto-Application

`autoCheck` is a modifier that gives the student instant feedback on each selection (and removes the separate Undo / Check buttons). Normally it is applied only when the writer's intended behaviour calls for it.

**EXCEPTION — three templates always get autoCheck.** When the structural reference is one of these dedicated template files:

- `refresh_template_0.0_1_template_ECH`
- `refresh_template_0.0_2_template_1-3`
- `refresh_template_0.0_3_template_4-6`

then `autoCheck` MUST be applied automatically to **every interactive that supports it**, whether or not the writer asked for it. Apply it silently — no red flag needed.

**Interactives that support `autoCheck`** — apply the attribute / class per the component's documented structure, and drop the now-unneeded Undo / Check buttons exactly as that component's "With autoCheck" example shows: Drag & Drop (all answer-checked layouts), Dropdown Quiz, MCQ, multiChoiceQuiz, Radio Quiz, Word Select, and any other interactive whose COMP section documents an `autoCheck` variant.

**Interactives that do NOT support `autoCheck`** — leave unchanged: components with no right/wrong answer (Self Check, Self Reflection, reflection sliders/surveys, Sketcher, Stop Watch, free-form Area-layout D&D) and content-segmentation components (accordion, carousel, tabs, etc.).

**Rules:**
- If a component's COMP section documents both a plain and an `autoCheck` form, use the `autoCheck` form for these three templates.
- If the writer ALSO explicitly requested instant feedback, there is no conflict — `autoCheck` is applied either way.
- For any OTHER template, do NOT auto-apply `autoCheck` — apply it only when the writer's behaviour calls for it.
- **Typing Quiz exception:** the typing quiz supports `autoCheck` (add `autoCheck` to the `.typing` container), but — unlike every other interactive — it KEEPS its `reset` / `checkAnswer hidden` / `showAnswer hidden` buttons under `autoCheck`. Do NOT drop the buttons for a typing quiz. See COMP_02 — Typing Quiz.
- A designer may issue a one-off instruction to suppress `autoCheck` on a specific interactive even within these three templates — honour that as a one-off override (see `08_MODULE_SUPPORT_DEBUGGING.md` → One-Off Module Overrides).

---

## Component File Index

| Section | Location | Components |
|---------|----------|-----------|
| `COMP_01` | `03_COMP_CORE_INTERACTIVES.md` | Drag & Drop (standard, column, FIB, scatter, area, venn layouts) |
| `COMP_02` | `03_COMP_CORE_INTERACTIVES.md` | Dropdown Quiz, MCQ, multiChoiceQuiz (Survey/Self-Assessment `checkAll` + graded multi-select `mcqSomeSelected`), Radio Quiz, Typing Quiz |
| `COMP_03` | `03_COMP_CORE_INTERACTIVES.md` | Self Check, Self Reflection, Reflection Slider |
| `COMP_04` | `03_COMP_CORE_INTERACTIVES.md` | Memory Game, Puzzle, Crossword, Word Find, Bingo, Word Drag |
| `COMP_05` | `03_COMP_CORE_INTERACTIVES.md` | Reorder, Clicking Order, Word Select, Checklist |
| `COMP_06` | `03_COMP_CORE_INTERACTIVES.md` | Slider (Scale/Survey), Slider Chart |
| `COMP_07` | `04_COMP_SEGMENTS_OVERLAYS.md` | Accordion, Carousel, Rotating Banner, Click Drop, Flip Card, Tabs, Hint, Hint Slider, Modal |
| `COMP_08` | `04_COMP_SEGMENTS_OVERLAYS.md` | Info Trigger, Audio Trigger, Audio Image, Image Label, Image Zoom, Word Highlighter |
| `COMP_09` | `04_COMP_SEGMENTS_OVERLAYS.md` | Speech Bubbles (all variants) |
| `COMP_10` | `04_COMP_SEGMENTS_OVERLAYS.md` | Shape Hover, Timeline, Venn Diagram |
| `COMP_11` | `04_COMP_SEGMENTS_OVERLAYS.md` | Sketcher, Number Line, Stop Watch |
| `COMP_12` | `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` | Glossary, Kanji Cards, Language Fonts, Translate Section, Reo Translate, MathJax |
| `COMP_13` | `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` | Video, Audio, PDF, Padlet, Desmos |
| `COMP_14` | `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` | Activities, Alerts, Cultural Alerts, Buttons, Tables, Columns, Quotes, etc. |

---

## Button Class Quick Reference

| Interactive | Reset Class | Check Class | Other |
|---|---|---|---|
| Drag and Drop | `activityButton reset` | `activityButton checkAnswer hidden` | `activityButton undo hidden` |
| Dropdown Quiz | `activityButton reset` | `activityButton checkAnswer hidden` | — |
| MCQ (standard) | `activityButton mcqReset` | `activityButton hidden mcqAswers` | — |
| MCQ (image) | `activityButton mcqReset` | `activityButton mcqAnswers hidden` | `activityButton undo hidden` |
| multiChoiceQuiz (survey/self-assessment) | `activityButton mcqReset` | — | `activityButton undo hidden` |
| multiChoiceQuiz (graded — mcqSomeSelected) | `activityButton mcqReset` | `activityButton hidden mcqAswers` | optional Show-explanations: `mcqReset hideShowAnswer` + `mcqAswers revealShowAnswer` + `showAnswer hidden` |
| Radio Quiz | `activityButton reset` | `activityButton checkAnswer hidden` | — |
| Typing Quiz | `activityButton reset` | `activityButton checkAnswer hidden` | `activityButton showAnswer hidden` |
| Memory Game | `activityButton memGameReset` | — | — |
| Reorder | `reorderReset button activityButton` | `reorderAnswer button activityButton` | — |
| Slider Chart | `activityButton reset` | `activityButton checkAnswer hidden` | — |
| Bingo | `activityButton reset-btn` | `activityButton hidden check-btn` | — |
| Clicking Order | `activityButton cloReset` | `activityButton cloCheck hidden` | — |
| Word Drag | `activityButton reset` | `activityButton checkAnswer hidden` | `activityButton undo hidden` |
| Word Select | `activityButton reset` | `activityButton hidden checkAnswer` | — |
| Sketcher | `activityButton skResetButton` | — | — |
| Venn (D&D) | `activityButton reset` | `activityButton checkAnswer hidden` | `activityButton undo hidden` |

**⚠️ CRITICAL — No leading spaces:** Class attribute values must NEVER begin with a leading space. Always write `class="activityButton reset"`, never `class=" activityButton reset"`. This applies to ALL elements across ALL generated HTML files.

**MCQ SPELLING:** Standard = `mcqAswers` (no 'n'). Image = `mcqAnswers` (with 'n'). This is intentional.

---

## Deprecated Components — DO NOT USE

| Component | Reason |
|---|---|
| `layout="feedback"` (D&D) | Commented out |
| `layout="mixedContent"` (D&D) | "not to be used until properly styled" |
| `randomSelect` (standard) | "not developed. dont use." |
| TikTok embeds | "TikTok no longer allowed" |
| `imageZoom` layout="hover"/"hoverContained" | Commented out — only `hoverFollow` is active |

---

## Show/Hide Answer Pattern (Cross-Component)

Applies to D&D, MCQ, and other interactives:

```html
<div class="row">
    <div class="activityButton reset hideShowAnswer">Reset</div>
    <div class="activityButton hidden checkAnswer revealShowAnswer">Check answers</div>
    <div class="activityButton hidden showAnswer">
        <span>Show</span><span>Hide</span> answers
    </div>
</div>
<div class="showAnswerContent">
    <p>Detailed answer explanation here.</p>
</div>
```

---

## Key Rules (Repeated for Emphasis)

- **Accordion Fallback:** Each term/item is its own accHead/accContent pair
- **Exploratory Dropdown:** All options correct using `answer="1 2 3 ..."` — this is intentional for student exploration activities (no red flag needed)
- **Shuffle Default:** Allow shuffling by default. Only `noShuffle` when explicitly requested
- **Two-Sided Content:** Writer's tag determines component (click drop vs flip card)
- **Writer Tag Primacy:** Tag overrides table headers




