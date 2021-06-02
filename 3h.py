#!/usr/bin/env python
import re
str_re = re.compile(r'^[a-zA-Z]+$')
while True:
  b = input("Input the string to convert:")
  if str_re.match(b):
    print(''.join(list(map(lambda x: (x % 2 and b[x].upper() or b[x].lower()), range(len(b))))))
    break
