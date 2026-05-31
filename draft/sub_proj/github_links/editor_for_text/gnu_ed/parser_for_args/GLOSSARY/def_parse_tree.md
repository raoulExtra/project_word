---
id: def_parse_tree
name: Parse Tree
kind: concept
status: active
domain: arg_parser_python
---

# Parse Tree

## Definition
The internal representation of parsed arguments and subcommands, used for dispatch to appropriate handlers.

## Details
- **Purpose**: Internal representation of parsed CLI input
- **Key aspects**: Hierarchical structure, subcommand dispatch
- **Role**: Enable routing to correct handlers

## Context
The parse tree enables complex CLI tools to route to the correct subcommand handler based on user input.