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

for skill in setup-surf surf log-session board-buy; do
  file=".claude/skills/$skill/SKILL.md"
  [ -f "$file" ] || fail "Missing $file"
  first_line="$(sed -n '1p' "$file")"
  [ "$first_line" = "---" ] || fail "$file is missing YAML frontmatter"
done

for template in profile.md active-location.md sessions.csv personal-calibration.md; do
  [ -f "templates/$template" ] || fail "Missing templates/$template"
done

if command -v rg >/dev/null 2>&1; then
  if rg -n --hidden \
    -g '!scripts/validate.sh' \
    -e 'ghp_[A-Za-z0-9]{20,}' \
    -e 'github_pat_[A-Za-z0-9_]+' \
    -e 'sk-[A-Za-z0-9]{20,}' \
    -e 'SERPAPI_KEY[[:space:]]*=' \
    .; then
    fail "Possible credential detected"
  fi
else
  if grep -R -E \
    'ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]+|sk-[A-Za-z0-9]{20,}|SERPAPI_KEY[[:space:]]*=' \
    --exclude=validate.sh .; then
    fail "Possible credential detected"
  fi
fi

if command -v rg >/dev/null 2>&1; then
  if rg -n \
    -e 'exact accommodation' \
    -e 'seller phone' \
    -e 'raw session row' \
    locations/portugal; then
    fail "Possible private-data language detected in a public location pack"
  fi
fi

printf '%s\n' "Validation passed."
