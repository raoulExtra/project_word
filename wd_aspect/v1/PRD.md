# Product Requirements Document (PRD)

## Overview

A callable module to enrich information about words with clearly defined attributes from Wikidata (e.g., lexeme, item info, etc.).

## Goals

- Enable users to input a word and retrieve structured Wikidata attributes
- Identify the anchor lexeme of Wikidata via best match for a given word
- Create a JSON cache file for performance optimization

## User Stories

As a user, I want to provide a word as input and have the module look it up in Wikidata, returning a list of predefined attributes (like lexeme_id).

## Non-Functional Requirements

- Performance: Lookup operations should be performant (see `requi/070_performance.md`)
- Reliability: Module should handle edge cases gracefully (unknown words, API failures) (see `requi/080_api-failure.md`, `requi/090_unknown-word.md`)

## Success Metrics

- Response time under 2 seconds for cached queries
- Response time under 5 seconds for fresh Wikidata API calls
- Cache hit rate above 80% for repeated queries

## Dependencies

- Python 3.x
- `requests` library for HTTP calls
- Wikidata API access
- Network connectivity to Wikidata services

## Scope

### In-Scope
- Word lookup in Wikidata
- Extract lexeme_id, lexical category, language abbreviation, homograph lexeme IDs
- JSON caching in wd_cache folder at project root
- Batch processing support
- Path format: `wd_cache/lang_<code>/<lexical_category>/<first_letter>/wd_<word>.json`
- Item IDs (Q<number>) from search results are used internally to find lexemes but are not exposed in output

### Out-of-Scope
- User interface (API/module only)
- Support for non-lexeme Wikidata entities (Item IDs are not directly relevant)

## Examples

For verb "help" below there is the right lexeme_id reference:

https://www.wikidata.org/wiki/Lexeme:L1244

## Decisions

- Lexical category, Language abbreviation (e.g., en), Homograph lexeme IDs will be included in output
- Batch processing of multiple words will be supported
- Output format: Single word JSON with path `lang_<code>/<lexical_category>/<first_letter>/wd_<word>.json`
- Failure mode: Return empty JSON with error message when word has no matching lexeme
- Initial language support: English only
- Interface: Both CLI argument and programmatic API
- Updated timestamp: ISO 8601 format in JSON output
- Cache invalidation: Assume stable (Wikidata lexeme data rarely changes)
- Retry logic: 3 retries with fixed delay for network failures
- Test validation: Automated test for "help" → L1244 mapping

## Open Questions

- None currently; all key decisions resolved

## See Also

Detailed requirements are documented in the `requi/` folder:
- [001_5w_questions.md](requi/001_5w_questions.md) - Core question words analysis
- [000_glossary.md](requi/000_glossary.md) - Definitions
- [010_word_input.md](requi/010_word_input.md) - Word input acceptance
- [020_word_type_input.md](requi/020_word_type_input.md) - Word type input acceptance
- [100_wordnet_origin.md](requi/100_wordnet_origin.md) - WordNet origin support
- [030_attribute_extraction.md](requi/030_attribute_extraction.md) - Attribute extraction details
- [040_cache_file.md](requi/040_cache_file.md) - Cache file creation
- [050_wikidata_link.md](requi/050_wikidata_link.md) - Wikidata link validation
- [060_batch_processing.md](requi/060_batch_processing.md) - Batch processing support
- [070_performance.md](requi/070_performance.md) - Performance requirements
- [080_api_failure.md](requi/080_api_failure.md) - API failure handling
- [090_unknown_word.md](requi/090_unknown_word.md) - Unknown word handling

---

## 🎯 Why PRDs Matter

A strong PRD:

- Prevents misalignment between teams
- Reduces rework by clarifying expectations early
- Helps prioritize features
- Creates a shared mental model of the product
- Anchors decisions when trade-offs arise

In fast-moving teams, a PRD is less about bureaucracy and more about clarity.

---

## 🧠 A non-obvious insight

The best PRDs don't try to predict everything.

They define the boundaries of good decisions, not the decisions themselves.

A PRD should empower engineers and designers — not constrain them.