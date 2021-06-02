#!/usr/bin/env python
b = input("Input the string to convert:")
print(''.join(list(map(lambda x: (x % 2 and b[x] or b[x].upper()), range(len(b))))))
print(range(6))
