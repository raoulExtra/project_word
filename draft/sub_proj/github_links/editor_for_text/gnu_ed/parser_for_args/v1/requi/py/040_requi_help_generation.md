---
id: requi_help_generation
name: Help Generation
kind: requirement
status: active
domain: arg_parser_python
---

# Help Generation Requirements

## Definition
The Python argument parser must automatically generate help messages from argument metadata with customizable formatting.

## Details
- **Purpose**: Provide automatic documentation for CLI tools
- **Key aspects**:
  - Automatic -h/--help handling
  - Usage string generation
  - Argument descriptions from help text
  - Epilog and description support
- **Types**:
  - Brief help (-h)
  - Full help with all details
  - Custom formatters
- **Role**: Eliminate manual help documentation maintenance

## Context
Help generation is expected behavior in Python CLI tools. Users rely on -h to understand available options and their usage.
