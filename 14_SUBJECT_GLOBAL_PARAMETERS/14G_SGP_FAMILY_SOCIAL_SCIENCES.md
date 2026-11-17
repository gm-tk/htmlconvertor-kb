> **Last updated:** Tuesday, 17th November, 2026 7:37 PM
> **Granular part G (9 of 9) of `14_SUBJECT_GLOBAL_PARAMETERS.md`** — §14.17 Social Sciences, opened 17 November 2026 (CL-0147).
> All sibling parts live in `14_SUBJECT_GLOBAL_PARAMETERS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## 14.17 Social Sciences
**Scope — Cohort:** all **Social Sciences** modules. Codes seen in the source: `SSEA203` (module), `SSFUN07`,
`SSFUN08` (fundamentals) — identify by subject; no prefix rule is asserted. Source: *Global Edits Soc Sci*
(design team, re-exported 16 November 2026). Actioned 17 November 2026 (CL-0147). Writer guidance the document
gives about punctuation or capitalisation is for writers — the conversion copies the writer's text verbatim
(constraint 1).

### Intro page
- **Title.** `[Subject code]` + `[H1]` — the module title in **Te Reo and English** (example `SSEA203` *Making Choices With Money*).
- **Overview — the module menu.** `[Overview]` → `[tab] [H4] Learning Intentions` → `[Body] We are learning:` (bullets) → `[H4] How will I know I have learned it?` → `[Body] I can:` (bullets, in capabilities language) → `[tab] [H4] Knowledge` → `[Body]` → `[H4] Practices` → `[Body]`. The example shows two tabs — **Information** (Learning Intentions | How will I know I have learned it?) and **Overview** (Knowledge | Practices). Tab labels come from the writer's lines; menu mechanics stay in `01_PIPELINE_EXTRACTION_TAGS.md` → Module Menu Structures.
- **Introduction text.** `[Whakataukī]` → `[Body]` → `[Video]` or `[Image]`.
- **Fundamental links.** `[Alert]` *You might like to explore these fundamentals to support you with your learning in this module:* then the writer's list (e.g. *SSFUN07 - Enterprise*, *SSFUN08 - Thinking Critically And Processing Information*) — an ordinary `alert`.

### Lesson pages
- **Lesson title** `[H1]` — the **name of the lesson**, not the module title.
- **Overview** `[Overview]` → `[Body] We are learning:` (bullets) → `I can:` (bullets) — no tabs.
- **Lesson introduction** `[Alert]` — e.g. *In this lesson you are learning …* — an ordinary `alert`.
- **Lesson summary** `[Alert]` → `[H3] Lesson summary` → `[Body] Ka pai! This is what you have learned in this lesson.` → `[Checklist]` (the success criteria as a checkbox list) → `[Hint Button] [Title] Need help?` → `[Body]` the kaiako-contact paragraph, **copied as the writer gives it** (the document's own wording differs slightly from HPE's — never normalise it). Hint mechanics: `04_COMP_SEGMENTS_OVERLAYS.md` → Hint.
- **Activity alerts — `[RHS alert]` inside an activity** (capability explanation, fundamental support, a link to practise more) → the existing **activity sidebar** (`05` → Activities → Activity sidebar); a `[Link]` in it follows constraint 75. (The hatched-line look in the example is the sidebar's own styling — no extra class.)
- **Speech bubbles** `[Image] [Speech bubble]` — there is **no subject-specific character**; writers request an AI-generated or iStock character, so the image is an ordinary writer image (no `imageCentral`).
- **Think about it** `[Think about it alert]` → `[H3] Think about it` → `[Body]` (questions as bullets) → `[Button] Reveal` → `[body]` — an `alert` holding the heading and questions, the reveal built with the existing hint/clickDrop reveal pattern; the light-bulb picture in the example is an iStock image the writer supplies. Where the shape is uncertain, raise a `Red Flag:` and follow a built Social Sciences sibling (Mode B).
- **Safety** `[Safety Alert]` → the warning alert, `div.alert.warning` (constraint 101). (The source still reads *"Waiting for CTK to confirm"*; the alert was confirmed and built on 17 November 2026 — CL-0145.)
- **Sensitivity warning** `[Alert blank]` → `[H3] Sensitive content` → `[Body]` — placed at the **top** of the lesson, activity or media that may be sensitive; briefly says what it is and gives options (support-site links, talking to a trusted adult). Builds `alert blank` (`05` → Alerts) with the writer's `<h3>` and body.
- **Checkpoint** `[Dropbox] [H3] [Body] [Button] Go to your journal [Button] Upload to dropbox` — the same phase 1–4 suggested wording as §14.8 / §14.14 (a writer's own copy wins). Up to **3** dropboxes, **2** suggested (one Checkpoint, one end-of-module); several activities may link to the checkpoint dropbox. *Go to your journal* follows constraint 96; the button label *Upload to dropbox* is this family's (as §14.11).
- **Capability spotlight** `[Hint Button] [Title] Capability spotlight [Body] …` — at the **bottom of an activity or page**; a hint whose title is *Capability spotlight*.
- **Optional summative activity** — an ordinary activity (example 7A *Your final detective challenge*).

### Module summary page
- `[H1] Congratulations!` — **no overview**.
- `[Body] Ka pai, you have completed this module about…` with `[RHS image] [Centralised image Congratulations]` → the shared celebration gif `congradulations/Congradulations animation.gif` (§14.12 / §14.16 — misspelling kept), text column beside the image column.
- **Module summary text** `[Alert]` → `[Body] Here are some of the big ideas you have learned and practised:` → `[Checklist]` (success criteria) → `[Hint Button] Need help?` → the kaiako paragraph as written.
- **Dropbox** `[Dropbox] [H3] Share your learning …` — the §14.8 phase 1–4 *Share Your Learning* wording.
- **Link to other learning** `[alert]` → `[body] If you enjoyed this learning, you may like to explore:` → list → *Talk to your kaiako about these and other learning opportunities.*
