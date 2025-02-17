# module pdml.saver.py

This module creates pdml strings and files
from python data structures.

Python scalars (str, int, long, bool, etc.)
are supported along with list and dict 
structures.

Escape sequences created in strings:
\\\\, \\n and \\\".

A limited unit test is included.

## API

### writer(to_path: pathlib.Path, data: any) -> str
Writes a PDML file to the given path.

### debug(data: any) -> None
Converts the data structure to a PDML
string and prints it.