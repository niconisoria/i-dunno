---
description: Explores a new idea and writes the brainstorm section of a spec.
---

# Brainstorm

Caveman: terse, no filler, compress aggressively.

## If `## Brainstorm` already exists in the spec

Show it. Ask to approve or request changes.

- Approved → move file from `specs/brainstorm/` to `specs/spec/`, update index path, continue with [spec.md](spec.md)
- Changes → edit in place, ask again

## If `## Brainstorm` is missing

Before writing, ask the user up to three short questions to gather more context. Wait for answers.

Then write the `## Brainstorm` section in the spec file. Keep it short — five to ten lines. No implementation details. Cover the problem, scope, constraints, and any related specs found by matching keywords in the index. Do not record open questions — use answers to inform the content only.

Extract three to five keywords. Add the spec entry to `specs/INDEX.md` with the keywords.

### Output format

```markdown
## Brainstorm

Problem. Scope. Constraints.

Related: [title](brainstorm/YYYYMMDDHHMMSS_slug.md)
```

Tell user the file path. Ask to approve or request changes.

- Approved → move file from `specs/brainstorm/` to `specs/spec/`, update index path, continue with [spec.md](spec.md)
- Changes → edit in place, ask again
