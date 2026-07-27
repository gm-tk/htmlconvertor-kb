> **Last updated:** Thursday, 16th July, 2026 9:30 PM
> **Granular part A (1 of 5) of `02_DATA_CONTENT_VERIFICATION.md`** — Interactive data pattern recognition (patterns 1-13, speech bubbles, tag primacy).
> All sibling parts live in `02_DATA_CONTENT_VERIFICATION/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
> **Last updated:** Thursday, 16th July, 2026 9:30 PM

# 06 — Interactive Data Pattern Recognition
 
> **When to load:** During Phase 5, when extracting data from writer-provided interactive content in the PageForge text file.
 
---
 
## Overview
 
Writers provide interactive data in distinct patterns. Recognising these is essential for correctly extracting questions, answers, and options from the PageForge text content.
 
In the PageForge text file, tables are delimited by `┌─── TABLE ───` / `└─── END TABLE ───`, columns by `║`, and in-cell line breaks by `/`. Red text markers (`🔴[RED TEXT]...[/RED TEXT]🔴`) may appear inside table cells — process these normally (strip markers, extract tags, surface substantive instructions as VISIBLE red flags — see Comment & Red Flag Policy below).
 
---
 
## Pattern 1: Single Data Table (Most Common)
 
Interactive tag followed by a table with all data:
 
```
[drag and drop column autocheck]
┌─── TABLE ───
│ Row 0: Column 1 heading ║ Column 2 heading
│ Row 1: Item A (col 1) ║ Item B (col 2)
│ Row 2: Item C (col 1) ║ Item D (col 2)
└─── END TABLE ───
```
 
**Used by:** Drag and drop, dropdown quiz (grid), reorder, memory game, slider chart, word drag, bingo, clicking order, radio quiz, MCQ
 
---
 
## Pattern 2: Front/Back Table Rows
 
Data table with `[front]` and `[back]` (or `[flip]`) rows:
 
```
[flip cards]
┌─── TABLE ───
│ Row 0: [front] ║ Card 1 text + [image] ║ Card 2 text + [image]
│ Row 1: [back]  ║ Card 1 back text      ║ Card 2 back text
└─── END TABLE ───
```
 
In OSAI401/501, each card may have its own tag pair:
```
[flip card 1]
[front] [H3] Heading [image] URL
[back] [body] Description text
```
 
**Used by:** Flip cards, click drops
 
---
 
## Pattern 3: Hint/Slide Table
 
Two-column table with `hint` and `slide` headers:
 
```
[hint slider]
┌─── TABLE ───
│ Row 0: hint  ║ slide
│ Row 1: Prompt 1 ║ Reveal 1
│ Row 2: Prompt 2 ║ Reveal 2
└─── END TABLE ───
```
 
**Used by:** Hint slider
 
---
 
## Pattern 4: Numbered Items (Dropdown Paragraph)
 
Paragraph tag with individually numbered dropdown items:
 
```
[dropdown quiz paragraph]
[body] Paragraph text with blanks
[Dropdown 1] Options (correct: X)
[Dropdown 2] Options
...
```
 
**Used by:** Dropdown quiz (paragraph layout)
 
---
 
## Pattern 5: Numbered Slides
 
```
[carousel]
[slide 1] Text + [image] URL
[slide 2] Text + [image] URL
...
```
 
**Used by:** Carousel, rotating banner (note: these are DIFFERENT components — carousel uses `.carousel`/`.viewer`/`.item`, rotating banner uses `.rotateBanner`/`.bannerContainer`/`.bannerItem`)
 
---
 
## Pattern 6: Numbered Shapes/Tabs
 
```
[shape hover]
[shape 1] Content
[shape 2] Content
 
[tabs]
[tab 1] Label + content
[tab 2] Label + content
```
 
**Used by:** Shape hover, tabs
 
---
 
## Pattern 7: Numbered Accordions
 
```
[accordion]
[accordion 1] Heading + content
[accordion 2] Heading + content
[end accordions]
```
 
**Used by:** Accordion
 
---
 
## Pattern 8: Speech Bubble in Table Row
 
```
┌─── TABLE ───
│ [speech bubble] Character text ║ [image] URL
└─── END TABLE ───
```
 
**Used by:** All speech bubble variants
 
---
 
## Pattern 9: Conversation Layout
 
Multiple sequential speech entries:
 
```
[speech bubble] Conversation layout
Prompt 1: User question
AI response: Reply text
Prompt 2: Follow-up
AI response: Follow-up reply
```
 
**Used by:** Chat demonstrations (OSAI401, OSAI501)
 
---
 
## Pattern 10: Word Select Table
 
Table with coloured cell markers:
 
```
[Table wordSelect]
CS – Green cells = correct, Red = incorrect
┌─── TABLE ───
│ Item 1 ║ Item 2 ║ Item 3
│ Item 4 ║ Item 5 ║ Item 6
└─── END TABLE ───
```
 
CS red text identifies correct (green) and incorrect (red) cells.
 
**Used by:** Word select (table layout)
 
---
 
## Pattern 11: Axis Labels (Slider Chart)
 
```
[slider chart]
[X axis labels] Label 1 ║ Label 2 ║ Label 3
[Y axis labels] Value range
[image – thumbs up]
[image – thumbs down]
```
 
**Used by:** Slider chart
 
---
 
## Pattern 12: Info Trigger Image (Labelled Image Overlay)
 
Tag followed by an image reference and a list/table of trigger labels with their popup content:
 
```
[info trigger image]
[image] URL
Label 1: Popup text 1
Label 2: Popup text 2
Label 3: Popup text 3
```
 
Or in table format:
```
[info trigger image]
┌─── TABLE ───
│ Row 0: Label ║ Info text
│ Row 1: No feelings ║ AI can't feel happy, sad, or excited like people do.
│ Row 2: Needs examples ║ AI learns from lots of pictures, words, or data.
└─── END TABLE ───
[image] URL
```
 
**Used by:** Info trigger image
 
---
 
## Pattern 13: Self-Assessment / Survey Table (multiChoiceQuiz)
 
A table of self-assessment statements with rating column headers. May be accompanied by a CS red text instruction requesting "tick boxes", "checkboxes", or "columns where students can click".
 
```
🔴[RED TEXT] CS, please create three columns where ākonga can click what column they're in – tick boxes? [/RED TEXT]🔴
┌─── TABLE ───
│ Row 0: Section heading ║ Always ║ Sometimes ║ Not yet
│ Row 1: I take turns and let others have a go. ║  ║  ║ 
│ Row 2: I show respect when others are speaking. ║  ║  ║ 
│ Row 3: I cooperate to get things done together. ║  ║  ║ 
└─── END TABLE ───
```
 
Or as a simple list of statements with column headers:
```
🔴[RED TEXT] CS, tick boxes for self-assessment [/RED TEXT]🔴
Section heading
Always / Sometimes / Not yet
• Statement 1
• Statement 2
• Statement 3
```
 
**Used by:** multiChoiceQuiz (survey/self-assessment variant) — see COMP_02 in `03_COMP_CORE_INTERACTIVES.md`
 
**Key signals:** Writer keywords like "tick box", "checkbox", "click what column"; content shows "I can/do..." statements with discrete rating categories; all ratings are equally valid (self-reflection, not graded).
 
**⚠️ Two `multiChoiceQuiz` modes — do not confuse them:**
- **Self-assessment (`checkAll`)** — the pattern above. A self-rating rubric where *every* option is valid. All `mcqOption` elements carry `value="correct"`.
- **Graded multi-select (`mcqSomeSelected`)** — a *graded* MCQ where each question has some correct and some wrong options, and the student is scored. This is NOT a self-assessment table; it is a question-and-options set (often one scenario/question per row or per carousel slide, each with a list of selectable options where one or more are correct). Correct options carry `value="correct"`; wrong options carry **no** `value` attribute. Build this with `multiChoiceQuiz mcqSomeSelected` — NOT with the standard `multiQuiz` (`mQContainer`/`mQOption`) component, and NOT with `checkAll`. See COMP_02 in `03_COMP_CORE_INTERACTIVES.md` for the full graded-variant structure.
---
 
## Speech Bubble Handling
 
### Implementation
Use the documented `speechBubble` component from COMP_09 in `04_COMP_SEGMENTS_OVERLAYS.md`.
 
### Variant Mapping
| Writer Tag | Implementation |
|---|---|
| `[speech bubble]` | Single character: `bubble-basic` + positional class from layout (`bubble-left`/`bubble-right`/`bubble-top`/`bubble-bottom`) + `no-hover` on text-only bubbles. Conversation: alternating `bubble-right`/`bubble-left` + `no-hover` |
| `[speech bubble front]` | Same as standard |
| `[speech bubble tiles]` | Multiple bubbles with `bubble-basic no-hover` in grid |
| `[speech bubble two people]` | Two characters, alternating bubble-right/bubble-left + `no-hover` |
| `[thinking speech bubble]` | Standard bubble + `no-hover` + **RED FLAG** for thought bubble CSS variant |
 
### Positional Class for Single-Character Bubbles
The positional class on single-character speech bubbles is determined by the layout in the Writers Template:
- Text on LEFT, image on RIGHT → `bubble-left` (tail points left toward speaker on right)
- Image on LEFT, text on RIGHT → `bubble-right` (tail points right toward speaker on left)
- Writer CS instruction specifies "above" → `bubble-top` (image in separate row below)
- Writer CS instruction specifies "below" → `bubble-bottom` (image in separate row above)
**Writer positional instructions always override** the default left/right positioning derived from the table cell order.
 
### Content Merging
Speech bubble data from tables (text in one cell, image ref in another) MUST be merged into a single visual component — NOT rendered as separate table + paragraph.
 
### Multi-Paragraph Wrapping
When a speech bubble contains multiple `<p>` elements, the paragraphs MUST be wrapped in an additional `<div>` inside the bubble element. Single-paragraph bubbles do not need this wrapper.
 
### Image Column Padding
Image columns adjacent to speech bubbles in horizontal layouts require padding classes: `paddingL` when the image is on the right, `paddingR` when the image is on the left.
 
### Conversation Layout
Render as sequential prompt/response sections using alternating `bubble-right` / `bubble-left` classes, each with `no-hover`.
 
---
 
## Writer Tag Primacy Rule
 
**The writer's square-bracket tag is the primary directive for component selection.** Table column headers describe data structure, not component type. If writer tags `[click drop]`, implement click drops — even if table headers suggest another format.
 
 
 
 
