> **Last updated:** Friday, 28th August, 2026 1:30 PM
> **Granular part E (5 of 5) of `02_DATA_CONTENT_VERIFICATION.md`** — Edge cases, component whitelist, output specifications.
> All sibling parts live in `02_DATA_CONTENT_VERIFICATION/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## Edge Cases
 
| Situation | Action |
|---|---|
| No template file AND no reference module files | Ask for either a dedicated template or reference module HTML files (exception: MTK conversions are self-contained — no structural reference needed) |
| No content source provided | Ask for a content source — a PageForge `.txt`, a raw Writers Template `.docx`, or an MTK `.docx` |
| Content source is a raw (non-MTK) Writers Template `.docx` | Accepted — extract with `extract-text`, skip ALL front-matter (submission checklist, LOT tags, Section A merging, Section B guidance, contents, sign-off), convert ONLY from the first `[TITLE BAR]` onward. See `01_PIPELINE_EXTRACTION_TAGS.md` Section 02 |
| Content source is an MTK `.docx` | Follow `07_MTK_DOCX_CONVERSION.md` |
| Both a PageForge `.txt` and a `.docx` of the same module supplied | Prefer the `.txt` |
| Media List `.docx` supplied alongside content source | Optional aid — use it to verify media links and source acks titles/descriptions; never treat its rows as student content; never let it change page boundaries |
| Reference module files provided (Mode B) | Derive skeleton from reference files; replace all reference module codes/titles with new module's; note in verification summary |
| Reference module level mismatch | If reference `template="..."` doesn't match expected level for new module code, flag to user before proceeding |
| Ambiguous component | Red flag + best interpretation + visible fallback |
| Writer red text | Implement if structural, red flag if design input needed |
| Content in Word tables (not `[TABLE]`) | Bootstrap grid, NOT HTML tables |
| Multiple pages | Ask which to convert or convert all with labels |
| Missing overview content | Do not fabricate |
| Acknowledgements | ALWAYS at the bottom of the overview page (`-00` / lesson 0.0), after the footer — NEVER on the last page or any lesson page |
| Genuinely corrupt text | Extremely rare — RED FLAG with best-guess visible content |
| Exploratory dropdown | All options correct — intentional for student exploration (no red flag needed) |
| Full-heading italic/bold | Strip wrapping tag |
| Pre-MODULE-INTRODUCTION End page | Disregard (Rule 1) |
| Missing End page between lessons | Insert boundary (Rule 2) |
| Empty lesson segment | Disregard End page (Rule 3) |
| Orphaned title bar | Merge with next (Rule 4) |
| Unnumbered lessons | Sequential by appearance |
| `[thinking speech bubble]` | Standard speech bubble + `no-hover` + RED FLAG for thought CSS |
| `[rotating banner]` | Implement as `rotateBanner` component (NOT carousel) — see COMP_07 |
| Conversation-style speech | Alternating bubble-right / bubble-left with `no-hover` |
| Writer speech bubble positional instruction | CS instruction (e.g., "above the cat's head") overrides default left/right layout — use `bubble-top`/`bubble-bottom` with image in separate row |
| `[info trigger image]` or `[info trigger] image` | Use `infoImage` component — NOT flip cards |
| D&D standard with images + text descriptions | Text in `questionContainer` (col-7), images in `dragContainer` (col-5) — see COMP_01 |
| DropQuiz with standalone Q&A pairs (numbered) | Use list layout (no `layout` attribute, `<ol><li>` with row/column) — NOT paragraph layout |
| DropQuiz with inline blanks in sentences | Use paragraph layout (`layout="paragraph"`, `dropParaContainer`) |
| Interactive activity paired with alertImage | Use `col-md-8 col-12` container with `col-md-4` alertImage nested inside (8 + 4 = 12) — see COMP_14 |
| Lesson page title (any level, incl. Years 9–10/NCEA) | Use THAT LESSON'S OWN title in the header bar (constraint 79); strip any `Lesson N` prefix; drop the duplicate body heading, not the header title. One `<h1><span>` unless the writer gave the lesson its own bilingual name |
| Lesson name written twice (boundary tag + opening `[H2]`) | One title, not a conflict — header takes it, duplicate body heading dropped; never fall back to the module title |
| Lesson page with no lesson title anywhere | Module title in the header **plus** a visible `Designer/Developer To Do:` note that no lesson title was supplied |
| Lesson page missing Te Reo title | Not an error — a lesson page needs Te Reo only where the writer gave that lesson a bilingual name. Ask the user only for a missing Te Reo **module** title on the overview page (Years 9–10/NCEA) |
| Revision requests | Apply only requested changes; re-verify |
| `[LINK: URL]` in text | Preceding `__underlined text__` is the visible link text |
| Bare URL after media tag | Media reference (video URL, image URL) — not a text hyperlink |
 
---
 
## Component Whitelist — Known Partial/No-Match (v6)
 
Most components are FULL MATCH. Remaining items:
 
| Tag | Status | Fallback |
|---|---|---|
| `[thinking speech bubble]` | PARTIAL — thought CSS undocumented | Speech bubble + `no-hover` + RED FLAG |
| `[Pop up texts]` / `[Pop up texts that stay]` | CS instruction | Carousel + RED FLAG |
 
---
 
## Output Specifications
 
**Default:** Complete, standalone HTML files with full document skeleton.
 
**File naming:** `[MODULE_CODE]-[PAGE_NUMBER].html` (e.g., OSAI201-00.html)
 
**Module code source:** Extract from the PageForge metadata block (`Module Code:` field), the raw `.docx` metadata table, the `[TITLE BAR]` content, or the filename.
 
**Post-output — THE DESIGNER SUMMARY (constraint 88):**

The audience for a conversion run is a **designer, not a developer** — most have no coding background, which is why this project exists. So the run **verifies in full and reports by exception.**

**Every verification step still runs, unchanged** — the full checklist in `02C`, the Phase 7 confirmations in `00_MASTER_INSTRUCTIONS.md`, the div open/close count, the page-boundary validation, the class-attribute integrity check, all of it. **Nothing about the checking changes. Only what reaches the chat changes.**

What follows the HTML is a short **Designer Summary** carrying **only** what a designer must act on, decide, or be aware of:

1. **CONVENTION DEPARTURES — always FIRST, always its own labelled block, never merged into a list.** Anything the conversion produced that is **not** what this project's rules would normally produce, because the writer's template demanded it. State three things in plain English: **what was done**, **what the rule normally says**, and **where in the writer's template it came from**. *(The case this exists for: a module whose writer repeated the module title as the heading of every page. The conversion followed the writer, correctly — but that decision contradicted the project's own convention and the designer needed to see it. It was reported, and then lost among two dozen lines of counts and confirmations. A convention departure is the single most important thing a run can tell a designer; it is never buried and never abbreviated.)*
2. **Red flags raised in the output** — how many, on which pages, and what the designer must resolve for each.
3. **`Designer/Developer To Do:` items** — the deferred assets, URLs and setup the developer must supply during production.
4. **`Writers Note:` / `Note from {author}:` messages surfaced** — count and pages only, not the full text (it is already visible in the HTML).
5. **Anything the conversion could not do, guessed at, or fell back on** — an unbuildable structure, an ambiguous component, a documented fallback used.
6. **Any choice still owed by the designer** — e.g. an image output mode that was assumed rather than stated.

**NEVER emitted.** These checks are still performed; they are simply not narrated. Mention one **only** when it fails or is uncertain:

- div open/close counts · interactive component counts and types · data patterns identified
- page-boundary validation results · template source and level confirmation
- Mode B confirmation that reference codes/titles were replaced · heading-pattern, domain (`tekuradev`) and `stickyNav` notes
- class-attribute integrity · speech-bubble `no-hover` confirmation · click-drop grouping confirmation
- acknowledgements placement confirmation · "all student content is visible HTML" confirmation
- tag normalisation decisions · content-source format and media-list usage
- an **image output mode the designer stated** — it is not echoed back to them; one that had to be **assumed** is category (6) above

**A FAILED OR UNCERTAIN CHECK IS NEVER SILENT.** If any of the above fails, is ambiguous, or produced a correction the designer would want to know about, it is **promoted into category (2)** as a red flag and stated in plain English. Silence means *checked and clean* — never *not checked*.

**Plain English, no jargon.** Write "the same title appears at the top of every page", not "duplicate `<h1><span>` across page scaffolds". Name pages the way the designer names them.

**"Note in the verification summary" now means this.** Every instruction elsewhere in the knowledge base to *note X in the verification summary* (`01_PIPELINE_EXTRACTION_TAGS.md`, `06_TEMPLATE_RECOGNITION.md`, the Edge Cases table above, `00_MASTER_INSTRUCTIONS.md` → Phase 7) is re-scoped by this rule: **record it internally, and surface it in the Designer Summary only if it passes the test above.** A correction the project describes as silent stays silent.

**If nothing falls into categories (1)–(6), the Designer Summary is ONE LINE:** *"No red flags; nothing outstanding."*

**This changes the chat only — the generated HTML is byte-identical either way.** It is a mechanism change under constraint 87 and is not recorded in the PageForge Amalgamation Log.
