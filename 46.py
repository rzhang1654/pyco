#!/usr/bin/env python
#
import re
import sys

print re.findall(r'http://(?:\w+\.)*(\w+\.com)',
'http://google.com http://www.google.com http://code.google.com')

print re.findall(r'http://(?:\w+\.)*(\w+\.com)',
'http://go_ogle.com http://www.google.com http://code.google.com')

#\w does not inlcude dash
print re.findall(r'http://(?:\w+\.)*(\w+\.com)',
'http://gox-ogle.com http://www.google.com http://code.google.com')

print re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})',
'(800) 555-1212').groupdict()




