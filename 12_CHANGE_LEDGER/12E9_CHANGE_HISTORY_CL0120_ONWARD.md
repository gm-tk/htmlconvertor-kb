> **Last updated:** Tuesday, 20th October, 2026 12:14 PM
> **Granular part E9 (12 of 15) of `12_CHANGE_LEDGER.md`** — PART 3 change history: CL-0120 onward (continued) — THE OPEN PART: APPEND NEW ENTRIES HERE.
> All sibling parts live in `12_CHANGE_LEDGER/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.
> *The table header row below is repeated for readability; the rows continue the PART 3 history table. Opened 20 October 2026 when `12E8` reached the 30 KB soft limit and was closed at CL-0119 (`CLAUDE.md` §4).*

<!-- KB-PART-BODY-START -->
| ID | Date | Change summary | Scope | Affected file(s) / rule(s) | Source (intake channel) | Class | Status | Authority decision |
|----|------|----------------|-------|----------------------------|--------|-------|--------|--------------------|
| CL-0120 | Tuesday, 20th October, 2026 | **Click-drop choice sets carry no picture tiles above the buttons (pictures move into the panels); a "click the picture" request puts `clickDrop imgBorder` on the `<img>` with an `<h5>` caption above.** Designer inline styles and the HTML comment NOT codified | (c) Universal | `04A` → Click Drop (new section); `02C` | Finalized difference report (SCBI202, Difference 12) | Major | Implemented | Non-conflicting; not escalated. Styles excluded per designer decision (Chris, 20 Oct 2026) |
| CL-0121 | Tuesday, 20th October, 2026 | **Text + side image are sibling columns of one row (`col-md-8 col-12 paddingR` + `col-md-4 col-12 paddingL`), never an inner row nested in the text column; padding classes on every side-by-side pair (text + sidebar alert included).** Reverses the pre-ledger `02B` "inner row pattern", which had marked this exact form WRONG | (c) Universal | `02B` → Column Class Reference (3 rows) + inner-row paragraph + examples; `05D` → Standard Grid; `02C` | Finalized difference report (SCBI202, Difference 13) | Major | Implemented | Pre-ledger rule rewritten; no ledger conflict; not escalated |
| CL-0122 | Tuesday, 20th October, 2026 | **A writer's floating-nav glossary request → a separate `{CODE}_glossary.html` page (standard skeleton, `<h1><span>Glossary</span></h1>`, `glossary` / `search-table` in `#body`) + `stickyNav.js` in the `<head>` of every page;** no glossary on 0.0, no red flag. Split Mode's no-stickyNav rule unchanged | (c) Universal | `05A` → Glossary; `01A` → `stickyNav.js` presence; `14D` §14.11; `02C` | Finalized difference report (SCBI202, Difference 15) | Major | Implemented | Non-conflicting; not escalated |

---
