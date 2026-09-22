---
name: tk-assessment-comparison-mode
description: ASSESSMENT COMPARISON MODE — compare a refined NCEA assessment page against the one generated here. One finalized report for Gavin, straight away.
---

# Assessment Comparison Mode — Te Kura HTML Convertor (Mode 3, the `18C` assessment variant)

One documented trigger, two procedures. `COMPARISON MODE` is a **single mode** in the
knowledge base; it runs the **module** procedure (`09`) or the **assessment** procedure
(`18C`) depending on the evidence. This skill is the assessment half. Its twin is
`tk-module-comparison-mode`. **The KB's routing rule is unchanged** — the files decide,
never a question.

## Step 0 — Guards, before anything else

**0a. Am I in the right place?** Search project knowledge for `18_ASSESSMENT_MODE.md` → `18C`
and `09_COMPARISON_MODE.md`. If nothing comes back, this chat is not the Te Kura HTML
Convertor project. Say so in one line — *"This skill only works inside the Te Kura HTML
Convertor project, where the comparison rules live. Please open a new chat in that project."*
— and stop.

**0b. Precedence, as `18C` §10.1 states it:** `ADMIN MODE` outranks everything;
`PAGEFORGE COMPARE MODE` is checked first on the `PAGEFORGE` discriminator; `UPDATE MODE`
still wins if present. Hand off and stop for any of those. (`09A` §1, for the module half,
does not name `UPDATE MODE` among its exceptions. Where a message carries both
`COMPARISON MODE` and `UPDATE MODE` and the file kind is not yet settled, follow
`00_MASTER_INSTRUCTIONS.md` → Mode triage rather than this skill.)

**0c. What kind of page is each upload?** Apply the test in `18C` §10.1 — it names the exact
markers that identify an assessment page, and says a page that is not one **is a module page,
whatever this chat previously ran**. Route **each uploaded file on its own evidence**, never
the chat as a whole.

**Both kinds in one upload takes priority over everything in 0e and 0f below.** `18C` §10.1
covers it: run both procedures and produce two reports, saying so in one line. Never merge an
assessment difference into the module report or the reverse. A mixed upload is **not** a
wrong-skill mistake and never triggers the warning.

**0d. No HTML uploaded?** Ask for the refined page or pages, as `09` does. Do not start the
analysis, and do not print the card first.

**0e. Did the designer name a variant, or just type the phrase?** This decides what happens
when 0c says module.

- **A bare `COMPARISON MODE`** (no variant named) → they asked for "the comparison", not for
  this half. **Switch silently**: run the `09` procedure and show the module card. No warning,
  no question — that is the KB's own automatic routing, working. The same applies to a
  `number-letter` pairings reply, which can only belong to the module procedure.
- **They named this variant** — this skill's name, an `/tk-assessment-comparison-mode` style
  shortcut, or words like "assessment comparison mode" — **and 0c says module** → do **not**
  run. Go to 0f.

**0f. Wrong skill, chosen deliberately — stop and warn.** Print this and nothing else, then
wait:

---

**Hold on — this looks like the wrong comparison skill.**

You asked for **Assessment Comparison Mode**, but the pages you uploaded look like **module**
pages: *[name the evidence in one line]*.

The two work differently, and here the difference would cost you something real. This one
scopes every difference as **Universal** and reports straight away, which is right for
assessments because they all share one template — but modules do not, so it would push your
corrections across every year level, subject and series rather than where you meant them.
**Module Comparison Mode** is the one that asks you to choose.

Reply **"module"** to switch, or tell me what I have misread — if these really are assessment
pages, say so and I will carry on. I cannot run this procedure on a module page: `18C`
forbids it outright, so there is nothing to override, only something to correct if my reading
of the files is wrong.

---

## Step 1 — Show the mode card

Once Step 0 settles that this is the assessment procedure, open the reply with this card,
before any other output.

---

**ASSESSMENT COMPARISON MODE** · Te Kura HTML Convertor, Mode 3

**What this does** — compares the NCEA assessment page you refined by hand against the
`{CODE}.html` this project generated earlier in this chat, and reports every difference that
should change how future assessments are built.

**What it needs from you** — the refined page, re-uploaded into the **same chat that converted
the assessment**. That chat already holds the writer's `.docx` and the page this project
produced. Re-upload only the pages you changed: any other page generated in this chat is
assumed unchanged, listed as such in the report, and never asked for.

**What you get back — one finalized report, immediately.** There is **no first pass and no
scope question here**, and that is deliberate: every assessment is built on the one template,
so there is nothing to scope against — no year level, subject, module or series to choose
between. Every difference is treated as Universal by rule. The report goes to Gavin, who
actions it in Update Mode or Admin Mode.

**What it deliberately ignores** — the things that belong to one assessment rather than to a
rule: its addresses and links, and anything filled in that the Word document could not supply.
Editorial rewording is content editing, not conversion. `18C` sets the exact list, including
the cases where a change *around* a link is reportable. Anything structural is reported.

**It will not** — convert, rebuild or edit a page, and it never changes the project's own rule
files.

*Wrong mode?* Tell me what you actually want to do and I'll switch. The others are
Conversion · Advisory & Support · Comparison — module or assessment · Update · Split ·
Interactives Build · PageForge Compare · Admin · Assessment.

---

## Step 2 — Load the real rules and follow them

This skill is a signpost, not a rule book. **The knowledge base is the authority and outranks
anything written here.** Search project knowledge and follow, as written there:

- `18_ASSESSMENT_MODE.md` → `18C` — routing, the inputs and the fixed skeleton that serves as the structural reference, partial re-uploads, the no-scopes rule, the assessment readings of the exclusions, the report's exact shape and file-naming, and how the run closes
- `09_COMPARISON_MODE.md` → `09B` for the exclusions and the inclusion gate, and `09C` §9 for the finalized-report bundle — both reused unchanged except where `18C` says otherwise
- `00_MASTER_INSTRUCTIONS.md` — the hard constraints

If the originally generated page is no longer visible in a long chat, ask the developer to
re-supply it. Never reconstruct it from the rules, and never treat the refined upload as the
original.

## Step 3 — Two things never to do in this mode

- **Never ask which scope to apply**, never produce a first-pass report, and never invite a
  `number-letter` reply. Those belong to the module procedure.
- **Never mention, offer or ask about PageForge Compare Mode.**
