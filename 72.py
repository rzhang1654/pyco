#!/usr/bin/env python
# print all valid python identifiers a-z A-Z _
import re
import sys
string = open(sys.argv[1],'r').read()
arr = string.split()
print arr
pattern=r'^\w+$'
pattern_obj = re.compile(pattern)
for item in arr:
 m = pattern_obj.search(item)
 if m:
   print m.group()
