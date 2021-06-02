#!/usr/bin/env python
# character class
import re

m = re.search('^The', 'The end.') # match
if m is not None:
 print m.group()
m = re.search('^The', 'end. The') # not at beginning
if m is not None:
 print m.group()
m = re.search(r'\bthe', 'bite the dog') # at a boundary
if m is not None:
 print m.group()
m = re.search(r'\bthe', 'bitethe dog') # no boundary
if m is not None:
 print m.group()
m = re.search(r'\Bthe', 'bitethe dog') # no boundary
if m is not None:
 print m.group()
