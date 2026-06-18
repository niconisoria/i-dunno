#!/usr/bin/env python3
# Unit tests for benchmarks/agent_contracts.py — no API key needed.
# Run: pytest tests/test_agent_contracts.py

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from benchmarks.agent_contracts import (
    researcher_format,
    reviewer_contract,
    validator_contract,
)


# ── reviewer_contract ─────────────────────────────────────────────────────────


class TestReviewerContract:
    def test_lgtm_passes(self):
        r = reviewer_contract("LGTM")
        assert r["pass"] is True
        assert r["score"] == 1

    def test_lgtm_with_whitespace_passes(self):
        r = reviewer_contract("  LGTM  ")
        assert r["pass"] is True

    def test_numbered_list_passes(self):
        r = reviewer_contract(
            "1. `src/auth.py` — missing input validation — `user = req.body`\n"
            "2. `src/db.py` — SQL string concatenation — `query = 'SELECT' + id`"
        )
        assert r["pass"] is True
        assert r["score"] == 1

    def test_single_issue_passes(self):
        r = reviewer_contract(
            "1. `main.py` — no error handling on file open — `open(path)`"
        )
        assert r["pass"] is True

    def test_empty_output_fails(self):
        r = reviewer_contract("")
        assert r["pass"] is False
        assert r["score"] == 0

    def test_mixed_lgtm_and_issues_fails(self):
        r = reviewer_contract("LGTM\n1. `foo.py` — something wrong — `x = 1`")
        assert r["pass"] is False

    def test_prose_explanation_fails(self):
        r = reviewer_contract(
            "The code looks good overall. There are a few minor issues to consider."
        )
        assert r["pass"] is False

    def test_partial_numbered_list_fails(self):
        r = reviewer_contract(
            "1. `foo.py` — issue here — `x`\nAlso consider refactoring this."
        )
        assert r["pass"] is False


# ── validator_contract ────────────────────────────────────────────────────────


class TestValidatorContract:
    def test_lgtm_passes(self):
        assert validator_contract("LGTM")["pass"] is True

    def test_numbered_list_passes(self):
        r = validator_contract(
            "1. `feature.py` — acceptance criterion 3 not implemented: no rate limit check"
        )
        assert r["pass"] is True

    def test_empty_fails(self):
        assert validator_contract("")["pass"] is False


# ── researcher_format ─────────────────────────────────────────────────────────


class TestResearcherFormat:
    def test_valid_full_output_passes(self):
        r = researcher_format(
            "specs:\n"
            "- docs/specs/auth.md — JWT strategy decision\n"
            "\n"
            "files:\n"
            "- src/auth.rb — token verification pattern\n"
        )
        assert r["pass"] is True
        assert r["score"] == 1

    def test_none_entries_pass(self):
        r = researcher_format("specs:\n(none)\n\nfiles:\n(none)")
        assert r["pass"] is True

    def test_missing_specs_section_fails(self):
        r = researcher_format("files:\n- src/foo.py — something relevant")
        assert r["pass"] is False

    def test_missing_files_section_fails(self):
        r = researcher_format("specs:\n- docs/specs/foo.md — something")
        assert r["pass"] is False

    def test_empty_output_fails(self):
        r = researcher_format("")
        assert r["pass"] is False

    def test_malformed_entry_fails(self):
        r = researcher_format(
            "specs:\n"
            "- docs/specs/auth.md — valid entry\n"
            "  some prose that doesn't belong here\n"
            "\n"
            "files:\n"
            "(none)"
        )
        assert r["pass"] is False
