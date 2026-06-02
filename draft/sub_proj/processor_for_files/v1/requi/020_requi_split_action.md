```yaml
id: requi_split_action
name: "Requirement for Split Action"
kind: requi
status: active
version: V00.01.00
updated: '2026-06-01'
statement: Add "split" action to the file processor for extracting words from file paths
```

## Summary

We SHALL add a `split` action to the file processor that extracts and stores words from file paths in a SQLite database.

## Requirement

1. We SHALL support `action="split"` for `kind="frontmatter"`
2. We SHALL accept a `root` path that can be a file or directory
3. We SHALL extract words from the last path component using the split module
4. We SHALL store extracted words with full pathname in the database
5. We SHALL return `0` on success, non-zero on failure

## Implementation

- Use `extract_last_component()` to get the filename/directory name
- Use `split_words()` to tokenize the component
- Use `normalize_path()` and `normalize_word()` for lowercase conversion
- Store results via the SQLite database schema

## See Also

- [Processor for Files Requirement](010_requi_processor_for_files.md) - Main processor requirement
- [Names Split Requirements](../names/split/) - Word splitting requirements

## Change History

| Version | Date | Author | Model | Reason |
|---------|------|--------|-------|--------|
| V00.01.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Initial requirement for split action |