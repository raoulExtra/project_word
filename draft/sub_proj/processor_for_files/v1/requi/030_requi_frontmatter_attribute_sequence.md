```yaml
id: requi_frontmatter_attribute_sequence
name: Frontmatter Attribute Sequence Requirement
kind: requi
status: active
statement: YAML frontmatter attributes MUST follow a specific sequence and naming convention
version: V00.01.00
updated: '2026-06-01'
```

## Summary

We SHALL define the canonical attribute sequence and formatting rules for YAML frontmatter used across markdown files.

## Requirement

We SHALL:

1. Define a canonical attribute sequence for YAML frontmatter
2. Require that `name` be human-readable (not just an identifier)
3. Require that `name` does not repeat the `kind` value
4. Specify formatting rules for attribute values

## Canonical Attribute Sequence

The following sequence is recommended for YAML frontmatter attributes:

1. `id` - Unique identifier
2. `name` - Human-readable name (must not repeat `kind`)
3. `kind` - Document kind (optional)
4. `tags` - Optional tags
5. `status` - Document status
6. `version` - Document version
7. `updated` - Last updated timestamp
8. `statement` - One-sentence description

## Name Field Rules

1. `name` MUST be human-readable (e.g., "Visitor for Files Requirement" not "requi_visitor_for_files")
2. `name` MUST NOT repeat the `kind` value (e.g., if `kind: requi`, then `name` should not be "Requi Visitor for Files")
3. `name` SHOULD describe the subject of the document in plain language

## Formatting Rules

1. Use double quotes for string values containing spaces
2. Use consistent date format: `YYYY-MM-DD`
3. Use consistent timestamp format: `YYYY-MM-DDTHH:MM:SS+HH:MM` or `YYYY-MM-DD`

## Examples

### Valid
```yaml
id: requi_visitor_for_files
name: "Visitor for Files Requirement"
kind: requi
status: active
version: V00.01.00
updated: '2026-06-01'
statement: Output the files the processor visits
```

### Invalid
```yaml
id: requi_visitor_for_files
name: "Requi Visitor for Files"  # repeats "Requi" from kind
kind: requi
```

## Rationale

- Human-readable names improve documentation clarity
- Avoiding repetition reduces cognitive load
- Consistent formatting enables reliable parsing

## Acceptance Criteria

- Given a frontmatter block, the tool validates that `name` is human-readable
- Given a frontmatter block, the tool validates that `name` does not repeat `kind`
- Given a frontmatter block, the tool validates attribute sequence

---

## Change History

| Version | Date | Author | Reason |
|---------|------|--------|--------|
| V00.01.00 | 2026-06-01 | raoulExtra | Initial requirement for frontmatter attribute sequence |