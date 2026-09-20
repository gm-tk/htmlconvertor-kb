---
name: tekura-assessment-mode
description: ASSESSMENT MODE — convert a filled-in NCEA Assessment Activity Word template into its single-page {CODE}.html for D2L's shared assessment area. HTML Convertor Mode 9.
---

# Assessment Mode — Te Kura HTML Convertor (Mode 9)

## Step 0 — Guards, before anything else

**0a. Am I in the right place?** Search project knowledge for `18_ASSESSMENT_MODE.md`.
If nothing comes back, this chat is not the Te Kura HTML Convertor project. Say so in one
line — *"This skill only works inside the Te Kura HTML Convertor project, where the
assessment rules live. Please open a new chat in that project."* — and stop.

**0b. Precedence.** `ADMIN MODE`, `PAGEFORGE COMPARE MODE`, `COMPARISON MODE` and
`UPDATE MODE` all outrank this mode. If any is present, hand off and stop. `SPLIT MODE` and
`INTERACTIVES MODE` do not apply to an assessment at all.

**0c. The document identifies itself.** A `.docx` with the details table (`Activity name:`
… `Brief description:`) and the bold sections *What to do*, *How to present your learning*,
*Timeframe*, *Getting started*, *Student Resources*, *Dropbox* is an Assessment Activity. It
runs on a bare upload or a plain-English "please convert this word doc" — never fall through
to the ambiguous-`.docx` question.

## Step 1 — Show the mode card

Open the reply with this card, before any other output.

---

**ASSESSMENT MODE** · Te Kura HTML Convertor, Mode 9

**What this does** — turns the writer's filled-in NCEA Assessment Activity Word template into
**one** single-page `{CODE}.html` — for example `US4249.html` — hosted in D2L's
`/shared/assessment/…` area. This is an assessment page, not a module.

**What it needs from you** — the `.docx`. Nothing else: there is never a Media List, because
media is kept separate from the document. Upload several at once and you get one page each,
all in the same response.

**What you get back** — the finished page, then the usual plain-English Designer Summary. The
details table becomes the coloured header bar with its NZQA link; every bold heading becomes
one accordion in order, the Dropbox section becoming the Final Dropbox accordion with its
quickLink button; the standard acknowledgements block closes the page.

**What you will have to finish yourself** — the page marks each one with a visible
`Designer/Developer To Do:` rather than asking you first: the dropbox code, and every image or
PDF, each To Do naming the exact D2L destination the `src` was built on. **The footer links
are always left blank** — they are unique to each assessment, so they are never guessed and
never flagged.

**It will not** — build a module, build a journal, ask about image output mode, or offer
Split Mode.

*Wrong mode?* Tell me what you actually want to do and I'll switch. The nine modes are
Conversion · Advisory & Support · Comparison · Update · Split · Interactives Build ·
PageForge Compare · Admin · Assessment.

---

## Step 2 — Load the real rules and follow them

This skill is a signpost, not a rule book. **The knowledge base is the authority and outranks
anything written here.** Search project knowledge and follow, as written there:

- `18_ASSESSMENT_MODE.md` — `18A` trigger, mapping and skeleton · `18B` content rules, acknowledgements and the To Do list · `18C` the assessment variant of Comparison Mode. **Read `18A`'s skeleton section before emitting anything:** the example page it starts from is not used as-is, and the corrections to it are listed there. Take them from `18A`, never from memory
- `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` → `05C` for the acknowledgements block
- `00_MASTER_INSTRUCTIONS.md` — the hard constraints, including the constraint governing inline styles and this mode's narrow exception to it

## Step 3 — If `COMPARISON MODE` is typed later in this chat

It is the **assessment variant** (`18C`), not the module one: only the re-uploaded pages are
compared, URL changes are never logged, there is no scope question, and the output is one
finalized report for Gavin with every difference scoped (c) Universal.
