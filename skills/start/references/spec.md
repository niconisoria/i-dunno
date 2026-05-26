---
description: Turns an approved brainstorm into a user story with acceptance criteria.
---

# Spec

## If `## Story` already exists in the spec

Show it. Ask to approve or request changes.

- Approved → move file from `specs/spec/` to `specs/design/`, update index path, continue with [design.md](design.md)
- Changes → edit in place, ask again

## If `## Story` is missing

Append a `## Story` section to the spec file.

Describe behavior from the user's point of view — what it does, not how. Each criterion on one line. Check the `Related` field in the Brainstorm section and add any referenced specs to the `refs` field in the frontmatter.

### Output format

```markdown
## Story

As [role], want [goal], so [benefit].

AC:
1. Acceptance criterion
2. Acceptance criterion
```

Tell user the file path. Ask to approve or request changes.

- Approved → move file from `specs/spec/` to `specs/design/`, update index path, continue with [design.md](design.md)
- Changes → edit in place, ask again
