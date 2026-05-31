# Batch Processing

## Scenario
Module receives multiple words for simultaneous lookup.

## Behavior
- Accept list of words via `wd_lookup_batch()` function
- Process each word independently
- Return list of results in same order as input

## Input Format

### Programmatic API
```python
wd_lookup_batch(['help', 'run', 'jump'])
wd_lookup_batch(['help', 'tree'], ['verb', 'noun'])  # with word types
```

## Output
- Returns list of JSON objects
- Each object contains lexeme_id, lexical_category, language, homograph_lexeme_ids
- Error objects included for failed lookups

## Example
Input: `wd_lookup_batch(['help', 'run'])`
Output: `[{'lexeme_id': 'L1244', ...}, {'lexeme_id': 'L279', ...}]`