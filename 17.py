#!/usr/bin/env python
import sys
import re

infile=sys.argv[1]
ifh=open(infile,'r')
pattern=r't.p'
re_obj=re.compile(pattern)
for line in ifh:
  for match in re.findall(pattern,line):
    print "MATCHED->", match
