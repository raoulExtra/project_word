---
id: requi_subcommands
name: Subcommands
kind: requirement
status: active
domain: arg_parser_python
---

# Subcommands Requirements

## Definition
The Python argument parser must support subcommands (similar to git, docker, etc.) with separate argument parsers for each subcommand.

## Details
- **Purpose**: Enable CLI tools with multiple operations
- **Key aspects**:
  - Add subparsers to main parser
  - Each subcommand has its own arguments
  - Dispatch to appropriate handler function
- **Types**:
  - Required subcommands
  - Optional subcommands
  - Nested subcommands
- **Role**: Support complex CLI tools with multiple modes of operation

## Context
Many modern CLI tools use subcommands to organize related functionality. This is a key feature for building professional command-line interfaces in Python.
