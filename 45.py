#!/usr/bin/env python
# re verbose
import re

#search anywhere in the string and end when it find it
print re.search(r'''(?x)
\((\d{3})\)  #area code
[ ] # space
(\d{3}) # prefix
- # dash
(\d{4}) # endpoint number
''', '(800) 555-1212 (247) 234-9090').group()

