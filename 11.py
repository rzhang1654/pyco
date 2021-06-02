#!/usr/bin/env python
#match previous saved subgroup
import re
import sys

line = sys.argv[1]

filename = sys.argv[1]
file = open(filename, "r")
for line in file:

  entry_re = re.compile(r'''^(?P<street_num>\d+)
                              \s #seperator
                              (?P<street_name>\w+)
                              \s #seperator
                              (?P=street_name)
                              ''',re.VERBOSE)
  m = entry_re.match(line)

  if m:
   addrnum = m.groupdict()
   print addrnum

   for keys,values in addrnum.items():
    print "%s : %s" % (keys,values)
  else:
   print "%s does not match" % line

