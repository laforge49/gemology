# Python Data Markup Language (PDML)

Think of PDML as an alternative to JSON. 
The design goal of PDML is to make it easy to
maintain deeply nested data structures. The key
innovation of PDML is the use of indentation to
represent nested data structures. This is analogous 
to python's use of nesting to represent nested code.

Python scalars are supported, as well as the list
and dict collections. Multi-line strings are also
supported.

There are two keywords used in PDML: list and dict.
There are three special characters used as well, 
", : and #.
Each item in a list or dict starts on a new line. 
Dictionary keys are strings followed by a colon (:).

In PDML text, the # indicates the beginning
of a comment and the remainder of the line is not
processed.

And when serializing data into PDML text, a key
in a dictionary which starts with a # causes the 
key and its associated value to be ignored. By this 
means data structures can be serialized which contain
elements that are not supported by PDML. Case in point,
while PDML can only represent tree structures, the 
data being converted to PDML can include circular 
references.

For examples of PDML files, please see the test data 
directory.
