```yaml
id: conv_for_yaml_frontmatter
name: Convention for YAML Frontmatter
version: V00.01.00
updated: '2026-06-01'
```

## Convention

YAML frontmatter in markdown files MUST follow these conventions for naming and structure.

## Name Field

1. `name` MUST be human-readable (e.g., "Visitor for Files Requirement")
2. `name` MUST NOT repeat the `kind` value (e.g., if `kind: requi`, name should not be "Requi Visitor")
3. `name` SHOULD be concise but descriptive of the document's subject

## Kind Field

1. `kind` indicates the document type (e.g., `requi`, `def`, `conv`, `asp`)
2. `kind` SHOULD match the file prefix (e.g., `010_requi_visitor.md` has `kind: requi`)
3. `kind` is optional in frontmatter but required in file naming

## ID Field

1. `id` MUST be unique across all documents
2. `id` SHOULD follow the filename pattern without extension
3. `id` uses snake_case (e.g., `requi_visitor_for_files`)

## Example

```yaml
id: requi_visitor_for_files
name: "Visitor for Files Requirement"
kind: requi
status: active
version: V00.01.00
updated: '2026-06-01'
statement: Output the files the processor visits
```

## Rationale

- Human-readable names improve documentation discoverability
- Avoiding repetition reduces cognitive load when reading documents
- Consistent naming enables reliable tooling and automation

## See Also

- [Requirement 030](draft/sub_proj/processor_for_files/v1/requi/030_requi_frontmatter_attribute_sequence.md) - Frontmatter attribute sequence
- [Convention 040](040_conv_for_namings_of_files.md) - File naming convention

---

## Change History

| Version | Date | Author | Model | Reason |
|---------|------|--------|-------|--------|
| V00.01.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Initial convention for YAML frontmatter |