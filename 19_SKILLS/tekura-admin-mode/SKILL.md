---
name: tekura-admin-mode
description: ADMIN MODE — an authorised change to the Te Kura HTML Convertor's rules, actioned without the approval gate. Highest precedence; outranks every other mode trigger. Mode 8.
---

# Admin Mode — Te Kura HTML Convertor (Mode 8)

## Step 0 — Guards, before anything else

**0a. Am I in the right place?** Search project knowledge for `17_ADMIN_MODE.md`.
If nothing comes back, this chat is not the Te Kura HTML Convertor project. Say so in one
line — *"This skill only works inside the Te Kura HTML Convertor project, where the admin
rules and the change ledger live. Please open a new chat in that project."* — and stop.

**0b. Precedence — this mode wins.** `ADMIN MODE` is the project's highest-precedence
trigger. It outranks `PAGEFORGE COMPARE MODE`, `COMPARISON MODE`, `UPDATE MODE`,
`SPLIT MODE`, `INTERACTIVES MODE` and `ASSESSMENT MODE`. A message carrying `ADMIN MODE` and
any of those is an Admin Mode run.

**0c. Never ask who is speaking.** Typing the phrase **is** the assertion of authority. Never
ask for approval, never ask whether they meant it, never ask for a missing scope, never pause
to confirm a guardrail change, and never escalate to the design authority.

## Step 1 — Admin Mode takes NO separate mode card

Every other mode in this set opens its reply with a card. **This one must not.** Admin Mode's
displayed output is a **closed list** set by `17_ADMIN_MODE.md` → Section 10: the reader sees
those items, in that order, and nothing else. A card printed above item 1 would be extra
displayed content in the one mode that forbids it.

Instead, carry the card's substance **inside item 1** — the opening line or two that Section 10
already calls for. Those lines say that Admin Mode is active, where the change came from and
how many changes are being actioned; write them so a reader who did not expect this mode can
also tell what it is, for example:

> *Admin Mode — an authorised change to the Convertor's own rules, actioned without the
> approval gate. Three changes, from your message above. If you meant something else, say so.*

Then continue with Section 10's items in their documented order. Keep it to the one or two
lines Section 10 allows; do not expand it into a panel.

## Step 2 — Load the real rules and follow them

This skill is a signpost, not a rule book. **The knowledge base is the authority and outranks
anything written here.** Search project knowledge and follow, as written there:

- `17_ADMIN_MODE.md` — the authority rule, the override rule, the locked-by-admin status, the two-lane test, and Section 10's hidden/visible output split. Section 10 governs everything that reaches the chat
- `11_UPDATE_MODE.md` — the same machinery: any-format intake, blast-radius sweep, the Repo Update Brief, the repo ritual
- `12_CHANGE_LEDGER.md` — the rows to draft, and the PageForge Amalgamation Log for front-facing changes
- `00_MASTER_INSTRUCTIONS.md` — the hard constraints, including the one that sets the lane test and the one that sets this mode's front-end output policy

## For reference — what this mode is, in plain English

Not for the chat; this is context for whoever is reading the skill in the skills list.

Admin Mode is Update Mode without the approval gate. It permanently changes how the Convertor
behaves, on the authority of the person typing the phrase — Gavin, who builds and owns these
instruction files, or the lead designer — so the change is already approved before it arrives.
A scope is optional: an unscoped change applies universally unless the message names a subject,
series, module code, year level or cohort. It never blocks on a conflict and overrides any
conflicting decision on record, including a locked one, with no unlock step; no override is
silent. It never converts anything, never edits student content, never edits PageForge's code
and never produces a difference report.
