```yaml
id: rule_for_markers_ot_ai_lock
name: Rule for Markers OT AI_LOCK
status: active
version: V00.01.00
updated: '2026-06-02'
```

## Rule

1. **Marker Recognition**: Text enclosed between `[[AI_LOCK+]]` and `[[AI_LOCK-]]` markers is protected from AI modifications
2. **No Changes Allowed**: AI agents MUST NOT modify, delete, or alter any content within these markers
3. **Respect Intent**: These markers indicate content that requires human approval before changes

## Example

```markdown
[[AI_LOCK+]]
This paragraph is protected from AI changes.
[[AI_LOCK-]]

Normal content can be modified by AI.
```

## Rationale

- Ensures human control over critical content
- Allows selective protection of sensitive sections
- Provides clear boundaries for AI behavior
- Supports collaborative editing workflows

---

## Change History

| Version | Date | Author | Model | Reason |
|---------|------|--------|-------|--------|
| V00.01.00 | 2026-06-02 | assistant | Poolside/Laguna XS.2 | Initial rule for AI_LOCK markers |