Here’s the exact contents of the Markdown file for you to copy into a `.md` file (e.g., `PDML_overview.md`):

```markdown
### PDML Overview

PDML (Persistent Data Markup Language) maps to Python data structures using indentation, with selective persistence.

#### Structure
- **Indentation**: Required for hierarchy.
- **Keywords**: `list`, `dict`, `include`.
- **Scalars**: Python literals:
  - Numbers (e.g., `42`), booleans (`True`, `False`).
  - Strings: Use `"`, not `'`. Escapes: `\n`, `\"`. Can span lines or use `\n` in one line.
- **Dict Keys**: Strings, followed by `:` (e.g., `"key":`).
- **Comments**: `#` outside strings terminates the line (e.g., `42 # comment`).
- **Non-persisted Keys**: Keys starting with `#` (e.g., `"#temp":`) are excluded from persistence:
  - Output as comments with `...` (e.g., `#temp: ...`).
  - Allows objects without PDML representation and cyclic references in Python data.

#### Lists
From `test data/one.pdml`:
```
list
    1
    2
    3 # count
```
- Maps to: `[1, 2, 3]`.

#### Dicts
```
dict
    "key1": "value"
    "key2": 42
    "#obj": "complex object"
```
- Maps to: `{"key1": "value", "key2": 42}` (`"#obj"` omitted).
- Output: `dict\n    "key1": "value"\n    "key2": 42\n    "#obj": ...`.

#### Multi-line Strings
1. Single-line:
```
dict
    "text": "line1\nline2"
```
- Maps to: `{"text": "line1\nline2"}`.

2. Spanning lines:
```
dict
    "text": "line one
line two
line three"
```
- Maps to: `{"text": "line one\nline two\nline three"}`. No leading whitespace unless intended.

#### Includes
```
include
    "file.pdml"
```
- Imports another PDML file.

#### Errors
From `test data/bad1.pdml`:
```
list
    'single quotes'
```
- Error: Single quotes (`'`) unsupported; use `"`.

#### Notes
- Test data: https://github.com/laforge49/gemology/tree/main/pdml/test%20data.
- Manual examples: https://github.com/laforge49/gemology/tree/main/pdml/test%20data/manual.
```

---
