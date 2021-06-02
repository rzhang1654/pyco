#!/usr/bin/env python
#Recognize the following strings: bat,bit,but,hat,hit or hut.
import re
string='I love bit but I can not stand hat, so I decied to bat the hut with a hit'
pattern=r'\b([bh][aiu]t)\b'
pattern_obj = re.compile(pattern)
for item in pattern_obj.finditer(string):
  print item.group()
