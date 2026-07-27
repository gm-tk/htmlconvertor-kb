> **Last updated:** Thursday, 16th July, 2026 9:30 PM
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
| Lesson page title (Years 9–10/NCEA) | Use MODULE title in header bar; render lesson-specific H2 as body `<h3>` |
| Lesson page missing Te Reo title | Ask user for Te Reo module title before proceeding (Years 9–10/NCEA) |
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
 
**Post-output verification summary:**
- Content source format used (PageForge `.txt`, raw Writers Template `.docx`, or MTK `.docx`)
- Whether a Media List `.docx` was supplied and used (for media verification + acks)
- Template source identified (Mode A: dedicated template file, or Mode B: reference module files + which files used)
- If Mode B: confirmation all reference module codes/titles replaced with new module values
- Level confirmed (template attribute matches module code prefix)
- Image output mode used (Mode P — Placeholder, or Mode D — Direct Link)
- Page Boundary Validation results
- Total div open/close count
- Interactive component count and types
- Data patterns identified
- Speech bubble instances (with `no-hover` confirmation)
- Click drop grouping confirmed
- Acknowledgements placement confirmed (bottom of overview page 0.0)
- Red flags and reasons
- Tag normalisation decisions
- Ambiguities encountered
- Confirmation all student content is visible HTML