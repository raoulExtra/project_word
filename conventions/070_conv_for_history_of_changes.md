```yaml
id: conv_for_history_of_changes
name: Convention for History of Changes
tags:
- conventions
- change_history
status: active
version: V00.04.00
updated: '2026-05-31'
```

# Convention: Change History section
> Version: V00.04.00

## Rule

Documents that track changes over time SHOULD include a `## Change History` section at the end of the file.

### Format

Use a Markdown table with these required columns:

| Version | Date | Author | Model | Reason |

### Constraints

- `Version`
  - MUST use the repo version format: `V00.01.00`
  - See: `70_conv_versions.md`
- `Date`
  - MUST use ISO format: `YYYY-MM-DD`
- `Author`
  - SHOULD be a stable identifier (e.g. `peter`, `ai(cline)`)
  - See: `005_conv_for_IDE.md`
- `Model`
  - SHOULD reference the model used for the change
  - See: `005_conv_for_IDE.md`
- `Reason`
  - MUST be short and specific (what changed + why)
  - See style guidance: `90_conv_style_short_precise.md`

### Ordering

- Append-only: new rows are added at the bottom.
- The first row is typically `V00.01.00`.

## Example

```md
## Change History

| Version | Date | Author | Model | Reason |
|---------|------|--------|-------|--------|
| V00.01.00 | 2026-05-24 | ai(cline) | - | Initial publication |
| V00.02.00 | 2026-05-25 | peter | - | Clarify acceptance criteria wording |
```

## Rationale

- Standardizes change tracking across docs.
- Makes diffs easier to interpret.
- Enables automation (parsing versions/dates).

---

## Change History

| Version | Date | Author | Model | Reason |
|---------|------|--------|-------|--------|
| V00.01.00 | 2026-05-24 | ai(cline) | - | Initial publication |
| V00.02.00 | 2026-05-31 | ai(cline) | - | Update frontmatter to yaml |
| V00.03.00 | 2026-05-31 | raoulExtra | Poolside/Laguna XS.2 | Reference IDE convention for author info |
| V00.04.00 | 2026-05-31 | raoulExtra | Poolside/Laguna XS.2 | Add Model column to Change History table |
