```yaml
id: rule_for_github_actions
name: Rule for GitHub Actions
version: V00.01.00
updated: '2026-06-01'
```

## Rule

1. **No Automatic Workflows**: GitHub Actions workflows MUST NOT run automatically when files are modified
2. **Explicit Request Only**: Workflows only run when explicitly requested in a published workflow file or by user request
3. **No Auto-Triggers**: Do not define `on: push`, `on: pull_request`, `on: schedule` triggers for automatic execution

## Example

```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
```

## Rationale

- Prevents unintended automation costs
- Ensures workflows have clear purpose and trigger conditions
- Makes automation behavior predictable and auditable

---

## Change History

| Version | Date | Author | Model | Reason |
|---------|------|--------|-------|--------|
| V00.01.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Initial rule for GitHub Actions |
| V00.02.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Clarify: no auto workflows, explicit request only |