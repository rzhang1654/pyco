#!/usr/bin/env python
# 
import re
data  = 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'
patt = '^(\w{3})'
m = re.match(patt,data)
if m is not None:
  print m.group()
  print m.group(1)
  print m.groups()
#by moving 3 out, groups was replaced 3 times ended in u
patt = '^(\w){3}'
m = re.match(patt,data)
if m is not None:
  print m.group()
  print m.group(1)
  print m.groups()
