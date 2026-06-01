```yaml
id: requi_yaml_frontmatter_check
name: "YAML Frontmatter Check Requirement"
kind: requi
status: active
version: V00.08.00
updated: '2026-05-24'
statement: Provide YAML frontmatter tooling for validation and reading
```

# 010_requi_yaml_frontmatter_check

## Summary

We SHALL provide YAML frontmatter tooling that can:

- `check`: validate YAML frontmatter completeness for markdown files under a folder.
- `read`: read/parse YAML frontmatter for a single markdown file (for debugging and authoring support).

The tooling is invoked via the generic dispatcher defined in:

- `005_requi_file_processor.md`

## Requirement (check)

We SHALL provide a check that validates **YAML frontmatter completeness** for markdown files.

Prefix: frontmatter_attrib

The checker :

1. SHALL be callable via `process_files(kind="frontmatter", action="check", root=<folder>)`.
2. SHALL accept a **folder path(s)** (`root`) and recursively scan `*.md` files under it. Multiple root folders can be comma-separated.
3. SHALL accept an optional `--ext` argument to filter by file extension (e.g., `--ext md` matches files ending in `.md`).
4. SHALL only process files matching the pattern `NNN_<abbrev>_<title>.<extension>` where `<abbrev>` corresponds to the `kind` attribute.

### File pattern filtering

Prefix: file_pat

The root argument enables checking of all files below the folder which follow the naming pattern:

1. `NNN_<abbrev><title>.<extension>`

Where:

1. `NNN_` is a 3-digit prefix (e.g., `010_`, `020_`)
2. `<abbrev>` is the kind abbreviation defined in `ai_env/ai_entities/conventions/80_conv_abbrevs.md`
3. `<title>` is a descriptive title
4. `<extension>` can be `.md` or other extensions filtered via `--ext`

### Required attributes (completeness)

Prefix: attr_complete

For this repo, "complete" frontmatter means the following attributes are present:

1. `id`
2. `name`
3. `kind` (optional)
4. `tags` (optional)
5. `status`
6. `version`
7. `updated`
8. `statement` (one sentence)

Prefix: attr_sequence

Additionally, `name` MUST NOT repeat the `kind` value and SHOULD be human-readable. See `030_requi_frontmatter_attribute_sequence.md` for details.

Prefix:  

1. Extra attributes are allowed.
2. The checker SHALL treat missing attributes as a failure.

### Multiple root folders

The `root` argument accepts multiple comma-separated folder paths. All folders are scanned and results are aggregated.

## Rationale

1. Frontmatter is used as stable metadata for indexing and automation.
2. A completeness check prevents silent drift and partial documents.

## Acceptance Criteria

1. Given a folder argument, the tool scans all `*.md` files under that folder.
2. Multiple comma-separated root folders are supported; all are scanned and results aggregated.
3. For each scanned file:
   1. If frontmatter is missing: the tool reports the file and fails (non-zero exit).
   2. If the YAML frontmatter is malformed: the tool reports the file + YAML error and fails.
   3. If any required attribute is missing: the tool reports the file + missing keys and fails.
   4. If `kind` does not match the file prefix mapping: the tool reports the file + kind mismatch and fails.
4. On success (no failures), the tool exits with `0`.
5. The tool output is concise and greppable.

### Frontmatter attribute sequence / formatting

The canonical attribute sequence and formatting rules are specified in:

1. `030_requi_frontmatter_attribute_sequence.md`

### Example target

1. `projects/requi_ai_env/v4/requi/010_requi_simulate_person_core_aspects.md` is an example of a file with complete frontmatter.

## Test Notes (future)

- Unit tests should cover:
  1. missing frontmatter
  2. unterminated frontmatter (`---` without closing)
  3. invalid YAML
  4. missing keys
  5. happy path

---

## Change History

| Version | Date | Author | Reason |
|---------|------|--------|--------|
| V00.01.00 | 2026-05-24 | ai(cline) | Initial requirement for YAML frontmatter completeness checker |
| V00.02.00 | 2026-05-24 | ai(cline) | Define `check` explicitly and split out `read` into a separate requirement |
| V00.03.00 | 2026-05-24 | ai(cline) | Add `kind` as mandatory frontmatter attribute |
| V00.04.00 | 2026-05-24 | ai(cline) | Add `kind` value validation against filename prefix |
| V00.05.00 | 2026-05-24 | ai(cline) | Add `--ext` argument and file pattern filtering |
| V00.06.00 | 2026-05-24 | ai(cline) | Add `kind` value validation against filename prefix |
| V00.07.00 | 2026-05-24 | ai(cline) | Number all SHALL statements and add numbering to other lists |
| V00.08.00 | 2026-06-01 | ai(cline) | Number file pattern filtering list items |
| V00.09.00 | 2026-06-01 | raoulExtra | Add name attribute sequence and readability rules |
