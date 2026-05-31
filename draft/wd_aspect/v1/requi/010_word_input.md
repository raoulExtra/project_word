# Word Input Acceptance

## Scenario
Module receives a word as input via CLI or programmatic API.

## Behavior
- Accept word as first positional argument
- Validate word is not empty
- Support UTF-8 characters
- Pass word directly to Wikidata search API

## Input Formats

### CLI
```bash
python wd_lookup.py <word>
python wd_lookup.py <word> -wt <word_type>
python wd_lookup.py <word> -wt <word_type> -orig wn
```

### Programmatic API
```python
wd_lookup('help')
wd_lookup('help', 'verb')
```

## Validation
- Word must be non-empty string
- Empty input returns: `{"error": "Usage: python wd_lookup.py <word> [word_type]"}`

## Example
Input: `python wd_lookup.py help`
Output: JSON with lexeme_id L1244