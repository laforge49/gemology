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
list
1
2
3 # count

text
Wrap
Copy
- Maps to: `[1, 2, 3]`.

#### Dicts
dict
"key1": "value"
"key2": 42
"#obj": "complex object"

text
Wrap
Copy
- Maps to: `{"key1": "value", "key2": 42}` (`"#obj"` omitted).
- Output: ```
dict
    "key1": "value"
    "key2": 42
    "#obj": ...
Multi-line Strings
Single-line:
text
Wrap
Copy
dict
    "text": "line1\nline2"
Maps to: {"text": "line1\nline2"}.
Spanning lines:
text
Wrap
Copy
dict
    "text": "line one
line two
line three"
Maps to: {"text": "line one\nline two\nline three"}. No leading whitespace unless intended.
Includes
text
Wrap
Copy
include
    "file.pdml"
Imports another PDML file.
Errors
From test data/bad1.pdml:

text
Wrap
Copy
list
    'single quotes'
Error: Single quotes (') unsupported; use ".
Notes
Test data: https://github.com/laforge49/gemology/tree/main/pdml/test%20data.
Manual examples: https://github.com/laforge49/gemology/tree/main/pdml/test%20data/manual.
text
Wrap
Copy

---