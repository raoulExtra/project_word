```yaml
id: requi_sqlite_db
name: Requirement for SQLite Database
status: active
kind: requi
version: V00.01.00
updated: '2026-06-01'
statement: Provide SQLite database setup and management for storing processed words with full pathname association
```

## Summary

We SHALL provide a SQLite database for storing words extracted from file paths with proper schema and connection management.

## Requirement

1. We SHALL create a SQLite database at a configurable path
2. Default database path: `draft/sub_proj/processor_for_files/data/words.db`
3. We SHALL provide a schema for the words table:
   - `full_pathname` TEXT NOT NULL
   - `word` TEXT NOT NULL
   - `kind` TEXT
   - `source` TEXT
   - `position` INTEGER
   - `timestamp` DATETIME DEFAULT CURRENT_TIMESTAMP
3. We SHALL provide connection management functions
4. We SHALL handle database initialization and migrations
5. We SHALL enforce uniqueness on the combination of `full_pathname` and `word`

## Schema

```sql
CREATE TABLE IF NOT EXISTS words (
    full_pathname TEXT NOT NULL,
    word TEXT NOT NULL,
    kind TEXT,
    source TEXT,
    position INTEGER NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (full_pathname, word)
);
```

## See Also

- [Word Splitting Requirement](010_requi_split_words_from_filename.md) - Consumer of this database
- [Store Full Pathname with Words Requirement](030_requi_store_full_pathname_with_words.md) - Requires full_pathname column
- [Exclude Numbers from Split Requirement](040_requi_exclude_numbers_from_split.md) - Filtering logic
- [Recognize Abbrev Kind Requirement](050_requi_recognize_abbrev_kind.md) - Provides kind value
- [Lowercase Paths Requirement](070_requi_lowercase_paths.md) - Lowercase conversion
- [Split Action Requirement](../../020_requi_split_action.md) - Uses this database

## Note

The schema includes `full_pathname` to enable deduplication per the requirement that each pathname is stored once with its split words. The `kind` column stores the grammatical category (abbrev, noun, verb, etc.) determined from the path. The composite UNIQUE constraint ensures no duplicate word entries for the same pathname.

---

## Change History

| Version | Date | Author | Model | Reason |
|---------|------|--------|-------|--------|
| V00.01.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Initial database requirement |