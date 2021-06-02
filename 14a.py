#!/usr/bin/env python
import re
import sys

arrstr = ["abcY","abcN","1bcY","1bcN"]

myre = '^(\w)(\w)(\w)(?(1)Y|N)'
myre1 = '^(\d)(\w)(\w)(?(1)Y|N)'

for teststring in arrstr:
 if re.search(myre1,teststring):
    print "%s matched %s in %s" % (myre1,re.search(myre1,teststring).group(1),teststring)
 else:
    print "%s does not match %s" % (myre1,teststring)
