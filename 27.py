#!/usr/bin/env python
import sys
import re

infile=sys.argv[1]
data=open(infile,'r').read()
pattern1=r'<title>((?s)[a-z\s]*)</title>'
pattern2=r'<title>((?is)[a-z\s]*)</title>'
if re.search(pattern1,data):
  print re.search(pattern1,data).group(1)
if re.search(pattern2,data):
  print re.search(pattern2,data).group(1)
