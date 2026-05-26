---
description: Creates a technical design with flow, data shape, and affected modules.
---

# Design

Caveman: terse, no filler, compress aggressively.

## If `## Design` already exists in the spec

Show it. Ask to approve or request changes.

- Approved → continue with [implement.md](implement.md)
- Changes → edit in place, ask again

## If `## Design` is missing

Append a `## Design` section to the spec file.

### Output format

```markdown
## Design

### Flow

┌───────┐     ┌──────────┐     ┌─────────┐
│ start │ ──▶ │ validate │ ──▶ │ success │
└───────┘     └──────────┘     └─────────┘
                   │
              ┌─────────┐
              │  error  │
              └─────────┘

### Data

input: { field: type }
output: { field: type }

### Modules

- `path/to/file` — what changes
```

One flow diagram only — happy path + main failure path. Use only Unicode box-drawing characters (`┌ ─ ┐ │ └ ┘ ──▶`). No other diagram formats. Data: key inputs and outputs only. Modules: files that will be created or modified.

Tell user the file path. Ask to approve or request changes.

- Approved → continue with [implement.md](implement.md)
- Changes → edit in place, ask again
