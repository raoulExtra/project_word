```yaml
id: requi_query_processor
name: Requirement for Query Processor
status: active
kind: requi
version: V00.01.00
updated: '2026-06-01'
statement: Provide a query processor action to execute SQL queries against the words database
```

## Summary

We SHALL provide a `query` action that allows executing arbitrary SQL queries against the SQLite database and outputting results.

## Requirement

1. We SHALL support `action="query"` for `kind="frontmatter"`
2. We SHALL accept a `query` parameter containing SQL to execute
3. We SHALL output query results to stdout in a readable format
4. We SHALL return `0` on success, non-zero on failure
5. We SHALL handle SQL errors gracefully

## Implementation

- Connect to `draft/sub_proj/processor_for_files/data/words.db`
- Execute the provided SQL query
- Format results as table or list output
- Handle errors and print to stderr

## Example Usage

```bash
python3 src/processor_for_files.py --kind frontmatter --action query --query "SELECT * FROM words LIMIT 10;"
```

## See Also

- [Split Action Requirement](020_requi_split_action.md) - Uses the same database
- [SQLite Database Requirement](../names/split/020_requi_sqlite_db.md) - Database schema

## Change History

| Version | Date | Author | Model | Reason |
|---------|------|--------|-------|--------|
| V00.01.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Initial requirement for query processor |