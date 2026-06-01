```yaml
id: requi_name_check
name: Name Check Requirement
kind: requi
status: active
statement: Files and directories in the processor_for_files project MUST follow naming conventions
version:
updated:
```

## Summary

We SHALL provide validation that all files and directories follow the naming convention defined in `040_conv_for_namings_of_files.md`.

## Requirement

We SHALL check that:

1. Files follow the pattern `<number>_<kind>_<noun>_<connector>_<rest>.md` or `<number>_<kind>_<noun>.md`
2. Directories follow the pattern `<noun>_<connector>_<noun>` or `<kind>_<noun>`
3. Numbers are 3-digit (e.g., `010_`, `020_`)
4. Kind prefixes are valid (e.g., `requi_`, `def_`, `asp_`)
5. Verb forms in `-ed` or `-er` patterns are recognized (see `020_requi_verb_recognition.md`)
6. Processed names are split into POS and organized into `<data>/<first_two_letters>/<word>.md` structure (see `030_requi_pos_splitting.md`)

## Rationale

- Ensures consistency across the project
- Enables automated tooling to locate and process files
- Supports cross-referencing and search

## Acceptance Criteria

- Given a directory, the tool reports all files that don't match the naming pattern
- Given a directory, the tool reports all directories that don't match the naming pattern

---

## Change History

| Version | Date | Author | Reason |
|---------|------|--------|--------|
| V00.01.00 | 2026-06-01 | raoulExtra | Initial requirement for name checking |