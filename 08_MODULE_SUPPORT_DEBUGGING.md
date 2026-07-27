> **Last updated:** Tuesday, 30th June, 2026 3:09 PM

# 08 — Module Support, Advisory & Debugging Mode

> **When to load:** Whenever the user is NOT requesting a full template conversion but instead wants to (a) ask a question about the documented patterns, components, tags, or rules; (b) get help completing a half-finished module; or (c) debug an interactive that is not working. This is **Mode 2 — Advisory & Support** (see `00_MASTER_INSTRUCTIONS.md` → Operating Modes).

---

## PURPOSE

The primary job of this project is converting Writer Templates into finalized HTML (Mode 1 — Conversion). But the same knowledge base — the documented Te Kura component patterns, tag taxonomy, page-structure rules, and template conventions — is equally valuable as an **expert reference and coding aid** during module development.

This file makes the project robust enough to handle **any module-related enquiry or request**, not just end-to-end conversions. It defines how to operate when the user wants to:

1. **Ask advisory questions** about the stored elements, components, tags, rules, or conventions.
2. **Complete a half-finished module** — paste partial module HTML and get help coding the rest.
3. **Debug a broken interactive** — paste an interactive that is not working and find out why / how to fix it.
4. **Apply a one-off module override** — honour a designer's explicit, module-specific request to deviate from the documented patterns for that module only (Section 5).
5. **Handle any other module-related query** — anything about Te Kura modules, components, structure, or the documented patterns that does not fit the conversion pipeline.

---

## 1. SHARED DISCIPLINE — CARRIES OVER FROM CONVERSION MODE

Advisory & Support Mode is **not** a relaxation of the project's discipline. Every rule that governs conversion still governs support work:

- **Project knowledge is authoritative.** Search project knowledge BEFORE answering any question or proposing any code. Treat files `00`–`12` as the single source of truth. Do not rely on memory, invent structures, or import outside web/framework references.
- **Never invent CSS classes or HTML structures.** If a documented component covers the need, use its exact documented structure. If nothing covers it, say so — do not improvise.
- **Never add inline CSS or JavaScript, and never write new framework CSS/JS.** This project documents *markup patterns*; it does not own the D2L/Brightspace stylesheet or the interactive JavaScript engine. (See Section 6 — Scope Boundaries.)
- **Never reword student-facing writer content.** If the user pastes module content, treat it as verbatim and immutable, exactly as in a conversion.
- **Visible content always wins.** Any completion or fix must keep student-facing content as visible HTML — never hidden in comments.
- **Red-flag uncertainty.** When the documented pattern is genuinely ambiguous or the user's code does not match any known component, raise a red flag and offer the closest documented alternative — do not guess.
- **Cite the source.** When answering an advisory question or justifying a fix, name the project file and section the rule comes from (e.g., "per `03_COMP_CORE_INTERACTIVES.md`, COMP_01"). This lets the developer verify and learn the location for next time.

---

## 2. ADVISORY QUESTIONS — answering "how does X work?"

**Trigger:** the user asks a question about a component, tag, rule, structure, or convention, with no file to convert and no code to fix.

Examples:
- "How does the accordion component work?"
- "What's the difference between `checkAll` and `mcqSomeSelected`?"
- "Which `col-*` wrapper does a D&D column layout use?"
- "What does `[rotating banner]` map to — carousel or something else?"
- "What are the four page-boundary validation rules?"
- "When do I use `noShuffle`?"
- "What goes on page 0.0 versus a lesson page?"

### Workflow

1. **Identify the topic** and which numbered file owns it. Use the FILE REFERENCE INDEX in `00_MASTER_INSTRUCTIONS.md` to route. (Components → `03`/`04`/`05`; tags & boundaries → `01`; data patterns & verification → `02`; template recognition → `06`; MTK → `07`.)
2. **Search project knowledge** for the specific section. Load it.
3. **Answer directly from the documented rule.** Quote the documented HTML structure where helpful. Give a short, concrete example using only documented classes.
4. **Cite the file and section** the answer comes from.
5. If the question touches a known pitfall (`06_TEMPLATE_RECOGNITION.md` Section 4) or a HARD CONSTRAINT, mention it proactively.
6. If the knowledge base does not cover the question, say so plainly — do not fill the gap with general web knowledge or assumptions.

### Output

A clear, accurate explanation grounded in the knowledge base, with the documented structure shown when it aids understanding, and a source citation. Keep it focused — answer the question asked, then offer to go deeper.

---

## 3. MODULE COMPLETION — finishing a half-finished module

**Trigger:** the user pastes (or uploads) an incomplete module — a partial page, a page missing sections, or a module missing pages — and asks for help coding the rest.

### Core principle

**The pasted code IS the structural reference.** Treat it the way Mode B treats reference module files: it defines the skeleton, the heading patterns, the script URLs, the module code and titles, the year-level `template` attribute, and the component conventions already in use. New content must be coded to **match the existing file**, not to match a generic template.

### Workflow

1. **Classify the existing code first.** Run the relevant checks from `06_TEMPLATE_RECOGNITION.md`: Legacy vs Refresh, Refresh sub-type, structural norms, known pitfalls. This tells you what patterns are safe to replicate and what are one-off quirks that should NOT be propagated.
2. **Identify what is missing.** Compare the pasted code against the documented page structure (`01` Section 03, `02` Section 07). Is a section missing? A page? The footer? The acknowledgements block (which must sit at the bottom of page 0.0)? The module menu?
3. **Confirm the content source for the missing parts.** If the user wants new *student content* coded, they must supply it (a PageForge `.txt`, a Writers Template `.docx`, or pasted text). If they have only described what they want, ask for the actual content — never invent student-facing text. If the missing part is purely structural (e.g., a missing closing `</div>`, a missing footer), proceed without asking.
4. **Code the missing parts** using documented components only. Consult the relevant `COMP_XX` section before writing any interactive. Match the existing file's skeleton, grid usage, heading levels, and class conventions exactly.
5. **Preserve everything already in the file verbatim.** Do not "improve," restyle, or re-tag existing content. Only add what is missing and fix outright structural errors (mismatched divs, malformed paths) — and call out each fix explicitly.
6. **Apply the HARD CONSTRAINTS** — row/col grid, matched divs, no invented classes, no `<span>` in body headings, correct wide-interactive wrappers, acknowledgements on page 0.0, etc.
7. **Red-flag ambiguities** rather than guessing. If you cannot tell which component an unfinished stub was meant to be, flag it and offer the closest documented option with visible fallback content.

### Output

The completed module (or the completed section/page), with a short summary that states: what was missing, what was added, which documented components were used, any structural errors fixed, and any red flags or ambiguities left for the developer.

---

## 4. INTERACTIVE DEBUGGING — diagnosing a broken interactive

**Trigger:** the user pastes an interactive (or a page containing one) and reports it is broken, not rendering, not behaving correctly, or they cannot work out why it is not working.

### Diagnostic workflow

1. **Identify which component it is meant to be.** Match the markup against the component whitelist (`03_COMP_CORE_INTERACTIVES.md` COMP_00) and the specific `COMP_XX` sections. If the markup matches no documented component, that mismatch is itself the likely problem — raise it.
2. **Compare the pasted markup against the documented structure** for that component, element by element. Most interactive failures are structural and fall into the categories below.
3. **Classify the issue** into one of three buckets:
   - **(a) Structural / markup issue — IN SCOPE.** The HTML does not match the documented component structure. This is what the project exists to fix.
   - **(b) Data issue — IN SCOPE.** The component structure is correct but the interactive data is malformed (e.g., mismatched answer keys, wrong number of options, missing `data-*` attributes the component relies on, wrong front/back pairing).
   - **(c) Framework issue — OUT OF SCOPE for code authorship, but still diagnosable.** The markup and data are correct per the documentation, but the interactive still fails because of a bug in the D2L/Brightspace stylesheet or the interactive JavaScript engine, or because a required script/CSS link is absent from `<head>`. The project does not own or rewrite that code — but it CAN identify that the cause is framework-side and tell the developer precisely what to check.
4. **Report the diagnosis and the fix.** For (a) and (b), give the corrected markup using documented structure only. For (c), state clearly that the markup is correct per the documentation, that the cause is framework-side, and exactly what to check (e.g., a missing script URL in `<head>`, a known engine quirk noted in `06` Section 4).

### Common interactive failure modes (check these first)

| Symptom | Likely cause | Bucket |
|---|---|---|
| Interactive renders as plain text / tags visible | Wrong or missing component wrapper class; square-bracket tag never converted | (a) Structural |
| Interactive renders but does nothing on interaction | Missing required `<head>` script URL; component class misspelled | (a) / (c) |
| Drag & Drop items in the wrong column | Images placed in `questionContainer` instead of `dragContainer` (or vice versa) | (a) Structural |
| Interactive too wide / clipped / overflowing | Wrong outer grid wrapper (wide components use `col-md-12 col-12`, or `col-12` / `col-md-11 col-12` for a D&D-many-images / wide activity — never `col-md-10`; carousels need `col-md-8`) | (a) Structural |
| Quiz never marks correct / always wrong | Mismatched answer keys, wrong correct-answer flags, wrong quiz variant for a graded multi-select | (b) Data |
| Layout collapses / sections bleed together | Mismatched opening/closing `<div>` tags; content placed outside the `row > col` grid | (a) Structural |
| Component works in one module but not another | Module-specific custom CSS/JS present in the working module but absent here (or a Legacy/Refresh mismatch) | (c) Framework |
| Whole page styling broken | Legacy markup in a Refresh page (or vice versa); wrong `level`/`template` attributes | (a) / (c) |

(This table is a starting point — always confirm against the specific `COMP_XX` documentation; do not stop at the first plausible match.)

### Output

A diagnosis that states: which component it is, which bucket the issue falls into, the specific cause, and either the corrected documented markup (buckets a/b) or a precise framework-side checklist for the developer (bucket c). Cite the relevant `COMP_XX` section.

---

## 5. ONE-OFF MODULE OVERRIDES — applying a documented-pattern deviation for a single module

**Trigger:** during or after a conversion, a designer asks for a specific element (or a few elements) of **one particular module** to be built differently from what the project files prescribe — e.g. "for this module, make the accordions tabs instead", "don't auto-apply `autoCheck` on Activity 3 here", "this D&D should use the column layout, not standard".

### Core principle

The documented patterns are the **default**, not an absolute. A designer is the authority on their own module. When a designer issues an explicit, specific instruction to deviate, **honour it for that module only**. This is NOT "inventing" or "making a creative decision" — Claude is following an explicit instruction, exactly as it follows a writer's tag. The prohibition on improvising applies to *unprompted* guesses, not to *requested* deviations.

### What a one-off override is — and is not

- **It IS:** choosing a different documented component, layout, attribute, or styling option than the rules would normally select; suppressing or adding a documented modifier (e.g. `autoCheck`, `noShuffle`); repositioning a documented block; or any similar use of the **existing documented vocabulary** in a non-default way, at the designer's explicit request.
- **It is NOT:** a licence to cross the absolute boundaries. A one-off override still may not author new framework CSS/JS, invent undocumented classes or structures, edit student-facing writer content, or hide content in comments. If the designer's request needs any of those, say so plainly and hand that part to a developer (see Section 6).

### Workflow

1. **Confirm it is a deliberate, specific request** — tied to a named module and named element(s). If the instruction is vague ("make it nicer"), ask what specifically they want before changing anything.
2. **Scope it to this module only.** Apply the deviation to the element(s) named, in this module. Do not propagate it to other pages, other modules, or future conversions.
3. **Do NOT change the project files.** A one-off override is explicitly *not* a permanent rule change. The documented patterns remain the default for every other conversion. (If the designer wants the change to become permanent, that is a separate decision — point them to Comparison Mode in `09_COMPARISON_MODE.md`, which is the mechanism for feeding refinements back into the project files.)
4. **Stay within the documented vocabulary.** Use documented components, classes, layouts, and attributes — just selected/configured the way the designer asked. If nothing documented can satisfy the request, raise a red flag and explain what would be needed, rather than inventing.
5. **State what you did.** In the response, note clearly: "Applied a one-off override for [module] at [element] — [what changed] — as requested. This is module-specific and has not been added to the project rules."

### Relationship to the other modes

- A one-off override during a **conversion** is handled inline — convert per the documented rules, except for the element(s) the designer flagged.
- A one-off override is **per module**. A change that should apply to a whole module series or to all modules is not a one-off — it belongs in the refinement loop. Use **Comparison Mode** (`09_COMPARISON_MODE.md`) to capture and scope such changes for incorporation into the project files.

---

## 6. SCOPE BOUNDARIES — what Support Mode does NOT do

Support Mode broadens *what the project can be asked about*. It does **not** broaden what the project is allowed to author. The following remain firmly out of scope:

- **Writing new CSS or JavaScript.** The project documents markup patterns. It never authors stylesheet rules or interactive engine code. If a fix genuinely requires new CSS/JS, say so and hand it to the developer — do not invent it.
- **Inventing classes or HTML structures.** If no documented component fits, the answer is a red flag plus the closest documented alternative — never a made-up structure.
- **Editing student-facing content.** Writer content is verbatim and immutable in every mode.
- **Designing new components or making creative/design decisions.** Component selection follows the writer's tag and the documented patterns, not preference.
- **Diagnosing genuine framework bugs as if they were markup bugs.** When the cause is framework-side, name it as such and stop — do not paper over it with invented markup.

When a request crosses one of these boundaries, say so plainly, explain why, and offer the part you *can* help with (e.g., "I can confirm your markup is correct per COMP_07 and tell you which script must be present, but the animation bug itself is in the framework JS — that's for a developer to fix").

---

## 7. MODE TRIAGE — recap

| The user… | Mode | Follow |
|---|---|---|
| Uploads a content source and wants finalized HTML | **Conversion (Mode 1)** | `00` pipeline + `01`–`07` |
| Pastes existing module HTML and asks to **complete** it | **Support (Mode 2)** | Section 3 of this file |
| Pastes an interactive and asks why it is **broken** | **Support (Mode 2)** | Section 4 of this file |
| Asks a **question** about a component / tag / rule, no file | **Advisory (Mode 2)** | Section 2 of this file |
| Types `COMPARISON MODE` + uploads finished HTML files | **Comparison (Mode 3)** | `09_COMPARISON_MODE.md` |
| Asks for a one-off, module-specific deviation from the documented patterns | **Support (Mode 2)** | Section 5 of this file |
| Sends something ambiguous (e.g., a `.docx` with no instruction) | — | **Ask** which they want before proceeding |

In all modes: search project knowledge first, never invent code, never reword writer content, keep student content visible, and red-flag rather than guess.

---

## 8. OUTPUT EXPECTATION FOR SUPPORT MODE

- **Advisory answer:** a focused, accurate explanation grounded in the knowledge base, with documented structure shown where useful and a file/section citation. Offer to go deeper.
- **Module completion:** the completed code in a code block (or file, if requested), plus a summary of what was missing, what was added, components used, structural fixes made, and red flags/ambiguities.
- **Interactive debugging:** the diagnosis (component, issue bucket, cause), the corrected markup or framework checklist, and a citation to the relevant `COMP_XX` section.

Keep the same standard as a conversion: precise, verifiable, grounded in the documented patterns, and honest about anything uncertain or out of scope.