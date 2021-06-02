#!/usr/bin/env python
# ifference between match and search - ignorecase
import re

bt=r'bat|bet|bit'
m = re.match(bt,'bat')
if m is not None:
 print m.group()

m = re.match(bt, 'blt') # no match for 'blt'
if m is not None:
 print m.group()

m = re.match(bt, 'He bit me!') # does not match string
if m is not None:
  print m.group()

m = re.search(bt, 'He bit me!') # found 'bit' via search
if m is not None:
 print m.group()


