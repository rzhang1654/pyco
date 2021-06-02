#!/usr/bin/env python
# ifference between match and search - ignorecase
import re

pattern=r'foo'
re_pattern=re.compile(pattern,re.IGNORECASE)

m = re_pattern.match('seaFood')
if m is not None:
 print m.group()
m = re_pattern.search('seaFood')
if m is not None:
 print m.group()
