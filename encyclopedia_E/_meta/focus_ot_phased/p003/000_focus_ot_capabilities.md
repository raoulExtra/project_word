```yaml
id: focus_capabilities
name: Focus Interpretive Capabilities
kind: focus
status: active
version: V00.01.00
updated: '2026-06-02'
```

# Interpretive Capabilities Hierarchy

Priority capabilities for understanding and interpreting Encyclopedia E content, organized by layer:

## Capability Layers

### 1. Syntactic Parsing
- Parse YAML frontmatter (id, name, kind, status, version, updated)
- Parse markdown structure (headers, lists, tables)
- Identify metadata fields and content sections

### 2. Lexical Analysis
- Identify concept names and aliases
- Recognize reference patterns (/path/to/concept.md)
- Extract key terms and domain labels

### 3. Semantic Mapping
- Determine concept scope and boundaries
- Map relationships between concepts
- Understand domain context and positioning

### 4. Dependency Recognition
- Identify "uses", "references", "depends on" relationships
- Trace forward and backward references
- Catalog prerequisite connections

### 5. Phase Boundary Analysis
- Evaluate phase constraint compliance (N uses ≤N phases)
- Validate no circular dependencies
- Assess progressive accumulation of understanding

### 6. Cross-Cutting Evaluation
- Ensure consistency across multiple concepts/phases
- Identify conflicting definitions or interpretations
- Evaluate holistic coherence

### 7. Strategic Synthesis
- Plan release order based on dependency analysis
- Optimize phase boundaries for learning progression
- Balance completeness with early utility

## Application

Each capability builds upon previous layers. All 7 capabilities are required for full phase validation before release.

## See Also

- Ratio: Phased Development (Axiom 040)
- Ratio: High-Level Concepts First (Ratio 060)