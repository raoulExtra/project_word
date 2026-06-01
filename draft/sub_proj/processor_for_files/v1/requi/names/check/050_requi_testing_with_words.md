```yaml
id: requi_testing_with_words
name: Testing with Words Requirement
kind: requi
status: active
statement: Processed file names MUST support testing with words and expected results (expe argument)
version: V00.01.00
updated: '2026-06-01'
```

## Summary

We SHALL create a testing framework that processes words and validates results against expected outcomes. The framework uses an `expe` (expected) argument to specify what the output should be for each test word.

## Requirement

We SHALL:

1. Define test words with their expected outcomes using the `expe` argument
2. Process each word through the POS splitting pipeline
3. Compare actual results against expected results
4. Report pass/fail status for each test case
5. Support batch testing of multiple words

## Test Structure

Each test case follows this format:

- `word` - the word to test
- `expe` - the expected result (our data category)
- `pos` - expected part of speech (optional)
- `folder` - expected folder path (optional)

Note:
(our data category) is eigther POS or abbrev or unkown

## Python Implementation

Use Python's `shutil` and `pathlib` libraries for file operations and testing:

```python
from pathlib import Path
import shutil

def test_word_distribution(data_dir: Path, word: str, expe: str, pos: str = None):
    first_two = word[:2]
    expected_path = data_dir / expe
    actual_path = data_dir / pos / first_two / word if pos else None
    
    return {
        "word": word,
        "expe": str(expected_path),
        "actual": str(actual_path) if actual_path else None,
        "passed": str(expected_path) == str(actual_path)
    }

def run_tests(test_cases: list) -> list:
    results = []
    for case in test_cases:
        result = test_word_distribution(
            Path(case["data"]),
            case["word"],
            case["expe"],
            case.get("pos")
        )
        results.append(result)
    return results
```

## Example Tests

| Word | Expected POS | Expected Path |
|------|--------------|---------------|
| example | noun | `<data>/noun/ex/example/` |
| biological | adjective | `<data>/adjective/bi/biological/` |
| visit | verb | `<data>/verb/vi/visit/` |
| exte | abbrev | `<data>/abbrev/ex/exte/` |
| xxzy | unkown | `<data>/unkown/xx/xxzy/` |

## Rationale

- Enables systematic testing of the POS splitting functionality
- Uses `expe` argument for clear expected value specification
- Validates folder structure creation
- Uses standard Python libraries (`shutil`, `pathlib`) for reliable testing operations

## Acceptance Criteria

- Given a word and `expe` argument, the tool validates the expected output
- Test results are reported with pass/fail status
- Batch testing processes multiple words with their expected values
- Python's `shutil` library supports test file operations

---

## Change History

| Version | Date | Author | Reason |
|---------|------|--------|--------|
| V00.01.00 | 2026-06-01 | raoulExtra | Initial requirement for testing with words and expe argument |