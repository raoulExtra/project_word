---
id: requi_duplicate_options
name: Duplicate Options
kind: requirement
status: active
domain: arg_parser
---

# Duplicate Options Requirements

## Definition
The Arg_parser library must handle duplicate option specifications by using the last occurrence.

## Details
- **Purpose**: Provide predictable behavior for repeated options
- **Key aspects**:
  - Last occurrence wins for option values
  - All occurrences are recorded in the output
  - No error for duplicate options
- **Types**:
  - Repeated short options: `-v -v`
  - Repeated long options: `--verbose --verbose`
  - Mixed duplicates: `-v --verbose` (if same semantics)
- **Role**: Ensure deterministic parsing results

## Context
When users accidentally or intentionally specify the same option multiple times, the parser should accept this and the last value should be the effective one. This is standard POSIX behavior.
