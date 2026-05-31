---
id: requi_argument_order
name: Argument Order
kind: requirement
status: active
domain: arg_parser
---

# Argument Order Requirements

## Definition
The Arg_parser library must handle options appearing before, after, or interspersed with non-option arguments.

## Details
- **Purpose**: Support various command-line argument ordering conventions
- **Key aspects**:
  - Default: options can appear anywhere, non-options collected at end
  - In-order: preserve exact user argument order
  - Stop-on-non-option: stop parsing at first non-option argument
- **Types**:
  - ap_in_order: preserve argument order
  - ap_in_order_stop: stop at first non-option
  - ap_in_order_skip: skip non-options but don't collect them
  - ap_neg_non_opt: allow negative numbers as options
- **Role**: Accommodate different CLI conventions

## Context
Different tools have different expectations about argument order. The parser must be configurable to match these conventions.
