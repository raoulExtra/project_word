```yaml
id: requi_recognize_abbrev_kind
name: Requirement for Recognizing Abbrev Kind from Path
status: active
kind: requi
version: V00.01.00
updated: '2026-06-01'
statement: Recognize the "abbrev" kind by matching last directory names in the data/abbrev tree
```

## Summary

We SHALL identify files belonging to the "abbrev" kind by examining the last directory in the path under `draft/sub_proj/processor_for_files/data/abbrev/`.

## Requirement

1. We SHALL traverse the path to find if it starts with the abbrev data root
2. We SHALL extract the last directory component from the abbrev subtree
3. We SHALL match this against known two-letter abbreviation directories
4. We SHALL classify the file as "abbrev" kind when matched

## Implementation

- Path pattern: `.../data/abbrev/<two-letter>/<two-letter>/...`
- Example matches:
  - `.../data/abbrev/ex/exte/...` -> "abbrev"
  - `.../data/abbrev/co/conv/...` -> "abbrev"
  - `.../data/abbrev/db/db/...` -> "abbrev"
- The last directory before the filename determines the specific abbrev

## See Also

- [Word Splitting Requirement](010_requi_split_words_from_filename.md)
- [Store Full Pathname with Words Requirement](030_requi_store_full_pathname_with_words.md)

## Change History

| Version | Date | Author | Model | Reason |
|---------|------|--------|-------|--------|
| V00.01.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Initial requirement for abbrev recognition |