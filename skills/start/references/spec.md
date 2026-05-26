---
description: Turns an approved brainstorm into a user story with acceptance criteria.
---

# Spec

Append a `## Story` section to the spec file. Update the index path.

Describe behavior from the user's point of view — what it does, not how. Each criterion on one line. Check the `Related` field in the Brainstorm section and add any referenced specs to the `refs` field in the frontmatter.

## Output format

```markdown
## Story

As a [role], I want [goal], so that [benefit].

1. Acceptance criterion
2. Acceptance criterion
```

## Next

Tell user the file path. Ask to approve or request changes.

- Approved → move file from `specs/spec/` to `specs/design/`, update index path, continue with [design.md](design.md)
- Changes → edit in place, ask again
