```yaml
id: requi_exclude_numbers_from_split
name: Requirement for Excluding Numbers from Word Splitting
status: active
kind: requi
version: V00.01.00
updated: '2026-06-01'
statement: Numbers shall not be included as words when splitting names from path components
```

## Summary

We SHALL exclude numeric values from the word splitting process. Numbers in filenames or directory names should be filtered out and not stored as words.

## Requirement

1. We SHALL identify numeric sequences in the last path component
2. We SHALL exclude pure numbers from the split word list
3. We SHALL still split words around numbers (e.g., "file123name" -> "file", "name")
4. We SHALL NOT store numbers as standalone words in the database

## Implementation

- Pattern matching: identify sequences of digits `\d+`
- Split on word boundaries but exclude numeric-only tokens
- Examples:
  - `file123name` -> ["file", "name"]
  - `version2_0_update` -> ["version", "update"]
  - `2023_report` -> ["report"]
  - `123` -> [] (empty)

## See Also

- [Split Words from Filename Requirement](010_requi_split_words_from_filename.md) - base word extraction
- [Store Full Pathname with Words Requirement](030_requi_store_full_pathname_with_words.md) - storage with numbers excluded
- [SQLite Database Requirement](020_requi_sqlite_db.md) - database storage

## Change History

| Version | Date | Author | Model | Reason |
|---------|------|--------|-------|--------|
| V00.01.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Initial requirement for number exclusion |