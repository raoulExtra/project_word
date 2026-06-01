```yaml
id: requi_abbrevs_and_unknown_words
name: Abbreviations and Unknown Words Requirement
kind: requi
status: active
statement: Processed file names MUST be categorized into abbreviations and unknown words with specific folder handling
version: V00.01.00
updated: '2026-06-01'
```

## Summary

We SHALL categorize words that cannot be identified as known parts of speech into two special categories: abbreviations and unknown words. Each category has its own folder structure for storage.

## Requirement

We SHALL:

1. Identify abbreviations (words marked as abbreviated forms)
2. Identify unknown words (words not recognized in the known vocabulary)
3. Create folder structure for abbreviations: `<data>/abbrev/<first_two_letters>/<word>/`
4. Create folder structure for unknown words: `<data>/unkown/<first_two_letters>/<word>/`
5. Store each word in its corresponding special category folder

## Folder Structure

The data folder follows this pattern:

- `<data>/abbrev/ex/exte/` - for abbreviations starting with "ex"
- `<data>/unkown/xx/xxzy/` - for unknown words starting with "xx"

## Python Implementation

Use Python's `shutil` and `pathlib` libraries for file distribution:

```python
from pathlib import Path
import shutil

def distribute_special_word(data_dir: Path, category: str, word: str):
    first_two = word[:2]
    dest = data_dir / category / first_two / word
    dest.mkdir(parents=True, exist_ok=True)
    return dest
```

## Rationale

- Separates abbreviations and unknown words from regular POS categories
- Maintains consistent folder structure across all word types
- Enables special handling for words that don't fit standard POS categories
- Uses standard Python libraries (`shutil`, `pathlib`) for reliable file operations

## Acceptance Criteria

- Given an abbreviation, the tool creates the appropriate folder path `<data>/abbrev/<first_two_letters>/<word>/`
- Given an unknown word, the tool creates the appropriate folder path `<data>/unkown/<first_two_letters>/<word>/`
- Python's `shutil` library distributes words into correct category folders
- Special category words are stored with their metadata in the dedicated folder structure

---

## Change History

| Version | Date | Author | Reason |
|---------|------|--------|--------|
| V00.01.00 | 2026-06-01 | raoulExtra | Initial requirement for abbreviations and unknown words |