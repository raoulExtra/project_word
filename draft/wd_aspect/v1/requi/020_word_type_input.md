# Word Type Input Acceptance

## Scenario
Module receives a word type (part of speech) as input via CLI or programmatic API.

## Behavior
- Accept word_type as second positional argument
- Validate word_type against supported types
- Use word_type to filter lexeme search results

## Supported Word Types
- verb
- noun
- adjective
- adverb
- preposition
- pronoun
- conjunction
- interjection
- article

## Input Formats

### CLI
```bash
python wd_lookup.py <word> <word_type>
```

### Programmatic API
```python
wd_lookup('help', 'verb')
wd_lookup('tree', 'noun')
```

## Validation
- Word type is optional (defaults to None, uses first search result)
- Invalid word type is ignored (falls back to first search result)

## Example
Input: `python wd_lookup.py help verb`
Output: JSON with lexeme_id L1244 and lexical_category 'verb'