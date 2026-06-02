```yaml
id: ratio_phased_focus_within_phase
name: Ratio Phased Focus Within Phase
kind: rationale
status: active
version: V00.01.00
updated: '2026-06-02'
```

## Rationale

[[AI_LOCK+]]
The phased focus approach should be describable and implementable using concepts from the same phase or from phases below (more foundational). This ensures that higher phases do not depend on concepts that are defined later or at the same level.

Each phase builds upon and can be explained through the concepts of phases that came before it. When describing work within a phase, the terminology and conceptual framework should primarily draw from:

1. Concepts from the current phase
2. Concepts from all preceding (more foundational) phases

This creates a coherent, bottom-up progression where understanding accumulates progressively.


## Expected Benefits

- **Coherent progression**: Bottom-up understanding accumulates progressively
- **No circular dependencies**: Same-or-below concepts avoid logical loops
- **Foundational clarity**: Each phase builds on established concepts
- **Traceable reasoning**: Decision chains remain inspectable at every level

[[AI_LOCK-]]

## Guiding Principle

A phase's focus can be described using concepts from the same phase or below because:

- **Foundational dependency**: Each phase depends on concepts established in previous phases
- **Conceptual clarity**: Using same-or-below concepts avoids circular dependencies
- **Progressive elaboration**: Higher phases elaborate on foundations without presupposing advanced concepts
- **Traceable reasoning**: The reasoning chain remains inspectable at every level

## Application

When working on phase N:
- Use concepts from phases 0 to N to describe the work
- Avoid introducing concepts from phases N+1 or beyond
- Document how phase N concepts relate to and extend phase N-1 concepts

See `focus_ot_phased/000_focus_ot_initial.md` for phase structure.

[[AI_LOCK-]]

## Change History

| Version | Date | Author | Model | Reason |
|---------|------|--------|-------|--------|
| V00.01.00 | 2026-06-02 | raoulExtra | Poolside/Laguna XS.2 | init |