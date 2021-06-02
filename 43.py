#!/usr/bin/env python
# re split
import re

print re.findall(r'(?i)yes', 'yes? Yes. YES!!')

print re.findall(r'(?i)th\w+', 'The quickest way is through this tunnel.')

#multline """ can not have space on the start of each line
print re.findall(r'(?im)(^th[\w ]+)', """
This line is the first,
another line,
that line, it's the best
""")
