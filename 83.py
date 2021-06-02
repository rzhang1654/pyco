#!/usr/bin/env python
# match US street name
import re
import sys

filename = sys.argv[1]
file = open(filename, "r")
us_street_re = re.compile(r'''(?P<street_num>\d+)
                              (?P<street_name>((\s+[-a-zA-Z0-9_]+)+))
                           ''',re.VERBOSE)
for line in file:
 m = us_street_re.match(line)

 if m:
   mdict = m.groupdict()
   print mdict

   for keys,values in mdict.items():
     print "%s  %s" % (keys,values)
 else:
  print "%s does not match" % line
