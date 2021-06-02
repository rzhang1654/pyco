#!/usr/bin/env python
#match any pair of word seperated by s single space
#I presume it has to be from the start of sentence and not other thing in the line
import re
import sys
pattern=r'^[A-Za-z][A-Za-z_]*\s[A-Za-z_]+$'
pattern_obj = re.compile(pattern)
file_obj = open(sys.argv[1],'r')
for line in file_obj:
  m = pattern_obj.match(line)
  if m: 
    print m.group()
