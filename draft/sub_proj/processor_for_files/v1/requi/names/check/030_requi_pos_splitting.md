```yaml
id: requi_pos_splitting
name: POS Splitting Requirement
kind: requi
status: active
statement: Processed file names MUST be split into word types (POS) and organized into a three-level folder structure using Python's shutil library
version: V00.02.00
updated: '2026-06-01'
```

## Summary

We SHALL split processed names into their word type (POS) and organize them into a three-level folder structure using a Python library for distribution.

## Requirement

We SHALL:

1. Determine the part of speech (POS) for each word in a processed name
2. Create a folder structure: `<data>/<pos>/<first_two_letters>/<word>/`
3. Use the `shutil` Python library to distribute words into their corresponding folders
4. Place each word in its corresponding POS-specific folder organized by first two letters

## Folder Structure

The data folder follows this pattern:

- `<data>/noun/ex/example/` - for nouns starting with "ex"
- `<data>/adjective/bi/biological/` - for adjectives starting with "bi"
- `<data>/verb/vi/visit/` - for verbs starting with "vi"

## Python Implementation

Use Python's `shutil` and `pathlib` libraries for file distribution:

```python
from pathlib import Path
import shutil

def distribute_word(data_dir: Path, pos: str, word: str):
    first_two = word[:2]
    dest = data_dir / pos / first_two / word
    dest.mkdir(parents=True, exist_ok=True)
    return dest
```

## Rationale

- Enables fast lookup by first two letters within each POS category
- Organizes words by their part of speech for semantic grouping
- Supports scalable word database organization
- Uses standard Python libraries (`shutil`, `pathlib`) for reliable file operations

## Acceptance Criteria

- Given a processed name, the tool identifies word types (POS tags)
- Given a word and POS, the tool creates the appropriate folder path `<data>/<pos>/<first_two_letters>/<word>/`
- Python's `shutil` library distributes words into correct POS folders
- Words are stored with their POS metadata in the three-level hierarchy

---

## Change History

| Version | Date | Author | Reason |
|---------|------|--------|--------|
| V00.01.00 | 2026-06-01 | raoulExtra | Initial requirement for POS splitting |
| V00.02.00 | 2026-06-01 | raoulExtra | Adapt to data folder examples, add Python shutil implementation