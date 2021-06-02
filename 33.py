#!/usr/bin/env python
# ifference between match and search - ignorecase
import re

pattern=r'foo'
re_pattern=re.compile(pattern)

m = re_pattern.search('seafood',3,6)
if m is not None:
 print m.group()
m = re_pattern.search('seafood',3,5)
if m is not None:
 print m.group()
