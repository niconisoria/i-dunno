#!/usr/bin/env bash
# PostToolUse: run tests after Write/Edit — skip docs/config, skip unknown framework.
set -uo pipefail

input=$(cat)

file_path=$(jq -r '.tool_input.file_path // .file_path // ""' <<< "$input" 2>/dev/null)

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
