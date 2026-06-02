```yaml
id: requi_splitt_words_from_filename
name: Requirement for Splitting Words from Visited Filenames
status: active
kind: requi
version: V00.01.00
updated: '2026-06-01'
statement: For visited files, extract words from the last directory or filename and store them in a SQLite database
```

## Summary

We SHALL extract words from the last component of visited file paths and persist them to a SQLite database for analysis.

## Requirement

1. We SHALL identify the last directory or filename component from the visited file path
2. We SHALL split the component into individual words using linguistic rules
3. We SHALL insert each word into a SQLite database with metadata
4. We SHALL handle both directory names and filenames

## Implementation

- Extract logic: if filepath has an extension, use `path.basename(filepath)`; otherwise use `path.basename(path.dirname(filepath))`
- Split using word boundaries and linguistic patterns
- Insert into DB with: full_pathname, word, kind, source, position, timestamp

## See Also

- [Database Requirement](020_requi_sqlite_db.md) - SQLite database setup
- [Convention 040](../../../conventions/040_conv_for_namings_of_files.md) - File naming conventions

---

## Change History

| Version | Date | Author | Model | Reason |
|---------|------|--------|-------|--------|
| V00.01.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Initial requirement for word splitting |