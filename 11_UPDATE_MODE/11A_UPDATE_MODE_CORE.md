> **Last updated:** Thursday, 13th August, 2026
> **Granular part A (1 of 3) of `11_UPDATE_MODE.md`** — Update Mode: purpose, trigger, input, scope, ledger use, classification, conflict check and escalation (§1-7). The pre-flight confirmations and the blast-radius sweep (§8-9) live in `11C`.
> All sibling parts live in `11_UPDATE_MODE/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
> **Last updated:** Thursday, 16th July, 2026 9:30 PM

# 11 — Update Mode (Mode 4)

> **When to load:** Whenever a message contains the trigger phrase **`UPDATE MODE`** (case-insensitive) — typically accompanied by, or immediately followed by, the changes the designer wants permanently implemented (a finalized Comparison Mode difference report, or free-typed instructions in any format). This is **Mode 4 — Update** (see `00_MASTER_INSTRUCTIONS.md` → Operating Modes). Together with `COMPARISON MODE`, the `UPDATE MODE` trigger takes precedence over the ordinary Conversion / Advisory / Support mode signals.

---

## PURPOSE

Comparison Mode (`09_COMPARISON_MODE.md`) is the *capture* half of the project's self-improvement loop: it documents what a designer corrected and records, per difference, how widely that correction should apply. Comparison Mode deliberately **never edits the project files** — it ends with a finalized report and hands off.

**Update Mode is the *actioning* half of that same loop.** It takes the designer's intended changes, **checks them against the permanent change ledger for conflicts**, and — since 27 July 2026 (ledger `CL-0053`), when the knowledge base moved into the **`htmlconvertor-kb` GitHub repository** as granular part files — **actions the safe, non-conflicting ones by producing ONE Repo Update Brief**: a precisely-worded, copy-paste instruction block for a **Claude Code session opened on that repository**, which edits the exact part files in place, appends the ledger row(s), runs the repo's checks, and commits (`11B` → Section 10). Update Mode **no longer regenerates or outputs any project file**. When **a change submitted via a finalized difference report conflicts with a prior decision that was also lodged via a finalized difference report**, it **catalogs the conflicting differences for the team's design authority (Persephone)** to review and resolve, so the surviving decision can be **locked** against future override. Non-conflicting changes (whatever their class) are actioned directly via the brief and reported **in-run** via the restated change list and the per-change log. After the brief's commit is pushed and the project's GitHub knowledge sync refreshes, all *future* conversions, advisory answers, and comparison reports reflect the change.

> **⚠️ NO DIFFERENCE REPORT IS PRODUCED FOR THE DESIGNER (constraint 76).** Update Mode does **not** generate, write out, or present a finalized difference report of the actioned changes for Gavin — permanently, for every run, whatever the intake channel or classification. The run's own output (the restated change list, the conflict report, the Repo Update Brief, and the per-change log) **is** the record. Do not offer to produce one; do not remind anyone to email one. Standing designer instruction, 16 July 2026 (ledger `CL-0052`), superseding the report-to-Gavin limb of `CL-0006`. The **Persephone conflict catalog is unaffected** — it is a different artefact on a different path (Section 7.1) and is still produced whenever a report-vs-report conflict occurs.

In short:

- **Comparison Mode** = *"Here is what I changed and how broadly each change should apply."* (report only — no file edits)
- **Update Mode** = *"Check this against what we've already decided, then hand me the Repo Update Brief that makes the safe changes permanent via Claude Code on the repository, and catalog any report-vs-report conflict for the design authority to resolve."*

Update Mode is what `09_COMPARISON_MODE.md` → Section 10 ("What happens after — actioning is a separate conversation") refers to. The separate conversation is **this mode**.

---

## 1. THE TRIGGER

Update Mode is entered when a message contains the literal phrase **`UPDATE MODE`** (case-insensitive) anywhere in the text.

The changes to action may arrive in **either** of two ways — Update Mode accepts both:

1. **In the same message** as the trigger (pasted finalized report, pasted notes, an uploaded report file, etc.).
2. **In a following message** — the designer types `UPDATE MODE` first, and then sends the changes (or uploads the report) in their next message.

If `UPDATE MODE` arrives with **no accompanying changes and none in the immediately preceding/following turn**, do not start editing. Acknowledge that Update Mode is active and ask the designer to supply the changes they want implemented (in any format — see Section 2). Wait until received.

> Update Mode is a **deliberate, source-of-truth-changing action.** Unlike Advisory/Support answers, its output (the Repo Update Brief) changes the project's stored instruction files once run in Claude Code. Treat the trigger as explicit authorisation to draft those edits — but still run the conflict check (Section 6), confirm scope and guardrail-level changes (Section 8), and route any report-vs-report conflict through the escalation/lock gate (Section 7) before anything is treated as final.

---

## 2. ACCEPTED INPUT — ANY FORMAT

A core design goal of Update Mode is **format-agnostic intake.** The designer must be able to express the changes however is convenient. Accept and correctly interpret **all** of the following, and anything resembling them:

- **A finalized Comparison Mode difference report** (`[MODULE_CODE]_difference_report_finalized.md` or similar) — the standard, richest input. Each included difference already carries its raw content, the cited source rule (file/section/constraint), the before/after code, and a `Scope decision:` block or an `(e) Ignore always` instruction block. Use these directly.
- **A streamlined (Phase 1) report plus separately-typed scope letters** — if only a Phase 1 report is supplied, look for the `number-letter` scope pairings in the message; if absent, ask for them (Section 8).
- **Free-typed instructions in plain English** — e.g. *"From now on, every typing quiz input should use placeholder='Type here' — apply to all modules."* or *"For the OSAI series only, stop adding autoCheck to sliders."*
- **A bulleted or numbered list of changes** with or without explicit scope.
- **A single one-line instruction.**
- **An uploaded file** (`.md`, `.txt`, `.docx`) containing any of the above — read it with the appropriate tool, then proceed.
- **A mix** of the above in one message.

Whatever the shape, the first job is to **normalise the input into a discrete, numbered list of proposed changes**, each with: (i) *what* should change, (ii) the *scope/breadth* it should apply at, and (iii) the *reason/evidence* if given. Restate this normalised list back to the designer as part of the run (Section 12, Step 0) so they can catch a misread before any file is rewritten.

If any part of the input is genuinely unintelligible or self-contradictory, ask about that specific item rather than guessing — never invent a change the designer did not ask for.

---

## 3. SCOPE / GRANULARITY VOCABULARY

Update Mode reuses the **same five-scope vocabulary as Comparison Mode** (`09_COMPARISON_MODE.md` → Section 7). It accepts the letter form, the full-English form, or plain-English paraphrases, and maps every change to exactly one breadth before editing:

| Scope | Meaning | How Update Mode actions it |
|---|---|---|
| **(a) Series + level** | Every current/future module at this module's level **within its own subject series only** (`[PREFIX]` modules at `[LEVEL_DESCRIPTOR]`) — not other subjects at the same level. | Edit the cited project-knowledge rule and **scope its wording** to `[PREFIX]` modules at `[LEVEL_DESCRIPTOR]`. |
| **(b) Module-series** | Every `[PREFIX]` module, across all year levels. | Edit the cited rule, **scoped to the `[PREFIX]` series**. |
| **(c) Universal** | Every future conversion, regardless of template or series. | Edit the cited rule as a **global rule** (and, if it is a hard constraint, update the CONSTRAINTS list in `00`). **Always a MAJOR change** — see Sections 6–7. |
| **(d) Ignore once** | A bespoke one-off; not to be propagated. | **No project-file change.** Record it in the run summary as "noted, no action" and move on. |
| **(e) Ignore always** | This *category* of change should never be reported by Comparison Mode again. | **Do not change any conversion rule.** Add a new standing exclusion to `09_COMPARISON_MODE.md` → Section 4.1 (Differences NOT to Capture) describing the category. |

`[PREFIX]` and `[LEVEL_DESCRIPTOR]` are resolved exactly as in `09_COMPARISON_MODE.md` → Sections 7.1–7.2 (e.g. `OSAI` from `OSAI201`; `Phase 2 (Years 4–6)` from `template="4-6"`). If the level descriptor for a needed scope is not yet documented, use the year range alone and proceed.

**If a change arrives with no stated or clearly-implied scope**, do not default it. Plain-English breadth cues count as scope (e.g. *"for all modules"* → (c); *"only the TRR series"* → (b); *"just this once"* → (d)). When breadth is genuinely absent for one or more changes, list exactly those items and ask the designer to choose a scope before editing (Section 8). This mirrors the project's standing rule never to guess.

---

## 4. THE CHANGE LEDGER (`12_CHANGE_LEDGER.md`) — CONFLICT & LOCK REGISTRY

Update Mode keeps a **persistent, append-only record of every change it has actioned**, in the single project-knowledge file `12_CHANGE_LEDGER.md`. **Everything stays in-house** — there is no external spreadsheet, export, or manual upkeep for the designer. This ledger is the memory that lets a *later* Update Mode run know what has already been decided — so a new difference report can be checked for conflicts before anything is changed, and so signed-off decisions are protected from being silently overwritten.

The ledger serves three jobs, and is organised into three parts so the conflict-relevant data stays compact as the history grows:

1. **Conflict source** — **Part 1 (Locked Decisions)** is the list Update Mode checks first to detect whether a newly-requested change contradicts a locked decision; **Part 3 (Change History)** is scanned for prior *unlocked* decisions (Section 6).
2. **Lock registry** — **Part 1** records which changes the design authority has approved and **locked**, so they cannot be overridden by any future report (Section 7).
3. **Audit trail** — **Part 3** is the dated history of everything changed, at what scope, from which report, and who approved it. **Part 2** holds changes currently awaiting approval.

### 4.1 How Update Mode uses the ledger every run

- **Read it first.** At the start of every run, read the ledger (it is project knowledge — retrieve it with `project_knowledge_search`; in the repo it is the `12_CHANGE_LEDGER/` folder of parts — Part 1 Locked and Part 2 Pending live in `12A_LEDGER_CORE_AND_LOCKS.md`, the Part 3 history spans the `12x_CHANGE_HISTORY_…` parts). Check Part 1 (Locked) and Part 2 (Pending) in full, and search the Part 3 history parts for prior decisions on the same rule.
- **Append via the brief, last.** Every Update Mode run that actions anything **drafts the new ledger row(s) in exact table format and includes them in the Repo Update Brief** (`11B` → Section 10); the Claude Code session appends them to the **latest** history part (starting a new part first if it exceeds 30 KB, per the repo `CLAUDE.md`) and refreshes that part's timestamp. The ledger is never regenerated in full.

### 4.2 Status lifecycle of a ledger entry

| Status | Meaning | Lives in |
|---|---|---|
| **Implemented** | A non-conflicting change (routine **or** major) that was actioned and is now in effect. No authority sign-off required; collated into the designer's difference report. | Part 3 |
| **Pending approval** | A **report-vs-report conflict** actioned provisionally, awaiting Persephone's resolution (it has been catalogued — Section 7). *(Legacy: the pre-19-June model also used this for any major change awaiting sign-off.)* | Part 2 |
| **Locked** | A major change the design authority approved. **Immutable** — no future report may override it unless the authority explicitly unlocks it first. | Part 1 (+ a history row in Part 3) |
| **Reverted** | A change the design authority rejected (or the designer withdrew/superseded). The edit is undone in the repository via a follow-up Repo Update Brief; the row is kept for audit. | Part 3 |
| **Blocked (conflict)** | A newly-requested change that was **not** actioned because it conflicts with a Locked entry. Logged for audit; requires an unlock decision before it can proceed (Section 6). | Part 3 + Blocked-request log |

### 4.3 What each entry records

Every ledger row carries: a unique **ID** (e.g. `CL-0007`, permanent and sequential — the same ID is used wherever a change appears across parts), the **date**, a one-line **change summary**, the **scope** (a/b/c and resolved breadth), the **affected file(s)/rule(s)**, the **source / intake channel** — exactly one of **finalized difference report** (recorded with its report reference), **direct-typed** (typed straight into an Update Mode message), or **project instruction** (established via the project instructions) — the **classification** (Routine / Major), the **status** (above), and the **authority decision** (approver + date, where applicable). The exact column layouts live in `12_CHANGE_LEDGER.md`.

> **The intake channel is decision-driving, not just descriptive.** Section 6 reads it to decide whether a clash is escalated to the design authority: a conflict is catalogued for Persephone **only** when both the new change and the conflicting prior entry are `finalized difference report`. A clash involving a `direct-typed` or `project instruction` source is never escalated to her — it is blocked (if the prior is locked) or paused for the designer's own confirmation (if not). Always record the channel so a *later* run can apply this rule.

### 4.4 Everything stays in-house — no external store

The whole ledger lives in the `12_CHANGE_LEDGER/` parts inside project knowledge (synced from the `htmlconvertor-kb` repository). There is **no spreadsheet, no export, and no manual step** for the designer to maintain — every Repo Update Brief carries the drafted row(s) and the Claude Code session appends them, so the ledger stays current as a by-product of actioning changes. This is feasible at scale because:

- **Conversion chats never read this file** (only Update Mode does), so its length never affects day-to-day Word-to-HTML conversions.
- **Project knowledge is retrieved, not bulk-loaded, once large enough** — so the file is not sitting in full in ordinary conversations.
- **Conflict-checking depends only on Part 1 (Locked)**, which stays compact; Part 3's growing history is inert audit data.

Part 3 can never become unwieldy: the repo's size guard splits the history into a new `12x_CHANGE_HISTORY_…` part whenever the latest one passes 30 KB (repo `CLAUDE.md`), so growth is absorbed structurally. Old rows are never trimmed or archived; Part 1 is never trimmed. Routine use requires zero manual upkeep.

---

## 5. MAJOR vs ROUTINE CLASSIFICATION

Every actionable change is classified before editing — the class is recorded in the ledger and the per-file change log, and informs how fully the change is documented. **Classification no longer decides whether the design authority is involved**: under the conflict-routing in Sections 6–7, Persephone's sign-off is reserved for **report-vs-report conflicts**. A major change that clashes with nothing is actioned and reported to the designer like any other.

**A change is MAJOR when any of these is true:**

- Its scope is **(c) Universal** (it would become the new standard for every module).
- It is a **structural or design change** — adding/removing/replacing a component or layout, changing grid/wrapper structure, changing a skeleton/`<head>`/header/footer/menu pattern, changing how a whole class of interactives is built, or any change to the look-and-feel rules.
- It **weakens, reverses, or contradicts a CORE PHILOSOPHY or an ABSOLUTE/HARD CONSTRAINT** (these also require the explicit confirmation in Section 8).

**A change is ROUTINE when it is none of the above** — typically a narrow-scope (a)/(b) correction, a small attribute/casing fix, a copy-edit to a rule's wording that doesn't change behaviour broadly, or a purely additive clarification.

**(d)** and **(e)** are neither: (d) actions no rule change; (e) only edits the Comparison Mode exclusions list.

When a change's classification is genuinely borderline, treat it as **Major** (favour the more cautious label and a fuller account in the change log).

---

## 6. CONFLICT CHECK (runs before any file is edited)

This is the safeguard for serious decisions: **before actioning anything, confirm the project has not already decided this question differently.** Run it for every proposed change, and apply extra care to **(c) Universal / "all modules"** changes, which are the highest-stakes.

For each proposed change:

1. **Search the ledger** (`12_CHANGE_LEDGER.md`, Section 4) for any prior entry affecting the **same rule, file, behaviour, or element** — check **Part 1 (Locked Decisions)** first (these can *block* the change), then scan **Part 3 (Change History)** for any prior unlocked decision. Match on the affected file/section/constraint and on the behaviour described, not just on wording.
2. **If a prior entry targets the same thing with the SAME result** → it is already in effect. Note "already in effect — no change needed" and do not duplicate it.
3. **If a prior entry targets the same thing with a DIFFERENT result** → it is a **conflict**. Resolve it by the prior entry's lock state and by the **intake channel** (Section 4.3) of *both* sides:
   - **Prior entry is `Locked`** → **BLOCK.** Do **not** action the new change and do **not** include any edit for it in the Repo Update Brief. Draft a `Blocked (conflict)` ledger row for the brief referencing the locked entry, and surface it prominently to the designer: *this contradicts a locked decision ([ID], approved by [name] on [date]); it cannot be actioned unless the design authority explicitly unlocks that decision first.* (Channel is irrelevant here — a lock blocks regardless of source.)
   - **Both sides arrived via a `finalized difference report`** (and the prior is not locked) → **CATALOG FOR THE DESIGN AUTHORITY.** Do **not** silently flip the decision and do **not** resolve it in-chat. Add the item to the **"Cataloged differences that require approval"** block (Section 7.1), showing the *previously submitted difference* and the *current difference*, and route it to **Persephone** to resolve. Log the new row `Pending approval`. On her decision the surviving difference is `Locked` and the other `Reverted`.
   - **The conflict involves any non-report source on either side** — the prior decision came from a `project instruction` or a `direct-typed` Update Mode message, **or** the new change was typed directly rather than submitted via a finalized difference report (and the prior is not locked) → **PAUSE for the designer's own confirmation.** Show the previous decision vs the new request (old result → new result) and ask whether they intend to **overturn** the earlier decision. Action only on explicit confirmation; if confirmed, the new entry supersedes the old (mark the old row `Reverted — superseded by [new ID]`). This case is **never** escalated to Persephone's approval catalog. Never silently flip-flop a prior decision.
4. **If no prior entry exists** → no conflict; continue to classification and the normal pipeline.

Conflicts are reported to the designer in the run summary as a distinct list (see Section 12), separate from the changes that were actioned.

---

## 7. CONFLICT ESCALATION & LOCKING

Most changes need no sign-off. A change that **clashes with nothing** — whatever its class — is actioned and logged `Implemented`, and is accounted for in the run's per-file change log (Section 16). **No difference report is produced for the designer** (constraint 76). The design authority (Persephone) is involved on exactly one path: when two **finalized difference reports** disagree.

**The escalation path** — a change that arrived via a **finalized difference report** and **conflicts** with a prior decision that **also** arrived via a finalized difference report, where the prior decision is not `Locked` (Section 6):

1. **Action it provisionally** — include the edits in the Repo Update Brief as normal but marked **PROVISIONAL** (so the work is ready), and draft the row for **Part 2 (Pending approval)** with status **`Pending approval`**.
2. **Catalog the conflict** in the **"Cataloged differences that require approval"** block (Section 7.1) — one item per conflicting pair, showing the *previously submitted difference* and the *current difference* — and route it to **Persephone** to resolve. This block is part of the run's output for the designer to forward to her.
3. **On Persephone's decision** (relayed back by the designer in a later message or a short follow-up Update Mode turn):
   - **Current difference wins →** issue a follow-up Repo Update Brief that moves the row into **Part 1 (Locked Decisions)** with status **`Locked`** (record approver + date), adds a corresponding history row in Part 3, and marks the superseded prior decision `Reverted — superseded by [new ID]`. The surviving decision is now immutable; future reports that contradict it hit the Section 6 block.
   - **Prior difference stands →** issue a follow-up Repo Update Brief that **reverts** the provisional edit in the affected parts and records the row in **Part 3** as **`Reverted`**.

> If the team prefers a conflict is **held and not applied until Persephone decides** (rather than applied provisionally), follow that preference instead: leave the edit out of the brief, log the row `Pending approval`, catalog the conflict, and only include the edit in a later brief once the decision comes back. Either way, **a conflicting decision is never `Locked` without Persephone's sign-off.**

**Conflicts that are NOT report-vs-report never reach Persephone.** A clash with a `Locked` decision is **blocked** (Section 6); a clash with a `project instruction` or `direct-typed` decision **pauses for the designer's own confirmation** (Section 6). Neither appears in the approval catalog.

**Unlocking.** A `Locked` change can only be changed later if Persephone explicitly approves unlocking it. When that happens (relayed by the designer), move the row out of **Part 1** and record it in **Part 3** as `Reverted — unlocked by [name] on [date]`, then process the new change normally.

### 7.1 "Cataloged differences that require approval" block

Produce this **only when at least one report-vs-report conflict exists this run** (Section 6). **If there are none, omit the section entirely.**

This is not a forwarded email and carries **no subject line, no salutation, no "major decision" preamble, and no YES/NO voting instruction** — all of those are removed. It opens with a single sentence stating why it exists and who resolves it, then lists each conflicting pair. For each item, **show both the previously submitted difference and the current difference**, and **do not include an "Affects" line.**

```
Cataloged differences that require approval

The difference(s) below were submitted via a finalized difference report and conflict with
a difference previously lodged via a submitted finalized difference report. Because both
sides came through finalized difference reports, they are sent to Persephone to review and
resolve.

1. [Conflict summary]
   • Previously submitted difference (finalized report [prior report ref]): [what the prior
     difference established]
   • Current difference logged for action (finalized report [current report ref]): [the new
     difference being requested]
   • How widely: [(c) every module / structural change to ...]
   • Why it was requested: [rationale]

[...additional conflicting items...]
```

---

---

> **Sections 8 and 9 continue in `11C_UPDATE_MODE_PREFLIGHT_SWEEP.md`** — the pre-flight confirmations and the blast-radius sweep. The section numbering is ONE continuous sequence across `11A`, `11C` and `11B` (§10-16); a reference to "Section 8" or "Section 9" anywhere in this topic means `11C`.
