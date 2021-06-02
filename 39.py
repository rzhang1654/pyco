#!/usr/bin/env python
# findall finditer
import re

print re.findall('car','car')
print re.findall('car','scary')
print re.findall('car','carry the barcardi to the car')

s = 'This and that.'
print re.findall(r'(th\w+) and (th\w+)',s,re.I)
print re.findall(r'(th\w+) and (th\w+)',s,re.I)[0]
print re.findall(r'(th\w+) and (th\w+)',s,re.I)[0][0]
print re.findall(r'(th\w+) and (th\w+)',s,re.I)[0][1]

print re.finditer(r'(th\w+) and (th\w+)',s,re.I).next().groups()
print re.finditer(r'(th\w+) and (th\w+)',s,re.I).next().group()
print re.finditer(r'(th\w+) and (th\w+)',s,re.I).next().group(1)
print re.finditer(r'(th\w+) and (th\w+)',s,re.I).next().group(2)

print [g.groups() for g in re.finditer(r'(th\w+) and (th\w+)',s,re.I)]
