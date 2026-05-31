# WordNet Origin Support

## Scenario
Module searches for words in Wikidata using WordNet lexical categories.

## Behavior
- Accept `--orig wn` CLI argument to indicate WordNet origin
- Map WordNet lexical categories to Wikidata QIDs
- Use WordNet categories for filtering lexeme search results

## WordNet Category Mapping

Wikidata QID 
L14452

## WordNet WD Item Category Mapping

| WordNet Category | Wikidata QID | Lexeme ID Example | Description |
|-----------------|--------------|-------------------|-------------|
| verb | Q24905 | L1244 | Action words |
| noun | Q110 | L279 | Object/Concept words |
| adjective | Q1065 | L949 | Descriptive words |
| adverb | Q94 | L1055 | Modification words |
| adj.adverbial | Q214407 | L1055 | Adverbial adjective forms |

## CLI Usage
```bash
python wd_lookup.py <word> --orig wn <wordnet_category>
```

Example:
```bash
python wd_lookup.py help --orig wn verb
python wd_lookup.py happy --orig wn adjective
```

## Programmatic API
```python
wd_lookup('help', word_type='verb', origin='wn')
```

## Implementation Notes
- WordNet categories are subset of supported lexical categories
- If WordNet category not found, fall back to first search result
- Origin parameter is informational (used for logging/tracking)