---
id: requi_error_handling_py
name: Error Handling (Python)
kind: requirement
status: active
domain: arg_parser_python
---

# Error Handling Requirements (Python)

## Definition
The Python argument parser must provide Pythonic error handling with SystemExit for argument errors and helpful error messages.

## Details
- **Purpose**: Integrate with Python's error handling conventions
- **Key aspects**:
  - SystemExit on argument errors
  - Formatted error messages
  - Usage display on error
  - Custom error handlers
- **Types**:
  - ArgumentError exceptions
  - UsageError handling
  - Exit code management
- **Role**: Provide familiar Python CLI error behavior

## Context
Python CLI tools expect argparse-like error handling. Users should see familiar error messages and the program should exit with appropriate codes on argument errors. Custom error handlers are supported for advanced use cases.
