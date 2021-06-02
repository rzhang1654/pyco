#!/usr/bin/env python
#remove \n \012, \t \011
import re
import os

f = os.popen('who','r')
for line in f:
    print re.split(r'\s\s+|\t',line.rstrip())
f.close()  
