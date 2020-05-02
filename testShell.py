import fileinput
import sys

data = None
with fileinput.input() as lines:
    for line in lines:
        if lines.lineno() != 1:
           data += lines.lineno()