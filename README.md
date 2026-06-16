# i-dunno

Spec-driven TDD workflow for Claude Code. Idea goes in, working reviewed documented code comes out.

## Agents

| # | Agent | Role |
|---|---|---|
| 1 | `start` | Entry point. Guides idea through brainstorm → spec → design, then spawns implementer. |
| 2 | `implementer` | Orchestrator. Reads spec, drives TDD loop, spawns all subagents. |
| 3 | `researcher` | Finds prior art in `docs/specs/` and codebase before tests are written. |
| 4 | `reviewer` | Code quality: conventions, security, error handling, test correctness. |
| 5 | `validator` | Feature compliance: AC coverage, spec intent, Architecture and UI sections. |
| — | `gc` | Maintenance: prunes stale/out-of-scope entries from `CLAUDE.md` and all `docs/` reference files. |

## Workflow

```mermaid
flowchart TD
    A([User + idea]) --> B[start: ask up to 3 questions]
    B --> C[start: write Brainstorm section]
    C --> D{approve?}
    D -- changes --> C
    D -- yes --> E[start: write Story + ACs]
    E --> F{approve?}
    F -- changes --> E
    F -- yes --> G[start: write Design + Modules]
    G --> H{approve?}
    H -- changes --> G
    H -- yes --> I[implementer: read spec + docs]
    I --> J[Detect framework]
    J --> K{bin/run-tests exists?}
    K -- no --> L([ask user])
    K -- yes --> M[researcher: find prior art]
    M --> N[Write failing tests]
    N --> O[Write implementation]
    O --> P{tests pass?}
    P -- no, up to 5 --> O
    P -- yes --> Q[reviewer + validator in parallel]
    Q --> R{issues?}
    R -- fix + retry failing agents only, up to 3 --> Q
    R -- both LGTM --> S[Append file refs + Summary to spec]
    S --> T[Update docs/MEMORY.md]
    T --> U[advance-spec: implemented]
    U --> V([Done])
```

## Hooks

| Hook | Trigger | Blocks |
|---|---|---|
| `file-guard.sh` | Write / Edit | `.env`, key files, `bin/` writes, out-of-root paths, secret patterns in content |
| `bash-guard.sh` | Bash | `rm -rf`, force push, pipe-to-shell, shell reads of key files |

## Structure

```
docs/
  specs/            — feature specs (status-tracked, workflow-owned)
  MEMORY.md         — decision rationales: why X over Y, never file paths or patterns
  architecture.md   — system-wide structural decisions (hand-maintained, optional)
  design-system.md  — colors, tokens, UI rules (hand-maintained, optional)
```

`CLAUDE.md` — tech stack, folder purposes, and iron-law rules only. Everything else goes in `docs/`.
