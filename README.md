---
id: glossary_root
name: Glossary Root
kind: documentation
status: active
domain: glossaries
---

# Glossary Documentation

This repository contains structured glossaries organized by domain and project. Each glossary defines key terms, concepts, and definitions for specific areas of knowledge or software development projects. The goal is to have something unified which allows fast understanding for Agents and Humans.

## Structure Overview

```
glossaries/
├── disciplines_ot_academic/          # Academic discipline glossaries
│   ├── philosophy/                   # Philosophy terminology
│   ├── computer_sciences/           # Computer science terms
│   └── engineering_of_ontologies/   # Ontology engineering concepts
├── sciences_for_systems/             # Systems thinking glossary
│   ├── o/                           # Organizational concepts
│   └── s/                           # Systems concepts
└── [project-specific]/               # Project domain glossaries
    └── GLOSSARY/                    # Argument parser glossary
```

## Glossary Types

### 1. Academic Disciplines
Organized by academic field (philosophy, computer science, engineering). Each discipline contains subcategories for specific concepts.

**Structure:**
- `disciplines_ot_academic/[discipline]/` - Main glossary directory
- `[subcategory]/` - Concept categories (e.g., o/ for organizational)
- `[term].md` - Individual term definitions

### 2. Systems Thinking
Focused on systems theory, organizational structures, and interdisciplinary concepts.

**Structure:**
- `sciences_for_systems/[prefix]/` - Prefix-based categorization
- `[concept].md` - Concept definitions with cross-references

### 3. Project-Specific Glossaries
Domain-specific terminology for software projects (e.g., argument parsing, CLI tools).

**Structure:**
- `project/GLOSSARY/` - Project glossary directory
- `README.md` - Glossary metadata and overview
- `[term].md` - Term definitions with links to implementation

## Glossary Metadata Format

Each glossary uses YAML frontmatter for metadata:

```yaml
---
id: glossary_identifier
name: Human-readable title
kind: documentation | reference | terminology
status: active | draft | deprecated
domain: domain_identifier
---
```

## Term Definition Format

Individual terms use markdown with cross-references:

```markdown
# Term Name

Definition and explanation of the term.

## Usage

Example usage or context where the term applies.

## Related Terms

- [RelatedTerm](path/to/related.md) - Connection to other concepts
```

## Navigation

### By Domain
- **Philosophy**: `disciplines_ot_academic/philosophy/`
- **Computer Science**: `disciplines_ot_academic/computer_sciences/`
- **Systems**: `sciences_for_systems/`

### By Project
- **Argument Parser**: `sub_proj/github_links/editor_for_text/gnu_ed/parser_for_args/GLOSSARY/`

## Contributing

1. Create a new glossary in the appropriate domain folder
2. Add YAML frontmatter with proper metadata
3. Define terms using markdown with cross-references
4. Update parent README.md with term links
