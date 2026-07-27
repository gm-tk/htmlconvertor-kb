> **Last updated:** Thursday, 16th July, 2026 9:30 PM
> **Granular part F (6 of 6) of `12_CHANGE_LEDGER.md`** — Blocked-request log, housekeeping, notes.
> All sibling parts live in `12_CHANGE_LEDGER/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## BLOCKED-REQUEST LOG (audit)

Requests that were **not** actioned because they clashed with a locked decision (they also appear as `Blocked (conflict)` rows in Part 3). Kept so the history of attempted overrides is visible.

| Date | Blocked request (summary) | Clashed with (ID) | Outcome |
|------|---------------------------|-------------------|---------|
| _—_ | _none yet_ | _—_ | _—_ |

---

## HOUSEKEEPING (optional — nothing here is a recurring task)

- **Normal use requires zero manual upkeep.** Update Mode appends rows and regenerates this file for you; you just replace it in the project like the other files.
- **Optional one-off trim (only if ever needed):** if Part 3 grows very large after years of use, you can ask Update Mode, in a single run, to move history rows older than a date you choose into a downloadable archive file and remove them from the live Part 3. **Part 1 (Locked) is never trimmed** — it must stay complete for conflict-checking. This is entirely optional and not part of the regular workflow.

---

## NOTES

- This file is created/seeded by the first Update Mode run that needs it and regenerated thereafter. If it is ever missing, Update Mode treats all parts as empty and recreates it.
- Keep this ledger in the project-knowledge area alongside the other project files so every Update Mode run can read it.
