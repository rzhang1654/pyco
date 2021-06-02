#!/usr/bin/env python
import sys
import re

infile=sys.argv[1]
data=open(infile,'r').read()
pattern1=r'<title>(.*)</title>'
pattern1_obj=re.compile(pattern1)
pattern2_obj=re.compile(pattern1,re.DOTALL|re.IGNORECASE)
if pattern2_obj.search(data):
  print pattern2_obj.search(data).group(1)
if pattern1_obj.search(data):
  print pattern1_obj.search(data).group(1)
