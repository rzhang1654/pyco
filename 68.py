#!/usr/bin/env python
#difference between search and match, greedy and non-greedy 
import re
data  = 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'
patt = '\d+-\d+-\d+'
m = re.search(patt,data)
# group() - entire match, groups for subgroup
if m is not None:
  print m.group()
  print m.groups()
patt = '.+(\d+-\d+-\d+)'
m = re.match(patt,data)
# greey version
if m is not None:
  print m.group()
  print m.group(1)
  print m.groups()
#non-greedy, ? can not used with * + ?
patt = '.+?(\d+-\d+-\d+)'
m = re.match(patt,data)
# greey version
if m is not None:
  print m.group()
  print m.group(1)
  print m.groups()

# another way using split
print data.split('::')[-1]
