# Cache File Creation

## Scenario
Module creates and maintains JSON cache file after successful lookup.

## Behavior
- Create cache file only for successful lookups (no error)
- Path format: `wd_cache/lang_en/<lexical_category>/<first_letter>/wd_<word>.json`
- Create parent directories if they don't exist
- Add `updated` timestamp in ISO 8601 format

## Cache Structure
```json
{
  "lexeme_id": "L1244",
  "lexical_category": "verb",
  "language": "en",
  "homograph_lexeme_ids": [],
  "updated": "2026-05-30T10:26:23.094505Z"
}
```

## Example
For word "help" (verb):
Path: `wd_cache/lang_en/verb/h/wd_help.json`

For word "tree" (noun):
Path: `wd_cache/lang_en/noun/t/wd_tree.json`