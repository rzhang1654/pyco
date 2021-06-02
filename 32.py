#!/usr/bin/env python
# difference between match and search
import re

m = re.match('(?i)foo','seaFOOD')
if m is not None:
 print m.group()
m = re.search('(?i)foo','seaFOOD')
if m is not None:
 print m.group()
