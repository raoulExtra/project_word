```yaml
id: requi_split_directory
name: "Split Directory Requirements"
kind: requi
status: active
version: V00.01.00
updated: '2026-06-01'
```

# Split Requirements

This directory contains requirements for splitting words from file paths.

## Files

- `010_requi_split_words_from_filename.md` - Extract words from last path component
- `020_requi_sqlite_db.md` - Database schema for storing words
- `030_requi_store_full_pathname_with_words.md` - Store full pathname with split words
- `040_requi_exclude_numbers_from_split.md` - Filter out numeric tokens
- `050_requi_recognize_abbrev_kind.md` - Recognize abbrev kind from path
- `060_requi_edge_cases_path_ot_full.md` - Handle edge cases in pathnames
- `070_requi_lowercase_paths.md` - Convert paths to lowercase

## Database

The SQLite database for storing words is located at:
`draft/sub_proj/processor_for_files/data/words.db`

## Query Processor

Use `src/query_processor.py` to run SQL queries against the database:

```bash
python3 src/query_processor.py "SELECT * FROM words LIMIT 10;"
python3 src/query_processor.py "SELECT word, COUNT(*) as count FROM words GROUP BY word ORDER BY count DESC LIMIT 10;"
```