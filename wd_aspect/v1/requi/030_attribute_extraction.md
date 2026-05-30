# Attribute Extraction

## Scenario
Module extracts and returns predefined attributes from Wikidata lexeme data.

## Required Attributes
1. **lexeme_id**: Wikidata lexeme identifier (e.g., L1244)
2. **lexical_category**: Part of speech (verb, noun, adjective, adverb, preposition, etc.)
3. **language**: Language code (always "en" for English lexemes)
4. **homograph_lexeme_ids**: List of related homograph lexeme IDs

## Source
- lexeme_id: From Lexeme entity ID
- lexical_category: From `lexicalCategory` field in lexeme entity
- language: Always "en" (English lexemes)
- homograph_lexeme_ids: Extracted from `forms` array in lexeme entity (form IDs excluding main lexeme)

## Example Output
```json
{
  "lexeme_id": "L1244",
  "lexical_category": "verb",
  "language": "en",
  "homograph_lexeme_ids": ["L1244-F1", "L1244-F2"]
}
```