# module pdml.loader.py

Converts PDML strings and files into 
python data structures.

Scalars are converted from string form
to python data structures using 
ast.literal_eval.
The exception here is strings, which
may span multiple lines.


A limited unit test is included.

## API

### string_reader(pdml_string: str) -> any
Converts a PDML string to a python data
structure.

### file_reader(from_path: pathlib.Path) -> any
Reads a PDML file and converts it into a
python data structure.
