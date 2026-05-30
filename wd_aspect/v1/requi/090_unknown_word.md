# Unknown Word Handling

## Scenario
Word is not found in Wikidata lexeme namespace.

## Behavior
- Return JSON with error key: `{"error": "Word not found: <word>"}`
- Do not create cache file for unknown words
- Do not raise exception

## Example
Input: `xyznonexistentword12345`
Output: `{"error": "Word not found: xyznonexistentword12345"}`