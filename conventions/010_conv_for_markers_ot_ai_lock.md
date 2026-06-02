```yaml
id: conv_for_markers_ot_ai_lock
name: Convention for Markers OT AI_LOCK
kind: convention
tags:
- ai-lock
status: active
version: V00.01.00
updated: '2026-06-02'
```

## Convention

1. **Marker Syntax**: Use `[[AI_LOCK+]]` to open and `[[AI_LOCK-]]` to close protected sections
2. **Protected Content**: Any content between these markers MUST NOT be modified by AI agents
3. **Document Placement**: Place markers at the beginning of files or around specific paragraphs that require human approval
4. **Purpose Documentation**: Optionally include a comment explaining the reason for protection

### Example Structure

```markdown
---
frontmatter
---

[[AI_LOCK+]]
This entire section requires human review before AI changes.
[[AI_LOCK-]]

Normal content below can be modified by AI.
```

## Rationale

- Ensures human oversight of critical content
- Provides clear boundaries for AI modification scope
- Supports collaborative workflows between humans and AI
- Prevents accidental changes to sensitive sections

## See Also

- [Rule 010: Rule for Markers OT AI_LOCK](rules/010_rule_for_markers_ot_ai_lock.md)

## Change History

| Version | Date | Author | Model | Reason |
|---------|------|--------|-------|--------|
| V00.01.00 | 2026-06-02 | assistant | Poolside/Laguna XS.2 | Initial convention for AI_LOCK markers |