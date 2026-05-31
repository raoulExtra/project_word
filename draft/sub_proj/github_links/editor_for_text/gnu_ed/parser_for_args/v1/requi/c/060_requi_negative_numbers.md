---
id: requi_negative_numbers
name: Negative Numbers
kind: requirement
status: active
domain: arg_parser
---

# Negative Numbers Requirements

## Definition
The Arg_parser library must correctly handle negative numbers passed as arguments, preventing them from being interpreted as options.

## Details
- **Purpose**: Allow programs to accept negative numeric values as arguments
- **Key aspects**:
  - Detect numeric-looking arguments (including negative numbers)
  - Treat negative numbers as non-option arguments by default
  - Support special values: "inf", "Inf", "INF"
- **Types**:
  - Integer negatives: -1, -42, -100
  - Floating point negatives: -3.14, -0.5
  - Special numeric values: inf, Inf, INF
- **Role**: Prevent misparsing of numeric arguments that start with '-'

## Context
Without this feature, a command like `prog -value -42` would incorrectly parse `-42` as an option. The `ap_neg_non_opt` flag enables proper handling of negative numbers as arguments.
