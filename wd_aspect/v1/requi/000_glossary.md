# Glossary

## Definitions

### Wikidata

Wikidata is a collaboratively edited multilingual knowledge graph hosted by the Wikimedia Foundation that stores structured data as items with unique QIDs and lexemes with unique LIDs. It serves as a central repository for open data that can be queried and reused across Wikimedia projects and external applications.

**Part of speech:** noun

**Open-class categories:**

| Word type    | Wikidata ID | Notes                                    |
|--------------|-------------|------------------------------------------|
| Noun         | Q1084       | Open class; includes common & proper nouns |
| Verb         | Q24905      | Open class; includes transitive/intransitive |
| Adjective    | Q34698      | Open class                              |
| Adverb       | Q380057     | Open class                              |

**Closed-class categories (function words):**

| Word type           | Wikidata ID | Notes                                      |
|---------------------|-------------|--------------------------------------------|
| Pronoun             | Q36224      | Includes personal, demonstrative, etc.     |
| Preposition         | Q4833830    | English has prepositions; other languages may not |
| Postposition        | Q161873     | Used in languages like Japanese, Hindi     |
| Classifier          | Q63153      | Used in East Asian languages               |
| Article / Determiner| Q103184     | "the", "a", "an"                           |
| Conjunction         | Q36484      | Coordinating & subordinating                 |
| Interjection        | Q83034      | "oh!", "wow!", "hey!"                        |

### Wordnet

WordNet is a lexical database for the English language developed at Princeton University that organizes words into synonym sets (synsets) grouped by semantic meaning and linked by lexical relations like hypernymy and hyponymy. It provides a structured network of lexical entries with part-of-speech tags, definitions, synonyms, and semantic relationships.

**Part of speech:** noun, verb, adjective, adverb

In Wordnet json files the first number after the `<word>%` encodes the POS:

| Code | POS | Meaning     |
|------|-----|-------------|
| 1    | n   | noun        |
| 2    | v   | verb        |
| 3    | a   | adjective   |
| 4    | r   | adverb      |
| 5    | s   | adjective   |

**Extractable fields from entries files:**

| Field       | Description                           |
|-------------|---------------------------------------|
| word        | lemma (base form)                     |
| pos         | part of speech                          |
| definition  | gloss/definition of the synset          |
| synonyms    | other words in same synset              |
| hypernyms   | broader semantic categories             |
| synsets     | all synset details with IDs             |
| derivation  | derived forms (e.g., bankable from bank)|
| agent       | who performs the action                 |
| location    | where the action occurs                 |
| subcat      | syntactic subcategorization             |
| sent        | example sentence                        |
| uses        | usage notes                             |

**Subcat values examples (from frames.json):**

| Code   | Pattern                           | Example verb usage        |
|--------|-----------------------------------|---------------------------|
| vtai   | Somebody ----s something          | "He banks the river"       |
| via    | Somebody ----s                     | "He banks (on the topic)"  |
| via-pp | Somebody ----s PP                  | "He banks on saving money" |
| vtaa   | Somebody ----s somebody            | "She banks him as expert"  |

**Extractable fields from synset files:**

| Field       | Description                           |
|-------------|---------------------------------------|
| definition  | gloss/definition                      |
| example     | usage example                         |
| hypernym    | parent synset ID                      |
| mero_part   | meronym (part) relationships          |
| mero_member | meronym member relationships          |
| ili         | Interlingual Index                    |
| partOfSpeech| POS tag                               |
| source      | provenance information                |
| domain_topic| topic domain                          |
| frames    | verb argument patterns (from frames.json) |
| also      | additional senses/usage notes           |
| attribute | attribute words                         |
| entails   | entailments (for verbs)                 |
| similar   | similar to                              |
| wikidata  | Wikidata QID mapping                    |
| members   | words in this synset                    |

## Abbreviations

| letter | abbrev_up | abbrev | item     |
|--------|-----------|--------|----------|
| P      | POS       | -      | Part of speech |
| W      | WD        | wd     | Wikidata |
| W      | WN        | wn     | Wordnet  |

## Related examples

See `wn_transform/v1/` for word examples:
- `031_requi_example_for_word_huge.md` - huge examples
- `033_requi_example_for_word_noun_core.md` - core noun examples
- `034_requi_example_for_word_verb_core.md` - core verb examples
- `035_requi_example_for_word_noun_bank.md` - bank noun examples
- `036_requi_example_for_word_verb_bank.md` - bank verb examples 