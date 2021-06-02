#!/usr/bin/env python
# sub ans subn
import re

print re.sub('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')
print re.subn('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')
print re.subn('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')[0]
print re.sub('[ae]', 'X', 'abcdef')
print re.subn('[ae]', 'X', 'abcdef')
print re.subn('[ae]', 'X', 'abcdef')[0]
