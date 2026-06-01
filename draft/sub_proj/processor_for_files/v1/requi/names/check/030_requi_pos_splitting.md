```yaml
id: requi_pos_splitting
name: POS Splitting Requirement
kind: requi
status: active
statement: Processed file names MUST be split into word types (POS) and organized into a two-level folder structure
version:
updated:
```

## Summary

We SHALL split processed names into their word type (part of speech) and organize them into folders based on the first two letters of the word.

## Requirement

We SHALL:

1. Determine the part of speech (POS) for each word in a processed name
2. Create a folder structure: `<data>/<first_two_letters>/<word>.md`
3. Place each word file in its corresponding POS-specific folder

## Folder Structure

- `<data>/ab/about.md` - for words starting with "ab"
- `<data>/ca/cache.md` - for words starting with "ca"
- `<data>/ch/checker.md` - for words starting with "ch"

## Rationale

- Enables fast lookup by first two letters
- Organizes words by their part of speech
- Supports scalable word database organization

## Acceptance Criteria

- Given a processed name, the tool identifies word types
- Given a word, the tool creates the appropriate folder path
- Words are stored with their POS metadata

---

## Change History

| Version | Date | Author | Reason |
|---------|------|--------|--------|
| V00.01.00 | 2026-06-01 | raoulExtra | Initial requirement for POS splitting |