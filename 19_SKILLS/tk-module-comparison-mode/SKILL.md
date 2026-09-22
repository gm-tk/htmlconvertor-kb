---
name: tk-module-comparison-mode
description: MODULE COMPARISON MODE — IMPORTANT! This will generate an initial document that you use to let Claude know the scope for each change to generate the final document to send to Gavin!
---

# Module Comparison Mode — Te Kura HTML Convertor (Mode 3, the `09` module variant)

One documented trigger, two procedures. `COMPARISON MODE` is a **single mode** in the
knowledge base; it runs the **module** procedure (`09`) or the **assessment** procedure
(`18C`) depending on the evidence. This skill is the module half. Its twin is
`tk-assessment-comparison-mode`. **The KB's routing rule is unchanged** — the files
decide, never a question.

## Step 0 — Guards, before anything else

**0a. Am I in the right place?** Search project knowledge for `09_COMPARISON_MODE.md` and
`18_ASSESSMENT_MODE.md` → `18C`. If nothing comes back, this chat is not the Te Kura HTML
Convertor project. Say so in one line — *"This skill only works inside the Te Kura HTML
Convertor project, where the comparison rules live. Please open a new chat in that project."*
— and stop.

**0b. Precedence.** `ADMIN MODE` present → **Admin Mode**, always; hand off and stop. The
phrase preceded by `PAGEFORGE` → **PageForge Compare Mode (Mode 7)**; `PAGEFORGE COMPARISON
MODE` contains the substring `COMPARISON MODE`, and the leading word `PAGEFORGE` is the
discriminator. Hand off and stop. Otherwise `09A` §1 says this trigger takes precedence over
every other mode signal. **One point the KB is not uniform on:** `18C` §10.1 adds that
`UPDATE MODE` wins if present, while `09A` §1 does not name it. If a message carries both
`COMPARISON MODE` and `UPDATE MODE`, follow `00_MASTER_INSTRUCTIONS.md` → Mode triage; do not
settle it from this skill.

**0c. What kind of page is each upload?** Apply the test in `18C` §10.1 — it names the exact
markers that identify an assessment page, and says a page that is not one **is a module page,
whatever this chat previously ran**. Route **each uploaded file on its own evidence**, never
the chat as a whole.

**Both kinds in one upload takes priority over everything in 0d and 0e below.** `18C` §10.1
covers it: run both procedures and produce two reports, saying so in one line. Never merge a
module difference into the assessment report or the reverse. A mixed upload is **not** a
wrong-skill mistake and never triggers the warning.

**0d. No HTML uploaded?** `09A` §1 is explicit: do not start the analysis — ask the designer
to upload their refined HTML files for the module. Do not print the card first.

**0e. A `number-letter` pairings reply.** Under `09A` §1 this is the Phase 2 trigger and needs
no keyword. It can only follow a `09` Phase 1 report, so it always belongs to **this**
procedure — never switch to the assessment one on a pairings reply. If pairings arrive and no
Phase 1 report exists in this chat, take `09A`'s documented branch: ask the designer to run
`COMPARISON MODE` first.

**0f. Did the designer name a variant, or just type the phrase?** This decides what happens
when 0c says assessment.

- **A bare `COMPARISON MODE`** (no variant named) → they asked for "the comparison", not for
  this half. **Switch silently**: run the `18C` procedure and show the assessment card. No
  warning, no question — that is the KB's own automatic routing, working.
- **They named this variant** — this skill's name, a `/tk-module-comparison-mode` style
  shortcut, or words like "module comparison mode" — **and 0c says assessment** → do **not**
  run. Go to 0g.

**0g. Wrong skill, chosen deliberately — stop and warn.** Print this and nothing else, then
wait:

---

**Hold on — this looks like the wrong comparison skill.**

You asked for **Module Comparison Mode**, but the page you uploaded looks like an
**assessment** page: *[name the evidence in one line]*.

The two work differently. **Assessment Comparison Mode** gives you one finalized report
straight away, with every difference scoped Universal — right here, because every assessment
is built on the one template. **Module Comparison Mode** would instead ask you to scope each
difference against year level, subject, series and module, none of which an assessment has.

Reply **"assessment"** to switch, or tell me what I have misread — if these really are module
pages, say so and I will carry on. I cannot run the module comparison on an assessment page:
`18C` forbids it outright, so there is nothing to override, only something to correct if my
reading of the files is wrong.

---

## Step 1 — Show the mode card

Once Step 0 settles that this is the module procedure, open the reply with this card, before
any other output.

---

**MODULE COMPARISON MODE** · Te Kura HTML Convertor, Mode 3

**What this does** — compares the module HTML you refined by hand against the HTML this
project generated earlier in this chat, and reports the differences that the project's own
stored rules could be changed to prevent. Differences that came from the supplied structural
reference or example module are dropped silently, because no rule change can alter what an
external template ships.

**What it needs from you** — your finished, refined HTML files, uploaded into the **original
conversion chat**. That chat already holds the other three things this needs: the raw content
source, the structural reference, and the HTML this project produced.

**What you get back — two passes, two downloadable files.**
**Pass 1**, now: the initial report. Every qualifying difference as original raw content →
originally generated code → your refined code, numbered straight through, with the scope
options listed once at the top. **Then it is over to you:** read the numbered differences and
reply in this chat with number-and-letter pairings, in the format the report shows, saying how
widely each correction should apply.
**Pass 2**, after your reply: the finalized report. Same numbering, but each surviving
difference now also names the exact rule that produced the original output, and carries its
scope written out in full. This is the file that goes to whoever actions changes into the
project.

**It will not** — convert anything, edit student content, or change the project's own rule
files. Acting on the finalized report is Update Mode (Mode 4) or Admin Mode (Mode 8), in a
separate conversation.

*Wrong mode?* Tell me what you actually want to do and I'll switch. The others are
Conversion · Advisory & Support · Comparison — module or assessment · Update · Split ·
Interactives Build · PageForge Compare · Admin · Assessment.

---

## Step 2 — Load the real rules and follow them

This skill is a signpost, not a rule book. **The knowledge base is the authority and outranks
anything written here.** Search project knowledge and follow, as written there:

- `09_COMPARISON_MODE.md` — `09A` the trigger, the four required inputs, handling missing context, what counts as a difference · `09B` the exclusions and the inclusion gate · `09C` both report structures, the scope legend and how many options it carries, parsing the pairings, and the file name for each pass
- `18_ASSESSMENT_MODE.md` → `18C` — the routing test, and the procedure for any file that turns out to be an assessment page
- `00_MASTER_INSTRUCTIONS.md` — the hard constraints, which still apply

**Missing context — recover before you refuse.** If the original conversion turn is not in
this chat, follow `09A` §2 as written: try to recover it, then ask for the specific missing
piece, then use that input's documented fallback. Do not turn a documented recovery into a
hard stop.

## Step 3 — The one thing never to do in this mode

**Never mention, offer or ask about PageForge Compare Mode** at the end of a run, or anywhere
else. That mode starts only when the developer types its phrase, because only some developers
are testing PageForge.
