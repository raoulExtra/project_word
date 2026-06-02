```yaml
id: requi_store_full_pathname_with_words
name: Requirement for Storing Full Pathname with Split Words
status: active
kind: requi
version: V00.01.00
updated: '2026-06-01'
statement: Store the full pathname together with split words from the last filename or last directory, ensuring each full pathname is associated with its split names exactly once
```

## Summary

We SHALL store the full pathname alongside extracted words from the last directory or filename, with deduplication ensuring each full pathname appears only once in the association.

## Requirement

1. We SHALL store the complete file path (full pathname) for each visited file
2. We SHALL associate the split words with their originating full pathname
3. We SHALL ensure each full pathname is stored exactly once with its split names
4. We SHALL store the last directory or filename component separately for word extraction
5. We SHALL split words only from the last filename if present, otherwise from the last directory in the path

## Implementation

- Store: `full_pathname`, `last_component`, `split_words`, `timestamp`
- Deduplication key: `full_pathname`
- If same pathname visited again, update timestamp but don't duplicate the split words association
- Split logic: if path ends with a filename (has extension or non-directory component), split from filename; otherwise split from last directory

## See Also

- [Split Words from Filename Requirement](010_requi_split_words_from_filename.md) - word extraction
- [SQLite Database Requirement](020_requi_sqlite_db.md) - database storage

## Change History

| Version | Date | Author | Model | Reason |
|---------|------|--------|-------|--------|
| V00.01.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Initial requirement for pathname storage |