---
id: architecture
name: architecture
kind: requirement
status: active
domain: calculator
subdomain: mini
---

# Architecture

## Definition
The calculator uses a simple von Neumann architecture with accumulator-based operations.

## Components
- **Accumulator (AC)** - Primary register for arithmetic operations
- **Memory** - Word-addressable storage
- **Instruction Register** - Holds current instruction
- **Program Counter** - Points to next instruction

## Word Size
- 16-bit words (can represent -32,768 to 32,767)

## Memory Layout
- Addresses 0-100: Program storage
- Addresses 100+: Data storage