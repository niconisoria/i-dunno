# i-dunno

Spec-driven TDD workflow for Claude Code. Idea goes in, working reviewed documented code comes out.

## Skills

| Skill | Role |
|---|---|
| `/define` | Entry point. Guides idea through brainstorm → spec → design, then hands off to `/implement`. |
| `/implement` | TDD loop. Reads spec, researches prior art, writes failing tests, implements, reviews quality and compliance, wraps up. |
| `/gc` | Maintenance. Prunes stale, duplicate, out-of-scope, and unverifiable entries from `CLAUDE.md` and `docs/` files. |

## Workflow

```mermaid
flowchart TD
    A([User + idea]) --> B[define: ask up to 3 questions]
    B --> C[define: write Brainstorm section]
    C --> D{approve?}
    D -- changes --> C
    D -- yes --> E[define: write Story + ACs]
    E --> F{approve?}
    F -- changes --> E
    F -- yes --> G[define: write Design + Modules]
    G --> H{approve?}
    H -- changes --> G
    H -- yes --> I([Run /implement spec-path])
    I --> J[Detect framework]
    J --> K{detected?}
    K -- no --> L([ask user])
    K -- yes --> M[Research prior art in specs + codebase]
    M --> N[Write failing tests]
    N --> O[Write implementation]
    O --> P{tests pass?}
    P -- no, up to 5 --> O
    P -- yes --> Q[Review: quality + compliance]
    Q --> R{issues?}
    R -- fix + retry, up to 3 --> Q
    R -- LGTM --> S[Append file refs + Summary to spec]
    S --> T[Update docs/MEMORY.md]
    T --> U[Mark spec: implemented]
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
