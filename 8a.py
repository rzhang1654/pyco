#!/usr/bin/env python
#match previous saved subgroup
import re
import sys

p = re.compile(r'\b(\w+)\s+\1\s(\d+)\b')
print p.search('Paris in the the 123').group()
print p.search('Paris in the the 123').group(0)
print p.search('Paris in the the 123').group(1)
print p.search('Paris in the the 123').group(2)
print p.search('Paris in the the 123').groups()[0]
print p.search('Paris in the the 123').groups()[1]
print p.search('Paris in the the 123').groups()[2]


