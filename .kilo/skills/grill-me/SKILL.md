---
name: grill-me
description: Interview the user about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".
---

# Grill Me

Interview the user relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one.

## Process

**Ask ONE question at a time.** Wait for user response before continuing. Persist state to avoid duplicate questions on interruption.

## When to Explore

If a question can be answered by exploring the codebase, explore the codebase instead of asking.

## Format

For each question:

1. State the question clearly
2. Provide numbered options (1-5), with the last option being "Other (specify)"
3. Wait for user response

## State Persistence

Before asking each question, write current state to `grill-me.tmp.md`:

```markdown
# Grill-Me Session State

- Current Question: N
- Answers:
  - Q1: answer
  - Q2: answer
```

On restart, read this file to resume.

## Example Question

What are the non-functional requirements for this system?
- 1. Performance and scalability
- 2. Security and compliance
- 3. Maintainability and extensibility
- 4. User experience and accessibility
- 5. Other (specify)

2. What are the failure modes?
   - 1. Component unavailability
   - 2. Data corruption or loss
   - 3. Network failures
   - 4. Invalid input handling
   - 5. Other (specify)

Start with high-level architecture, then drill into specifics.