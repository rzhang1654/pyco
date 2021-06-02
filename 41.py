#!/usr/bin/env python
# \n as replacement of group
import re

print re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})',r'\2/\1/\3','2/20/91')
print re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})',r'\2/\1/\3','2/20/1991')

