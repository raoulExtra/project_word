```yaml
id: conv_filename_by_term_start
name: Convention for Filename by Term Start
version: V00.01.00
updated: '2026-05-31'
```

## Convention

Files in `_/` subdirectories should be organized by the **first letter of the term name**, not by the prefix (def_/asp_/ref_).

Frontmatter MUST use ```yaml code blocks, NOT `---` delimiters.

### Rule

- `def_model_for_simulation.md` → should be in `s/` directory (term starts with "simulation")
- `def_simulation_model.md` → should be in `s/` directory
- `asp_applicability.md` → should be in `a/` directory (term starts with "applicability")
- `def_abstraction.md` → should be in `a/` directory

### Exception

If multiple terms start with the same letter, use subdirectories:
- `s/` could contain: `def_simulation_model.md`, `def_scenario.md`, `def_system.md`

## Change History

| Version | Date | Author | Model | Reason |
|---------|------|--------|-------|--------|
| V00.01.00 | 2026-05-31 | raoulExtra | Poolside/Laguna XS.2 | init |