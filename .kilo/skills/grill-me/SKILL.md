---
name: grill-me
description: Interview the user about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".
---

# Grill Me

Interview the user relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one.

## Process

VERY IMPORTANT: Ask **one question at a time** using **numbered options**. Always include an option for custom input. Wait for feedback before continuing.

## When to Explore

If a question can be answered by exploring the codebase, explore the codebase instead of asking.

## Format

For each question:

1. State the question clearly
2. Provide numbered options (1-5), with the last option being "Other (specify)"
3. Wait for user response

## Example Questions

1. What are the non-functional requirements?
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