#!/usr/bin/env python

bb=[0,1,2,3,4]
b=['a','b','c','d','e']

print(''.join(list(map(lambda x: (x % 2 and b[x] or b[x].upper()), bb))))
#print(''.join(list(map(lambda x: (x % 2 and b[x] or b[x].upper()), range(len(b))))))
