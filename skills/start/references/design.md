---
description: Creates a flow diagram showing how the feature works technically.
---

# Design

Append a `## Flow` section to the spec file. Update the index path.

Draw a Unicode box-drawing diagram. Cover the happy path and the main failure path. One diagram only.

## Output format

```markdown
## Flow

┌───────┐     ┌──────────┐     ┌─────────┐
│ start │ ──▶ │ validate │ ──▶ │ success │
└───────┘     └──────────┘     └─────────┘
                    │
               ┌─────────┐
               │  error  │
               └─────────┘
```

## Next

Tell user the file path. Ask to approve or request changes.

- Approved → continue with [implement.md](implement.md)
- Changes → edit in place, ask again
