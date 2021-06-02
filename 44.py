#!/usr/bin/env python
# re split
import re

print re.findall(r'th.+', '''
The first line
the second line
the third line
''')
print re.findall(r'(?s)th.+', '''
The first line
the second line
the third line
''')
