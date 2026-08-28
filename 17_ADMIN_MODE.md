> **Last updated:** Friday, 28th August, 2026 1:30 PM

# 17 — Admin Mode (Mode 8)

> **When to load:** Whenever a message contains the trigger phrase **`ADMIN MODE`** (case-insensitive). This is **Mode 8 — Admin** (see `00_MASTER_INSTRUCTIONS.md` → Operating Modes). **`ADMIN MODE` is the project's highest-precedence trigger** — it outranks `PAGEFORGE COMPARE MODE`, `COMPARISON MODE`, `UPDATE MODE`, `SPLIT MODE` and `INTERACTIVES MODE`. Load this file together with `12_CHANGE_LEDGER.md` (the ledger row and, for a front-facing change, the PageForge Amalgamation Log) and `11_UPDATE_MODE.md` → Sections 9–10, 13 (the blast-radius sweep, the Repo Update Brief format and the timestamp convention, which Admin Mode reuses unchanged).

---

## PURPOSE

Admin Mode is **Update Mode without the approval gate.**

Update Mode (`11_UPDATE_MODE.md`) exists for changes that arrive from a **designer** — usually as a finalized Comparison Mode difference report — and it is deliberately cautious: it asks for a missing scope, it pauses before overturning a prior decision, it blocks anything that contradicts a locked decision, and it escalates report-vs-report disagreements to the design authority. That caution is correct, because a designer's judgement on one module can be wrong, and the ledger exists so a later contradiction is re-flagged rather than silently absorbed.

**Admin Mode is for changes that carry their authority with them.** A change submitted through `ADMIN MODE` comes from **Gavin — who builds and owns this project's instruction files — or from the lead designer.** It is therefore **already approved before it arrives**: it is actioned without asking, at the scope stated (or universally if none is stated), and it **overrides any conflicting decision already on record**, whatever that decision's source and whether or not it is locked.

Admin Mode changes **nothing about how the edits are carried out**. Like Update Mode it produces ONE **Repo Update Brief** for a Claude Code session on the `htmlconvertor-kb` repository (`11_UPDATE_MODE.md` → Section 10), it obeys the repo's maintenance ritual, and it **always writes a ledger row**. What it removes is the *deliberation* — the scope questions, the guardrail confirmations, the conflict pause, and the escalation path.

In short:

- **Update Mode** = *"A designer has proposed this. Check it, question it where it is unclear, and escalate it where it disagrees with something already decided."*
- **Admin Mode** = *"An authorised person has decided this. Apply it everywhere it is scoped to apply, override whatever it contradicts, record what was overridden, and tell me what you did."*

---

## 1. THE TRIGGER AND ITS PRECEDENCE

Admin Mode is entered when a message contains the literal phrase **`ADMIN MODE`** (case-insensitive) anywhere in the text.

**It is checked FIRST, before every other trigger.** If a message contains `ADMIN MODE` it is an Admin Mode run, even if it also contains `UPDATE MODE`, `COMPARISON MODE`, `PAGEFORGE COMPARE MODE`, `SPLIT MODE` or `INTERACTIVES MODE`, and even if files are attached. A message carrying both `ADMIN MODE` and `UPDATE MODE` is an **Admin Mode** run — the authorised instruction wins.

The change to action may arrive **in the same message** as the trigger or **in the next message**, exactly as in Update Mode. If `ADMIN MODE` arrives with no accompanying change, say Admin Mode is active and ask for the change; wait.

**Typing the phrase is the assertion of authority.** The Convertor does not verify who is speaking, does not ask "are you authorised?", and does not ask anyone to confirm they meant it. Access to the trigger is controlled by the team, not by this project.

---

## 2. ACCEPTED INPUT

Admin Mode accepts a change in **any format**, exactly as Update Mode does (`11_UPDATE_MODE.md` → Section 2): a typed instruction, a bullet list, a one-liner, a pasted note, or an uploaded file. Normalise the input into a discrete, numbered list of changes and restate that list back — the restatement is a comprehension check, not a request for approval, and the run continues in the same turn.

**A finalized Comparison Mode difference report belongs in Update Mode, not here.** Update Mode remains the mode for actioning a designer's difference report, with its conflict routing and its escalation path intact. Admin Mode is for a change an authorised person has already decided. If a finalized difference report is submitted under `ADMIN MODE`, action it as an Admin Mode change (the trigger governs) but say plainly in the run summary that a difference report would normally be routed through Update Mode, so the designer can correct the routing next time if that was a mistake.

**The one question Admin Mode may still ask** is a question of *comprehension*, never of approval: if an instruction is genuinely unintelligible, or names a target that does not exist, or is internally self-contradictory, ask about that specific item rather than guessing. Never invent a change. Everything else proceeds without asking.

---

## 3. SCOPE — UNIVERSAL BY DEFAULT

Admin Mode uses the **same five-scope vocabulary** as Update Mode and Comparison Mode (`11_UPDATE_MODE.md` → Section 3): (a) series + level, (b) module-series, (c) universal, (d) ignore once, (e) ignore always.

**The default is different, and this is deliberate.**

| | Update Mode | Admin Mode |
|---|---|---|
| Change arrives with a stated or clearly-implied scope | Use it | Use it |
| Change arrives with **no** scope | **Ask** — never default | **Default to (c) Universal** and say so in the run summary |

An Admin Mode change applies **everywhere** unless the message names a narrower cohort. A narrower scope is recognised from any of: a subject or series name, a module code or code prefix, a year level or template band, a named cohort or family documented in `14_SUBJECT_GLOBAL_PARAMETERS.md`, or a phrase such as *"for the Languages modules only"* / *"just the FUNdamentals templates"*. When one is named, scope the rule's wording to it exactly as Update Mode would.

This carve-out **overrides** Update Mode's standing rule that an unscoped change is never defaulted (`11_UPDATE_MODE.md` → Section 3, and the pre-flight in `11C` → Section 8.1). It applies **only** to Admin Mode runs.

---

## 4. THE OVERRIDE RULE — ADMIN MODE WINS

Admin Mode **still runs the conflict check** (`11_UPDATE_MODE.md` → Section 6) — but it runs it to *record* what is being overridden, never to decide whether to proceed. The outcome is always: the Admin Mode change is applied.

For each proposed change, search the ledger for a prior entry on the same rule, file, behaviour or element, then:

| What the conflict check finds | Update Mode does | **Admin Mode does** |
|---|---|---|
| No prior entry | Proceed | Proceed |
| Prior entry, **same** result | "Already in effect" — drop | "Already in effect" — drop, and say so |
| Prior entry from a `direct-typed` or `project instruction` source, different result | **Pause** for the designer to confirm | **Override.** Apply the new change; mark the prior row `Reverted — superseded by [new ID] (ADMIN MODE)` |
| Prior entry from a **finalized difference report**, different result | **Catalog for Persephone**; log `Pending approval` | **Override.** Apply; mark the prior row `Reverted — superseded by [new ID] (ADMIN MODE)`. **Never escalated to Persephone** |
| Prior entry is **`Locked`** | **BLOCK** — cannot proceed without an unlock | **Override.** Apply; move the locked row out of Part 1 and record it in Part 3 as `Reverted — superseded by [new ID] (ADMIN MODE)`. **No unlock step is required** |
| Prior entry is a previous **Admin Mode** decision | — | **Override.** The newest Admin Mode instruction always wins |
| Two changes **within the same Admin Mode run** contradict each other | — | **Ask** — this is a comprehension question (Section 2), not an approval question |

**Overriding is never silent.** Every override is stated in the run summary — *"this replaces `CL-nnnn` (…), which said …"* — and both rows are written: the new one, and the reversal on the old one. The point of the ledger is that the history stays legible, so an override that is not recorded defeats the purpose of applying it through this mode at all.

**Admin Mode never escalates to the design authority.** The "Cataloged differences that require approval" block (`11_UPDATE_MODE.md` → Section 7.1) is **never produced by an Admin Mode run**, whatever the conflict. Persephone's approval path exists to resolve two designers' reports disagreeing; an Admin Mode change is already the answer to that question.

### 4.1 An Admin Mode decision is locked against ordinary Update Mode

Once actioned, every Admin Mode change is recorded in **Part 1 (Locked Decisions)** of the ledger with the status **`Locked (admin)`** and is treated by `11_UPDATE_MODE.md` → Section 6 exactly like any other locked row: a later **Update Mode** change that contradicts it is **`Blocked (conflict)`** and is not actioned.

The difference from an ordinary lock is how it is released: a `Locked (admin)` row does **not** need Persephone's unlock. It is superseded by **another `ADMIN MODE` message**, which overrides it under Section 4 without ceremony. A designer whose Update Mode change is blocked by a `Locked (admin)` row is told plainly that the decision came in through Admin Mode and that changing it needs an Admin Mode instruction from Gavin or the lead designer.

---

## 5. THE TWO LANES — WHAT GETS LOGGED WHERE

This is the distinction that decides a change's paperwork. **Every** Admin Mode change gets a ledger row (Section 6). Only a **front-facing** change additionally gets an entry in the **PageForge Amalgamation Log** (`12_CHANGE_LEDGER/12G_PAGEFORGE_AMALGAMATION_LOG.md`).

### 5.1 The test

> **Would a developer comparing two generated modules — one built before the change, one after, from the same Writers Template — see any difference in the HTML or CSS?**

- **YES → Lane 2 (front-facing).** Ledger row **plus** a PageForge Amalgamation Log entry.
- **NO → Lane 1 (mechanism).** Ledger row **only**.
- **Genuinely borderline → treat it as Lane 2.** An over-logged entry costs one block in a log; a missed one costs PageForge a silent divergence that nobody discovers until a module is rebuilt.

### 5.2 Lane 1 — mechanism / internal (ledger row only)

Changes to **how this project operates**, which leave the generated HTML byte-for-byte unchanged:

- Mode definitions, triage, trigger phrases, precedence.
- What the Convertor says in the chat — progress messages, verification reporting, summaries, how it phrases things to a designer (**constraint 88** — the Designer-Facing Output Policy — is the worked example: it changed only what is *said*, never what is *built*).
- How the knowledge base itself is structured, maintained, indexed, split or committed.
- The intake, conflict-checking, ledger and approval machinery — including this file.
- Which files to load for which task; how a mode gathers its inputs.

These are invisible to PageForge because PageForge does not have a chat, a ledger, or a mode. **They are not logged to `12G`.**

### 5.3 Lane 2 — front-facing (ledger row + `12G` entry)

Anything that changes **what the outputted module looks like or contains**:

- The **HTML produced** — which element a writer tag becomes, what content appears, what is omitted, what is added.
- The **hierarchy and code structure** — nesting, wrappers, grid/column structure, page scaffold, head/header/footer/menu patterns, page boundaries and page-to-file mapping.
- **Syntax, classes, IDs and attributes** — class names, id conventions, data attributes, answer-key attributes, `autoCheck` and similar defaults.
- **Styles and layout** — any CSS-affecting rule, any change to how content is arranged on the page.
- **How writer content is conveyed** — titles and headings, red flags and designer-facing notes rendered into the page, acknowledgements format and placement, image output modes, alt-text rules, interactive build rules, subject global parameters that alter output.

**Why this lane exists:** PageForge (the standalone HTML Generator, `pageforge-site` / `CONVERTER_V2`) is being developed to do automatically what this project does by instruction. Every front-facing decision made here is a decision PageForge will eventually have to mirror. The log is not a request to change PageForge now — nothing in an Admin Mode run touches PageForge's code, and this project never does. It is the **ordered, implementable record** so that, when PageForge development next picks the thread up, the full history of front-facing decisions is in one place and in one form, rather than scattered through the ledger's audit prose.

**Update Mode obeys the same lane test.** The amalgamation log is not an Admin Mode artefact — it is the project's front-facing decision record, and an Update Mode change that passes the Section 5.1 test is logged to `12G` in exactly the same way (`11_UPDATE_MODE.md` → Sections 4, 9, 10).

---

## 6. THE LEDGER ROW

Every Admin Mode run drafts its ledger row(s) into the Repo Update Brief like any other change (`11_UPDATE_MODE.md` → Section 4). The columns are unchanged; three of the values are Admin-specific:

- **Source (intake channel):** `ADMIN MODE (authorised)` — optionally naming the person, e.g. `ADMIN MODE (authorised — Gavin)`. This is a fourth intake channel alongside `Finalized difference report`, `Direct-typed (Update Mode)` and `Project instruction`, and it is what a later run reads to know that a decision may only be overridden by another Admin Mode message.
- **Class:** Routine or Major, judged exactly as in `11_UPDATE_MODE.md` → Section 5. Classification is descriptive here — it changes no approval, because there is no approval.
- **Status:** `Locked (admin)`. The row is written to **Part 1 (Locked Decisions)** and to the **Part 3** history. Where the change overrides something, the superseded row is updated to `Reverted — superseded by [new ID] (ADMIN MODE)`, and a `Locked` row being overridden leaves Part 1.

For a **Lane 2** change, the run additionally drafts the `12G` entry (Section 5.3, format in `12G`'s own header) into the same Repo Update Brief.

---

## 7. WHAT ADMIN MODE STILL DOES

Removing the approval gate removes questions — not discipline. Every one of these still applies, unchanged:

1. **The blast-radius sweep** (`11_UPDATE_MODE.md` → Section 9). Find *every* part file that must change so the rule is consistent and does not recur in a stale form: the owning rule, the CONSTRAINTS list in `00`, the file-load map, every cross-reference, `09_COMPARISON_MODE.md` for an (e) exclusion, the ledger, and `_project_instructions_.md` where mode triage or output expectations move. **Search, do not recall.**
2. **Sweeping out retired wording** (`11C` → Section 8.7). A change that supersedes a rule is not finished until the old phrasing is removed or unmistakably marked retired.
3. **The Repo Update Brief** (`11_UPDATE_MODE.md` → Section 10) — precise, finished old→new wording per part file. Never "update the rule accordingly". No project file is ever regenerated or presented for download.
4. **The repo maintenance ritual** — edit parts in place, refresh each touched part's `Last updated` stamp (Section 13 format), update `INDEX.md`, run `python3 tools/check_kb.py`, commit. Admin authority does not exempt a change from the guard.
5. **The `_project_instructions_.md` re-paste reminder** when that file is a target — it does not sync from the repository.
6. **A full account in the run summary** (Section 10).

## 8. WHAT ADMIN MODE DOES NOT DO

- It does **not** convert modules, build interactives, produce difference reports, or edit student-facing content — ever.
- It does **not** ask for approval, ask for a missing scope, ask the designer to confirm a guardrail change, or pause on a conflict.
- It does **not** produce the "Cataloged differences that require approval" block, and never routes anything to Persephone (Section 4).
- It does **not** produce a finalized difference report for the designer (constraint 76 applies here exactly as it does to Update Mode).
- It does **not** skip the ledger. There is no such thing as an unrecorded Admin Mode change — the ledger is what lets a later run know the decision exists.
- It does **not** log a Lane 1 mechanism change to the PageForge Amalgamation Log (Section 5.2).
- It does **not** edit PageForge's own code. `pageforge-site` and `CONVERTER_V2` are a separate project; this project only ever records what PageForge will need to mirror.
- It does **not** regenerate whole files, and it does **not** bypass `check_kb.py`.

---

## 9. WORKFLOW (pseudo-code)

```
FUNCTION admin_mode(authorised_input):

    # ── STEP 0: INTAKE ──
    CONFIRM the ADMIN MODE trigger is present  (it outranks every other trigger)
    GATHER the change(s) — this or the next message, any format
        IF none → say Admin Mode is active; ASK for the change; STOP until received
    READ 12_CHANGE_LEDGER: Part 1 (Locked) in full, scan Part 3 for prior decisions
    NORMALISE into a numbered list; RESTATE it (comprehension, not approval — do not stop)
    IF an item is unintelligible / targets nothing that exists / self-contradictory
        → ASK about that item only; everything else continues

    # ── STEP 1: SCOPE ──
    FOR EACH change:
        IF a cohort / series / module code / year level / subject is named → scope to it
        ELSE                                                              → (c) UNIVERSAL   # Section 3
        STATE the resolved scope in the run summary

    # ── STEP 2: CONFLICT CHECK — TO RECORD, NOT TO DECIDE ──   # Section 4
    FOR EACH change:
        SEARCH the ledger for a prior entry on the same rule / behaviour
        SAME result       → "already in effect"; drop
        DIFFERENT result  → OVERRIDE regardless of source or lock state
                            RECORD: prior row → 'Reverted — superseded by [new ID] (ADMIN MODE)'
                            IF the prior row was Locked → it leaves Part 1
                            NEVER catalog for Persephone; NEVER pause
        none              → continue

    # ── STEP 3: CLASSIFY THE LANE ──                            # Section 5
    FOR EACH change:
        ASK: would the generated HTML/CSS differ before vs after?
        YES or BORDERLINE → LANE 2 (front-facing): ledger row + 12G entry
        NO                → LANE 1 (mechanism):    ledger row only
        ALSO classify Routine / Major for the ledger row (descriptive only)

    # ── STEP 4: BLAST-RADIUS SWEEP ──                           # 11 → Section 9
    FOR EACH change: SEARCH + literal scan; BUILD the full set of affected part files
        INCLUDE the retired-wording sweep (11C → 8.7)

    # ── STEP 5: DRAFT ──
    FOR EACH change: draft the precise old→new edit for every affected part
    DRAFT the ledger row(s): Source = 'ADMIN MODE (authorised)', Status = 'Locked (admin)',
        written to Part 1 AND the Part 3 history; plus every supersession row
    FOR EACH Lane 2 change: DRAFT the 12G amalgamation entry
    SWEEP for stale statements / contradictions / dangling cross-references; draft those too

    # ── STEP 6: DELIVER ──
    OUTPUT ONE Repo Update Brief (11 → Section 10) as a single fenced block
    WRITE the run summary (Section 10): what changed, at what scope, what it overrode,
        which lane each change fell in, and what the designer must do next
    # NO approval request, NO Persephone catalog, NO difference report
```

---

## 10. OUTPUT EXPECTATION

A completed Admin Mode run delivers:

1. **The restated change list** — each change as understood, with its **resolved scope** (and, where the scope was defaulted, the words *"no scope was given, so this applies universally"*), and its Routine/Major class.
2. **The override account** — for every change that contradicted something on record: the prior decision's ID, what it said, and the plain statement that the Admin Mode change replaces it. If nothing was overridden, one line saying so.
3. **The lane for each change** — mechanism (ledger only) or front-facing (ledger + PageForge Amalgamation Log), with a one-line reason.
4. **ONE Repo Update Brief** for the Claude Code session on the `htmlconvertor-kb` repository — numbered precise edits with granular part paths, the drafted ledger row(s) including supersessions, any `12G` entries, the standing repo-ritual block, and the `_project_instructions_.md` re-paste reminder where applicable.
5. **A per-change log** — which part files each edit targets, what changes, and why.
6. **A reminder** to run the brief in Claude Code, commit and push, and wait for the project's GitHub knowledge sync before relying on the new rule in a conversion.

**No approval request, no conflict catalog, no difference report, no regenerated files.** An authorised instruction in, a precise brief and a complete account of what it displaced out.

---

## 11. RELATIONSHIP TO THE OTHER MODES

- **Update Mode (`11`) is unchanged** for everything it already did. A designer's finalized difference report still runs through Update Mode, with the scope questions, the conflict pause, the lock block and the Persephone escalation all intact. Admin Mode does not replace it — it sits above it.
- **Comparison Mode (`09`) hands off to Update Mode**, not to Admin Mode.
- **Conversion / Split / Interactives / Support / Advisory** are untouched. Admin Mode never converts and never emits module HTML.
- **PageForge Compare Mode (`16`)** reports PageForge's faults *to Gavin*. The PageForge Amalgamation Log (`12G`) is the other half of that relationship: Mode 7 says what PageForge got wrong on one module; the log says what PageForge must be taught in general.
