---
name: grill-me
description: Interview the user about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".
---

# Grill Me

Interview the user relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one.

## Process

Ask questions one at a time. Wait for feedback before continuing.

## When to Explore

If a question can be answered by exploring the codebase, explore the codebase instead of asking.

## Format

For each question:

1. State the question clearly
2. Provide your recommended answer (or "I don't know" if you need to explore)
3. Wait for user response

## Example Questions

- What are the non-functional requirements?
- What are the failure modes?
- What assumptions does this make about data?
- What happens if X is unavailable?
- How does this interact with existing systems?

Start with high-level architecture, then drill into specifics.