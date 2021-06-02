#!/usr/bin/env python
import sys
import re

infile=sys.argv[1]
ifh=open(infile,'r')
pattern=r'uxbuild'
re_obj=re.compile(pattern,re.IGNORECASE)
for line in ifh:
  for match in re_obj.findall(line):
    print "MATCHED->", match
