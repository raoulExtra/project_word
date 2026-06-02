```yaml
id: requi_lowercase_paths
name: Requirement for Lowercase Path Conversion
status: active
kind: requi
version: V00.01.00
updated: '2026-06-01'
statement: Convert all path and filename components to lowercase before storing in the database
```

## Summary

We SHALL normalize all path and filename components to lowercase to ensure case-insensitive matching and consistent storage.

## Requirement

1. We SHALL convert full_pathname to lowercase before database storage
2. We SHALL convert extracted words to lowercase before database storage
3. We SHALL preserve original case in a separate column if needed for display
4. We SHALL apply lowercase conversion after path normalization but before word extraction

## Implementation

- Use `String.toLowerCase()` or equivalent on full_pathname
- Apply lowercase to each word after extraction
- Optional: store `original_pathname` and `original_word` columns for reference

## Test Cases

| # | Input | Expected Lowercase |
|---|-------|-------------------|
| 1 | `/Path/To/File.TXT` | `/path/to/file.txt` |
| 2 | `C:\Users\NAME\file` | `c:\users\name\file` |
| 3 | `UPPERCASE_NAME` | `uppercase_name` |

## See Also

- [Store Full Pathname with Words Requirement](030_requi_store_full_pathname_with_words.md)
- [SQLite Database Requirement](020_requi_sqlite_db.md)
- [Word Splitting Requirement](010_requi_split_words_from_filename.md)

## Change History

| Version | Date | Author | Model | Reason |
|---------|------|--------|-------|--------|
| V00.01.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Initial requirement for lowercase conversion |