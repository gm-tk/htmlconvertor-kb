> **Last updated:** Thursday, 13th August, 2026
> **Granular part B (2 of 3) of `11_UPDATE_MODE.md`** — Update Mode: the Repo Update Brief, exclusions, workflow pseudo-code, timestamps (SS10-16).
> All sibling parts live in `11_UPDATE_MODE/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## 10. THE REPO UPDATE BRIEF — PRECISE EDITS FOR CLAUDE CODE, NOT FILE REGENERATION

**(Superseded workflow note, 27 July 2026 — CL-0053.)** The knowledge base now lives in the **`htmlconvertor-kb` GitHub repository** as granular part files (the repo's `INDEX.md` maps every part; its `CLAUDE.md` holds the maintenance ritual). Update Mode **no longer regenerates or outputs any project file, ever** — regenerating full files in chat is the timeout-prone failure mode the repository was created to eliminate. Instead, once the edits for every safe, non-conflicting change are determined, the run's deliverable is ONE **Repo Update Brief**: a single fenced markdown block, written to be pasted verbatim into a **Claude Code session opened on that repository**, which carries out the edits, the ledger append, the checks, and the commit.

The brief must contain, in this order:

1. **Header** — date, intake channel (finalized report / direct-typed / uploaded file), and a one-line purpose.
2. **One numbered edit instruction per change**, each carrying:
   - the ledger id (**next sequential `CL-nnnn`** — with an instruction that Claude Code verify the sequence against the latest `12_CHANGE_LEDGER` history part before committing);
   - the resolved scope (a/b/c/e) and Routine/Major classification;
   - the **target part file path(s)** in granular form (e.g. `02_DATA_CONTENT_VERIFICATION/02D_COMMENT_POLICY_CONSTRAINTS.md`). If the exact part letter is uncertain from project knowledge, name the topic folder plus the section heading and tell Claude Code to confirm the part via the repo `INDEX.md`;
   - the **precise edit**: quote the existing wording to be changed and give the exact replacement wording — or, for an addition, the exact new text and its anchor ("insert after the paragraph beginning …"). **Never** write "update the rule accordingly" — the brief carries the finished wording, so Claude Code performs edits, not drafting.
3. **The drafted ledger row(s)** in the exact PART 3 table format, ready to append verbatim.
4. **A standing-instructions block** (include verbatim in every brief): *Follow the repo `CLAUDE.md` ritual — edit the named parts in place (never regenerate a topic); refresh each touched part's header `Last updated` line (Section 13 format); append the ledger row(s) to the LATEST history part, starting a new part first if it exceeds 30 KB; update `INDEX.md` if any file's section list changed; run `python3 tools/check_kb.py` and fix any failure; commit as `CL-nnnn: <summary>`; report back a summary of the diff.*
5. **The `_project_instructions_.md` reminder** — only when that file is a target: after the commit, the designer must manually re-paste its content into the Claude.ai project's **Instructions** field (that file does not sync from the repo).

Discipline carried over from the old workflow: preserve the project's existing structure, tone, numbering style, and formatting conventions; instruct no edit to any part no change affects; and keep the knowledge base internally consistent — sweep for now-stale statements, contradictory examples, or dangling cross-references the change would introduce, and include those consequential edits in the brief too.

**Sync caveat:** the project's knowledge reflects the repo only after the commit is pushed and the project's GitHub sync refreshes. Until then, this conversation is reading the pre-change knowledge — say so if the designer asks to use the new rule immediately.

---

## 11. (e) IGNORE ALWAYS — GROWING THE EXCLUSIONS LIST

When a change is scoped **(e) Ignore always**, Update Mode does **not** alter any conversion behaviour. Instead it **logs the category as a standing exclusion** so Comparison Mode stops reporting it:

1. Target `09_COMPARISON_MODE.md` → **Section 4.1 (Differences NOT to Capture / Exclusions)** (in the repo: the `09_COMPARISON_MODE/` part holding Section 4.1 — confirm via `INDEX.md`).
2. Draft the new numbered exclusion describing the category in the same style as the existing Exclusions: a heading, a one-line scope, and a short rationale.
3. Include it in the Repo Update Brief (Section 10) as a precise anchored insertion — no file regeneration.
4. Draft the matching `12_CHANGE_LEDGER` history row for the brief and note the exclusion in the run summary.

This is the designer-driven mechanism for *shrinking* future report noise, exactly as anticipated by `09_COMPARISON_MODE.md` → Section 4.1 (Note on Phase 2 option (e)) and Section 9.3.

---

## 12. WORKFLOW (pseudo-code)

```
FUNCTION update_mode(designer_input):

    # ── STEP 0: INTAKE & NORMALISE ──
    CONFIRM the UPDATE MODE trigger is present
    GATHER the changes (this/adjacent message OR uploaded file);
        IF none → say Update Mode is active; ASK for changes (any format); STOP until received
    READ 12_CHANGE_LEDGER.md (create-empty if absent): Part 1 Locked + Part 2 Pending in full, search Part 3 History
    NORMALISE input (any format) into a numbered list of proposed changes,
        each with {what changes, scope (if given), reason/evidence (if given)}
    RESTATE the normalised list back to the designer

    # ── STEP 1: SCOPE ──
    FOR EACH change: DETERMINE breadth (a/b/c/d/e) from letters or plain-English cues
        IF missing/ambiguous → COLLECT for a clarifying question

    # ── STEP 2: CONFLICT CHECK (Section 6) ──
    FOR EACH change:
        LOOK UP the ledger for prior entries on the same rule/behaviour
        SAME result                                            → mark "already in effect", drop
        DIFFERENT result + prior LOCKED                        → BLOCK (log Blocked-conflict); do not action
        DIFFERENT result + BOTH sides via finalized report     → CATALOG for Persephone (7.1); log Pending approval
        DIFFERENT result + any non-report source (not locked)  → COLLECT as "overturns prior decision" (designer confirm)
        none                                                   → continue

    # ── STEP 3: CLASSIFY (Section 5) ──
    FOR EACH surviving change: CLASSIFY Routine vs Major (borderline → Major)

    # ── STEP 4: PRE-FLIGHT CONFIRM (Section 8) ──
    IF any: missing scope / blocked or overturning conflicts / guardrail-weakening /
            internal contradictions / ambiguous target
        → ASK one concise round; STOP until answered

    # ── STEP 5: BLAST-RADIUS SWEEP (Section 9) ──
    FOR EACH actionable change (a/b/c, or e):
        SEARCH knowledge + literal scan; BUILD the set of every affected file
    (d) contributes no files; (blocked) contributes only a ledger row

    # ── STEP 6: DRAFT THE EDITS (Section 10 / 11) ──
    FOR EACH change:
        (a)/(b)/(c) ROUTINE → draft the precise old→new edit for every affected part; ledger = Implemented
        (a)/(b)/(c) MAJOR   → draft the edit marked PROVISIONAL (or hold per team pref); ledger = Pending approval
        (e)                 → draft the 09 Section 4.1 exclusion insertion; ledger row
        (d)                 → no edit (record "noted, no action")
        BLOCKED             → no edit (ledger = Blocked-conflict)
    SWEEP for stale statements / contradictions / dangling cross-references the changes
        would introduce; draft those consequential edits too

    # ── STEP 7: CONFLICT CATALOG (Section 7) ──
    IF any report-vs-report conflicts → BUILD the "Cataloged differences that require approval"
        block for Persephone (one item per conflict; show previous + current difference)
    ELSE → omit it

    # ── STEP 8: LEDGER ROWS & THE BRIEF (Sections 4 / 10 / 13) ──
    DRAFT the new 12_CHANGE_LEDGER row(s) in exact PART 3 table format (next CL-nnnn)
    ASSEMBLE the Repo Update Brief (Section 10): header; numbered precise edits with
        granular part paths; the ledger rows; the standing-instructions block
        (timestamps, INDEX.md, check_kb.py, commit convention);
        the _project_instructions_ re-paste reminder IF that file is targeted

    # ── STEP 9: DELIVER ──
    OUTPUT the Repo Update Brief as ONE fenced markdown block (no project files are
        regenerated or presented — constraint / Section 10)
    WRITE: per-change log; the conflict list (blocked / overturned);
           the "Cataloged differences that require approval" block for Persephone IF any
           report-vs-report conflicts (else omit); (d) noted-no-action; (e) exclusions added
    # NO difference report for the designer — never produced (constraint 76)
    REMIND the designer to paste the brief into a Claude Code session on the
           htmlconvertor-kb repo, push the commit, and wait for project-knowledge sync;
           forward any conflict catalog to Persephone and relay her decisions so pending
           rows can be locked or reverted
```

---

## 13. THE TIMESTAMP CONVENTION (project-wide)

Every project-knowledge file carries a **"Last updated" line as its very first line**, so the designer can see at a glance when each file was last updated. In the granular repo each PART file's header (first) line is that stamp; the Claude Code session refreshes it on every part it edits, as instructed by the Repo Update Brief's standing-instructions block (Section 10).

**Canonical format** (line 1 of the file, followed by a blank line, then the file's `# Title`):

```
> **Last updated:** Weekday, Dth Month, YYYY h:MM AM/PM
```

e.g. `> **Last updated:** Thursday, 18th June, 2026 4:39 PM`. The weekday name and an ordinal day suffix (`st`/`nd`/`rd`/`th`) are always included.

Rules:

- **On every update of a file (in any mode), refresh this line** to the current New Zealand date/time (`Pacific/Auckland`; obtain the actual current time rather than reusing a stale value).
- **If a file has no such line, add it** at the very top as part of updating that file ("added if not present").
- **If it already exists, update it in place** — do not stack a second line.
- The timestamp reflects when the file was **last updated**, not when its content was first authored.
- Write the weekday in full, the day with an ordinal suffix (`18th`), the month name in full, the four-digit year, then 12-hour time with no leading zero on the hour and an `AM`/`PM` suffix (e.g. `2:47 PM`). Times are New Zealand local.
- Only files that an Update Mode (or other) run actually updates get a refreshed timestamp; untouched files keep their existing one. (The convention was first rolled out across all files on Thursday, 18th June, 2026.)

---

## 14. RELATIONSHIP TO COMPARISON MODE & ONE-OFF OVERRIDES

- **Comparison Mode → Update Mode** is the intended pipeline: Comparison Mode produces the finalized, scoped report; the designer feeds it into Update Mode to make the changes permanent. Update Mode is the "separate downstream conversation" named in `09_COMPARISON_MODE.md` → Section 10. The two stay in agreement: Comparison Mode captures and scopes; Update Mode checks, drafts the Repo Update Brief for Claude Code to action, and gates the serious ones.
- **Update Mode also works without Comparison Mode.** The designer may bypass the report entirely and type changes straight into Update Mode (Section 2). The scope vocabulary, conflict check, and escalation/lock gate are identical — though a change typed directly is a `direct-typed` intake and so can never itself trigger the report-vs-report escalation to Persephone (Section 6).
- **One-off overrides** (`08_MODULE_SUPPORT_DEBUGGING.md` → One-Off Module Overrides) are the opposite of an Update Mode change: they apply to a single module live, are never propagated, and never touch the project files. An Update Mode change scoped **(d) Ignore once** is the report-driven equivalent — recorded, but no file edited.

---

## 15. WHAT UPDATE MODE DOES NOT DO

- It does **not** convert raw content to HTML (Mode 1), nor complete/debug module code (Mode 2), nor produce difference reports (Mode 3).
- It does **not** edit student-facing writer content — ever.
- It does **not** invent changes the designer did not request, and does **not** silently weaken a core philosophy or absolute constraint (it confirms first — Section 8).
- It does **not** override a `Locked` decision — a conflicting request is blocked until the design authority unlocks it (Sections 6–7).
- It does **not** lock a major change without the design authority's sign-off (Section 7).
- It does **not** regenerate, rewrite, or output project files — its deliverable is the Repo Update Brief of precise, finished edits (Section 10); the actual file changes happen in the Claude Code session on the `htmlconvertor-kb` repository. Vague instructions ("update the rule accordingly") are equally banned — every edit in the brief carries its exact final wording.
- It does **not** produce a finalized difference report for the designer (Gavin) — never, in any run (constraint 76). The run's restated change list and per-file change log are the record. The Persephone conflict catalog is a separate artefact and is unaffected.
- It does **not** change conversion behaviour for **(e) Ignore always** items — those only add a Comparison Mode exclusion (Section 11).
- It does **not** include edits in the brief for parts that no change affected.
- It does **not** default an unscoped change to a breadth — scope comes from the designer (Section 3).

---

## 16. OUTPUT EXPECTATION

A completed Update Mode run delivers:

1. **A restated, normalised list** of the changes as understood (Step 0), with each change's resolved scope, intake channel, and Routine/Major classification.
2. **A conflict report** — any change blocked by a locked decision, any change that would overturn a prior unlocked (non-report) decision (with the old vs new result), and a pointer to the Persephone catalog (item 6) for any report-vs-report conflict.
3. **The Repo Update Brief** (Section 10) — ONE fenced markdown block for the Claude Code session on the `htmlconvertor-kb` repository: numbered precise edits with granular part paths, the drafted `12_CHANGE_LEDGER` row(s), the standing-instructions block (timestamps, `INDEX.md`, `check_kb.py`, commit convention), and the `_project_instructions_.md` re-paste reminder when applicable. **No project files are regenerated or presented for download.**
4. **NO difference report for the designer.** Update Mode does **not** produce a finalized difference report of the actioned changes for Gavin — not for any run, any intake channel, or any classification (constraint 76). The restated change list (item 1), the conflict report (item 2), and the per-file change log (item 5) are the complete record. Do not offer one; do not remind anyone to send one.
5. **A per-change log** — for each edit in the brief: which part file(s) it targets, what changes, at what scope, and why (citing the change number); plus a roll-up of any **(d)** items noted-no-action and any **(e)** exclusions added to `09`.
6. **The "Cataloged differences that require approval" block (Section 7.1) — only if at least one report-vs-report conflict occurred this run; otherwise omitted entirely** — listing each conflicting pair (previous + current difference) for **Persephone** to resolve.
7. **A reminder** to paste the brief into a Claude Code session opened on the `htmlconvertor-kb` repository, push the resulting commit, wait for the project's GitHub sync (until then this project reads the pre-change knowledge), forward any conflict catalog to Persephone, and relay her decisions so pending rows can be locked or reverted.

No converted HTML, no student-content edits, no regenerated files, **no difference report for the designer** — one precise Repo Update Brief, a clear account of what changed, and (only when two finalized reports disagree) a conflict catalog for the design authority.
