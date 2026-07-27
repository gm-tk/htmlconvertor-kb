> **Last updated:** Thursday, 16th July, 2026 9:30 PM
> **Granular part B (2 of 2) of `09_COMPARISON_MODE.md`** — Comparison Mode: phase 1 & 2 reports, scope options, discipline (SS6-15).
> All sibling parts live in `09_COMPARISON_MODE/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## 6. THE PHASE 1 REPORT — STRUCTURE (streamlined)
 
Comparison Mode produces **one downloadable report**. In Phase 1 it is deliberately lightweight: each difference is just three sections, and the precise rule citation is withheld until Phase 2. Differences are numbered in a **single continuous sequence**.
 
### 6.1 Report header + scope legend
 
The report opens with its header, and then — **once, immediately below the header** — the full five-option scope legend from Section 7.
 
```
# Comparison Difference Report — [MODULE_CODE] [Module Title]
Module series: [PREFIX] (e.g. OSAI)
Structural reference: [filename] ([Mode A | Mode B])
Template level: [LEVEL_DESCRIPTOR] (e.g. Phase 2 (Years 4–6))
Files compared: [list of page files]
Original content source: [PageForge .txt | raw Writers Template .docx | MTK .docx]
Differences reported: [N total]
Generated: [date]
 
Scope of this report: only differences where the project's HTML output (B) was
produced by this project's STORED INSTRUCTIONS (files 00–08, COMP_*, hard
constraints, tag taxonomy, auto-rules, comment & red-flag policy). Differences
where the project's output was lifted or mirrored from the supplied structural
reference, example module, or other templated file have been filtered out, as
refining the project files cannot change what an external template ships.
 
[INSERT THE SCOPE LEGEND FROM SECTION 7 HERE — VERBATIM, ALL FIVE OPTIONS]
```
 
### 6.2 Comparison bundle (Phase 1 — three sections, repeat per difference)
 
In **Phase 1**, each difference is documented as **three labelled sections only** — there is **no scope block beneath it** (the five options live once at the top) and **no "source of the project's output" section** (that detail is added in Phase 2). Each bundle carries its globally-unique number.
 
```
## Difference [n] — [short title] — [file/page, location]
 
### 1. Original raw content (source)
> The content as it appeared in the original raw input (A) — the uploaded
> Writers Template .docx or PageForge .txt. Quote the relevant tag(s) and text.
 
### 2. Originally generated code (this project's output)
```html
[the exact HTML this project produced for that content — input B]
```
 
### 3. Designer's refined code (the correct target)
```html
[the exact HTML from the designer's finished file — input C]
```
 
**What changed:** [one or two sentences plainly describing the difference]
```
 
The three sections must always appear **in this order**: raw → original output → designer's correction. Use `ORIGIN UNCERTAIN — verify before actioning` in the "What changed" line for any difference whose origin could not be confirmed (Section 5.4).
 
### 6.3 How Phase 1 closes — the on-screen scope key
 
After presenting the report, write a brief chat summary (module, files compared, the number of differences reported). Then **end the chat message with the scope key as its final lines.** Putting it last keeps the five plain-English options and the reply format visible on screen while the designer scrolls through the differences and composes their reply, so they never have to scroll back up to remember what each letter means.
 
The people reading this key are **not developers** — they will not make the code changes themselves; their choices are compiled into the final report that a developer then actions. So the key MUST be warm, plain English with no technical jargon (no "scope", "propagate", "template-derived", "module code prefix", etc.). Emit it exactly like the block below, filling in `[LEVEL_DESCRIPTOR]` with the friendly year range (e.g. "Years 4–6") and `[PREFIX]` with the plain series name (e.g. "OSAI"):
 
> **What would you like done with each change?**
>
> Each change above has a number next to it. For every change, just tell me how widely it should apply by choosing one letter:
>
> - **A — Just this year group in this subject.** Use this change for every module at the same level as this one, but only within this same subject (all [LEVEL_DESCRIPTOR] modules in the [PREFIX] series) — not other subjects.
> - **B — This whole subject series.** Use it for every [PREFIX] module, across all year levels.
> - **C — Every module.** Make it the new standard for all modules from now on.
> - **D — Just this once.** This was a one-off choice for this module only — don't change anything elsewhere, and you can leave it out of the final summary.
> - **E — Leave it out for good.** This kind of change isn't worth tracking — please stop reporting it in future.
>
> **How to reply:** for each change, type its number, a dash, and your chosen letter. Put each on its own line, or separate them with commas — for example: `1 - A, 2 - C, 3 - D`.
>
> Please give an answer for every numbered change. Capital or lower-case letters are both fine, and don't worry about exact spacing. Once you send these back to me, I'll turn them into the final tidy report to pass on for actioning.
 
This key must be the **last thing** in the message — nothing after it. When the designer replies with their choices, proceed to Phase 2 (Section 8).
 
---
 
## 7. THE FIVE SCOPE OPTIONS (the legend — shown once at the top of the report)
 
This legend is inserted **verbatim** at the top of the Phase 1 report, immediately under the header. It is shown **once** — never repeated after individual differences.
 
```
**SCOPE OPTIONS** — for each difference below, decide how widely its correction should apply.
Reply in chat with one `number-letter` pair per difference (e.g. `1-A, 2-C, 3-D`).
 
(a) Series + level scope — applies to all modules at this module's level that are
    ALSO in this module's subject series. For [MODULE_CODE], this means every current
    and future [LEVEL_DESCRIPTOR] module in the [PREFIX] series only — NOT other
    subjects at the same level. Refining for this scope updates the cited
    project-knowledge rule, scoped to [PREFIX] modules at [LEVEL_DESCRIPTOR].
(b) Module-series scope — applies to all modules that share the leading alphabetic
    prefix of the module code, i.e. every [PREFIX] module regardless of year level.
(c) Universal scope — applies to every future conversion, regardless of template
    or series.
(d) Ignore once — this change is a bespoke, one-off designer decision for this
    module; do not propagate it, and OMIT it from the finalized report.
(e) Ignore always — this kind of change is not worth documenting and should never
    be captured in a difference report again; it is kept in the finalized report
    only as an instruction to add it to the standing exclusions.
```
 
### 7.1 Fill-in values
 
| Placeholder | Source | Examples |
|---|---|---|
| `[MODULE_CODE]` | The module code being compared | `OSAI201`, `ENGR401` |
| `[LEVEL_DESCRIPTOR]` | The template-level descriptor derived from the structural reference's `template` attribute on `<html>`. Includes the Phase number when known, with the year range in brackets. | `Phase 2 (Years 4–6)` (from `template="4-6"`) |
| `[PREFIX]` | The leading alphabetic portion of the module code | `OSAI` (from OSAI201), `ENGR` (from ENGR401), `TRR` (from TRR107) |
 
### 7.2 Known template-level → descriptor mappings
 
| `template` attribute on `<html>` | Year range | Phase | Descriptor to insert for option (a) |
|---|---|---|---|
| `4-6` | Years 4–6 | Phase 2 | `Phase 2 (Years 4–6)` |
 
Other template levels (`ECH`, `1-3`, `7-8`, `9-10`, `NCEA`) will be added as the Te Kura phase taxonomy is confirmed. **If the Phase number for a given level is not yet documented, use the year range alone** — e.g. `all current and future Years 9–10 modules`. The descriptor must always be specific enough that the designer can unambiguously identify which other modules option (a) would cover.
 
### 7.3 Semantics & relationships of the five options
 
- **(a) / (b) / (c) are propagating scopes of increasing breadth, and they now nest:** (a) this subject series *at this level only* ⊂ (b) this whole subject series *across all levels* ⊂ (c) every module. Pick the narrowest one that still covers everywhere the correction should apply. All three are actioned by editing the **cited project-knowledge file** at the chosen breadth (every reported difference is knowledge-derived by the Section 5 gate). Note that "this level across *all* subjects" is deliberately **not** one of the options — (a) is restricted to the module's own series.
- **(d) and (e) are non-propagating.** (d) records a deliberate one-off — it is **omitted from the finalized report** (Section 9). (e) records that this category of change should be *suppressed from future reports* — it is **kept in the finalized report** with an instruction to add it to the Section 4.1 exclusions (Section 9.3).
- **One letter per difference is the norm.** If the designer genuinely wants a correction applied at two propagating scopes at once, they may list more than one letter for a difference (e.g. `1-A&B`); apply all letters given. (d) and (e) are mutually exclusive with everything else — if combined with another letter, ask the designer to clarify.
 
---
 
## 8. PHASE 2 — PARSING THE DESIGNER'S SCOPE ASSIGNMENTS
 
After Phase 1, the designer replies with a compact list of pairings, one per difference. Parse it leniently.
 
### 8.1 Accepted input shapes
 
- A pairing is a **difference number** followed by a **scope letter (a–e)**, in that order.
- The two may be joined by any of: a hyphen, en/em dash, colon, full stop, the word "to", one or more spaces, or nothing at all. All of these mean the same thing: `1-A`, `1 - A`, `1 A`, `1:A`, `1.A`, `1A`, `1 to A`.
- Pairings may be separated by commas, semicolons, new lines, or spaces: `1-A, 2-C, 3-D` or one per line.
- **Letters are case-insensitive** (`A` = `a`).
- A multi-scope pairing for one difference may list more than one propagating letter joined by `&`, `+`, `/`, or `and`: `4-A&B` (apply both). See Section 7.3.
 
### 8.2 Validation
 
- **Every** difference number must exist in the Phase 1 report. If a number is out of range or duplicated with conflicting letters, say which and ask the designer to confirm — do not guess.
- **Every** letter must be one of `a`–`e`. Reject anything else and ask.
- If the designer supplies **fewer pairings than there are differences**, list the difference numbers still missing a scope and ask for them before producing the finalized report. Do not silently default an unassigned difference to any scope.
- If `(d)` or `(e)` is combined with a propagating letter for the same difference, ask the designer to pick one (they conflict).
 
### 8.3 What to confirm back
 
Before (or alongside) regenerating, briefly restate the parsed mapping in plain terms — e.g. *"Got it: 1 → series (b), 2 → universal (c), 3 → ignore once (d, will be dropped from the final report), 4 → ignore always (e, will be flagged for permanent exclusion). Regenerating the finalized report now."* This lets the designer catch a mistyped pair.
 
---
 
## 9. PHASE 2 OUTPUT — THE FINALIZED DETAILED REPORT
 
Regenerate the report with the **same numbering and the same difference titles** as Phase 1, but now **detailed**: each included difference gains a precise **source of the project's output** section and **four** sections in total, plus its scope decision. This finalized report is the single deliverable that the developer later hands to a separate conversation to action — so it must carry as much actionable detail as possible.
 
### 9.1 What changes from Phase 1
 
1. The top-of-report **scope legend is removed** (it has served its purpose) and replaced with a one-line note: *"Finalized report — each difference below records the single scope chosen by the designer, with the source of the project's output identified for actioning. Differences chosen 'ignore once' have been omitted."*
2. Each included difference now has **four** sections (the new Section 2 is inserted):
 
```
## Difference [n] — [short title] — [file/page, location]
 
### 1. Original raw content (source)
> The content as it appeared in the original raw input (A) — the uploaded
> Writers Template .docx or PageForge .txt. Quote the relevant tag(s) and text.
 
### 2. Source of the project's output
The exact project-knowledge rule(s) — file, section, and constraint number
where applicable — that produced the project's output (B). Quote the rule
wording. (Every reported difference is knowledge-derived by the Section 5 gate,
so this is always a project-file citation, never a template block.)
 
### 3. Originally generated code (this project's output)
```html
[the exact HTML this project produced for that content — input B]
```
 
### 4. Designer's refined code (the correct target)
```html
[the exact HTML from the designer's finished file — input C]
```
 
**What changed:** [one or two sentences plainly describing the difference]
 
[Scope decision / instruction block — see 9.2 / 9.3]
```
 
### 9.2 Scope handling for (a) / (b) / (c)
 
Include the difference in full (all four sections) and append exactly **one** `Scope decision:` block containing only the chosen scope, written out in full English. Every option the designer did not choose is omitted. Use these renderings (fill the placeholders):
 
- **(a) Series + level:** `Scope decision: (a) Series + level — incorporate this correction for every module at [MODULE_CODE]'s level within its own subject series only, i.e. every current and future [LEVEL_DESCRIPTOR] module in the [PREFIX] series (not other subjects at this level). Action: update the cited project-knowledge rule (see Section 2 above) so it is scoped to [PREFIX] modules at [LEVEL_DESCRIPTOR].`
- **(b) Module-series:** `Scope decision: (b) Module-series — incorporate this correction for every module in the [PREFIX] series, regardless of year level. Action: update the cited project-knowledge rule so it is scoped to the [PREFIX] series.`
- **(c) Universal:** `Scope decision: (c) Universal — incorporate this correction for every future conversion, regardless of template or series. Action: update the cited project-knowledge rule as a global rule.`
 
For a **multi-scope** difference (e.g. `A&B`), state both chosen scopes under one `Scope decision:` block and omit the rest.
 
### 9.3 Scope handling for (d) Ignore once and (e) Ignore always
 
- **(d) Ignore once — OMIT ENTIRELY.** A difference scoped (d) does **not** appear in the finalized report at all — no bundle, no number reuse, no mention. It was a bespoke one-off; there is nothing to action, so it is removed. (It still existed in the Phase 1 report as evidence; the finalized report simply drops it.)
- **(e) Ignore always — KEEP, with an explicit instruction for the future update conversation.** Include the difference in full (all four sections), then append, in place of a `Scope decision:` block, this **instruction block** addressed to the future, separate conversation that will edit the project files:
 
```
Instruction for the future project-file update — action in UPDATE MODE (`11_UPDATE_MODE.md`); do NOT action inside Comparison Mode:
(e) Ignore always — the designer has marked this CATEGORY of change as one that
should never be reported again. In the next Update Mode run, add a new standing
exclusion to `09_COMPARISON_MODE.md` → Section 4.1 (Differences NOT to Capture)
describing this category, so future Comparison Mode runs skip it silently.
Category to exclude: [one-line description of the kind of change].
No behavioural conversion rule changes for this item — exclusion only.
```
 
### 9.4 Refinement summary index
 
End the finalized report with a short **`Actioning summary`** table: every *included* difference number → its chosen scope → the artefact the future conversation should touch (the cited `00`–`08` file for a/b/c; `09` Section 4.1 for e). Differences scoped (d) are absent from this table because they were omitted. This table is the actionable index for the separate update conversation.
 
### 9.5 No project files are regenerated here
 
Phase 2 ends with the finalized report. **Do NOT regenerate, rewrite, or output any updated project files in Comparison Mode** — not the `00`–`12` files, not the structural reference. The finalized report is handed off; the edits happen elsewhere (Section 10).
 
---
 
## 10. WHAT HAPPENS AFTER — ACTIONING IS A SEPARATE CONVERSATION (UPDATE MODE)
 
The finalized report is the end of Comparison Mode. Editing the project files is a **separate, deliberate step the developer initiates in a different conversation — Update Mode** (`11_UPDATE_MODE.md`), entered with the trigger phrase `UPDATE MODE` — by feeding the finalized report in (or typing the changes directly) and asking for the project files to be updated. That downstream conversation — not Comparison Mode — is where:
 
- **(a) / (b) / (c)** differences are folded into the cited project-knowledge file at the recorded breadth (the level, the series, or universally).
- **(e)** differences have their category added to `09_COMPARISON_MODE.md` → Section 4.1 as a new standing exclusion.
- **(d)** differences require nothing (they were already omitted from the finalized report).
 
Comparison Mode's responsibility is to make that downstream step trivial: every included difference already names its source rule (Section 2), its before/after code (Sections 3–4), and its scope decision or exclusion instruction. **Within Comparison Mode, never edit the project files and never edit student content** — only analyse, report, and hand off.
 
---
 
## 11. THE DOWNLOADABLE REPORT
 
- Produce the report as a **downloadable file** — Markdown (`.md`) is the default; the designer may request another format.
- Suggested filenames:
  - Phase 1 (streamlined): `[MODULE_CODE]_difference_report.md`
  - Phase 2 (finalized): `[MODULE_CODE]_difference_report_finalized.md`
- Save it to the outputs location and present it with `present_files`.
- After presenting **Phase 1**, give a brief summary (module, files compared, number of differences reported), then **end the message with the scope-key block from Section 6.3** so the codes and reply format stay visible while the designer reviews the differences.
- After presenting **Phase 2**, give a brief summary: the parsed mapping, a note of which differences were omitted (d) and which were flagged for permanent exclusion (e), and a reminder that the finalized report is to be actioned in a separate conversation — the project files are not changed here.
- If **no qualifying differences** are detected (everything was either excluded by Section 4.1 or filtered out by the Section 5 gate), still produce the file with the header and a single line stating "No knowledge-derived differences detected for this module." Do not silently produce nothing.
 
---
 
## 12. SHARED DISCIPLINE
 
Comparison Mode obeys the same project discipline as every other mode:
 
- **Project knowledge is authoritative.** When identifying which project file/section produced a difference (the Phase 2 Section 2 citation), search files `00`–`08` and cite the real section — do not guess.
- **Apply the inclusion gate honestly.** Only report knowledge-derived differences. If you cannot confirm a difference is knowledge-derived, either drop it (if it looks template-derived) or keep it tagged `ORIGIN UNCERTAIN` (Section 5.4) — never silently treat a template-derived chunk as knowledge-derived to pad the report.
- **Never edit content, never edit project files.** Comparison Mode reports; it does not convert, complete, correct module content, or rewrite the project's own instruction files. The designer's file is the input, not something to "fix"; the project files are updated only later, in a separate conversation.
- **Quote accurately.** The before/after sections must reproduce the *actual* code from inputs B and C, and the Phase 2 Section 2 must reproduce the *actual* rule wording. Do not paraphrase or "tidy" the code being compared — the value of the report is in the exact before/after.
- **Be honest about uncertainty.** If a change's purpose is unclear, say so in the "What changed" line rather than inventing a rationale.
- **Stay neutral.** The designer's version (C) is treated as the correct target by definition — the report explains *what* changed, not whether the designer was "right".
 
---
 
## 13. WHAT COMPARISON MODE DOES NOT DO
 
- It does **not** convert raw content to HTML — that is Mode 1.
- It does **not** complete, debug, or fix module code — that is Mode 2.
- It does **not** edit student-facing writer content, ever.
- It does **not** report template-derived differences — anything the project lifted or mirrored from the supplied structural reference, example module, or other templated file is filtered out (Section 5).
- It does **not** edit the project files (`00`–`12`) or the structural reference. Producing the numbered evidence (Phase 1) and the finalized scoped report (Phase 2) is the whole job; actioning the report into the project files is a **separate downstream conversation — Update Mode** (`11_UPDATE_MODE.md`, Section 10).
- It does **not** include (d)-scoped differences in the finalized report — they are omitted.
- It does **not** apply changes to other modules itself — the scope choices are recorded for the downstream conversation.
- It does **not** default an unassigned difference to a scope — every difference's scope comes from the designer.
 
---
 
## 14. RELATIONSHIP TO ONE-OFF OVERRIDES
 
A **one-off override** (`08_MODULE_SUPPORT_DEBUGGING.md` → Section 5) and **Comparison Mode** are two ends of the same spectrum:
 
- A one-off override is applied **live, during support**, to a single module, and is deliberately **not** propagated.
- Comparison Mode is the **after-the-fact** capture of the corrections a designer made to knowledge-derived output, each later tagged with a scope so the genuinely general ones can be folded back into the project files (in the downstream actioning conversation).
 
In this model, a deliberate one-off is expressed simply by assigning **scope (d) — Ignore once** to that difference in Phase 2. The bundle appeared in the Phase 1 report as documented evidence, but is **omitted from the finalized report** and no rule update is propagated for it. Module-level one-off overrides continue to be tracked separately via `08_MODULE_SUPPORT_DEBUGGING.md`.
 
---
 
## 15. OUTPUT EXPECTATION
 
**Phase 1:** one downloadable difference report containing **only knowledge-derived differences** (template-derived output is filtered out per Section 5). It opens with its summary header (module, series, structural reference, template level, files compared, content-source format, total number of differences) followed — **once** — by the five-option scope legend (Section 7). Differences are numbered in a single continuous sequence. Each difference is a **three-section bundle** (raw content → original generated code → designer's refined code) plus a plain "what changed" line; the "source of the project's output" detail is intentionally withheld at this stage. Close the chat message with a brief summary, then **end it with the warm scope-key block** (Section 6.3) as the final, on-screen lines so the designer can refer to it while typing their pairings.
 
**Phase 2:** after the designer replies with `number-letter` pairings, regenerate the **finalized detailed report** — same numbering and titles, but now **four sections per included difference** (raw content → source of the project's output → original generated code → designer's refined code), the top legend replaced by a one-line note, and after each difference its scope handling: **(a)/(b)/(c)** print a single full-English `Scope decision:` block; **(d)** differences are **omitted entirely**; **(e)** differences are **kept with an explicit instruction block** for the future project-file-update conversation (Section 9.3). End with the `Actioning summary` table (Section 9.4). **The project files are not regenerated** — the finalized report is the deliverable, handed off to **Update Mode** to action (Section 10).