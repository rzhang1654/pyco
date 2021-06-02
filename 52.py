#!/usr/bin/env python
#negative look ahead - finditer is more efficient than findall
import re

print ['%s@aw.com' % e.group(1) for e in \
re.finditer(r'(?m)^\s*(?!noreply|postmaster)(\w+)',
'''
sales@phptr.com
postmaster@phptr.com
eng@phptr.com
noreply@phptr.com
admin@phptr.com
''')]
