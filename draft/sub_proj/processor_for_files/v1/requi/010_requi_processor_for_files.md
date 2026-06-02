```yaml
id: requi_processor_for_files
name: "Processor for Files Requirement"
kind: requi
status: active
statement: Provide reusable file-processing library that dispatches to processors by kind and action
version: V00.01.00
updated: '2026-05-24'
```

## Summary

We SHALL provide a reusable **file-processing library** that dispatches to file processors by:

- `kind` (what domain is being processed, e.g. `frontmatter`)
- `action` (what operation to perform, e.g. `visit`,`check`, `read`, `split`)
- `root` (a path that can represent either a folder or file depending on the action)

This is a library-level requirement (no CLI entrypoint required here).

## Requirement

We SHALL provide a python module/package that exposes:

- `process_files(kind: str, action: str, root: pathlib.Path) -> int`

Behavior:

- SHALL dispatch to the correct processor based on `kind`.
- SHALL execute the requested `action`.
- SHALL return a process-style return code:
  - `0` on success
  - non-zero on failure
- SHALL raise a `ValueError` for unknown `kind` or unknown `action`.

Initial supported processor:

- `kind = "frontmatter"`
  - `action = "check"` : validate YAML frontmatter completeness under a folder
  - `action = "read"` : parse YAML frontmatter for a single markdown file
  - `action = "split"` : extract words from paths and store in database

## See Also

- [Split Action Requirement](020_requi_split_action.md) - Split action specification

## Rationale

- Encourages a consistent interface for future repo automation that needs to process many file types.
- Allows re-use from different callers (CLI, tests, scripts, pipelines) without hard-coding domain logic.

## Acceptance Criteria

- Given `kind="frontmatter"`, `action="check"`, and an input folder path:
  - returns `0` when no failures
  - returns non-zero when failures exist
- Given `kind="frontmatter"`, `action="read"`, and an input markdown file:
  - returns `0` and prints parsed YAML to stdout on success
  - returns non-zero and prints a concise error to stderr on failure
- Given `kind="frontmatter"`, `action="split"`, and an input path:
  - extracts and stores words from the path in the database
  - returns `0` on success, non-zero on failure
- Given unknown kinds/actions, raises `ValueError`.

---

## Change History

| Version | Date | Author | Model | Reason |
|---------|------|--------|-------|--------|
| V00.01.00 | 2026-05-24 | ai(cline) | Initial requirement for generic file processor dispatcher |
| V00.02.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Add split action and see also reference |
