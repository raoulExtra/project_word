```yaml
id: conv_for_namings_of_files
name: Convention for Namings of Files
kind: convention
tags:
- filename
version: V00.10.00
updated: '2026-06-01'
```

## Convention

Files in this filesystem SHOULD use the format `<number>_<kind>_<noun_or_nouned_word>_<connector>_<rest>.md`

Where:
- `<number>` is optional; when present, a 3-digit number like `010_`, `020_`
- `<kind>` is the document kind: `requi_`, `def_`, `asp_`, `ref_`, etc.
- `<noun>` describes the subject (see noun examples below)
- `<connector>` can be e.g. `ot`, `for`, `of` - **optional**
- `<rest>` is additional descriptive words

**Note:** The connector component (`<connector>`) is optional. Some files may use `<number>_<kind>_<noun>_<rest>` format.

#### Noun Examples (middle component)
These are nouns that describe the subject of the file:

- handler
- visitor (nouned verbs)
- namings 

#### Verb-ed Examples (alternative middle component)
These are `-ed` or `-er` forms derived from verbs:

- checking (from check)
- processing (from process)
- handling (from handle)
- visiting (from visit)
- reading (from read)
- validating (from validate)


### Examples

#### Requirements with prefix and 3-digit number

- `010_requi_visitor_for_files.md` - file visitor requirement
- `010_requi_checker_for_files.md` - file checker requirement
- `010_requi_reader_for_files.md` - file reader requirement
- `010_requi_validator_for_frontmatter.md` - frontmatter validator requirement
- `020_requi_processor_for_markdown.md` - markdown processor requirement

#### Requirements without prefix

- `requi_handler_for_files.md` - file handler requirement
- `requi_parser_for_yaml.md` - YAML parser requirement
- `requi_validator_for_frontmatter.md` - frontmatter validator requirement
- `requi_word_input.md` - word input requirement (no connector)
- `def_model_for_simulation.md` - simulation model definition

#### Folders following the convention

- `disciplines_ot_academic/`
- `architectures_for_computers/`
- `sciences_ot_formal/`
- `processor_for_files/`

#### Files following the convention

- `asp_efficience_ot_binary.md`
- `requi_visitor_for_files.md`
- `requi_processor_for_markdown.md`
- `010_requi_file_processor.md`
- `020_requi_yaml_frontmatter_check.md`
- `010_requi_visitor_for_files.md`

#### Project examples (processor_for_files)

All files in `draft/sub_proj/processor_for_files/` already follow the convention:

- `010_requi_file_processor.md` - file processor requirement
- `020_requi_yaml_frontmatter_check.md` - YAML frontmatter check requirement
- `visit/010_requi_visitor_for_files.md` - file visitor requirement
- `names/check/010_requi_name_check.md` - name validation requirement
- `names/check/020_requi_verb_recognition.md` - verb recognition requirement
- `names/check/030_requi_pos_splitting.md` - POS splitting requirement (three-level structure: `<data>/<pos>/<first_two_letters>/<word>/`)
- `names/check/040_requi_abbrevs_and_unknown_words.md` - abbreviations and unknown words handling
- `names/check/050_requi_testing_with_words.md` - testing with words and expe argument
- `names/010_requi_directory_structure.md` - directory structure requirement

The directory name `processor_for_files` follows the `<noun>_<connector>_<noun>` pattern.

**Note:** For files in `_/` subdirectories, see `030_conv_filename_by_term_start.md` - files should be organized by the first letter of the term name, not the prefix.

### Rationale

- Consistent naming pattern across filenames
- Clear hierarchical refinement
- Easy to cross-reference and search elements (higher order element comes first)

### See Also

- [Convention 030](030_conv_filename_by_term_start.md) - organization of files in `_/` subdirectories
- [Convention 070](070_conv_for_history_of_changes.md) - change history format
- [Visitor for Files Requirement](draft/sub_proj/processor_for_files/v1/requi/visit/010_requi_visitor_for_files.md) - relates to this convention

## Change History

| Version | Date | Author | Model | Reason |
|---------|------|--------|-------|--------|
| V00.01.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | init |
| V00.02.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Clarify format, add connector as optional, improve examples |
| V00.03.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Reorganize format to emphasize kind prefix, add more noun examples |
| V00.04.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Add project examples, fix cross-references |
| V00.05.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Update project examples for renamed directory |
| V00.06.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Add processor_for_files to folder examples |
| V00.07.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Add name_check and directory_structure requirements |
| V00.08.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Add verb_recognition requirement |
| V00.09.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Add pos_splitting requirement |
| V00.10.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Add cross-reference to visitor_for_files requirement |
| V00.11.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Update pos_splitting requirement with three-level structure |
| V00.12.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Add abbrevs_and_unknown_words requirement |
| V00.13.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Add testing_with_words requirement |