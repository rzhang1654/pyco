#!/usr/bin/env python
#match previous saved subgroup
import re
import sys

#match float point number
p = re.compile(r'\d+(\.\d*)?')
print "#### p1 ####"
p1=p.search('123.456')
print p1.group()
print p1.group(0)
print p1.group(1)
print p1.groups()
print "#### p2 ####"
p2=p.search('123')
print p2.group()
print p2.group(0)
print p2.group(1)
print p2.groups()
print "#### p3 ####"
p3=p.search('123.')
print p3.group()
print p3.group(0)
print p3.group(1)
print p3.groups()

#match people's name
p = re.compile(r'(Mr?s?\.)?([A-Z][a-z]*) ([A-Za-z-]+)')
print "#### p1 ####"
p1=p.search('Mr.Run Zhang')
print p1.group()
print p1.group(0)
print p1.group(1)
print p1.group(2)
print p1.group(3)
print p1.groups()

print "#### p2 ####"
p2=p.search('Mr. Run Zhang')
print p2.group()
print p2.group(0)
print p2.group(1)
print p2.group(2)
print p2.group(3)
print p2.groups()

print "#### p3 ####"
p3=p.search('run Zhang')
print p3.group()
print p3.group(0)
print p3.group(1)
print p3.group(2)
print p3.group(3)
print p3.groups()

