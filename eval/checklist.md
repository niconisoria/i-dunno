# Eval Checklist

Run from `eval/fixture/` with the plugin loaded.

---

## 1. Stage Routing

| Input | Expected |
|---|---|
| `/i-dunno:start "user notifications"` | Creates brainstorm spec, asks questions |
| `/i-dunno:start 20260526100000` | Resumes brainstorm (user_auth) |
| `/i-dunno:start 20260526110000` | Resumes spec stage (payment) |
| `/i-dunno:start 20260526120000` | Resumes design stage (notifications) |
| `/i-dunno:start 20260526090000` | Reports done, offers new spec |

- [ ] Each route lands in the correct reference file
- [ ] Timestamp lookup uses `find`, not hardcoded path

---

## 2. Brainstorm Stage

Run `/i-dunno:start "user notifications"`:

- [ ] Asks up to 3 clarifying questions (question mark format)
- [ ] Waits for user answers before writing
- [ ] Brainstorm section is caveman — no filler, no open questions recorded
- [ ] Keywords extracted and added to INDEX.md
- [ ] Related field populated (check against INDEX.md keywords)
- [ ] On approve: file moves to `specs/spec/`, index path updated

---

## 3. Spec Stage

Run `/i-dunno:start 20260526100000` → approve brainstorm:

- [ ] Story follows "As X, want Y, so Z" format
- [ ] ACs are numbered, no prose
- [ ] Refs listed in frontmatter match Related from brainstorm
- [ ] On approve: file moves to `specs/design/`, index path updated

---

## 4. Design Stage

Run `/i-dunno:start 20260526120000` (notifications, already in design):

- [ ] Flow diagram uses Unicode box-drawing characters only
- [ ] Covers happy path + at least one failure path
- [ ] Data section has input + output shapes
- [ ] Modules section lists files to create/modify
- [ ] On approve: spawns implementer agent

---

## 5. Implementer Agent

Run from design stage approval on `20260526120000`:

- [ ] Reads only: spec file + refs + MEMORY.md — nothing else
- [ ] Detects Minitest from `Gemfile` (MEMORY.md is empty)
- [ ] Writes tests before any implementation code
- [ ] Asks user to run tests, waits for confirmation of failure
- [ ] Writes implementation
- [ ] Asks user to run tests, waits for confirmation of pass
- [ ] Asks user to manually validate each AC
- [ ] Appends file refs as inline links (no `## Files` heading)
- [ ] Appends `## Summary` (2–4 sentences)
- [ ] Moves spec to `implemented/`
- [ ] Updates INDEX.md path from `design/` to `implemented/`

---

## 6. CLAUDE.md / MEMORY.md Guard

During implementer run on `20260526120000`:

- [ ] Does NOT add "use Minitest" to MEMORY.md — already in CLAUDE.md
- [ ] DOES add any novel decision not covered by CLAUDE.md

To test cached path: add `- framework: Minitest` to MEMORY.md, rerun implementer on a fresh spec. Verify detection step is skipped.

---

## 7. Edge Cases

| Scenario | How to test | Expected |
|---|---|---|
| Missing INDEX.md | Delete it, run new idea | Creates INDEX.md |
| Ref file missing | Add nonexistent ref to spec frontmatter | Warns user |
| No framework found | Remove Gemfile, rerun implementer | Asks user |
| Spec already implemented | `/i-dunno:start 20260526090000` | "Done. Want new spec?" |
| User requests change at design | Say "change the flow" | Edits in place, asks again |

---

## 8. Output Quality Spot-Check

Pick any generated file and verify:

- [ ] Caveman style: no "In conclusion", no "It's important to note"
- [ ] Proper markdown: headings hierarchy, no orphan bold
- [ ] Section names capitalized (`## Brainstorm`, not `## brainstorm`)
- [ ] File refs are inline links, not a `## Files` section
- [ ] No implementation-specific code in MEMORY.md entries
