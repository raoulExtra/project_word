```yaml
id: conv_for_github_actions
name: Convention for GitHub Actions
version: V00.01.00
updated: '2026-06-01'
```

## Convention

GitHub Actions workflows MUST NOT run automatically when files are modified unless explicitly requested in a published workflow file or by user request.

## Rule

1. No automatic workflows on file changes (push, pull_request, etc.) unless explicitly defined
2. Workflows triggered by `workflow_dispatch` or `repository_dispatch` require explicit user request
3. Only run workflows when explicitly requested by user or through published workflow definitions

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
| V00.01.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Initial convention for GitHub Actions |
| V00.02.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Clarify: no auto workflows on file changes, only on explicit request |