---
description: Implements a spec using test-driven development. Reads only the target spec and its references.
---

# Implement

Read `specs/MEMORY.md`, the target spec, and every spec in its `refs` field — nothing else.

Detect the test framework from the project files. If multiple candidates exist, check the file contents for dependencies to narrow it down.

| File | Framework |
|---|---|
| `package.json` | Jest, Vitest, Mocha, Jasmine, or AVA — check `devDependencies` |
| `Gemfile` | RSpec or Minitest |
| `pyproject.toml` / `setup.py` / `pytest.ini` | pytest or unittest |
| `go.mod` | Go test |
| `Cargo.toml` | Cargo test |
| `pom.xml` | JUnit or TestNG |
| `build.gradle` / `build.gradle.kts` | JUnit 5 or Kotest |
| `composer.json` | PHPUnit or Pest |
| `*.csproj` / `*.sln` | xUnit, NUnit, or MSTest — check project references |
| `Package.swift` | XCTest |
| `mix.exs` | ExUnit |
| `pubspec.yaml` | Flutter test or dart test |
| `build.sbt` | ScalaTest or MUnit |
| `project.clj` / `deps.edn` | clojure.test |
| None found | Ask user |

## Test

1. Write tests from the acceptance criteria in the Story section
2. Ask user to run tests — confirm all fail before continuing

## Code

3. Write implementation to make them pass
4. Ask user to run tests — confirm all pass before continuing
5. Ask user to manually validate each criterion in the Story section

## Wrap up

6. Append file references at the bottom of the spec
7. Update `specs/MEMORY.md` with any new project-wide decisions — each entry short, references pattern or existing file, no specific code. Skip if nothing new.
8. Move file from `specs/design/` to `specs/implemented/`
9. Update index path

## Output format

List every file created or modified as an inline link at the bottom of the spec. No heading.

```markdown
[filename](path/to/file.rb) [test_filename](path/to/test_file.rb)
```

## Next

Continue with [summarize.md](summarize.md)
