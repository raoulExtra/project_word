```yaml
id: conv_for_grill_me_persistence
name: Convention for Grill-Me Persistence
status: active
version: V00.01.00
updated: '2026-06-01'
kind: conv
```

## Convention

When the grill-me skill is interrupted, persist the current state to avoid asking duplicate questions.

## Rule

1. **Write State to File**: Before interruption, write current question number and answers to `grill-me.tmp.md`
2. **Resume from File**: On restart, read `grill-me.tmp.md` to continue from last question
3. **Clear on Completion**: Delete `grill-me.tmp.md` when grill-me session completes
4. **File Location**: Store `grill-me.tmp.md` in the current working directory

## Format

```markdown
# Grill-Me Session State

- Current Question: N
- Answers:
  - Q1: answer
  - Q2: answer
```

## Rationale

- Prevents redundant questioning
- Maintains conversation flow
- Enables interruption recovery

---

## Change History

| Version | Date | Author | Model | Reason |
|---------|------|--------|-------|--------|
| V00.01.00 | 2026-06-01 | raoulExtra | Poolside/Laguna XS.2 | Initial convention for grill-me persistence |