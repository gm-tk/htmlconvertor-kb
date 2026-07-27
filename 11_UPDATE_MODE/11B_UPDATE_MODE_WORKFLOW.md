> **Last updated:** Thursday, 16th July, 2026 9:30 PM
> **Granular part B (2 of 2) of `11_UPDATE_MODE.md`** — Update Mode: regeneration, exclusions, workflow pseudo-code, timestamps (SS10-16).
> All sibling parts live in `11_UPDATE_MODE/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## 10. REGENERATION — FULL FILES, NOT PATCHES

Once the edits for every safe, non-conflicting change are determined:

1. **Apply every edit** to the affected files, at the resolved scope, preserving the project's existing structure, tone, numbering style, and formatting conventions. Do not restructure a file beyond what the change requires.
2. **Regenerate each affected file IN FULL.** The deliverable for every touched file is the **complete, replacement file** — never a diff, patch, or "insert this snippet" instruction. The designer replaces the obsolete copy wholesale.
3. **Do NOT touch files that no change affected.**
4. **Apply the timestamp convention (Section 13) to every regenerated file** — including `12_CHANGE_LEDGER.md`.
5. **Keep the knowledge base internally consistent.** After editing, re-scan for any now-stale statement, contradictory example, or dangling cross-reference introduced by the change, and fix it before presenting.

Save every regenerated file and present them with `present_files` so the designer can download and swap them in.

---

## 11. (e) IGNORE ALWAYS — GROWING THE EXCLUSIONS LIST

When a change is scoped **(e) Ignore always**, Update Mode does **not** alter any conversion behaviour. Instead it **logs the category as a standing exclusion** so Comparison Mode stops reporting it:

1. Open `09_COMPARISON_MODE.md` → **Section 4.1 (Differences NOT to Capture / Exclusions)**.
2. Add a new numbered exclusion describing the category in the same style as the existing Exclusions: a heading, a one-line scope, and a short rationale.
3. Regenerate `09_COMPARISON_MODE.md` in full (with refreshed timestamp).
4. Record it in `12_CHANGE_LEDGER.md` and note it in the run summary.

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

    # ── STEP 6: EDIT (Section 10 / 11) ──
    FOR EACH change:
        (a)/(b)/(c) ROUTINE → edit cited rule across all affected files; ledger = Implemented
        (a)/(b)/(c) MAJOR   → edit provisionally (or hold per team pref); ledger = Pending approval
        (e)                 → add 09 Section 4.1 exclusion; ledger row
        (d)                 → no edit (record "noted, no action")
        BLOCKED             → no edit (ledger = Blocked-conflict)
    RE-SCAN edited files for newly-introduced contradictions/stale refs; fix

    # ── STEP 7: CONFLICT CATALOG (Section 7) ──
    IF any report-vs-report conflicts → BUILD the "Cataloged differences that require approval"
        block for Persephone (one item per conflict; show previous + current difference)
    ELSE → omit it

    # ── STEP 8: TIMESTAMP, LEDGER & REGENERATE (Sections 13 / 4 / 10) ──
    APPEND new rows to 12_CHANGE_LEDGER.md
    FOR EACH affected file (incl. the ledger): REFRESH the top "Last updated" line; WRITE the full file

    # ── STEP 9: DELIVER ──
    PRESENT every regenerated file (present_files)
    WRITE: per-file change log; the conflict list (blocked / overturned);
           the "Cataloged differences that require approval" block for Persephone IF any
           report-vs-report conflicts (else omit); (d) noted-no-action; (e) exclusions added
    # NO difference report for the designer — never produced (constraint 76)
    REMIND the designer to replace the obsolete files,
           forward any conflict catalog to Persephone, and relay her decisions so pending rows
           can be locked or reverted
```

---

## 13. THE TIMESTAMP CONVENTION (project-wide)

Every project-knowledge file carries a **"Last updated" line as its very first line**, so the designer can see at a glance when each file was last regenerated.

**Canonical format** (line 1 of the file, followed by a blank line, then the file's `# Title`):

```
> **Last updated:** Weekday, Dth Month, YYYY h:MM AM/PM
```

e.g. `> **Last updated:** Thursday, 18th June, 2026 4:39 PM`. The weekday name and an ordinal day suffix (`st`/`nd`/`rd`/`th`) are always included.

Rules:

- **On every regeneration of a file (in any mode), refresh this line** to the current New Zealand date/time (`Pacific/Auckland`; obtain the actual current time rather than reusing a stale value).
- **If a file has no such line, add it** at the very top as part of regenerating that file ("added if not present").
- **If it already exists, update it in place** — do not stack a second line.
- The timestamp reflects when the file was **last regenerated/updated**, not when its content was first authored.
- Write the weekday in full, the day with an ordinal suffix (`18th`), the month name in full, the four-digit year, then 12-hour time with no leading zero on the hour and an `AM`/`PM` suffix (e.g. `2:47 PM`). Times are New Zealand local.
- Only files that an Update Mode (or other) run actually regenerates get a refreshed timestamp; untouched files keep their existing one. (The convention was first rolled out across all files on Thursday, 18th June, 2026.)

---

## 14. RELATIONSHIP TO COMPARISON MODE & ONE-OFF OVERRIDES

- **Comparison Mode → Update Mode** is the intended pipeline: Comparison Mode produces the finalized, scoped report; the designer feeds it into Update Mode to make the changes permanent. Update Mode is the "separate downstream conversation" named in `09_COMPARISON_MODE.md` → Section 10. The two stay in agreement: Comparison Mode captures and scopes; Update Mode checks, actions, regenerates, and gates the serious ones.
- **Update Mode also works without Comparison Mode.** The designer may bypass the report entirely and type changes straight into Update Mode (Section 2). The scope vocabulary, conflict check, and escalation/lock gate are identical — though a change typed directly is a `direct-typed` intake and so can never itself trigger the report-vs-report escalation to Persephone (Section 6).
- **One-off overrides** (`08_MODULE_SUPPORT_DEBUGGING.md` → One-Off Module Overrides) are the opposite of an Update Mode change: they apply to a single module live, are never propagated, and never touch the project files. An Update Mode change scoped **(d) Ignore once** is the report-driven equivalent — recorded, but no file edited.

---

## 15. WHAT UPDATE MODE DOES NOT DO

- It does **not** convert raw content to HTML (Mode 1), nor complete/debug module code (Mode 2), nor produce difference reports (Mode 3).
- It does **not** edit student-facing writer content — ever.
- It does **not** invent changes the designer did not request, and does **not** silently weaken a core philosophy or absolute constraint (it confirms first — Section 8).
- It does **not** override a `Locked` decision — a conflicting request is blocked until the design authority unlocks it (Sections 6–7).
- It does **not** lock a major change without the design authority's sign-off (Section 7).
- It does **not** emit patches or partial snippets — every affected file is regenerated in full (Section 10).
- It does **not** produce a finalized difference report for the designer (Gavin) — never, in any run (constraint 76). The run's restated change list and per-file change log are the record. The Persephone conflict catalog is a separate artefact and is unaffected.
- It does **not** change conversion behaviour for **(e) Ignore always** items — those only add a Comparison Mode exclusion (Section 11).
- It does **not** regenerate files that no change affected.
- It does **not** default an unscoped change to a breadth — scope comes from the designer (Section 3).

---

## 16. OUTPUT EXPECTATION

A completed Update Mode run delivers:

1. **A restated, normalised list** of the changes as understood (Step 0), with each change's resolved scope, intake channel, and Routine/Major classification.
2. **A conflict report** — any change blocked by a locked decision, any change that would overturn a prior unlocked (non-report) decision (with the old vs new result), and a pointer to the Persephone catalog (item 6) for any report-vs-report conflict.
3. **Every affected project file, regenerated in full and presented for download**, each carrying a refreshed top-of-file timestamp — including the updated **`12_CHANGE_LEDGER.md`**.
4. **NO difference report for the designer.** Update Mode does **not** produce a finalized difference report of the actioned changes for Gavin — not for any run, any intake channel, or any classification (constraint 76). The restated change list (item 1), the conflict report (item 2), and the per-file change log (item 5) are the complete record. Do not offer one; do not remind anyone to send one.
5. **A per-file change log** — for each regenerated file: what changed, at what scope, and why (citing the change number); plus a roll-up of any **(d)** items noted-no-action and any **(e)** exclusions added to `09`.
6. **The "Cataloged differences that require approval" block (Section 7.1) — only if at least one report-vs-report conflict occurred this run; otherwise omitted entirely** — listing each conflicting pair (previous + current difference) for **Persephone** to resolve.
7. **A reminder** to replace the obsolete files, forward any conflict catalog to Persephone, and relay her decisions so pending rows can be locked or reverted.

No converted HTML, no student-content edits, no diffs, **no difference report for the designer** — full replacement files, a clear account of what changed, and (only when two finalized reports disagree) a conflict catalog for the design authority.
