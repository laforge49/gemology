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
```
list
    1
    2
    3 # count
```

- Maps to Python: `[1, 2, 3]`.

#### Dicts
- Python: `{"key1": "value", "key2": 42`, "#obj" "Ignore this"}
- Output: 
```
dict
    "key1": "value"
    "key2": 42
    # "#obj": ...
```

#### Multi-line Strings 
```
dict
    "text": "line1\nline2"
```
Maps to Python: {"text": "line1\nline2"}.
#### Spanning lines:
```
dict
    "text": "line one
line two
line three"
```
Maps to: {"text": "line one\nline two\nline three"}. No leading whitespace unless intended.

#### Includes
```
include
    "file.pdml"
```

Imports another PDML file.
#### Errors
From test data/bad1.pdml:

```
list
    'single quotes'
```
Error: Single quotes (') unsupported; use ".
Notes
Test data: https://github.com/laforge49/gemology/tree/main/pdml/test%20data.
Manual examples: https://github.com/laforge49/gemology/tree/main/pdml/test%20data/manual.

---