---
name: pageforge-interactives-mode
description: "!!!PAGEFORGE TESTING ONLY!!! Build the un-built complex interactives listed in a PageForge {CODE}_interactives.txt file that is later stitched back into the original HTML files."
---

# Interactives Build Mode — Te Kura HTML Convertor (Mode 6)

## Step 0 — Guards, before anything else

**0a. Am I in the right place?** Search project knowledge for `15_INTERACTIVES_BUILD_MODE.md`.
If nothing comes back, this chat is not the Te Kura HTML Convertor project. Say so in one
line — *"This skill only works inside the Te Kura HTML Convertor project, where the component
markup rules live. Please open a new chat in that project."* — and stop.

**0b. Precedence.** `ADMIN MODE` outranks this mode; hand off and stop if it is present.
`PAGEFORGE COMPARE MODE`, `COMPARISON MODE` and `UPDATE MODE` also take precedence over it.
This mode outranks the ordinary Conversion and Advisory signals, because a worklist upload is
unambiguous.

**0c. Is this really a worklist?** A PageForge interactives worklist identifies itself: an
`INTERACTIVE REFERENCE — {CODE}` header plus a `REFERENCE CODE:` line per entry. A `.txt`
that opens `--- CONTENT START ---` or `[TITLE BAR]` is a **content source** and means
Conversion Mode — never confuse the two. If the worklist carries no reference codes, ask for
a re-conversion instead of building.

**0d. The cadence here is not Split Mode's.** Mode 5 emits one file per response; this mode
does not. Follow `15_INTERACTIVES_BUILD_MODE.md`'s own batching and single-response rule as
written there, and never end by inviting the developer to ask for the next file.

## Step 1 — Show the mode card

Open the reply with this card, before any other output.

---

**INTERACTIVES BUILD MODE** · Te Kura HTML Convertor, Mode 6

**What this does** — PageForge's HTML Generator built your pages but left the interactives it
cannot yet build as reference-code placeholders, listing them in a `{CODE}_interactives.txt`
worklist. This mode builds production-quality HTML for every one of them.

**What it needs from you** — the `{CODE}_interactives.txt` worklist. Uploading it is enough;
you do not have to type the phrase.

**What you get back** — an announced build plan, then **every** finished file in that same
response, batched by the documented file-size rule. Each build is wrapped in its reference-code
anchor so PageForge's Page Stitcher can splice it into the exact right spot automatically.

**It will not** — convert a module, or emit pages, menus, headers, footers, acknowledgements,
activity boxes or head scripts. The generator has already produced all of that; each section
starts at the widget's own wrapper.

*Wrong mode?* Tell me what you actually want to do and I'll switch. The others are
Conversion · Advisory & Support · Comparison — module or assessment · Update · Split ·
Interactives Build · PageForge Compare · Admin · Assessment.

---

## Step 2 — Load the real rules and follow them

This skill is a signpost, not a rule book. **The knowledge base is the authority and outranks
anything written here.** Search project knowledge and follow, as written there:

- `15_INTERACTIVES_BUILD_MODE.md` — the anchor contract and exactly how a reference code is carried, the worklist anatomy, the batching and delivery rule, the fragment build rules, the worked example
- `03` / `04` / `05` COMP files — still the markup authority for every widget
- `02_DATA_CONTENT_VERIFICATION.md` for data patterns, and `14_SUBJECT_GLOBAL_PARAMETERS.md` for family conventions
- `00_MASTER_INSTRUCTIONS.md` — every hard constraint still applies
