#!/usr/bin/env python
# positive and negative look behind assertion
import re
import sys

pattern = re.compile(r'(?<=John\s)McLane')
result = pattern.finditer("I would rather go out with John McLane than with John Smith or John Bon Jovi")
for i in result:
  print i.start(), i.end()
  print i.group()

pattern1 = re.compile(r'(?<=JOHN\s)McLane')
string1 = "I would rather go out with John McLane than with John Smith or John Bon Jovi"
if re.search(pattern1,string1):
       print "matched %s" % string1
else: 
       print "does not matched %s" % string1


pattern = re.compile(r'(?<!JOHN\s)McLane')
result = pattern.finditer("I would rather go out with John McLane than with John Smith or John Bon Jovi")
for i in result:
  print i.start(), i.end()
  print i.group()

pattern1 = re.compile(r'(?<!John\s)McLane')
if re.search(pattern1,string1):
       print "matched %s" % string1
else:
       print "does not matched %s" % string1

