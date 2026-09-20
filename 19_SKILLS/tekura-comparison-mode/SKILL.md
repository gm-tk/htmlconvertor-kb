---
name: tekura-comparison-mode
description: COMPARISON MODE — compare the designer's refined Te Kura module HTML against what this project generated and report the differences. Not PAGEFORGE COMPARISON MODE, which is Mode 7.
---

# Comparison Mode — Te Kura HTML Convertor (Mode 3)

## Step 0 — Guards, before anything else

**0a. Am I in the right place?** Search project knowledge for `09_COMPARISON_MODE.md`.
If nothing comes back, this chat is not the Te Kura HTML Convertor project. Say so in one
line — *"This skill only works inside the Te Kura HTML Convertor project, where the
comparison rules live. Please open a new chat in that project."* — and stop.

**0b. Precedence, as `00A2` → Mode triage and `09A` state it:**

- `ADMIN MODE` present → **Admin Mode**, always. Hand off and stop.
- The phrase preceded by `PAGEFORGE` — `PAGEFORGE COMPARE MODE`, `PAGEFORGE COMPARISON MODE`
  or `PAGEFORGE COMPARE` → **PageForge Compare Mode (Mode 7)**, not this one.
  `PAGEFORGE COMPARISON MODE` contains the substring `COMPARISON MODE`; the leading word
  `PAGEFORGE` is the discriminator. Hand off and stop.
- Otherwise this trigger takes precedence over every other mode signal.

If a message makes the ordering genuinely unclear, `00_MASTER_INSTRUCTIONS.md` → Mode triage
decides it, not this skill.

**0c. Which variant?** Decided by the uploaded files, never by asking. A page carrying
`class="alertAssessment"` or `template="NCEA"` in a chat that ran Assessment Mode is the
**assessment variant** (`18C`). A module page is ordinary Comparison Mode (`09`).

**0d. Missing context — recover before you refuse.** This mode compares against output this
project produced earlier. If the original conversion turn is not in this chat, follow `09A`
§2 "Handling missing context" as written: try to recover it first, then ask the designer to
re-supply the specific missing piece, and where an input still cannot be had, use that input's
documented fallback. Do not turn a documented recovery into a hard stop.

## Step 1 — Show the mode card

Open the reply with this card, before any other output.

---

**COMPARISON MODE** · Te Kura HTML Convertor, Mode 3

**What this does** — compares the HTML you refined by hand against the HTML this project
generated, and reports the differences that the project's own stored rules could be changed to
prevent. Differences that came from the supplied template or reference file are dropped
silently, because no rule change can alter what an external template ships.

**What it needs from you** — your finished, refined HTML files, uploaded into the **original
conversion chat**.

**What you get back** — two passes. **Pass 1** is a streamlined report: every qualifying
difference as original raw content → originally generated code → your refined code, numbered
straight through, with the five scope options listed once at the top. You reply with
number-letter pairings such as `1-A, 2-C`. **Pass 2** is the finalized detailed report, each
included difference gaining the rule it came from and its scope written out in full.

**It will not** — convert anything, edit student content, or change the project's own rule
files. Acting on the report is Update Mode (Mode 4), in a separate conversation.

*Wrong mode?* Tell me what you actually want to do and I'll switch. The nine modes are
Conversion · Advisory & Support · Comparison · Update · Split · Interactives Build ·
PageForge Compare · Admin · Assessment.

---

## Step 2 — Load the real rules and follow them

This skill is a signpost, not a rule book. **The knowledge base is the authority and outranks
anything written here.** Search project knowledge and follow, as written there:

- `09_COMPARISON_MODE.md` — the trigger, the inputs, handling missing context, the exclusions gate, the report architecture and what each pass contains, the IMPORTANT scope block
- `18_ASSESSMENT_MODE.md` → `18C` — only if this is the assessment variant
- `00_MASTER_INSTRUCTIONS.md` — the hard constraints, which still apply

## Step 3 — The one thing never to do in this mode

**Never mention, offer or ask about PageForge Compare Mode** at the end of a Comparison Mode
run, or anywhere else. That mode starts only when the developer types its phrase, because only
some developers are testing PageForge.
