#!/usr/bin/env python
#negative look ahead - find email name, key:not consuming
import re

print re.findall(r'(?m)^\s*(?!noreply|postmaster)(\w+)',
'''
sales@phptr.com
postmaster@phptr.com
eng@phptr.com
noreply@phptr.com
admin@phptr.com
''')

