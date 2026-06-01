```yaml
id: requi_visitor_for_files
name: requi_visitor_for_files
kind: requi
related_id: conv_for_namings_of_files
see_also: conv_for_namings_of_files
status: active
statement: Output the files the processor visits based on root paths and extensions, with logging for files missing kind YAML entries
version: V00.03.00
updated: '2026-06-01'
```

## Summary

We SHALL provide a file visit capability that outputs the list of files matching the specified criteria.

## Requirement

We SHALL provide a `visit` action that:

1. SHALL be callable via `process_files(kind="frontmatter", action="visit", root=<folder>)`.
2. SHALL accept a **folder path(s)** (`root`) and recursively scan files under it. Multiple root folders can be comma-separated.
3. SHALL accept an optional `--ext` argument to filter by file extension (e.g., `--ext md` matches files ending in `.md`).
4. SHALL produce a log file for warnings if files have no related "kind" YAML entry.

## Output

- SHALL output each matching file path, one per line, to stdout.
- SHALL output nothing if no files match.
- SHALL write warnings to a log file for files without related "kind" YAML entries.

## Rationale

- Allows debugging which files will be processed before running other actions.
- Enables preview of the file set before running checks or other operations.

## Acceptance Criteria

1. Given a root folder, the tool outputs all matching `*.md` files under that folder.
2. Multiple comma-separated root folders are supported; all files are output.
3. The `--ext` argument filters files by extension.
4. File pattern filtering is applied based on the kind abbreviation.
5. Output is one file path per line.
6. A log file is produced for files without related "kind" YAML entries.

---

## Change History

| Version | Date | Author | Reason |
|---------|------|--------|--------|
| V00.01.00 | 2026-06-01 | ai(cline) | Initial requirement for file visit output |
| V00.02.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Add id and related_id to frontmatter, update see_also reference |
| V00.03.00 | 2026-06-01 | raoulExtra | Add log file requirement for files without kind YAML entries |