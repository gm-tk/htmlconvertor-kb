#!/bin/sh
# build_skills.sh — package each skill folder as an uploadable .zip in dist/.
#
# Claude.ai requires the skill FOLDER to be the root of the zip (not a sub-folder),
# and the folder name to match the skill's `name:` frontmatter exactly.
#
# Run from anywhere:  sh 19_SKILLS/build_skills.sh
set -e

HERE=$(cd "$(dirname "$0")" && pwd)
DIST="$HERE/dist"

command -v zip >/dev/null 2>&1 || {
  echo "ERROR: the 'zip' command is not installed. On Debian/Ubuntu: sudo apt install zip"
  exit 1
}

rm -rf "$DIST"
mkdir -p "$DIST"

count=0
for dir in "$HERE"/*/; do
  name=$(basename "$dir")
  [ "$name" = "dist" ] && continue
  [ -f "$dir/SKILL.md" ] || continue
  ( cd "$HERE" && zip -q -r "$DIST/$name.zip" "$name" -x '*.DS_Store' )
  echo "  built  dist/$name.zip"
  count=$((count + 1))
done

echo ""
echo "build_skills: $count skill zip(s) in 19_SKILLS/dist/"
