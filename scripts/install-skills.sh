#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${1:-}"
MODE="${MODE:-copy}"

usage() {
  cat <<'EOF'
Usage: scripts/install-skills.sh <target-dir|codex|openclaw>

Installs every skill directory in this pack into the target.
Set MODE=symlink to symlink instead of copy.

Targets:
  codex     ~/.codex/skills
  openclaw  ~/.openclaw/workspace/skills
EOF
}

if [[ -z "$TARGET" || "$TARGET" == "-h" || "$TARGET" == "--help" ]]; then
  usage
  exit 0
fi

case "$TARGET" in
  codex) DEST="$HOME/.codex/skills" ;;
  openclaw) DEST="$HOME/.openclaw/workspace/skills" ;;
  *) DEST="$TARGET" ;;
esac

mkdir -p "$DEST"

for skill in "$ROOT"/*; do
  [[ -d "$skill" ]] || continue
  [[ -f "$skill/SKILL.md" ]] || continue
  name="$(basename "$skill")"
  rm -rf "$DEST/$name"
  if [[ "$MODE" == "symlink" ]]; then
    ln -s "$skill" "$DEST/$name"
  else
    cp -R "$skill" "$DEST/$name"
  fi
  echo "installed $name -> $DEST/$name"
done
