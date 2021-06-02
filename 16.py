#!/usr/bin/env python
import sys
import re

infile=sys.argv[1]
ifh=open(infile,'r')
pattern=r'bat|Bat|BAT'
re_obj=re.compile(pattern)
for line in ifh:
  match = re_obj.search(line)
  if match:
   print "MATCHED->",match
   print "MATCHED->",match.group()
ifh.seek(0)
for line in ifh:
  for match in re.findall(pattern,line):
    print "MATCHED->", match
