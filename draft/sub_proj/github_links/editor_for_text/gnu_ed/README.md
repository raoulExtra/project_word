```yaml
prog_lang: C
github_repo: https://github.com/happy5214/gnu-ed
documentation: https://github.com/happy5214/gnu-ed/tree/main/doc
'''

## About

GNU ed is a line-oriented text editor, the standard text editor for Unix. It is used to create, display, modify and otherwise manipulate text files, both interactively and via shell scripts. A restricted version called `red` can only edit files in the current directory and cannot execute shell commands.

## Key Features

- Line-oriented editing (commands operate on lines)
- Standard Unix editor available on all systems
- Can edit binary files
- Supports BSD-style extensions to POSIX standard
- Includes test suite for POSIX compliance verification

## Extensions

- Binary file editing support
- BSD command compatibility (`s`, `W`, `wq`, `z`)
- Multiple command execution within global commands
- SunOS `ed` compatibility (runs as `red` for restricted mode)

## Building & Testing

See `INSTALL` for compilation and installation instructions. Run `make check` from the build directory to execute the test suite.

## Dependencies

### Arg_parser
GNU ed uses **Arg_parser** (carg_parser.c/h) for command-line argument parsing. This is a POSIX/GNU compliant argument parser library that supports:
- Short and long option syntax
- Optional and required arguments
- Abbreviated long options
- Error handling for invalid/missing arguments
- Binary/binary file editing support

Source: `parser_for_args/v1/src/c/`
- Source archive: `carg_parser.tar.gz`

## Requirements

### C Version (see `parser_for_args/v1/requi/`)
- [Basic Parsing](parser_for_args/v1/requi/001_requi_basic_parsing.md)
- [Memory Management](parser_for_args/v1/requi/010_requi_memory_management.md)
- [Option Arguments](parser_for_args/v1/requi/020_requi_option_arguments.md)
- [Error Handling](parser_for_args/v1/requi/030_requi_error_handling.md)
- [Long Option Matching](parser_for_args/v1/requi/040_requi_long_option_matching.md)
- [Argument Order](parser_for_args/v1/requi/050_requi_argument_order.md)
- [Negative Numbers](parser_for_args/v1/requi/060_requi_negative_numbers.md)
- [Empty Arguments](parser_for_args/v1/requi/070_requi_empty_arguments.md)
- [Boundary Conditions](parser_for_args/v1/requi/080_requi_boundary_conditions.md)
- [Short Option Edge Cases](parser_for_args/v1/requi/090_requi_short_option_edge_cases.md)
- [Unicode Support](parser_for_args/v1/requi/100_requi_unicode_support.md)
- [Duplicate Options](parser_for_args/v1/requi/110_requi_duplicate_options.md)

### Python Version (see `parser_for_args/v1/requi/py/`)
- [Glossary](parser_for_args/GLOSSARY/)

## Unit Tests

### C Version
Unit tests are located in `parser_for_args/v1/src/c/tests/unit/`:
- `test_basic_parsing.c`
- `test_memory_management.c`
- `test_option_arguments.c`
- `test_error_handling.c`
- `test_long_option_matching.c`
- `test_argument_order.c`
- `test_negative_numbers.c`
- `test_empty_arguments.c`
- `test_boundary_conditions.c`
- `test_short_option_edge_cases.c`
- `test_unicode_support.c`
- `test_duplicate_options.c`

### Python Version
Python unit tests will be located in `parser_for_args/v1/src/py/tests/`

## License

GPL-2.0
