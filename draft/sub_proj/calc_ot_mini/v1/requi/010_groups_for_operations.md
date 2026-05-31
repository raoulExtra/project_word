---
id: op_groups
name: operation groups
kind: requirement
status: active
domain: calculator
subdomain: mini
---

# Operation Groups

## Definition
The operation set defines the supported arithmetic and logical operations for the calculator.

## Required Operations

### Arithmetic Operations
- **ADD** - Addition of two numbers
- **SUB** - Subtraction of two numbers
- **MUL** - Multiplication of two numbers
- **DIV** - Division of two numbers
- **INC** - Increment accumulator by 1
- **DEC** - Decrement accumulator by 1

### Logical Operations
- **AND** - Bitwise AND
- **OR** - Bitwise OR
- **XOR** - Bitwise XOR
- **NOT** - Bitwise NOT

### Control Operations
- **LOAD** - Load value into register
- **STORE** - Store register value to memory
- **JMP** - Unconditional jump to instruction
- **JZ** - Jump if accumulator is zero
- **JNZ** - Jump if accumulator is not zero
- **JL** - Jump if accumulator is less than zero
- **JG** - Jump if accumulator is greater than zero
- **HLT** - Halt execution

### Comparison Operations
- **CMP** - Compare two values (sets flags)
- **JE** - Jump if equal (used after CMP)
- **JNE** - Jump if not equal (used after CMP)

## Implementation Notes
- All operations work on word-sized integers
- Division returns integer quotient (truncated)
- Logical operations work on bit patterns

## Loops with Conditions

### While Loop Pattern
```
LOOP:
  ; condition check
  LOAD counter
  JZ END_LOOP    ; exit if zero
  ; loop body
  ; decrement counter
  DEC counter
  JMP LOOP
END_LOOP:
```

### For Loop Pattern
```
LOAD start_value
STORE counter
LOOP:
  ; check condition
  LOAD counter
  CMP limit
  JG END_LOOP    ; exit if greater than limit
  ; loop body
  ; increment counter
  INC counter
  JMP LOOP
END_LOOP:
```

### If-Else Pattern
```
LOAD value
CMP threshold
JL ELSE         ; jump if less than
; if block
JMP END
ELSE:
; else block
END:
```