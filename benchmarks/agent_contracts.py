"""
Deterministic graders for i-dunno agent output contracts.

Each function takes a string (agent output) and returns:
  {"pass": bool, "score": 0|1, "reason": str}

Proven by tests/test_agent_contracts.py — no API key needed.
Used by behavioral evals (benchmarks/behavior.yaml) for scored LLM runs.
"""

import re


def reviewer_contract(output: str) -> dict:
    """Reviewer must return exactly LGTM or a numbered issue list — nothing else."""
    text = (output or "").strip()

    if text == "LGTM":
        return {"pass": True, "score": 1, "reason": "Returned LGTM."}

    lines = [line for line in text.splitlines() if line.strip()]
    numbered = [line for line in lines if re.match(r"^\d+\.", line.strip())]

    if not lines:
        return {"pass": False, "score": 0, "reason": "Empty output."}

    if numbered and len(numbered) == len(lines):
        return {
            "pass": True,
            "score": 1,
            "reason": f"Returned {len(numbered)}-item issue list.",
        }

    if "LGTM" in text and numbered:
        return {
            "pass": False,
            "score": 0,
            "reason": "Mixed LGTM and issue list — must be one or the other.",
        }

    return {
        "pass": False,
        "score": 0,
        "reason": "Output is neither LGTM nor a clean numbered list.",
    }


def validator_contract(output: str) -> dict:
    """Validator must return exactly LGTM or a numbered issue list — same contract as reviewer."""
    return reviewer_contract(output)


def researcher_format(output: str) -> dict:
    """Researcher must return specs: and files: sections with dash-prefixed entries or (none)."""
    text = (output or "").strip()

    has_specs = bool(re.search(r"^specs:\s*$", text, re.MULTILINE))
    has_files = bool(re.search(r"^files:\s*$", text, re.MULTILINE))

    if not has_specs or not has_files:
        return {
            "pass": False,
            "score": 0,
            "reason": "Missing specs: or files: section header.",
        }

    sections = re.split(r"^(specs:|files:)\s*$", text, flags=re.MULTILINE)
    for section in sections:
        section = section.strip()
        if not section or section in ("specs:", "files:"):
            continue
        lines = [line.strip() for line in section.splitlines() if line.strip()]
        for line in lines:
            if not re.match(r"^-\s+\S+.*—.*|^\(none\)$", line):
                return {
                    "pass": False,
                    "score": 0,
                    "reason": f"Malformed entry (expected '- path — summary' or '(none)'): {line!r}",
                }

    return {"pass": True, "score": 1, "reason": "Output matches specs:/files: format."}
