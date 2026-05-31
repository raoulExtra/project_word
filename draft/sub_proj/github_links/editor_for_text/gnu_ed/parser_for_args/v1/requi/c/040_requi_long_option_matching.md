---
id: requi_long_option_matching
name: Long Option Matching
kind: requirement
status: active
domain: arg_parser
---

# Long Option Matching Requirements

## Definition
The Arg_parser library must support exact and abbreviated long option matching with proper ambiguity detection.

## Details
- **Purpose**: Provide flexible long option specification while avoiding confusion
- **Key aspects**:
  - Exact match: --option matches only --option
  - Abbreviated match: --opt matches --option if unambiguous
  - Ambiguity detection: report error if abbreviation matches multiple options
- **Types**:
  - Exact match (preferred)
  - Unique abbreviation (acceptable)
  - Ambiguous abbreviation (error)
- **Role**: Balance user convenience with correctness

## Context
Long options allow descriptive names. Abbreviation support is convenient but must not lead to unexpected behavior.
