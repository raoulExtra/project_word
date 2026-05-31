---
id: requi_subcommand_nested
name: Nested Subcommands
kind: requirement
status: active
domain: arg_parser_python
---

# Nested Subcommands Requirements

## Definition
The Python argument parser must support subcommands within subcommands for deeply nested CLI structures.

## Details
- **Purpose**: Enable complex CLI tools with multiple levels of subcommands
- **Key aspects**:
  - Subparsers can have their own subparsers
  - Deep nesting (3+ levels) support
  - Proper dispatch through multiple levels
- **Types**:
  - Two-level: "tool db create"
  - Three-level: "tool db migration generate"
- **Role**: Support enterprise CLI tools with complex command hierarchies

## Context
Advanced CLI tools like cloud providers' CLIs use nested subcommands for organizing many related commands.
