#!/usr/bin/env python
#match previous saved subgroup
import re
import sys

line = "13627 Corello"

entry_re = re.compile(r'''^(?P<street_num>\d+)
                              \s #seperator
                              (?P<street_name>\w+)
                              ''',re.VERBOSE)
m = entry_re.match(line)

if m:
   addrnum = m.groupdict()
   print addrnum

   for keys,values in addrnum.items():
    print "%s : %s" % (keys,values)

