#!/usr/bin/env python
COLSIZ = 10
FIELDS = ('login', 'userid', 'projid')
tformat = lambda s: str(s).title().ljust(COLSIZ)
cformat = lambda s: s.upper().ljust(COLSIZ)
print '\n%s' % ''.join(map(cformat, FIELDS))
print '\n%s' % ''.join(map(tformat, FIELDS))
