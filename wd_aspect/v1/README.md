# wd_aspect v1 - Wikidata Word Lookup Module

A Python module to enrich word information with Wikidata lexeme attributes.

## Usage

### CLI (Command Line)

```bash
python src/wd_lookup.py <word> [word_type] [--orig wn]
```

Example:
```bash
python src/wd_lookup.py help verb
python src/wd_lookup.py happy adjective --orig wn
```

Output:
```json
{
  "lexeme_id": "L1244",
  "lexical_category": "verb",
  "language": "en",
  "homograph_lexeme_ids": [],
  "updated": "2026-05-30T10:26:23.094505Z"
}
```

### Programmatic API

```python
from src.wd_lookup import wd_lookup, wd_lookup_batch, save_to_cache

# Single word lookup (with optional word_type filter)
result = wd_lookup('help', 'verb')
# {'lexeme_id': 'L1244', 'lexical_category': 'verb', 'language': 'en', 'homograph_lexeme_ids': [], 'updated': '...'}

# With origin parameter
result = wd_lookup('help', 'verb', origin='wn')

# Save to cache
save_to_cache('help', result)

# Batch processing
results = wd_lookup_batch(['help', 'run', 'jump'])
# With word types
results = wd_lookup_batch(['help', 'tree'], ['verb', 'noun'])
```

## Output Format

Each lookup returns a JSON object with:

| Field | Description |
|-------|-------------|
| `lexeme_id` | Wikidata lexeme identifier (e.g., L1244) |
| `lexical_category` | Part of speech (verb, noun, adjective, etc.) |
| `language` | Language code (e.g., "en") |
| `homograph_lexeme_ids` | List of homograph lexeme IDs |
| `updated` | ISO 8601 timestamp |

## Cache Location

Results are cached at:
```
wd_cache/lang_en/<lexical_category>/<first_letter>/wd_<word>.json
```

Example: `wd_cache/lang_en/verb/h/wd_help.json`

## Running Tests

```bash
cd wd_aspect/v1
python3 -m pytest src/tests/unit/ -v
```

## Dependencies

- Python 3.x
- `requests` library

Install:
```bash
pip install requests pytest
```