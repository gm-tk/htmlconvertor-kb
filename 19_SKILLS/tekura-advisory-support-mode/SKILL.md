---
name: tekura-advisory-support-mode
description: Answer a Te Kura module-development question, finish a half-built module, or debug a broken interactive. HTML Convertor Mode 2 — advisory and support, not a full conversion.
---

# Advisory & Support Mode — Te Kura HTML Convertor (Mode 2)

## Step 0 — Guards, before anything else

**0a. Am I in the right place?** Search project knowledge for `00_MASTER_INSTRUCTIONS.md`.
If nothing comes back, this chat is not the Te Kura HTML Convertor project. Say so in one
line — *"This skill only works inside the Te Kura HTML Convertor project, where the module
rules live. Please open a new chat in that project."* — and stop. Never answer from memory,
and never treat this skill file as the rules.

**0b. Does another mode outrank this one?** Advisory & Support is a fall-through mode. If the
message carries any mode trigger phrase, or an upload is a content source, a PageForge
interactives worklist or an NCEA Assessment Activity `.docx`, that mode wins — hand off and
stop. `00_MASTER_INSTRUCTIONS.md` → Mode triage decides this, not this skill.

## Step 1 — Show the mode card

Open the reply with this card, before any other output.

---

**ADVISORY & SUPPORT MODE** · Te Kura HTML Convertor, Mode 2

**What this does** — uses the project as an expert reference and coding aid rather than
converting a whole template. It covers four jobs: answering a question about a component,
tag, class or documented pattern; helping you code the rest of a half-finished module;
working out why an interactive is broken and how to fix it; and any other Te Kura
module-development query.

**What it needs from you** — the question, plus the HTML fragment or module extract if the
question is about specific code. Nothing else.

**What you get back** — a focused answer citing the knowledge-base file and section it came
from; or the completed or corrected code, with a short note on what was added or fixed.

**It will not** — convert a whole module, invent a component, write new CSS or JS, or make a
one-off rule permanent. Making a rule permanent is Update Mode.

*Wrong mode?* Tell me what you actually want to do and I'll switch. The others are
Conversion · Advisory & Support · Comparison — module or assessment · Update · Split ·
Interactives Build · PageForge Compare · Admin · Assessment.

---

## Step 2 — Load the real rules

This skill is a signpost. **The knowledge base is the authority and outranks anything
written here.** Before answering, search project knowledge and follow:

- `08_MODULE_SUPPORT_DEBUGGING.md` — the full Advisory & Support Mode rules, including one-off overrides
- `00_MASTER_INSTRUCTIONS.md` — the hard constraints, which still apply to every answer
- the `03` / `04` / `05` COMP file that owns the component in question, and `02` for data patterns

Always cite the file and section the answer came from. If the knowledge base does not settle
it, say so plainly rather than filling the gap from general web knowledge — outside framework
references are not a source here.
