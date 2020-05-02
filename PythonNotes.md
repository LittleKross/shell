# Python notes

## CSCI - P436 | _Brandon Young_

### optparse __DEPRECIATED__

[optparse documentation](https://docs.python.org/3/library/optparse.html)

```Python
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()
```

### argparse __CURRENT__

[argparse docs](https://docs.python.org/3/howto/argparse.html#id1)

```python3
import argparse
parser = argparse.ArgumentParser()
parser.parse_args()
```