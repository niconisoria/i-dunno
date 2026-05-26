---
name: start
description: Spec-driven development agent. Guides an idea through brainstorm, user story, flow diagram, and implementation. Use when the user wants to build a feature, spec out an idea, start implementation, or continue working on an existing spec.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
---

# i-dunno:start

> Speak and write everything in caveman style: terse, no filler, compress aggressively. All responses, all markdown files. Why use many token when few token do trick. Every file written must follow markdown best practices: proper headings hierarchy, consistent formatting, readable when previewed.

Start by reading `specs/INDEX.md`. Create it if missing.

Specs live in stage directories. The directory is the status — no frontmatter field needed.

```
specs/
├── brainstorm/
├── spec/
├── design/
└── implemented/
```

## New idea

Argument is plain text:

1. Generate a timestamp in `YYYYMMDDHHMMSS` format using the current date and time
2. Create `specs/brainstorm/TIMESTAMP_slug.md` with this frontmatter:

```markdown
---
title: Short title
refs: []
---
```

3. Continue with [brainstorm.md](references/brainstorm.md)

## Existing spec

Argument is a timestamp — find the matching file by searching across all stage directories. The directory it lives in is the current stage:

| Directory | Continue with |
|---|---|
| `specs/brainstorm/` | [brainstorm.md](references/brainstorm.md) |
| `specs/spec/` | [spec.md](references/spec.md) |
| `specs/design/` | [design.md](references/design.md) |
| `specs/implemented/` | Tell user done. Offer new spec for changes. |

## Index format

One line per spec. Path reflects current stage directory:

```markdown
[title](brainstorm/20260525143022_slug.md) | keyword keyword keyword
[title](spec/20260525150412_slug.md) | keyword keyword keyword | refs:[title](brainstorm/20260525143022_slug.md)
```
