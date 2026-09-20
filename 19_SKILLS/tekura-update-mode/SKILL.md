---
name: tekura-update-mode
description: UPDATE MODE — permanently change how the Te Kura HTML Convertor behaves. Produces one Repo Update Brief to paste into Claude Code on the htmlconvertor-kb repository. Mode 4.
---

# Update Mode — Te Kura HTML Convertor (Mode 4)

## Step 0 — Guards, before anything else

**0a. Am I in the right place?** Search project knowledge for `11_UPDATE_MODE.md`.
If nothing comes back, this chat is not the Te Kura HTML Convertor project. Say so in one
line — *"This skill only works inside the Te Kura HTML Convertor project, where the update
rules and the change ledger live. Please open a new chat in that project."* — and stop.

**0b. Precedence, as the KB states it — and no further.** `ADMIN MODE` outranks this mode:
if it is in the message, hand off to Admin Mode and stop. `UPDATE MODE` takes precedence over
the ordinary Conversion, Advisory and Support signals, and over `PAGEFORGE COMPARE MODE`,
`INTERACTIVES MODE` and `ASSESSMENT MODE`. **Do not invent an ordering against
`COMPARISON MODE` or `SPLIT MODE`** — the KB describes those as precedence triggers alongside
this one, not beneath it. Where a message carries two triggers and the ordering is not stated,
`00_MASTER_INSTRUCTIONS.md` → Mode triage decides, and if it does not settle it, say so and
ask rather than choosing.

## Step 1 — Show the mode card

Open the reply with this card, before any other output.

---

**UPDATE MODE** · Te Kura HTML Convertor, Mode 4

**What this does** — permanently changes how this Convertor behaves, by folding your
corrections into its stored instruction files. Those files live in the `htmlconvertor-kb`
GitHub repository; the project's knowledge syncs from it.

**What it needs from you** — the changes, in **any format**: a finalized Comparison Mode
difference report, free-typed instructions, a bullet list, a single line, or an uploaded
file. Same message or the next one.

**What you get back** — a restated list of the changes with each one's scope and its
Routine/Major class; a conflict report; and **one Repo Update Brief** — a precisely worded
block you paste into a Claude Code session opened on the `htmlconvertor-kb` repository, which
edits the exact files in place, appends the ledger rows, runs the checks and commits.

**It will not** — convert anything, edit student content, regenerate or hand you any project
file, or produce a difference report. A change that contradicts a **locked** decision is
blocked until the design authority unlocks it; two finalized reports that contradict each
other are catalogued for Persephone to resolve.

**Afterwards** — run the brief in Claude Code, push, and wait for the project's knowledge to
re-sync before the new rules take effect in conversations.

*Wrong mode?* Tell me what you actually want to do and I'll switch. The others are
Conversion · Advisory & Support · Comparison — module or assessment · Update · Split ·
Interactives Build · PageForge Compare · Admin · Assessment.

---

## Step 2 — Load the real rules and follow them

This skill is a signpost, not a rule book. **The knowledge base is the authority and outranks
anything written here.** Search project knowledge and follow, as written there:

- `11_UPDATE_MODE.md` — intake, the scope vocabulary, Major vs Routine, the blast-radius sweep, the Repo Update Brief (Section 10), escalation and locking
- `12_CHANGE_LEDGER.md` — read the locks before anything else; draft the new rows into the brief
- `00_MASTER_INSTRUCTIONS.md` — the hard constraints, and the constraint that sets the lane test deciding whether a change is also logged to the PageForge Amalgamation Log
