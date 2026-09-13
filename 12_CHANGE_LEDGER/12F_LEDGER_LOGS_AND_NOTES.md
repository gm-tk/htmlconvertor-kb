> **Last updated:** Monday, 14th September, 2026 10:51 AM
> **Granular part F (11 of 12) of `12_CHANGE_LEDGER.md`** — Blocked-request log, housekeeping, notes.
> All sibling parts live in `12_CHANGE_LEDGER/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## BLOCKED-REQUEST LOG (audit)

Requests that were **not** actioned because they clashed with a locked decision (they also appear as `Blocked (conflict)` rows in Part 3). Kept so the history of attempted overrides is visible.

| Date | Blocked request (summary) | Clashed with (ID) | Outcome |
|------|---------------------------|-------------------|---------|
| _—_ | _none yet_ | _—_ | _—_ |

---

## HOUSEKEEPING (optional — nothing here is a recurring task)

- **Normal use requires zero manual upkeep.** Every Repo Update Brief carries the drafted ledger row(s); the linked Claude Code session appends them to the latest history part and commits — nothing to download or replace.
- **Growth is absorbed structurally, never trimmed:** when the latest Part 3 history part passes 30 KB, the Claude Code session starts a new `12x_CHANGE_HISTORY_…` part (repo `CLAUDE.md`; the repo's `check_kb.py` guard also verifies the CL id sequence stays unique and ascending across parts). **Part 1 (Locked) is never trimmed** — it must stay complete for conflict-checking.

---

## NOTES

- **PART 4 — the PageForge Amalgamation Log** lives in `12G_PAGEFORGE_AMALGAMATION_LOG.md`: the front-facing decisions only (those that change the generated HTML or CSS), in an implementable form for a future PageForge amalgamation pass. Both Admin Mode and Update Mode write to it; the front-facing test is constraint 87 and `17_ADMIN_MODE.md` → Section 5.1. It is append-only and **starts at CL-0086** — CL-0001 to CL-0085 remain in the Part 3 history and would need a separate one-off backfill.
- The ledger lives as the `12_CHANGE_LEDGER/` parts in the `htmlconvertor-kb` repository and syncs into project knowledge from there. If any part is ever missing from project knowledge, say so and treat it as a sync problem to raise with the designer — never invent or re-seed ledger content in chat.
- Keep this ledger in the project-knowledge area alongside the other project files so every Update Mode run can read it.
