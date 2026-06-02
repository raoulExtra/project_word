```yaml
id: requi_names_processing
name: "Names Processing Requirements"
kind: requi
status: active
version: V00.01.00
updated: '2026-06-01'
```

# Name Processing Requirements

This directory contains requirements for processing file names and extracting words from path components.

## Structure

- `split/` - Requirements for splitting words from file paths
- `check/` - Requirements for validating and checking names

## Key Requirements

- [010_requi_split_words_from_filename.md](split/010_requi_split_words_from_filename.md) - Extract words from last path component
- [020_requi_sqlite_db.md](split/020_requi_sqlite_db.md) - Database schema for storing words
- [030_requi_store_full_pathname_with_words.md](split/030_requi_store_full_pathname_with_words.md) - Store full pathname with split words
- [040_requi_exclude_numbers_from_split.md](split/040_requi_exclude_numbers_from_split.md) - Filter out numeric tokens
- [050_requi_recognize_abbrev_kind.md](split/050_requi_recognize_abbrev_kind.md) - Recognize abbrev kind from path
- [060_requi_edge_cases_path_ot_full.md](split/060_requi_edge_cases_path_ot_full.md) - Handle edge cases in pathnames
- [070_requi_lowercase_paths.md](split/070_requi_lowercase_paths.md) - Convert paths to lowercase

## See Also

- [Visitor for Files](../visit/) - File visiting requirements
- [Convention 040](../../../conventions/040_conv_for_namings_of_files.md) - File naming conventions

## Usage

The `split` module provides functions for extracting and processing words from file paths:

### Python API

```python
from src.split import extract_last_component, split_words, normalize_path, normalize_word

# Extract last component from a path
component = extract_last_component("/path/to/myfile.txt")  # "myfile.txt"
component = extract_last_component("/path/to/mydirectory")  # "mydirectory"

# Split component into words
words = split_words("myFileName")  # ["my", "File", "Name"]
words = split_words("my_file_name")  # ["my", "file", "name"]
words = split_words("file123name")  # ["file", "name"] - numbers excluded

# Normalize path/words to lowercase
lower_path = normalize_path("/Path/To/File.TXT")  # "/path/to/file.txt"
lower_word = normalize_word("MyWord")  # "myword"
```

### Command Line

```bash
python3 -c "
from src.split import extract_last_component, split_words, normalize_path
path = '/some/path/to/MyFile.TXT'
component = extract_last_component(path)
words = split_words(component)
print(normalize_path(path), words)
"
```

## Tests

Run the unit tests:

```bash
python3 -m pytest tests/unit/test_split.py -v
```