---
name: tk-module-conversion-mode
description: Convert a Te Kura Writers Template, a PageForge .txt or an MTK .docx into finished D2L/Brightspace module HTML. HTML Convertor Mode 1 — the ordinary conversion job.
---

# Conversion Mode — Te Kura HTML Convertor (Mode 1)

## Step 0 — Guards, before anything else

**0a. Am I in the right place?** Search project knowledge for `00_MASTER_INSTRUCTIONS.md`.
If nothing comes back, this chat is not the Te Kura HTML Convertor project. Say so in one
line — *"This skill only works inside the Te Kura HTML Convertor project, where the
conversion rules live. Please open a new chat in that project."* — and stop. Never convert
from memory, and never treat this skill file as the rules.

**0b. Does another mode outrank this one?** Conversion is the fall-through mode. If the
message carries `ADMIN MODE`, `PAGEFORGE COMPARE MODE`, `COMPARISON MODE`, `UPDATE MODE`,
`SPLIT MODE`, `INTERACTIVES MODE` or `ASSESSMENT MODE`, or the upload is a PageForge
interactives worklist or an NCEA Assessment Activity `.docx`, that mode wins — hand off and
stop. `00_MASTER_INSTRUCTIONS.md` → Mode triage decides this, not this skill.

**0c. Ambiguous input — ask, do not guess.** Everything unmatched lands here, so this is where
the ambiguity guard belongs: a `.docx` with no clear instruction **that does not pass the
Assessment fingerprint** means asking the user which mode they want before proceeding.

## Step 1 — Show the mode card

Open the reply with this card, before any other output.

---

**CONVERSION MODE** · Te Kura HTML Convertor, Mode 1

**What this does** — turns tagged writer content into finished, spec-compliant HTML for
D2L/Brightspace, following the documented conversion pipeline end to end.

**What it needs from you** — two required things and one optional. Required: a **content
source** (a PageForge `.txt`, a raw Writers Template `.docx`, or an MTK `.docx`) and a
**structural reference** (the skeleton the output is derived from — either supplied directly
or, in Mode B, drawn from completed HTML files of a closely related module). Optional: a
**Media List**, if the module has media.

**What you get back** — the module HTML (one file per page, or one single-page file),
followed by a short plain-English Designer Summary that reports only what needs your
attention: convention departures, red flags, `Designer/Developer To Do:` items, writer and
reviewer notes surfaced, anything guessed at, and any choice still owed by you.

**It will not** — reword writer content, invent classes or components, write new CSS or JS,
or design anything new.

*Wrong mode?* Tell me what you actually want to do and I'll switch. The others are
Conversion · Advisory & Support · Comparison — module or assessment · Update · Split ·
Interactives Build · PageForge Compare · Admin · Assessment.

---

## Step 2 — Load the real rules and follow them

This skill is a signpost, not a rule book. **The knowledge base is the authority and outranks
anything written here.** Search project knowledge and follow, as written there:

- `00_MASTER_INSTRUCTIONS.md` — the Conversion Pipeline and the full hard-constraint list. Two constraints shape the opening of a run: the **image output mode** prompt, and deriving the skeleton from the supplied structural reference
- `01_PIPELINE_EXTRACTION_TAGS.md` — input formats, page boundaries, tag taxonomy, red text, image output modes
- `02_DATA_CONTENT_VERIFICATION.md` — data patterns, content rules, Comment & Red Flag Policy, verification checklist
- `03` / `04` / `05` COMP files — the markup authority for every component
- `06_TEMPLATE_RECOGNITION.md` — Legacy vs Refresh, sub-types, Mode B validation
- `07_MTK_DOCX_CONVERSION.md` — only if the source is an MTK `.docx`
- `13_SPLIT_MODE.md` — for the proactive single-page offer and when to make it
- `14_SUBJECT_GLOBAL_PARAMETERS.md` — the per-subject conventions that apply automatically

Follow the pipeline in full. If anything here disagrees with those files, they win.
