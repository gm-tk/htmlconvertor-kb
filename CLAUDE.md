# CLAUDE.md — Te Kura HTML Convertor Knowledge Base (maintenance rules)

Read this first in every session. This repository IS the knowledge base for the Te Kura
"HTML Convertor" Claude project — the project's knowledge files sync from here. Your job
in this repo is **maintenance**: applying instruction changes (Update Mode changes,
Comparison-report outcomes, new conventions) by **editing the granular part files in
place**. You are NOT converting modules here and you never invent or reword conversion
rules on your own initiative — you apply the changes the designer gives you.

---

## 1. The layout (why it looks like this)

The original sixteen knowledge files grew so large that regenerating one in full timed
out. They were therefore split (2026-07-27, byte-identical — proof in
`tools/kb_manifest.json`) into **topics**:

- A large topic is a **folder** named after the original file
  (e.g. `02_DATA_CONTENT_VERIFICATION/`) holding small lettered **parts**
  (`02A_…`, `02B_…`). Each part opens with a provenance header and a
  `<!-- KB-PART-BODY-START -->` sentinel; everything below the sentinel is
  source-of-truth content.
- A small topic is still a **single file** (`06_…`, `08_…`, `10_…`, `13_…`).
- `INDEX.md` is the map: every content file, what it contains, its size.
- Cross-references in the content to old filenames (e.g. "see
  `02_DATA_CONTENT_VERIFICATION.md`") resolve to the folder of the same name.

## 2. The five non-negotiable rules

1. **EDIT IN PLACE, NEVER REGENERATE A TOPIC.** A change touches only the specific
   part file(s) that own the affected rule. Find them via `INDEX.md` (or grep).
   Full-topic regeneration is the failure mode this repo exists to eliminate.
2. **SIZE LIMITS ARE HARD.** No content `.md` may exceed **40,000 bytes** (the check
   script FAILS the commit). At **30,000 bytes** a file is due to be split as part of
   the very next update that touches it (§4). Aim for parts of 10–25 KB.
3. **RUN THE GUARD AFTER EVERY CHANGE:** `python3 tools/check_kb.py` must pass
   (it also runs from the pre-commit hook and in CI). Never commit over a FAIL.
4. **NEVER LOSE CONTENT.** Edits are surgical diffs; the git diff is the audit trail.
   The change ledger is append-only — never rewrite or delete an existing CL row.
5. **KEEP THE FURNITURE IN SYNC.** Any edit to a part refreshes that part's
   `> **Last updated:**` line (first line, format: `> **Last updated:** Monday, 27th
   July, 2026 9:30 PM`). Adding/splitting/renaming a file updates `INDEX.md` in the
   same commit.

## 3. The update ritual (every change request)

1. **Locate** — use `INDEX.md` + grep to find every part that owns the affected rule
   (the Update Mode "blast-radius sweep" in `11_UPDATE_MODE/` still applies: one
   change often touches a component part AND `00_MASTER_INSTRUCTIONS/00D/00E`
   constraints AND `02_…/02D_COMMENT_POLICY_CONSTRAINTS.md`).
2. **Check the ledger** — read `12_CHANGE_LEDGER/12A_LEDGER_CORE_AND_LOCKS.md`
   (locked decisions block conflicting changes; escalate per `11_UPDATE_MODE/`).
3. **Edit** the part file(s) in place; refresh each touched part's timestamp.
4. **Record** — append a new `| CL-nnnn | … |` row to the **latest**
   `12_CHANGE_LEDGER/12x_CHANGE_HISTORY_…` part (next sequential CL id). If that
   part is over 30 KB, start the next history part instead (§4).
5. **Verify** — `python3 tools/check_kb.py` passes; `git diff` shows exactly the
   intended change and nothing else.
6. **Commit** — message: `CL-nnnn: <summary>` (or `KB: <summary>` for
   non-ledger housekeeping). Push only with the designer's go-ahead.

## 4. How to split a file that has grown past 30 KB

1. Choose a clean boundary: an `##` heading (or `#` internal doc boundary) that
   divides the file into coherent halves — never mid-section, never inside a code
   fence.
2. Create the next lettered part in the same folder (e.g. `03G_…`). Give it the
   standard header: timestamp line, `> **Granular part …** of the original file`
   provenance line, sibling-folder line, blank line, `<!-- KB-PART-BODY-START -->`.
3. **Move** the content verbatim — cut from the old part, paste below the new
   part's sentinel. No rewording, no re-ordering.
4. Ledger history parts only: if the split lands mid-table, repeat the table's
   two header lines directly below the sentinel and note the repetition in the
   provenance header (see `12C`/`12D` for the pattern).
5. Update `INDEX.md` (new entry + adjusted "contains" lines) and re-run the guard.
6. If a single-file topic (e.g. `13_SPLIT_MODE.md`) outgrows the limit: create a
   folder of that exact name, split into `13A_…`/`13B_…` inside it, delete the
   root file, update `INDEX.md`.

## 5. Things that trip people up

- **The sentinel is load-bearing.** Tools treat everything above
  `<!-- KB-PART-BODY-START -->` as furniture and everything below as verbatim
  content. Never edit content into the header zone; never delete the sentinel.
- **`_project_instructions_.md` is special** — it is the Claude.ai project's
  system-prompt text, not synced knowledge. If it changes, the designer must
  manually re-paste it into the project's Instructions field. Say so in the
  commit message and tell the designer.
- **Part A of each split topic still contains the original file's own
  `> **Last updated:**` line inside its body** (verbatim-migration artefact).
  The authoritative stamp is the header (first) line of each part.
- **The ledger CL sequence is checked** — `check_kb.py` fails on duplicate or
  out-of-order CL ids across the history parts.
- **Sync lag** — after pushing, the Claude.ai project reflects changes only when
  its GitHub-synced knowledge re-syncs. Remind the designer if a change is urgent.
