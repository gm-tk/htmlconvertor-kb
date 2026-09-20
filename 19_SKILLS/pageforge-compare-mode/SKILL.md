---
name: pageforge-compare-mode
description: PAGEFORGE COMPARE MODE, PAGEFORGE COMPARISON MODE or PAGEFORGE COMPARE — compare PageForge's generated HTML against the developer's finished HTML and report its faults to Gavin. Mode 7.
---

# PageForge Compare Mode — Te Kura HTML Convertor (Mode 7)

## Step 0 — Guards, before anything else

**0a. Am I in the right place?** Search project knowledge for `16_PAGEFORGE_COMPARE_MODE.md`.
If nothing comes back, this chat is not the Te Kura HTML Convertor project. Say so in one
line — *"This skill only works inside the Te Kura HTML Convertor project, where the compare
rules live. Please open a new chat in that project."* — and stop.

**0b. Precedence.** `ADMIN MODE` outranks everything — hand off and stop if it is present.
`UPDATE MODE` also outranks this mode. Otherwise this mode is checked **before**
`COMPARISON MODE`, because `PAGEFORGE COMPARISON MODE` contains that substring and the
leading word `PAGEFORGE` is the discriminator: it is Mode 7, not Mode 3.

**0c. Typed trigger only.** This mode starts **only** when the developer types the phrase.
Never raise it, offer it, ask whether someone has PageForge files, or name the report for
Gavin in any other mode — Comparison Mode above all. Only some developers are testing
PageForge.

**0d. Same chat only.** It runs in the original conversion chat, which already holds the
writer's template and the developer's finished HTML.

## Step 1 — Show the mode card

Open the reply with this card, before any other output.

---

**PAGEFORGE COMPARE MODE** · Te Kura HTML Convertor, Mode 7

**What this does** — compares the pages PageForge generated against the go-live-quality HTML
the developer built by hand, and reports where PageForge mis-read the writer's tags, so its
converter code can be fixed.

**What it needs from you** — **PageForge's original, un-stitched HTML pages**, uploaded into
the original conversion chat. That is the only thing to upload. The `{CODE}_interactives.txt`
worklist is never needed; if you volunteer one it is treated as evidence, not as a build
order.

**What you get back** — one downloadable report written for Gavin: numbered findings grouped
by class — **A** tag to element · **B** activity and interactive boundaries · **C** a
non-complex interactive left un-built · **D** content fidelity and placement · **E** page
scaffold — plus a short "for Gavin to judge" section, an interactive inventory table and a
coverage block. The report is produced even when there are no findings.

**The measure is the writer's template, never the developer's taste.** A developer decision
that is nowhere in the template — including anything agreed with the writer directly — is not
a PageForge fault and is never reported. Comments, developer notes and restated writer
instructions are ignored entirely, in both files and both directions.

**It will not** — convert, build, fix or edit anything, and it never changes this project's
own knowledge files. That is Comparison Mode into Update Mode.

*Wrong mode?* Tell me what you actually want to do and I'll switch. The others are
Conversion · Advisory & Support · Comparison — module or assessment · Update · Split ·
Interactives Build · PageForge Compare · Admin · Assessment.

---

## Step 2 — Load the real rules and follow them

This skill is a signpost, not a rule book. **The knowledge base is the authority and outranks
anything written here.** Search project knowledge and follow, as written there:

- `16_PAGEFORGE_COMPARE_MODE.md` — the three inputs, the five finding classes, SPILL/SWALLOW, the non-complex list, the exclusions, the one-shot report format, and in particular its section on **how to tell the upload states apart**. Read that section before judging any interactive: it is decided per interactive rather than per file, it has more than two possible answers, and the KB is explicit that one of the obvious shortcuts is wrong. Follow what it says, and where it tells you to ask rather than infer, ask
- `09_COMPARISON_MODE.md` → `09B` Exclusion 1 — the comment and developer-note exclusion this mode shares
- `00_MASTER_INSTRUCTIONS.md` — the hard constraints
