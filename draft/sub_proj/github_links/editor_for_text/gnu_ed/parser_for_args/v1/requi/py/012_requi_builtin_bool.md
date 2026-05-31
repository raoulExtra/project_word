---
id: requi_builtin_bool
name: Built-in Boolean Conversion
kind: requirement
status: active
domain: arg_parser_python
---

# Built-in Boolean Conversion Requirements

## Definition
The Python argument parser must convert string arguments to boolean values with flexible true/false recognition.

## Details
- **Purpose**: Enable boolean argument parsing with common true/false representations
- **Key aspects**:
  - True values: "true", "yes", "1", "on" (case-insensitive)
  - False values: "false", "no", "0", "off" (case-insensitive)
  - True/False for flags
- **Types**:
  - True: "true", "yes", "1", "on"
  - False: "false", "no", "0", "off"
  - Invalid: "maybe", "2", ""
- **Role**: Provide intuitive boolean argument handling

## Context
Boolean flags are common in CLI tools. Supporting multiple true/false representations improves user experience.
