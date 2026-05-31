---
id: datatypes_efficient
name: datatypes for efficiency
kind: requirement
status: active
domain: calculator
subdomain: mini
---

# Datatypes for Efficiency

## Definition
Efficient data representation strategies for the calculator to minimize memory usage and maximize performance.

## Requirements

### Integer Representation
- **Size**: 16-bit signed integers
- **Range**: -32,768 to 32,767
- **Encoding**: Two's complement

### Boolean Interpretation
- **True**: Any non-zero value (1, -1, 42, etc.)
- **False**: Zero (0)
- **Logical Operations**: Treat integers as bit patterns for AND, OR, XOR, NOT
- **Conditional Branching**: Test if value is zero (false) or non-zero (true)
- **Comparison Flags**: CMP sets flags for zero, negative, and greater-than conditions

### Memory Alignment
- Words aligned on 16-bit boundaries
- No padding required for word-sized data

### Register Usage
- Single accumulator for primary operations
- Secondary registers for intermediate results

## Optimization Goals
- Minimize memory accesses
- Reduce instruction count for common operations
- Use bit manipulation for efficiency