```yaml
id: conv_for_asp_or_def_references
name: Convention for ASP or Definition References
status: active
version: V00.01.00
updated: '2026-05-31'
```

## Convention

Documents that define concepts (def_) or aspects (asp_) SHOULD reference the appropriate higher-level documents.

### Reference Format

Use the `extends` field in frontmatter to reference parent concepts:

```yaml
extends: def_parent_concept
```

## Change History

| Version | Date | Author | Model | Reason |
|---------|------|--------|-------|--------|
| V00.01.00 | 2026-05-31 | raoulExtra | Poolside/Laguna XS.2 | init |