---
id: prd_glossary
name: Glossary System Article
kind: arti
status: active
elements:
- Overview section describing glossary system purpose
- Goals section outlining system objectives
- User Stories section with contributor perspectives
- Structure section with directory organization
- Entry Format section with YAML template
- Article Files section explaining arti type
- Success Metrics section for validation
---

# Glossary System Article

## Overview

A glossary system is a structured collection of definitions organized by domain, providing consistent terminology and cross-referencing for knowledge organization.

## Goals

- Create a standardized format for glossary entries
- Organize definitions by domain and subdomain
- Enable cross-referencing between related concepts
- Support multiple glossaries within a unified system

## User Stories

- As a user, I want to find definitions organized by subject area
- As a contributor, I want a clear template for new entries
- As a maintainer, I want consistent formatting across all entries

## Structure

### Directory Organization
```
encyclopedia_E/
├── computing/
├── disciplines_ot_academic/
│   ├── _/
│   ├── concepts_ot_core/
│   ├── philosophy/
│   │   ├── _/
│   │   ├── logic_ot_philosophical/
│   │   ├── metaphyiscs/
│   │   └── c/
│   ├── sciences_ot_empirical/
│   ├── sciences_ot_formal/
│   ├── techniques_ot_concrete_in/
│   ├── computer_sciences/
│   │   ├── _/
│   │   │   ├── s/
│   │   │   └── h/
│   └── sciences_for_systems/
│       └── _/
│           └── o/
├── engineering_of_ontologies/
│   └── asp_ot_structural/
│       └── _/
├── linguistics/
├── mathematics/
├── morphology/
├── software_development/
│   └── arg_parser/
└── prd_glossary.md
```

### Entry Format
Each entry follows YAML frontmatter + Markdown:
```yaml
---
id: unique_identifier
name: term_name
kind: concept|aspect|suffix|requirement|documentation|arti
status: active|draft
domain: subject_domain
subdomain: optional_subdivision
extends: parent_guide_reference
related: cross_reference_path (optional)
elements: list of concrete described elements (arti only)
---

# Term Name

## Definition
[Clear definition of the term]

## Details
- **Purpose**: primary function or use
- **Key aspects**: main characteristics
- **Types**: classifications or variations
- **Examples**: examples or use cases
- **Role**: position in knowledge structure
```

### Article (arti) Files
Articles are concrete described elements containing specific structured content:
- `elements`: YAML list of concrete described elements inside the article
- Contains detailed exposition, examples, and applied knowledge

## Success Metrics

- All entries have consistent YAML frontmatter
- Cross-references are functional
- New contributors can easily add entries
- Terms are discoverable by domain