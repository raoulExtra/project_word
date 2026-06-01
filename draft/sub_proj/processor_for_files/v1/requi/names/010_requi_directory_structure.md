```yaml
id: requi_directory_structure
name: "Directory Structure Requirement"
kind: requi
status: active
statement: The processor_for_files project directory structure MUST follow naming conventions
version: V00.01.00
updated: '2026-06-01'
```

## Summary

We SHALL provide a directory structure that follows the naming convention:
- `<project>/<version>/<kind>/<noun>/` or `<project>/<version>/<kind>/<noun>/<connector>/`

## Requirement

We SHALL organize files in:

- `<project>/v<version>/<kind>/` - main requirement directories
- `<project>/v<version>/<kind>/<noun>/` - specialized subdirectories
- `<project>/v<version>/<kind>/<noun>/<connector>/` - further subdivision

## Rationale

- Keeps related requirements grouped
- Enables predictable navigation
- Supports automated tooling

## Acceptance Criteria

- All requirements in `processor_for_files/v1/requi/` follow the directory structure

---

## Change History

| Version | Date | Author | Reason |
|---------|------|--------|--------|
| V00.01.00 | 2026-06-01 | raoulExtra | Initial requirement for directory structure |