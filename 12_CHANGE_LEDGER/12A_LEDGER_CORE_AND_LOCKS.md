> **Last updated:** Monday, 27th July, 2026 12:34 PM
> **Granular part A (1 of 6) of `12_CHANGE_LEDGER.md`** — Ledger purpose, status values, PART 1 locked decisions, PART 2 pending approval.
> All sibling parts live in `12_CHANGE_LEDGER/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
> **Last updated:** Thursday, 16th July, 2026 9:30 PM

# 12 — Change Ledger (Conflict & Lock Registry)

> **When to load:** At the **start of every Update Mode run** (read it to check new changes for conflicts and locked decisions) and at the **end** (draft the outcome row(s) for the Repo Update Brief, which the linked Claude Code session appends to the latest history part — the ledger is never regenerated in full; see `11_UPDATE_MODE.md` → Sections 4 and 10). Comparison Mode and the conversion pipeline do **not** read or edit this file.

---

## PURPOSE

This ledger (in the repository: the `12_CHANGE_LEDGER/` folder of parts — Parts 1 and 2 in this part, the Part 3 history across the `12x_CHANGE_HISTORY_…` parts) is the project's **complete, permanent, in-house record** of every change actioned through Update Mode. **Nothing is stored externally** — there is no spreadsheet, no export, and no manual step for the designer to maintain. Every Repo Update Brief carries the drafted row(s), and the linked Claude Code session appends them, so the ledger stays current as a by-product of actioning changes (`11_UPDATE_MODE.md` → Section 4).

It does three jobs:

1. **Conflict source** — what has already been decided, and was it decided differently before? (Conflict checking reads **Part 1** first.)
2. **Lock registry** — which decisions has the design authority (Persephone) resolved in favour of and **locked** against future override? (**Part 1**.)
3. **Audit trail** — a dated history of everything that has changed, at what scope, from which report, and who approved it. (**Part 3**.)

---

## WHY ONE IN-HOUSE FILE IS FINE (feasibility note)

Keeping everything here does **not** slow the project's main job or eat into chat space, because:

- **Conversion chats never read this file** — only Update Mode does. So however long it grows, it has zero effect on day-to-day Word-to-HTML conversions.
- **Project knowledge is retrieved, not pre-loaded, once it is large enough** — Claude searches the knowledge base and pulls in only what's relevant, so this file is not sitting in full in every conversation.
- **The conflict check only needs Part 1 (Locked Decisions)**, which stays compact — it is just the list of binding rules, which grows slowly and levels off. The long history in Part 3 is inert audit data.

So this ledger can accumulate for years with no practical downside. **The designer never has to do anything to maintain it.** Growth is absorbed structurally: when the latest Part 3 history part passes 30 KB, the Claude Code session starts a new `12x_CHANGE_HISTORY_…` part (repo `CLAUDE.md`) — no trimming, no archiving, nothing removed.

---

## STATUS VALUES

| Status | Meaning |
|---|---|
| **Implemented** | A change that is actioned and in effect. Covers both routine changes **and non-conflicting Major changes** — any non-conflicting change is actioned directly via the Repo Update Brief and accounted for in the run's restated change list and per-change log (**no difference report is produced for the designer** — constraint 76, `CL-0052`). No authority sign-off needed. Lives in Part 3. |
| **Pending approval** | A **report-vs-report conflict** actioned provisionally, awaiting the design authority's (Persephone's) resolution — i.e. a change that arrived via a finalized difference report and clashes with a prior change that *also* arrived via a finalized difference report. Lives in Part 2 until resolved. *(Legacy note: CL-0001–CL-0004 carry this status under the pre-19-June model, in which every Major change awaited sign-off; CL-0005 was reverted on 30th June 2026, superseded by CL-0007 — see the note under Part 3.)* |
| **Locked** | Major change the design authority approved. **Immutable.** Lives in Part 1; also recorded in Part 3. |
| **Reverted** | A change rejected, withdrawn, superseded, or unlocked. Edit undone in the repository via a follow-up Repo Update Brief; row kept in Part 3 for audit. |
| **Blocked (conflict)** | A requested change **not** actioned because it clashed with a `Locked` row. Logged in Part 3 + the Blocked-request log; needs an unlock decision to proceed. |

**Classification:** `Routine` or `Major` (Major = universal scope, structural/design change, or guardrail-affecting — see `11_UPDATE_MODE.md` → Section 5).

---

## HOW TO READ / MAINTAIN THIS LEDGER

- **IDs are permanent and sequential** (`CL-0001`, `CL-0002`, …). Never reuse or renumber an ID. An ID keeps the same number everywhere it appears (e.g. a `Locked` change appears in both Part 1 and Part 3 under one ID).
- **Append-only.** New changes are added as new rows. A row's `Status` may be updated in place (e.g. `Pending approval` → `Locked`), but history stays legible (note supersessions, e.g. "superseded by CL-0042").
- **Conflict scan order:** check **Part 1 (Locked)** first — those are the rows that can *block* a new change. Then scan **Part 3** for any prior *unlocked* decision on the same thing (a soft duplicate/reversal check). Match on the affected file/section/constraint and the behaviour described, not just on wording.
- **Locked rows are protected.** A new change that contradicts a Part 1 row is logged `Blocked (conflict)` and not actioned (see `11_UPDATE_MODE.md` → Section 6).
- **Source = intake channel.** The `Source` column records *how* each change entered the project — `Finalized difference report`, `Direct-typed (Update Mode)`, or `Project instruction` — and this is what drives conflict routing. A clash is escalated to the design authority (Persephone) **only when both sides arrived via a finalized difference report**. If the new change contradicts a `Locked` row it is **blocked** regardless of channel; if it clashes with a prior change that came in by any non-report channel (direct-typed or project instruction), Update Mode **pauses for the designer to confirm** rather than escalating. See `11_UPDATE_MODE.md` → Sections 6–7.
- Every ledger part the Claude Code session touches gets its header **Last updated** timestamp refreshed (per the Repo Update Brief's standing instructions).

---

## PART 1 — LOCKED DECISIONS (binding & immutable — conflict check reads this FIRST)

The authoritative "do not override" list. A newly-requested change that contradicts any row here is **blocked** until the design authority explicitly unlocks it. This section stays small by nature (it is the set of standing, signed-off rules).

| ID | Date locked | Locked decision | Scope | Affected file(s) / rule(s) | Approved by (date) |
|----|-------------|-----------------|-------|----------------------------|--------------------|
| _—_ | _—_ | _No locked decisions yet._ | _—_ | _—_ | _—_ |

---

## PART 2 — PENDING APPROVAL (report-vs-report conflicts awaiting the design authority's resolution)

**Report-vs-report conflicts** actioned provisionally; each is catalogued for the design authority (Persephone) to resolve — a change that arrived via a finalized difference report and clashes with a prior change that *also* arrived via a finalized difference report. On resolution in favour of the change, its row moves to Part 1 as `Locked`; if the prior decision survives, the change is reverted in the files and recorded `Reverted` in Part 3. *(CL-0001–CL-0004 below predate this model — see the note under Part 3 — and are retained as-is rather than re-routed; CL-0005 was reverted on 30th June 2026, superseded by CL-0007, and has left this list.)*

| ID | Date actioned | Change summary | Scope | Affected file(s) / rule(s) | Source (intake channel) | Approval message sent |
|----|---------------|----------------|-------|----------------------------|--------|-----------------------|
| CL-0001 | Thursday, 18th June, 2026 | Image `alt` text: for iStock images prioritise the iStock/Getty API image name; never use the words "stock photo" in alt text | (c) Universal | `01` → Images (alt text), iStock Acknowledgements File; `00` constraint 52 | Direct-typed (Update Mode) | Yes — this run |
| CL-0002 | Thursday, 18th June, 2026 | iStock acknowledgements file (API-sourced) is authoritative: its iStock acks entries are used verbatim in the acks block (overriding URL-slug derivation) | (c) Universal | `05` → Acknowledgements (Sourcing); `01` → iStock Acknowledgements File + Media List note; `00` INPUT FILES / WHEN-TO-LOAD / constraint 53 | Direct-typed (Update Mode) | Yes — this run |
| CL-0003 | Thursday, 18th June, 2026 | Video/YouTube acks entry format → `Video: title, author, <a>link</a>, retrieved d/m/y. Used in online learning within the exception for education.`; retrieved date = processing date | (c) Universal | `05` → Acknowledgements (Entry format); `00` constraint 54 | Direct-typed (Update Mode) | Yes — this run |
| CL-0004 | Thursday, 18th June, 2026 | Dropbox/portfolio submission buttons keep the full "Go to dropbox" / "Go to portfolio" label (the "Go to" prefix is not dropped) | (c) Universal | `05` → Buttons; `00` constraint 55 | Direct-typed (Update Mode) | Yes — this run |

---

