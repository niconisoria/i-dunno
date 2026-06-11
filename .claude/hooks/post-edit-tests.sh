#!/usr/bin/env bash
# PostToolUse: run tests after Write/Edit — skip docs/config, skip unknown framework.
set -uo pipefail

input=$(cat)

file_path=$(echo "$input" \
  | grep -oE '"file_path"[[:space:]]*:[[:space:]]*"[^"]*"' \
  | grep -oE '"[^"]*"$' \
  | tr -d '"')

[[ -z "$file_path" ]] && exit 0

case "$file_path" in
  *.md|*.json|*.yaml|*.yml|*.txt|*.lock|*.toml) exit 0 ;;
  .claude/*|docs/*) exit 0 ;;
esac

output=$(bash bin/run-tests 2>&1)
exit_code=$?

echo "$output" | grep -q "Unknown framework" && exit 0

echo "$output"
exit $exit_code
