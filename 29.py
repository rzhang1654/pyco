#!/usr/bin/env python
#match only match from beging of the string
import re

m = re.match('foo','bar')
if m is not None:
 print m.group()
print re.match('foo', 'food on the table').group()
m = re.match('foo','bar foo')
if m is not None:
 print m.group()
m = re.match('foo','foo foo')
if m is not None:
 print m.group()
 print m.group(0)
 print m.group(1)
