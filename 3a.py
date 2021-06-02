#!/usr/bin/env python
b = input("Input the string to convert:")
for x in range(len(b)):
  if x % 2 == 0:
    print(b[x].upper(),end=''),
  else:
    print(b[x],end=''),
print("\n")
