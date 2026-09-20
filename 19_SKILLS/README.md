# 19_SKILLS — the operating modes as Claude Skills

Each of the Convertor's nine operating modes (`00_MASTER_INSTRUCTIONS/00A2_OPERATING_MODES.md`)
also exists here as a **Claude Skill**. There are **ten** skills for those nine modes, because
Mode 3 has two procedures that behave quite differently and are worth telling apart by name —
see *The two comparison skills* below. This folder holds the skill source; `build_skills.sh`
turns each sub-folder into the `.zip` that Claude.ai's uploader accepts, in `dist/`.

## What a skill here does and does not do

A skill in this folder is a **signpost, not a rule book**. It does three things:

1. **Guards** — refuses to run outside the HTML Convertor project, and checks mode precedence
   (`ADMIN MODE` beats everything; `PAGEFORGE COMPARE` before `COMPARISON`, and so on) before
   claiming the turn.
2. **Prints a mode card** — a short plain-English panel naming the mode, what it does, what it
   needs, what comes back, and what it will not do, so the designer can tell immediately
   whether they landed in the right mode. **Admin Mode is the one exception:** `17` Section 10
   makes its displayed output a closed list, so that skill carries the card's substance inside
   the opening line or two Section 10 already allows, and prints no separate panel.
3. **Points at the knowledge base** — names the KB files that own the mode's real rules.

**The knowledge base remains the single source of truth.** Every skill says so in its own
body. Nothing in this folder may restate a conversion rule, a constraint or a markup pattern:
that is how the two copies drift apart, which is the failure this repo exists to prevent. If a
rule changes, the KB part file changes and the skills are untouched.

That line is a rule, not an aspiration, and it is easy to break by accident. Where a skill
needs to stop a known mistake, it **names the rule and points at the file** — *"read `18A`'s
skeleton section before emitting anything; take the corrections from there, never from
memory"* — rather than listing the corrections. A number, a hostname, a class name or a count
copied into a `SKILL.md` is a defect waiting for the day the KB changes and this folder does
not. The mode cards describe what a mode is **for**, in the designer's language; they are not
specifications.

## Why the typed trigger phrases still work

There are **two** ways a skill starts in a claude.ai chat, and the skills here are built for both.

**Typing `/`** opens a picker in the message box that filters as you type and shows each matching
skill's name and its full description. Because every skill here is named `tekura-…`, typing
`/tekura` lists all ten together. This is why the `description` field is written for a human to
read at the moment of choosing, not only for Claude to match on.

**Typing anything else** selects a skill automatically, by matching the request against those same
descriptions. Each trigger-phrase mode carries its phrase — `COMPARISON MODE`, `UPDATE MODE`,
`SPLIT MODE`, `INTERACTIVES MODE`, `PAGEFORGE COMPARE MODE`, `ADMIN MODE`, `ASSESSMENT MODE` —
verbatim in its description, so typing the phrase still works exactly as before.

The mode triage in `_project_instructions_.md` and `00A2_OPERATING_MODES.md` is **unchanged and
still authoritative**. Even with every skill switched off, typing a trigger phrase works. The
skills are an additional way in, never a replacement.

## The two comparison skills

`COMPARISON MODE` is **one** mode in the knowledge base with **two** procedures behind it, and
the KB decides which runs from the evidence in the chat, never by asking (`09A` §1, `18C`
§10.1). They are not variations on a theme — they behave differently enough that landing in the
wrong one wastes a run:

| | `tekura-module-comparison-mode` (`09`) | `tekura-assessment-comparison-mode` (`18C`) |
|---|---|---|
| Passes | Two: initial report → designer scopes each difference → finalized report | One: the finalized report, immediately |
| Scope question | Yes — five options, `number-letter` reply | None. Every difference is Universal by rule |
| Why | Modules differ by year level, subject, series and module, so a correction has to be scoped | Every assessment shares one template, so there is nothing to scope against |
| Report goes to | Whoever actions changes, via Update or Admin Mode | Gavin |

Splitting them into two skills is what makes them tellable apart in the skills list. **It does
not split the mode**: both skills point at the same documented trigger, and the KB's file-based
routing is untouched. What the split adds is a safeguard, in each skill's Step 0:

- **A bare `COMPARISON MODE`** — the designer asked for "the comparison", not for a particular
  half. Whichever skill fires, it reads the evidence and, if it is the wrong half, **switches
  silently** and shows the other card. The old behaviour, unchanged.
- **A deliberately named variant** — the designer typed this skill's name or a
  `/module-comparison-mode` style shortcut — **and the evidence disagrees** → the skill
  **stops and warns** rather than running, names the evidence, explains in one short paragraph
  why the other one is probably right, and waits. It never silently overrides a deliberate
  choice, and it never silently obeys one that looks mistaken.
- **A mixed upload** — module pages and assessment pages together — is not a mistake:
  `18C` §10.1 says run both procedures and produce two reports. Neither skill treats it as one.

## The two hard limits Claude.ai enforces on upload

- `name` — 64 characters max, and it **must match the folder name exactly**.
- `description` — **200 characters max**. This is the one that bites: a longer description is
  rejected at upload with a generic error. `tools/check_kb.py` checks both.

## Changing a mode card

1. Edit the `SKILL.md` in the relevant sub-folder.
2. Run `python3 tools/check_kb.py` — it validates the frontmatter and the 200-character limit.
3. Run `bash 19_SKILLS/build_skills.sh` to rebuild `dist/`.
4. Commit. Then re-upload that one `.zip` — replacing a provisioned skill means deleting the
   old one and uploading the new, at **Organization settings → Skills**.

Skills do **not** sync from this repository the way project knowledge does. The repo is the
source of record and the audit trail; uploading is a manual step. `ROLLOUT.md` has the
click-by-click instructions.

## The nine skills

| Skill folder | Mode | Typed trigger |
|---|---|---|
| `tekura-conversion-mode` | 1 — Conversion | *(none — content source upload)* |
| `tekura-advisory-support-mode` | 2 — Advisory & Support | *(none — a question)* |
| `tekura-module-comparison-mode` | 3 — Comparison, `09` module procedure | `COMPARISON MODE` |
| `tekura-assessment-comparison-mode` | 3 — Comparison, `18C` assessment procedure | `COMPARISON MODE` |
| `tekura-update-mode` | 4 — Update | `UPDATE MODE` |
| `tekura-split-mode` | 5 — Split | `SPLIT MODE` |
| `tekura-interactives-mode` | 6 — Interactives Build | `INTERACTIVES MODE` |
| `tekura-pageforge-compare-mode` | 7 — PageForge Compare | `PAGEFORGE COMPARE MODE` |
| `tekura-admin-mode` | 8 — Admin | `ADMIN MODE` |
| `tekura-assessment-mode` | 9 — Assessment | `ASSESSMENT MODE` |

This folder is deliberately **excluded from the KB content checks** in `tools/check_kb.py`: a
`SKILL.md` opens with YAML frontmatter and cannot carry the `> **Last updated:**` stamp or the
`KB-PART-BODY-START` sentinel that every KB part file needs. A separate, lighter check in the
same script validates the skills instead.
