#!/usr/bin/env python
import re
str_re = re.compile(r'[a-z]+')
while True:
 b = input("Input the string to convert:")
 if str_re.match(b):
  for x in b:
   if b.index(x) % 2 == 0:
    print(x.upper(),end='')
   else:
    print(x,end='')
  print("\n")
  break
