```yaml
id: conv_for_code_change_propagation
name: Convention for Code Change Propagation
version: V00.01.00
updated: '2026-06-01'
```

## Convention

When code changes affect public interfaces, all connected files MUST be updated to maintain consistency, but only when explicitly requested by the user.

## Rules

1. **Adapt Connected Files**: When a module's interface changes, update all files that reference or depend on it (when requested)
2. **README References**: Each main module MUST include a comment referencing its related README.md
3. **Cross-References**: Update cross-references in related documentation files (when requested)

## Example

When renaming `file_processor.py` to `processor_for_files.py`:
- Update import statements in test files
- Update command examples in README.md
- Update cross-references in related requirement files

## README Reference Format

Each main module should include a comment like:
```python
# See: README.md for usage documentation
```

## Rationale

- Maintains documentation-code consistency
- Prevents broken references after refactoring
- Ensures discoverability of usage information

---

## Change History

| Version | Date | Author | Model | Reason |
|---------|------|--------|-------|--------|
| V00.01.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Initial convention for code change propagation |
| V00.02.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Adapt connected files only when explicitly requested |