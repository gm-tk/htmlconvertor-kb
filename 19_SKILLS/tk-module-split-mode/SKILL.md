---
name: tk-module-split-mode
description: SPLIT MODE - splits a long single-page Te Kura module that is being converted into separate files that are then fed into PageForge's Page Stitcher to output the single HTML file.
---

# Split Mode — Te Kura HTML Convertor (Mode 5)

## Step 0 — Guards, before anything else

**0a. Am I in the right place?** Search project knowledge for `13_SPLIT_MODE.md`.
If nothing comes back, this chat is not the Te Kura HTML Convertor project. Say so in one
line — *"This skill only works inside the Te Kura HTML Convertor project, where the split
contract lives. Please open a new chat in that project."* — and stop.

**0b. Precedence.** `ADMIN MODE` outranks this mode; hand off and stop if it is present.
`PAGEFORGE COMPARE MODE`, `COMPARISON MODE` and `UPDATE MODE` are the other precedence
triggers — if one of them is in the message, `00_MASTER_INSTRUCTIONS.md` → Mode triage decides,
not this skill.

**0c. Single-page only — check this before building anything.** If the module has `[LESSON]`
or `[End page]` boundaries it is genuinely multi-page: it uses the Page Boundary System and is
**never** split. Say so plainly and convert it normally instead. The two systems must never be
conflated.

## Step 1 — Show the mode card

Open the reply with this card, before any other output.

---

**SPLIT MODE** · Te Kura HTML Convertor, Mode 5

**What this does** — a packaging variant of Conversion, for a **single-page** module whose
finished HTML is too long to emit in one response. The conversion itself is unchanged — same
content fidelity, same skeleton, same red flags, same image-mode prompt, same reviewer
comments. Only the packaging changes.

**What it needs from you** — the same things Conversion needs: the content source and the
structural reference, plus the Media List if the module has media.

**What you get back** — one file per response, in order. First `<CODE>-base.html`: the full
page scaffold whose `#body` holds only an ordered list of splice markers. Then, one per
prompt, `<CODE>-lesson-<id>.html`: that lesson's raw `#body` content wrapped in section
markers. Every file also carries detailed `PAGEFORGE-GUIDE` comments telling a human developer
exactly where each piece goes.

**Putting it back together** — PageForge's Page Stitcher recombines the files into one
single-page file that is byte-identical to a normally built module, with no `PAGEFORGE-*`
markers left behind. You can also stitch by hand from the guide blocks.

**It will not** — split a multi-page module, or emit more than one file in a single turn.

*Wrong mode?* Tell me what you actually want to do and I'll switch. The others are
Conversion · Advisory & Support · Comparison — module or assessment · Update · Split ·
Interactives Build · PageForge Compare · Admin · Assessment.

---

## Step 2 — Load the real rules and follow them

This skill is a signpost, not a rule book. **The knowledge base is the authority and outranks
anything written here.** Search project knowledge and follow, as written there:

- `13_SPLIT_MODE.md` — the exact `PAGEFORGE-SPLICE` / `PAGEFORGE-SECTION` contract, what the base and each section file may and may not contain, the `PAGEFORGE-GUIDE` blocks, the one-file-per-response cadence, id pairing, the handling of a lesson whose content cannot be produced, and the round-trip guarantee. Read the whole contract before emitting the base; several of its rules apply to the section files as well as the base, and getting one half right is not enough
- `00_MASTER_INSTRUCTIONS.md` — the Conversion Pipeline, which runs unchanged, and the hard constraints
- the same `01` / `02` / `03` / `04` / `05` / `14` files any conversion uses
