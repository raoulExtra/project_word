---
id: requi_unicode_support
name: Unicode Support
kind: requirement
status: active
domain: arg_parser
---

# Unicode Support Requirements

## Definition
The Arg_parser library must correctly handle UTF-8 encoded option names and argument values.

## Details
- **Purpose**: Support internationalization and non-ASCII input
- **Key aspects**:
  - UTF-8 option names (long options)
  - UTF-8 argument values
  - Proper string length calculation for UTF-8
- **Types**:
  - Multibyte characters in option names
  - Unicode characters in argument values
  - Mixed ASCII/UTF-8 input
- **Role**: Enable global usage without character encoding issues

## Context
As command-line tools become global, they need to handle non-ASCII characters in both option names and argument values. UTF-8 is the standard encoding for this purpose.
