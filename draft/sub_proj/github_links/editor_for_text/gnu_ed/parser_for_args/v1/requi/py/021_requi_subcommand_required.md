---
id: requi_subcommand_required
name: Required Subcommands
kind: requirement
status: active
domain: arg_parser_python
---

# Required Subcommands Requirements

## Definition
The Python argument parser must support required subcommands that must be specified by the user.

## Details
- **Purpose**: Enforce subcommand specification for multi-command tools
- **Key aspects**:
  - Subparser with required=True
  - Error if no subcommand given
  - Dest attribute for subcommand name
- **Types**:
  - Required positional subcommand
  - Error message when missing
- **Role**: Ensure correct usage of multi-command CLI tools

## Context
Many CLI tools require a subcommand (e.g., "git clone", "docker run"). The parser must enforce this requirement.
