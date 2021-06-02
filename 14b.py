#!/usr/bin/env python
import re
import sys

arrstr = ["abcY","bcN","1bcY","bcN"]

myre = r'^(\w)?(\w)(\w)(?(1)Y|N)'
myre1 = r'^(\d)?(\w)(\w)(?(1)Y|N)'

for teststring in arrstr:
 m = re.search(myre,teststring)
 if m:
    print "%s matched %s" % (myre,teststring)
 else:
    print "%s does not match %s" % (myre,teststring)
for teststring in arrstr:
 m = re.search(myre1,teststring)
 if m:
    print "%s matched %s" % (myre1,teststring)
 else:
    print "%s does not match %s" % (myre1,teststring)
