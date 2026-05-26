---
description: Creates a technical design with flow, data shape, and affected modules.
---

# Design

Append a `## Design` section to the spec file. Move file from `specs/spec/` to `specs/design/`. Update the index path.

## Output format

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

One flow diagram only — happy path + main failure path. Data: key inputs and outputs only. Modules: files that will be created or modified.

## Next

Tell user the file path. Ask to approve or request changes.

- Approved → continue with [implement.md](implement.md)
- Changes → edit in place, ask again
