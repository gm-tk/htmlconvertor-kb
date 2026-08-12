> **Last updated:** Thursday, 13th August, 2026
> **Granular part C (3 of 3) of `11_UPDATE_MODE.md`** — Sections 8-9: the pre-flight confirmations and the blast-radius sweep. Split from `11A` on 13 August 2026 when it passed the 30 KB soft limit (`CLAUDE.md` §4); content moved verbatim.
> All sibling parts live in `11_UPDATE_MODE/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## 8. PRE-FLIGHT — WHAT TO CONFIRM BEFORE EDITING

Before drafting any edit for the Repo Update Brief, resolve these. Ask only about what is genuinely unresolved — keep it to one concise round of questions where possible.

1. **Scope for every change.** Each normalised change must have exactly one breadth (a/b/c/d/e or a clear paraphrase, or a permitted multi-scope like `A&B`). List any change missing a scope and ask.
2. **Conflicts (Section 6).** Surface every `Blocked (conflict)` item. For a **non-report conflict** that overturns a prior unlocked decision, get the designer's confirmation before editing. For a **report-vs-report conflict**, catalog it for Persephone (Section 7.1) rather than resolving it in-chat.
3. **Guardrail-level changes need explicit confirmation.** If an instructed change would **weaken, reverse, or contradict a CORE PHILOSOPHY or an ABSOLUTE/HARD CONSTRAINT** — e.g. "start allowing arbitrary inline CSS in output", "disclose interactive answers in comments", "let the converter reword writer content", "invent components when unsure" — pause and confirm in plain terms that the designer really intends to change a foundational guardrail, and restate the blast radius. (Such changes are also always Major — Section 5.) Action only on explicit confirmation.
4. **Internal contradictions.** If two requested changes conflict, or a change contradicts an existing rule that is *not* itself being changed, point out the clash and ask which should win.
5. **Ambiguous target.** If a change could plausibly live in more than one file/section, search project knowledge to determine the true owner; if still ambiguous, say where you propose to put it and why, and proceed unless the designer objects.
6. **A settled universal constraint is NEVER a pre-flight question — and a SUPERSEDED rule is never a live option.** Do not ask the designer to choose between a `(Universal)` constraint and some other behaviour, and never present retired wording found in the knowledge base as an alternative to the rule that superseded it. When a change request appears to contradict a universal constraint, name the constraint, say plainly that it already settles the point, and ask the designer to confirm they intend to **override** it — a confirmed override is a Major change that rewrites the constraint, not a one-off answer. **A designer answer that contradicts a universal constraint is flagged back, never followed silently.** *(Origin: SCES302, August 2026 — the retired "lesson `<h1>` = MODULE title" wording was surfaced during a conversion and offered as a choice against constraint 79; the answer was followed and eight lesson pages shipped with the wrong header. See `00B` → the pre-flight block.)*
7. **When superseding a rule, sweep the retired wording out.** A change that supersedes an existing rule is not finished when the new rule is written: search every part file for the **old phrasing** and remove it, or mark it unmistakably as retired with a pointer to the superseding constraint. Wording left live in a checklist line, a worked example or a sibling pathway file (MTK, Split, Interactives) is what a later search surfaces — and what a later conversion follows. This is part of the Section 9 blast-radius sweep, not optional tidy-up.

Update Mode does **not** edit student-facing module content, does not convert, and does not invent changes beyond what the designer instructed. It edits the **rule files only.**

---

## 9. THE BLAST-RADIUS SWEEP — FIND *EVERY* FILE THAT MUST CHANGE

This is the defining discipline of Update Mode: for each change, **identify every single file in the project-knowledge area that must be updated** so the issue is fixed *and never recurs*, then update all of them consistently. A rule that lives in one file is almost always **referenced, summarised, cross-linked, or indexed** in others; leaving those stale creates a self-contradicting knowledge base.

For each change, before editing, locate **all** of these that apply:

1. **The owning rule** — the primary file/section that defines the behaviour (e.g. a COMP section in `03`/`04`/`05`, a tag mapping in `01`, a data pattern in `02`).
2. **The CONSTRAINTS list in `00_MASTER_INSTRUCTIONS.md`** — if the change adds, removes, or alters a hard/universal constraint, the numbered CONSTRAINTS (Quick Reference) section must change too. Keep numbering and cross-references coherent.
3. **The FILE REFERENCE INDEX and "WHEN TO LOAD WHICH FILES" map in `00`** — if a topic moves, is added, or is renamed.
4. **Cross-references in other files** — any `See \`0X_...\` → Section` pointer, any duplicated statement of the rule, any example that would now be wrong. Search for the rule's keywords across all files and fix every hit.
5. **`09_COMPARISON_MODE.md`** — for any **(e) Ignore always** change (add the Section 4.1 exclusion), and whenever a changed rule is one Comparison Mode cites or depends on.
6. **`12_CHANGE_LEDGER.md`** — always, for any change that is actioned, blocked, pending, locked, or reverted (Section 4).
7. **The project-instructions field (`_project_instructions_.md`)** — if the change affects mode triage, the file map, the always-active ABSOLUTE RULES, the core philosophy, or the output expectation summarised there.
8. **This file (`11_UPDATE_MODE.md`)** — if the change affects Update Mode itself.

> **Search, don't recall.** Use `project_knowledge_search` (and a literal text scan of the files) for the rule's distinctive keywords to catch every occurrence. Do not rely on memory of where a rule appears. Missing a downstream reference is the most likely failure of Update Mode — sweep thoroughly.

Record the full set of affected files (granular part paths where known) for each change; that set drives the edit list in the Repo Update Brief (`11B` → Section 10).

---

