```yaml
id: conv_for_github_actions
name: Convention for GitHub Actions
version: V00.01.00
updated: '2026-06-01'
```

## Convention

GitHub Actions workflows MUST NOT run automatically unless there is an explicit trigger defined in the workflow file.

## Rule

1. Every workflow must have a clearly stated trigger (e.g., `on: push`, `on: pull_request`, `on: schedule`)
2. Automatic workflows without explicit triggers are prohibited
3. Workflows triggered by `workflow_dispatch` or `repository_dispatch` require documentation explaining when and why they are invoked

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