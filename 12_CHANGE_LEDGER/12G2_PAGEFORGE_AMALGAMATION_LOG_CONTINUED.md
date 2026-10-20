> **Last updated:** Wednesday, 21st October, 2026 11:46 AM
> **Granular part G2 (16 of 16) of `12_CHANGE_LEDGER.md`** — the PageForge Amalgamation Log, continued from `12G` (opened 21 October 2026 when `12G` reached the 30 KB soft limit). THE OPEN PART: append new entries here.
> All sibling parts live in `12_CHANGE_LEDGER/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
### CL-0123 — No `<h5>` inside a drag and drop
- **Date:** Wednesday, 21st October, 2026
- **Scope:** (c) Universal
- **Source:** ADMIN MODE (authorised) — direct-typed
- **Writer input (what triggers it):** any heading the writer asks for inside a drag and drop (e.g. an `[H5]` tag on a column heading or group label), in any layout.
- **Required output:** `<p><b>Heading text</b></p>` — never `<h5>` anywhere inside `.dragAndDrop`; no inline style. An unrequested column heading stays `<p>Column heading</p>`.
- **Supersedes:** —
- **KB rule:** `03_COMP_CORE_INTERACTIVES/03B` → Headings inside a drag and drop; `00H` constraint 94
- **PageForge status:** Not yet amalgamated

### CL-0124 — `dropbox` modifier on any activity containing a dropbox button (not BLL)
- **Date:** Wednesday, 21st October, 2026
- **Scope:** (c) Universal — BLL excepted
- **Source:** ADMIN MODE (authorised) — direct-typed
- **Writer input (what triggers it):** an activity holding a "Go to dropbox" / "Upload to dropbox" button or a `[trigger engagement]` tag, anywhere in the activity.
- **Required output:** append `dropbox` to the activity's classes — `activity dropbox` or `activity interactive dropbox` (keep any other modifiers). BLL: keep the button, no `dropbox` modifier. BLLR is not BLL.
- **Supersedes:** the `01F` sentence saying the modifier applies to BLL modules only (stale; never the intended rule)
- **KB rule:** `00D` constraint 43; `05_COMP_LANGUAGE_MEDIA_LAYOUT/05B` → Activities
- **PageForge status:** Not yet amalgamated

### CL-0125 — Every task interactive inside an activity box; tools exempt
- **Date:** Wednesday, 21st October, 2026
- **Scope:** (c) Universal
- **Source:** ADMIN MODE (authorised) — direct-typed
- **Writer input (what triggers it):** a task interactive tag (drag and drop, any quiz, self check, game, ordering, slider, sketcher) — including one the writer placed outside any `[Activity …]`.
- **Required output:** the widget always sits inside `<div class="activity interactive" number="…">`. An untagged one gets its own activity with the next consecutive number, the following activities renumbered, and one visible `<p style="color: red; font-weight: bold;">Red Flag: …</p>` at the top of the new box. Stop watch and number line (tools) need no activity box. Display components unchanged.
- **Supersedes:** —
- **KB rule:** `03_COMP_CORE_INTERACTIVES/03A` → Universal Rules; `00H` constraint 95
- **PageForge status:** Not yet amalgamated
