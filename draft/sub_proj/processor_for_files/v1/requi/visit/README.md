# File Visitor Processor

## Usage

### Command Line Interface

```bash
python3 src/file_processor.py --kind frontmatter --action visit --root /path/to/folder --ext md
```

### Arguments

- `--kind` (required): The kind to check for YAML frontmatter (currently supports "frontmatter")
- `--action` (required): The action to perform (currently supports "visit")
- `--root` (required): The root folder path to scan
- `--ext` (optional): File extension filter (e.g., "md")

### Python API

```python
from pathlib import Path
import sys
sys.path.insert(0, 'src')
from file_processor import process_files

# Visit files with frontmatter kind
process_files(kind="frontmatter", action="visit", root=Path("/path/to/folder"), ext="md")
```

## Examples

### Visit all markdown files in a folder

```bash
python3 src/file_processor.py --kind frontmatter --action visit --root draft/sub_proj/processor_for_files/data --ext md
```

### Visit files in multiple folders (comma-separated)

```bash
python3 src/file_processor.py --kind frontmatter --action visit --root "folder1,folder2" --ext md
```

### Visit without extension filter

```bash
python3 src/file_processor.py --kind frontmatter --action visit --root .
```

## Output

- **stdout**: File paths, one per line
- **stderr**: Errors and warnings

## Log File

Warnings about files missing YAML frontmatter are written to:
`draft/sub_proj/processor_for_files/data/visit_log.txt`

Format: `<filepath>: missing <field1>, <field2>`

## Exit Codes

- `0`: Success
- Exception raised on failure (e.g., log file cannot be written)