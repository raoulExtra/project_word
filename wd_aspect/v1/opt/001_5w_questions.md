# 5W Questions

## What
A callable module to enrich word information with Wikidata attributes (lexeme_id, lexical category, language, homograph IDs).

## When
Words are looked up on-demand or via batch processing, with results cached for performance optimization.

## Where
Lookups occur in Wikidata's knowledge base via API, with cache files stored locally in `wd_cache/` directory.

## Who
Users who need structured lexical data for words, such as linguists, researchers, or developers building language applications.

## Why
To provide accurate, performant access to Wikidata's lexical resources for word-based applications and research.