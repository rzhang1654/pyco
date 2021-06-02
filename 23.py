#!/usr/bin/env python
#match previous saved subgroup
import re
import sys

#match float point number
p = re.compile(r'\d+(\.\d*)?')
print p.search('123.456').group(1)
print p.search('123').group(1)
print p.search('123.').group(1)

#match people's name
p = re.compile(r'(Mr?s?\.)?([A-Z][a-z]*) ([A-Za-z-]+)')
print p.search('Mr.Run Zhang').group(1)
print p.search('Mr.Run Zhang').group(2)
print p.search('Mr.Run Zhang').group(3)
print p.search('Mr. Run Zhang').group(1)
print p.search('Mr. Run Zhang').group(2)
print p.search('Mr. Run Zhang').group(3)
print p.search('run Zhang').group(1)
print p.search('run Zhang').group(2)
print p.search('run Zhang').group(3)
print p.search('run Zha_ng').group(1)
print p.search('run Zha_ng').group(2)
print p.search('run Zha_ng').group(3)

