```yaml
id: requi_visitor_for_files
name: requi_visitor_for_files
kind: requi
related_id: conv_for_namings_of_files
see_also: conv_for_namings_of_files
status: active
statement: Output the files the processor visits based on root paths and extensions
version:
updated:
```

## Summary

We SHALL provide a file visit capability that outputs the list of files matching the specified criteria.

## Requirement

We SHALL provide a `visit` action that:

1. SHALL be callable via `process_files(kind="frontmatter", action="visit", root=<folder>)`.
2. SHALL accept a **folder path(s)** (`root`) and recursively scan files under it. Multiple root folders can be comma-separated.
3. SHALL accept an optional `--ext` argument to filter by file extension (e.g., `--ext md` matches files ending in `.md`).


## Output

- SHALL output each matching file path, one per line, to stdout.
- SHALL output nothing if no files match.

## Rationale

- Allows debugging which files will be processed before running other actions.
- Enables preview of the file set before running checks or other operations.

## Acceptance Criteria

1. Given a root folder, the tool outputs all matching `*.md` files under that folder.
2. Multiple comma-separated root folders are supported; all files are output.
3. The `--ext` argument filters files by extension.
4. File pattern filtering is applied based on the kind abbreviation.
5. Output is one file path per line.

---

## Change History

| Version | Date | Author | Reason |
|---------|------|--------|--------|
| V00.01.00 | 2026-06-01 | ai(cline) | Initial requirement for file visit output |
| V00.02.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Add id and related_id to frontmatter, update see_also reference |