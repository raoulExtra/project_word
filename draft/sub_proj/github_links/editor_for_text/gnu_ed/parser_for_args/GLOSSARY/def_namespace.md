---
id: def_namespace
name: Namespace
kind: concept
status: active
domain: arg_parser_python
---

# Namespace

## Definition
A simple object that holds parsed argument values as attributes. Returned by `parse_args()` method.

## Details
- **Purpose**: Container for parsed argument values
- **Key aspects**: Attribute access, dynamic attributes
- **Role**: Bridge between parsed arguments and application code

## Context
The Namespace provides a clean interface for accessing parsed arguments as object attributes rather than dictionary keys.