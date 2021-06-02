#!/usr/bin/env python
# character class
import re

m = re.match('\w{3}-\d{3}', 'abc-123')
if m is not None:
 print m.group()

m = re.match('(\w{3})-(\d{3})', 'abc-123')
if m is not None:
  print m.group() # entire match
  print m.group(1) # subgroup 1
  print m.group(2) # subgroup 2

m = re.match('ab', 'ab') # no subgroups
if m is not None:
 print m.group() # entire match
 print m.groups() # all subgroups, empty as not subgroup defined

m = re.match('(ab)', 'ab') # one subgroup
if m is not None:
  print m.group() # entire match
  print m.group(1) # subgroup 1
  print m.groups() # all subgroups, empty as not subgroup defined

m = re.match('(a)(b)', 'ab') # two subgroups
if m is not None:
  print m.group() # entire match
  print m.group(1) # subgroup 1
  print m.group(2) # subgroup 2
  print m.groups() # all subgroups, empty as not subgroup defined

m = re.match('(a(b))', 'ab') # two subgroups
if m is not None:
  print m.group() # entire match
  print m.group(1) # subgroup 1
  print m.group(2) # subgroup 2
  print m.groups() # all subgroups, empty as not subgroup defined

