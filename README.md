# i-dunno

Spec-driven TDD workflow for Claude Code. Give it a spec, get working, reviewed, documented code.

## Agents

| Agent | Role |
|---|---|
| `implementer` | Orchestrator. Reads spec, drives TDD loop, spawns all subagents. |
| `researcher` | Finds prior art in `docs/specs/` and codebase before implementation starts. |
| `reviewer` | Code quality: conventions, security, error handling, test correctness. |
| `validator` | Feature compliance: AC coverage, spec intent, Architecture and UI sections. |
| `gc` | Maintenance: prunes stale/out-of-scope entries from `CLAUDE.md` and all `docs/` reference files. |

## Workflow

```mermaid
flowchart TD
    A([User]) --> B[Read spec + CLAUDE.md + docs reference files]
    B --> C[Detect framework]
    C --> D{bin/run-tests exists?}
    D -- no --> E([ask user])
    D -- yes --> F[researcher: find prior art]
    F --> G[Write failing tests]
    G --> H[Write implementation]
    H --> I{tests pass?}
    I -- no, up to 5 --> H
    I -- yes --> J[reviewer + validator in parallel]
    J --> K{issues?}
    K -- fix + retry failing agents only, up to 3 --> J
    K -- both LGTM --> L[Append file refs + Summary to spec]
    L --> M[Update docs/MEMORY.md]
    M --> N[advance-spec: implemented]
    N --> O([Done])
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
