#!/usr/bin/env python
import re
str_re = re.compile(r'^[a-zA-Z]+$')
while True:
  b = input("Input the string to convert:")
  if str_re.match(b):
    for x in range(len(b)):
      if x % 2 == 0:
        print(b[x].lower(),end='')
      else:
        print(b[x].upper(),end='')
    print("\n")
    break
