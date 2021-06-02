#!/usr/bin/env python
b = input("Input the string to convert:")
bbb = list(range(len(b)))
print(bbb)

print(''.join(list(map(lambda x: (x % 2 and b[x] or b[x].upper()), bbb))))
#print(''.join(list(map(lambda x: (x % 2 and b[x] or b[x].upper()), range(len(b))))))
