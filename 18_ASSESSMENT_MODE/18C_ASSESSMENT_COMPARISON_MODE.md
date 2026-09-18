> **Last updated:** Friday, 18th September, 2026 3:30 PM
> **Granular part C (3 of 3) of `18_ASSESSMENT_MODE.md`** — Assessment Comparison Mode: the `COMPARISON MODE` phrase in an assessment chat, per-file routing, inputs, partial re-uploads, no scopes, the one finalized report for Gavin.
> All sibling parts live in `18_ASSESSMENT_MODE/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# 18C — Assessment Comparison Mode (the assessment variant of Mode 3)

> **When to load:** Whenever a message contains **`COMPARISON MODE`** (case-insensitive, not preceded by `PAGEFORGE`) together with uploaded HTML, **in a chat where Assessment Mode (`18A`) has run** — or where any uploaded file is an assessment page (Section 10.1). Load with `09_COMPARISON_MODE.md` → `09B` (the exclusions and the inclusion gate) and `09C` Section 9 (the finalized-report bundle), both reused unchanged except where this part says otherwise.

---

## 10. ASSESSMENT COMPARISON MODE

### 10.1 Purpose, trigger and routing — the chat decides which Comparison Mode runs

Developers refine the generated assessment pages by hand exactly as they refine modules, and those refinements must flow back into these instructions. The trigger is the **same phrase** as Mode 3 — `COMPARISON MODE` plus the developer's refined HTML re-uploaded into the chat that produced the original — and the Convertor works out **which** comparison to run from the evidence in front of it, never by asking:

- An uploaded HTML file is an **assessment page** when it carries `class="alertAssessment"` and `template="NCEA"` and no lesson menu — the `18A` skeleton. It is a **module page** otherwise. Each uploaded file is routed on its own evidence.
- A chat that ran **Assessment Mode** (it holds the assessment `.docx` and the `{CODE}.html` this project produced) routes assessment pages **here**; a chat that ran only module conversions routes to `09` untouched, and `09` never changes its behaviour for module work.
- Both kinds in one upload (rare): run both procedures and produce **two** reports, saying so in one line. Never merge a module difference into the assessment report or vice versa.
- `PAGEFORGE COMPARE MODE` is still checked first (the `PAGEFORGE` discriminator), `ADMIN MODE` outranks everything, and `UPDATE MODE` still wins if present. `COMPARISON MODE` with no HTML uploaded → ask for the refined page(s), as in `09`.

### 10.2 Inputs — three, plus a fixed skeleton

| Input | What it is | Where it comes from |
|---|---|---|
| **A — the assessment `.docx`** | the writer's document | already in this chat, from the Assessment Mode turn |
| **B — the generated page** | the `{CODE}.html` this project produced | already in this chat |
| **C — the developer's refined page** | the `{CODE}.html` re-uploaded now | uploaded with the trigger |
| **R — the structural reference** | the `18A` Section 5 skeleton — **fixed** for every assessment, never a supplied template | the knowledge base itself |

Match each C to its B by standard code (`{CODE}.html` filename, or the `<title>` / dropbox `<h3>` if the developer renamed the file). Because R is a knowledge-base rule rather than a supplied template, the `09B` Section 5 inclusion gate simplifies: **every** difference in a skeleton region is knowledge-derived and reportable (the rule that produced it is `18A` Section 5), and the gate's only job is the `09B` Section 4.1 exclusions. If B is no longer visible in a long chat, ask the developer to re-supply it — never reconstruct it from the rules, and never treat C as B.

**Partial re-upload — only what comes back is compared.** A chat may have generated several pages (`18A` Section 3). If the developer re-uploads only some of them, compare **only those** against their own B; every other page generated in this chat is **assumed unchanged**, is listed by name in the report header under *"Generated in this chat, not re-uploaded — assumed unchanged; no differences reported"*, and is **never asked for**.

### 10.3 No scopes — one phase, straight to the finalized report

Every assessment is built on the one template, so the `09` scope question does not exist here: there is **no Phase 1 report, no scope legend, no number-letter reply**. `COMPARISON MODE` produces the **finalized report directly**, with every difference treated as **(c) Universal** — as if the developer had answered "apply this everywhere" for each one. The report is written for **Gavin**, who actions it against these instructions in Update Mode or Admin Mode; nothing is actioned inside this mode.

### 10.4 What counts — and what is excluded

The `09A` Section 4 definition of a difference and every `09B` Section 4.1 exclusion apply as written (a red note, `Designer/Developer To Do:` or `Red Flag:` edited or removed → Exclusion 1; bespoke presentation → Exclusion 3; supplied metadata → Exclusion 4). Assessment-specific readings of those exclusions:

- **URLs are never reported — any of them.** The footer `href`s (blank when generated, filled in by the developer), the dropbox quickLink and its `rcode`, an image `src`, a PDF or button link, the NZQA link: every assessment's addresses are unique to it, so a changed, added or removed URL value is dropped silently and never logged. Only a change to the **element** around a URL (a link moved, a button restyled, an `<img>` given a new class) is a difference.
- **Filling in what the document could not supply is not a rule change.** The real dropbox `rcode`, the rubric image dropped into its To Do spot, a real dropbox sentence replacing the stock one, the NZQA year, a completed acknowledgement title/author, `acksAI` removed because the asset turned out to be hand-made — all Exclusion 4/7 material, dropped silently.
- **Editorial changes to the writer's words** (a fixed typo, a reworded sentence, a moved paragraph) are content editing, not conversion — excluded — **unless** the same transformation is applied to every instance of a pattern (e.g. every `Requirement n:` label loses its colon, every prompt paragraph loses its italics): that is a conversion rule and is reported.
- **Anything structural is reported:** a changed skeleton element, class, id or attribute; a different heading level; a list nested or un-nested; lettering changed; a table class or inline style changed; an accordion added, dropped, renamed or re-ordered; the acknowledgements block's structure; indentation style; script host; filename convention.
- Ordinary Comparison Mode's "template-derived" filter never removes an assessment difference, because R is a rule (10.2).

### 10.5 The report — one file, however many pages

Produce **one** downloadable Markdown file: `assessment_difference_report_finalized_{CODE}.md` for one page, `assessment_difference_report_finalized_{CODE1}_{CODE2}.md` for two or three, `assessment_difference_report_finalized_multi.md` beyond that. Its shape:

```
# Assessment Comparison — finalized report for Gavin
Generated: d/m/y · Chat: [one line naming the assessment(s) converted in this chat]
Compared: US4249.html (generated 16/9/2026 → developer's re-upload)
Generated in this chat, not re-uploaded — assumed unchanged; no differences reported: AS91956.html
Finalized report — every difference below is scoped (c) Universal by rule (all assessments share one
template), with the source of the project's output identified for actioning in Update Mode / Admin Mode.

# File: US4249.html

## Difference 1 — [short title] — [accordion / location]
### 1. Original raw content (source)
### 2. Source of the project's output          ← the exact 18A/18B/18C section (and 05C / constraint) that produced B
### 3. Originally generated code (this project's output)
### 4. Developer's refined code (the correct target)
**What changed:** …
Scope decision: (c) Universal — incorporate this correction for every future Assessment Mode conversion.
Action: update the cited rule (Section 2 above) in 18_ASSESSMENT_MODE as a global rule.

# File: AS91957.html
## Difference 2 — …            ← numbering runs on continuously across files

## Actioning summary
| # | File | Short title | Rule to change (18 part · section) |
```

The four-section bundle is the `09C` Section 9 bundle verbatim (Section 4's heading says *Developer's* rather than *Designer's*). Where the same change appears in several re-uploaded files, report it **once**, under the first file, and list the other files in its *What changed* line — Gavin needs one rule, not three copies. No qualifying differences → still produce the file, with the header and the single line *"No knowledge-derived differences detected for the compared assessment page(s)."*

### 10.6 How the run closes in chat

Present the file, then three or four plain-English lines: which pages were compared, which were assumed unchanged, how many differences were reported, and that the report goes to Gavin to action in Update Mode / Admin Mode — the instructions are not changed here. Never print the scope key, never invite a number-letter reply, never mention PageForge Compare Mode.

### 10.7 What this mode never does

- Never converts, rebuilds or edits a page; never regenerates any knowledge file.
- Never asks which scope to apply, never produces a Phase 1 report, never asks for pages the developer did not re-upload.
- Never reports a filled-in To Do, an edited red note, a changed URL (footer, dropbox, image, PDF, NZQA) or an editorial wording change as a rule.
- Never runs the module procedure on an assessment page, or this procedure on a module page.
