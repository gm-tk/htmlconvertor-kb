#!/usr/bin/env python3
"""check_kb.py — the knowledge-base guard. Run from anywhere: python3 tools/check_kb.py

Enforces the repo's structural rules so no file can silently grow unwieldy and no
part can go missing. Exits non-zero on any FAIL (used by the pre-commit hook and CI).

Checks:
  1. SIZE      — no content .md over HARD_LIMIT bytes (FAIL); over SOFT_LIMIT is a WARN
                 meaning "split this file at its next update" (see CLAUDE.md ritual).
  2. HEADERS   — every part file inside a topic folder carries the provenance header
                 ('> **Granular part') and the KB-PART-BODY-START sentinel.
  3. INDEX     — every content .md on disk is listed in INDEX.md, and every path
                 INDEX.md lists exists on disk (no orphans, no dead links).
  4. STAMPS    — every content file carries a '> **Last updated:**' line.
  5. LEDGER    — across the 12_CHANGE_LEDGER history parts, CL-nnnn IDs are unique
                 and strictly ascending (catches lost/duplicated ledger rows).
  6. SKILLS    — 19_SKILLS/<name>/SKILL.md carries YAML frontmatter whose `name`
                 matches its folder (<= 64 chars) and whose `description` is within
                 Claude.ai's 200-character limit. 19_SKILLS is exempt from checks
                 1-4: a SKILL.md opens with frontmatter and cannot carry the
                 '> **Last updated:**' stamp or the KB-PART-BODY-START sentinel.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOFT_LIMIT = 30_000   # bytes — WARN: split at next update
HARD_LIMIT = 40_000   # bytes — FAIL: must split before committing
SENTINEL = "<!-- KB-PART-BODY-START -->"
NON_CONTENT = {"README.md", "CLAUDE.md", "INDEX.md"}
# Not KB content parts: the tooling, and the Claude Skill sources (check 6 covers those).
SKIP_DIRS = {"tools", "19_SKILLS"}

fails, warns = [], []

def content_files():
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if not d.startswith(".") and d not in SKIP_DIRS]
        for fn in sorted(filenames):
            if fn.endswith(".md") and not (dirpath == ROOT and fn in NON_CONTENT):
                out.append(os.path.join(dirpath, fn))
    return sorted(out)

files = content_files()

# 1. SIZE
for p in files:
    size = os.path.getsize(p)
    rel = os.path.relpath(p, ROOT)
    if size > HARD_LIMIT:
        fails.append(f"SIZE: {rel} is {size:,} bytes (> hard limit {HARD_LIMIT:,}) — split it NOW per CLAUDE.md")
    elif size > SOFT_LIMIT:
        warns.append(f"SIZE: {rel} is {size:,} bytes (> soft limit {SOFT_LIMIT:,}) — split it at its next update")

# 2. HEADERS + 4. STAMPS
for p in files:
    rel = os.path.relpath(p, ROOT)
    text = open(p, encoding="utf-8").read()
    in_topic_folder = os.path.dirname(p) != ROOT
    if in_topic_folder:
        head = "\n".join(text.split("\n")[:6])
        if "> **Granular part" not in head:
            fails.append(f"HEADER: {rel} missing provenance header ('> **Granular part') in its first lines")
        if SENTINEL not in text:
            fails.append(f"HEADER: {rel} missing {SENTINEL} sentinel")
    if "> **Last updated:**" not in text.split("\n", 1)[0]:
        fails.append(f"STAMP: {rel} first line is not a '> **Last updated:**' stamp")

# 3. INDEX
index_path = os.path.join(ROOT, "INDEX.md")
if not os.path.exists(index_path):
    fails.append("INDEX: INDEX.md missing at repo root")
else:
    idx = open(index_path, encoding="utf-8").read()
    listed = set(re.findall(r"\*\*`([^`]+\.md)`\*\*", idx))
    on_disk = {os.path.relpath(p, ROOT) for p in files}
    on_disk.add("_project_instructions_.md") if os.path.exists(os.path.join(ROOT, "_project_instructions_.md")) else None
    for p in sorted(on_disk):
        if p not in listed:
            fails.append(f"INDEX: {p} exists on disk but is not listed in INDEX.md")
    for p in sorted(listed):
        if p not in on_disk and not p.startswith(("CLAUDE", "README", "tools/")):
            fails.append(f"INDEX: INDEX.md lists {p} but it does not exist on disk")

# 5. LEDGER integrity
ledger_dir = os.path.join(ROOT, "12_CHANGE_LEDGER")
if os.path.isdir(ledger_dir):
    ids = []
    for fn in sorted(os.listdir(ledger_dir)):
        if "CHANGE_HISTORY" in fn and fn.endswith(".md") and "FOOTNOTE" not in fn:
            body = open(os.path.join(ledger_dir, fn), encoding="utf-8").read()
            body = body.split(SENTINEL, 1)[-1]
            ids += [int(m) for m in re.findall(r"^\| CL-(\d{4}) \|", body, re.M)]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        fails.append(f"LEDGER: duplicate CL ids across history parts: {sorted(dupes)}")
    if ids != sorted(ids):
        fails.append("LEDGER: CL ids are not in ascending order across history parts")
    if ids:
        missing = sorted(set(range(min(ids), max(ids) + 1)) - set(ids))
        if missing:
            warns.append(f"LEDGER: gaps in CL id sequence (may be intentional): {missing}")


# 6. SKILLS — the Claude Skill sources in 19_SKILLS/
n_skills = 0
skills_dir = os.path.join(ROOT, "19_SKILLS")
if os.path.isdir(skills_dir):
    for d in sorted(os.listdir(skills_dir)):
        sub = os.path.join(skills_dir, d)
        if d == "dist" or not os.path.isdir(sub):
            continue
        sp = os.path.join(sub, "SKILL.md")
        if not os.path.exists(sp):
            fails.append(f"SKILL: 19_SKILLS/{d}/ has no SKILL.md")
            continue
        n_skills += 1
        text = open(sp, encoding="utf-8").read()
        m = re.match(r"---\n(.*?)\n---\n", text, re.S)
        if not m:
            fails.append(f"SKILL: 19_SKILLS/{d}/SKILL.md has no YAML frontmatter block")
            continue
        fm = m.group(1)
        nm = re.search(r"^name:\s*(.+?)\s*$", fm, re.M)
        ds = re.search(r"^description:\s*(.+?)\s*$", fm, re.M)
        if not nm:
            fails.append(f"SKILL: 19_SKILLS/{d}/SKILL.md frontmatter has no 'name:'")
        elif nm.group(1) != d:
            fails.append(f"SKILL: 19_SKILLS/{d}/SKILL.md name '{nm.group(1)}' != folder name — Claude.ai will reject the upload")
        elif len(nm.group(1)) > 64:
            fails.append(f"SKILL: 19_SKILLS/{d} name is {len(nm.group(1))} chars (> 64 limit)")
        if not ds:
            fails.append(f"SKILL: 19_SKILLS/{d}/SKILL.md frontmatter has no 'description:'")
        elif len(ds.group(1)) > 200:
            fails.append(f"SKILL: 19_SKILLS/{d} description is {len(ds.group(1))} chars (> 200 limit) — Claude.ai will reject the upload")

for w in warns:
    print(f"WARN  {w}")
for f in fails:
    print(f"FAIL  {f}")
print(f"\ncheck_kb: {len(files)} content files, {n_skills} skills, {len(warns)} warnings, {len(fails)} failures")
sys.exit(1 if fails else 0)
