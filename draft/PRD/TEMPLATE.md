# PRD Template

## What a PRD Is

A PRD is a structured document that captures:

- **The Problem** — what user pain or opportunity the product addresses
- **The Users** — who the product is for and what they need
- **The Requirements** — functional and non-functional expectations
- **The Scope** — what's in, what's out
- **Success Metrics** — how you'll know it worked
- **Constraints** — technical, legal, operational
- **Risks** — what could go wrong and how to mitigate

A PRD is not a technical spec, a design mock, or a project plan — but it informs all of them.

## Typical PRD Structure

Each section includes guidance and links to related documentation.

### 1. Overview
A crisp summary of the product and its purpose.

### 2. Goals
What the product aims to achieve.

See: `ai_env/ai_entities/glossaries/general/020_def_domain.md`

### 3. User Stories
Narrative descriptions of user needs in "As a [role], I want [capability] so that [benefit]" format.

### 4. Use Cases
Concrete scenarios showing how the system solves problems for users.

Each use case should include:
- **Name**: Brief descriptive title
- **Actor**: Who uses this capability
- **Precondition**: What must be true before
- **Flow**: Step-by-step interaction
- **Postcondition**: Result of the interaction
- **Example**: Specific instance of the use case

Example format:
```
#### Use Case: Process Documentation Analysis
- **Actor**: AGI researcher
- **Precondition**: Project documentation exists in markdown format
- **Flow**: 
  1. User runs `think_about projects/requi_ai_env/v8/requi/`
  2. System processes markdown files recursively
  3. Patterns are extracted and learned
  4. Thought outputs are generated
- **Postcondition**: Insight files created showing learned relationships
```

### 5. Functional Requirements
What the product must do, listed as specific, testable capabilities.

See: `ai_env/ai_entities/glossaries/general/030_def_layer.md`

Example format:
```
- [Requirement name] - Brief description of what is required
- [Feature] - Specific capability with acceptance criteria
```

### 6. Non-Functional Requirements
Performance, reliability, security, and other quality expectations.

See: `ai_env/ai_entities/glossaries/general/050_def_efficiency.md`

### 7. Success Metrics
KPIs, adoption targets, quality thresholds, and measurement methods.

### 8. Dependencies
Teams, systems, APIs, and external resources this product relies on.

### 9. Open Questions
Unresolved decisions, assumptions, or areas needing stakeholder input.

### 10. Constraints
Technical, legal, operational, or resource limitations.

### 11. Risks & Mitigations
Potential issues and planned responses.

### 12. Scope
- **In Scope**: What is included
- **Out of Scope**: What is explicitly excluded

### 13. Timeline & Milestones
Key delivery dates and checkpoints (optional).

## Why PRDs Matter

A strong PRD:

- Prevents misalignment between teams
- Reduces rework by clarifying expectations early
- Helps prioritize features
- Creates a shared mental model of the product
- Anchors decisions when trade-offs arise

In fast-moving teams, a PRD is less about bureaucracy and more about clarity.

## Non-Obvious Insight

The best PRDs don't try to predict everything. They define the boundaries of good decisions, not the decisions themselves.

A PRD should empower engineers and designers — not constrain them.

# 5W Questions help

## What
Brief description of the core functionality/product.

## When
Timing, frequency, or conditions for the action.

## Where
Location, environment, or system context.

## Who
Target users or stakeholders.

## Why
Purpose or rationale behind the product/functionality.
