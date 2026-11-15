> **Last updated:** Sunday, 15th November, 2026 7:15 PM
> **Granular part D (4 of 4) of `18_ASSESSMENT_MODE.md`** — The Pathways Assessment Activities Template (Level 1 Pathways unit-standard assessments): recognition, the header-bar mapping that replaces `18A` §4.1 for it, template guidance that is never rendered, the two What-to-do options, the centralised AI traffic-light image, the module button, the dropbox text. Added by CL-0142 (ADMIN MODE).
> All sibling parts live in `18_ASSESSMENT_MODE/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# 18D — Assessment Mode: the Pathways Assessment Activities Template

> **When to load:** with `18A` and `18B`, whenever Assessment Mode runs on a document that passes the Pathways test in Section 11.1. Section numbers continue from `18C` (which ends at Section 10).
>
> **Scope — (a) Series + level: Pathways Level 1 unit-standard assessments** (the sixteen Level 1 Pathways unit standards; Pathways Level 2 is held — `14_SUBJECT_GLOBAL_PARAMETERS.md` → §14.2). Everything in `18A` and `18B` still applies to these pages **except where this part says otherwise**; where the two disagree, this part wins for a Pathways-template document and has no effect on any other assessment.
>
> **Source:** Stephanie Charles (Curriculum Development Lead), *"Assessment Template tweaks for Pathways Unit Standard assessment"*, 12 November 2026, forwarded by Kate Scanlon and Persephone Samuels (Design Team Lead) to Gavin McGruddy — `Pathways Assessment Activities Template.docx`. Pathways revised the general template so all sixteen assessments share one wording; the page layout is unchanged, and the AI guidance is a centralised image that is the same on every page. Actioned by ADMIN MODE, CL-0142.

---

## 11. THE PATHWAYS ASSESSMENT TEMPLATE

### 11.1 Recognising it

A `.docx` that passes the `18A` §2 fingerprint is a **Pathways-template document** when its details table has `Subject:` reading **Pathways** **and** either a **`Classification`** row (with or without a colon) **or** the What-to-do lines **`Option 1: Separate assessment document`** / **`Option 2: Instructions included in this assessment`**. Its bold title line reads **"NCEA Internal Assessment Activity"**.

A Pathways assessment still written on the older general template (a `Brief description:` row, the standard's title after a dash in the `Unit Standard:` row, no `Classification` row and no Option lines — e.g. the US4249 page) is **not** a Pathways-template document: convert it by `18A`/`18B` alone, unchanged.

The template is colour-coded for writers — **blue** text is fixed wording every assessment shares, **red** text is guidance the writer replaces. Run colour still carries no meaning in the output (`18B` §6.1): the blue wording is ordinary student content and is converted as written; the red guidance is handled by Section 11.3.

### 11.2 The details table → the header bar (replaces the `18A` §4.1 table for this template)

| Word row | Goes to |
|---|---|
| `Activity name:` (the English module name) | `<h3>` in `.col-md-8 .assessment` — the big heading on the bar |
| `Classification` (e.g. `Communication Skills > Interpersonal Communications`) | the `<p>` directly under that `<h3>`, written as the writer has it (`>` escaped as `&gt;`) |
| `Unit Standard:` — the number and version as the writer types it (`12356v8`, `US12356 v8`, `12356 version 8`) **+** `Subject:` | `<p class="standard"><b>US{nnnn} (Version {v}), Pathways</b></p>` — the house form already used for Pathways pages (`US4249 (Version 10)`); no version given → `US{nnnn}, Pathways` + a `Designer/Developer To Do:` to add the version |
| `Title:` (the unit standard's own title) | `<p class="description">` |
| level **+** Internal **+** `Credits:` | `<p class="credits">Level {n} Internal Assessment <br>{n} Credits <i class="fa-solid fa-arrow-up-right-from-square"></i></p>` |
| the standard code `US{nnnn}` | the NZQA link (`https://www.nzqa.govt.nz/nqfdocs/units/pdf/{nnnn}.pdf`, `18A` §4.2), the `<title>` `NCEA Level {n} US{nnnn}` and the file name `US{nnnn}.html` |
| `Method of Assessment:` (`Written` / `Practical` / `Written and practical`) | **not rendered** — it no longer carries Internal/External; every Pathways-template assessment is **Internal** (the template's own title line says so) |
| `Are any 3rd Party Items required?` | as `18A` §4.1 — not rendered; **Yes** ticked → the `Designer/Developer To Do:` at the top of Student Resources |

**The level** is the first digit of the module code the writer gives for the Student Resources button (`PWY1009` → Level 1); with no module code it is **1** — every assessment in this series is Level 1 (§14.2), so no To Do is raised for it. The same module code gives the course folder for every media path (`PWY1009` → `PWY1000`, `18B` §7.2).

**A row left as the template's red instruction** (`[Use English module name]`, `[Insert title of unit standard]`, `[Insert classification …]`, `[Insert number of credits in numbers]`) is an empty field: `18B` §7 item 4 applies — build the bar with what exists plus a To Do naming the field, never the bracketed text.

### 11.3 Template guidance — never rendered

These are instructions to the writer, not student content. They are stripped exactly like `[body]` / `[H3]` / `[Button]` (`18A` §4.3, constraint 3):

1. **The opening note** — `Note: The blue text is templated, red to be customised.`
2. **Example boxes** — every one-cell table whose first line begins `Example` (`Example for US1285: …` under What to do; `Example` / `Submit: …` under How to present your learning). The whole box is dropped. Because a box is being removed, the Designer Summary says so in one line (item 5, *not rendered*) so the designer can check nothing of the writer's own went with it.
3. **The option labels** — the bold `Option 1: Separate assessment document`, `Option 2: Instructions included in this assessment` and the `OR` line between them (Section 11.4).
4. **A stray full-stop paragraph** — the template's lone `.` paragraph above the dropbox button.
5. **The bracketed red instructions**, where the writer has replaced them — `[use wording that reflects the purpose and outcomes …]`, `[Replace this section with the specific evidence requirements …]` and the list of formats inside it, `[delete "and quiz" if no quiz in the module]`, `[insert outcomes / performance criteria from unit standard below like a rubric]`, `[use module code for button text eg PWY1009]`, `[insert number]`.

**An instruction the writer did not act on** — the bracketed red text is still there and nothing replaces it — is a gap, not guidance: the bracketed text is never rendered, and a visible `Red Flag:` sits at that spot saying in plain words what the writer has not yet supplied (*"Red Flag: the writer has not added the unit standard's outcomes / performance criteria here — the assessment criteria the page refers to are missing."*). For `[delete "and quiz" if no quiz in the module]` the bullet is kept exactly as written and the Red Flag asks the designer to check whether the module has a quiz.

### 11.4 What to do — the two options

The What-to-do accordion opens with the two fixed sentences, the first completed by the writer: *In this assessment, you will …* and *Complete the assessment by following the instructions provided.* The writer then keeps **one** of two options:

| Writer kept | Output, inside What to do, after the two sentences |
|---|---|
| **Option 1 — separate assessment document** | `<p>Complete the tasks in the Word document linked below.</p>` then the button `<a href="https://tekura.desire2learn.com/shared/assessment/NCEA%20Level%20{n}/{COURSE}/{CODE}/pdf/{code}-assessment.docx" target="_blank" rel="noopener"><div class="button">Go to assessment</div></a>` (`{code}` lower-case, e.g. `us1285-assessment.docx`), with the `18B` §7.2 upload To Do directly under it: *export the assessment Word document, save it as `us1285-assessment.docx` and upload it to shared › assessment › NCEA Level 1 › PWY1000 › US1285 › pdf.* No answer tables are expected on the page. |
| **Option 2 — instructions included** | `<p>Complete the tasks that follow.</p>` then the writer's tasks, converted by `18B` §6 (headings, the nest-under-the-numbered-item rule, answer tables). |

The option labels and `OR` are never rendered (Section 11.3). **Both options left in** — the writer did not choose: keep both, as written and in order, with the labels as `<p><b>Option 1: Separate assessment document</b></p>` / `<p>OR</p>` / `<p><b>Option 2: Instructions included in this assessment</b></p>` (visible content wins — never pick one), and put a `Red Flag:` at the top of the What-to-do accordion: *the writer has left both options in — confirm which one this assessment uses and delete the other.*

### 11.5 The AI guidance — the centralised traffic-light image

`[Centralised image: AI traffic light - red]` is Te Kura's AI-use traffic light, a **centralised image that is the same on every Pathways assessment** (red = AI may not be used; Pathways assessment tasks are red). It sits where the writer places it — in the template, the end of the What-to-do accordion, after the option content (after the tasks, for Option 2).

**Its file location on the server has not been recorded yet**, so it is not registered as a central asset (`01D` → `central_image`, constraint 95 lists only the Science and Maths characters). Until it is:

- emit, at that spot, `<p style="color: red; font-weight: bold;">Designer/Developer To Do: insert the centralised AI traffic light image (red) here. It is the same shared image on every Pathways assessment; its file location has not yet been recorded in the Convertor's rules, so it could not be built automatically.</p>` — the colour copied from the tag (`red`, `amber`, `green`);
- **never** an `<img>` with a guessed path, **never** the `imageCentral` class, and **never** the AI Guidelines *Traffic Light PDF* block (`05A`, constraint 84) — that is a different asset;
- **no** acknowledgement entry and no `acksAI` — it is Te Kura's own image, not AI-generated media.

When the path is supplied, a follow-up Admin Mode or Update Mode change records it here and replaces this To Do with the built image.

### 11.6 Student Resources — the module button

`Use the resources in the module to support your assessment.` is converted as written. `[Link to module]` followed by the module code (`PWY1009`) builds a button labelled with the code — **this replaces, for this template only, the `18B` §6.6 rule that a cited module code is plain text**:

```html
<a href="" target="_blank" rel="noopener">
    <div class="button">PWY1009</div>
</a>
<p style="color: red; font-weight: bold;">Designer/Developer To Do: add the link to the PWY1009 module to this button.</p>
```

The `href` is left blank and flagged — the module's D2L address is not in the document and is never guessed. No module code given → no button, and a `Red Flag:` that the module code is missing (Section 11.3). The `Are any 3rd Party Items required?` To Do, when raised, still comes first in this accordion (`18A` §4.1).

### 11.7 Getting started, How to present your learning, Timeframe

- **Getting started** — `Before you begin:` and the fixed bullet list are converted as written (`<p>` + `<ul>`). The writer pastes the unit standard's outcomes / performance criteria **below the list, like a rubric**: a table → the `18B` §6.4 table rule (`table table-bordered`, `margin-bottom: 30px`), kept inside Getting started where the writer placed it; a merged picture of the rubric → `18B` §7.3.
- **How to present your learning** — the writer's evidence requirements, converted normally; the Example box is dropped (Section 11.3).
- **Timeframe** — `Work at your own pace. Complete all tasks before submitting your assessment.` as written.

### 11.8 The dropbox accordion

The Pathways template has no `[H3]` line, so the dropbox `<h3>` is the standard code (`US1285`) — the `18B` §6.7 fallback, with no To Do for it. The writer's dropbox text is kept **in full** in place of the skeleton's single `{dropbox body}` paragraph — `<p>Upload your completed assessment to the US 1285 assessment dropbox.</p>`, `<p>Make sure:</p>` and its bullet `<ul>` — followed by the quickLink button (`[Button] Upload to dropbox.` → `Upload to dropbox`, full stop dropped) and the dropbox-code To Do, exactly as `18B` §6.7 and §7.1. The closing `DROPBOX` title line is stripped as before.

### 11.9 What this part never does

- Never renders the template's note line, an Example box, the Option labels, `OR`, the stray `.` or any bracketed red instruction as text.
- Never picks one of two options the writer left in; never invents the AI traffic-light image path or substitutes the AI Guidelines PDF; never guesses the module link.
- Never applies these rules to a non-Pathways assessment, or to a Pathways assessment still on the older general template.
