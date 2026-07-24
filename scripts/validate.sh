#!/usr/bin/env sh
set -eu

fail() {
  printf '%s\n' "ERROR: $*" >&2
  exit 1
}

tracked_private="$(git ls-files 'data/*')"
if [ "$tracked_private" != "data/.gitkeep" ]; then
  printf '%s\n' "$tracked_private" >&2
  fail "Only data/.gitkeep may be tracked under data/"
fi

[ -f "AGENTS.md" ] || fail "Missing canonical AGENTS.md"
[ -L "CLAUDE.md" ] || fail "CLAUDE.md must be a compatibility symlink"
[ "$(readlink CLAUDE.md)" = "AGENTS.md" ] || fail "CLAUDE.md must point to AGENTS.md"
[ -L ".claude/skills" ] || fail ".claude/skills must be a compatibility symlink"
[ "$(readlink .claude/skills)" = "../.agents/skills" ] ||
  fail ".claude/skills must point to ../.agents/skills"

for skill in setup-surf surf log-session board-recommend scan; do
  file=".agents/skills/$skill/SKILL.md"
  [ -f "$file" ] || fail "Missing $file"
  first_line="$(sed -n '1p' "$file")"
  [ "$first_line" = "---" ] || fail "$file is missing YAML frontmatter"
  grep -q "^name: $skill$" "$file" ||
    fail "$file name must match its parent directory"
  grep -q "^description: " "$file" ||
    fail "$file is missing a description"
done

for template in profile.md active-location.md sessions.csv personal-calibration.md scan-config.md scan-log.md flight-price-log.csv; do
  [ -f "templates/$template" ] || fail "Missing templates/$template"
done

[ -f "scan/destinations.md" ] || fail "Missing public scan destination catalog"
[ -x "scripts/serpapi_flights.py" ] ||
  fail "scripts/serpapi_flights.py must be executable"
[ -f "scripts/validate_repo.py" ] ||
  fail "Missing scripts/validate_repo.py"

if command -v python3 >/dev/null 2>&1; then
  surf_guide_pycache="${TMPDIR:-/tmp}/surf-guide-pycache"
  PYTHONPYCACHEPREFIX="$surf_guide_pycache" \
    python3 -m py_compile \
      scripts/serpapi_flights.py \
      scripts/test_serpapi_flights.py \
      scripts/validate_repo.py
  PYTHONPYCACHEPREFIX="$surf_guide_pycache" \
    python3 -m unittest discover -s scripts -p 'test_*.py'
  python3 scripts/validate_repo.py
else
  fail "python3 is required for extended validation"
fi

if command -v ruby >/dev/null 2>&1; then
  yaml_files="$(git ls-files '.github/*.yml' '.github/*.yaml' '.github/**/*.yml' '.github/**/*.yaml')"
  if [ -n "$yaml_files" ]; then
    # shellcheck disable=SC2086
    ruby --disable-gems -e \
      'require "yaml"; ARGV.each { |f| YAML.safe_load(File.read(f), permitted_classes: [], permitted_symbols: [], aliases: true) }' \
      $yaml_files
  fi
else
  printf '%s\n' "WARNING: ruby unavailable; skipped GitHub YAML parsing." >&2
fi

printf '%s\n' "Validation passed."
