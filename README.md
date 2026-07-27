# Te Kura HTML Convertor — Knowledge Base

This repository is the single source of truth for the knowledge files behind the
**Te Kura HTML Convertor** Claude project (the Writer-Template-to-HTML conversion
agent for D2L/Brightspace).

**Why it exists:** the original sixteen knowledge files grew so large that
regenerating one in a chat timed out. On **27 July 2026** they were split —
byte-identically, proof in `tools/kb_manifest.json` — into small "part" files
(all under 30 KB) organised as one folder per original file. Instruction changes
are now applied by **Claude Code editing the specific part in place**, with git
providing the audit trail, instead of regenerating whole files in a chat.

**How to navigate:** start at **`INDEX.md`** — it lists every file and what it
contains. **`CLAUDE.md`** holds the maintenance rules (edit-in-place ritual,
size limits, how to split a growing file, ledger conventions).

**Guard rails:** `python3 tools/check_kb.py` enforces the structure — hard
40 KB size limit, provenance headers, index completeness, change-ledger
integrity. It runs from the pre-commit hook (`git config core.hooksPath
.githooks` once per clone) and in GitHub Actions on every push.

**Connected Claude project:** the project's knowledge syncs from this repo.
`_project_instructions_.md` is the exception — it is the project's
system-prompt text and must be re-pasted into the project's Instructions field
manually whenever it changes.
