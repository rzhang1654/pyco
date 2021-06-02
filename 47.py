#!/usr/bin/env python
#using saved match group using number or name
import re
import sys

#there must be a an r for using \n
print re.sub(r'\((\d{3})\) (\d{3})-(?:\d{4})',
r'(\1) \2-xxxx','(800) 555-1212')

print re.sub(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})',
'(\g<areacode>) \g<prefix>-xxxx', '(800) 555-1212')
