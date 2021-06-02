#!/usr/bin/env python
import re
import sys

arrstr = ["abcY","abcN","1bcY","1bcN"]

myre = r'^(\w)?(\w)(\w)(?(1)Y|N)'
myre1 = r'^(\d)?(\w)(\w)(?(1)Y|N)'

for teststring in arrstr:
 m = re.search(myre,teststring)
 if m:
    print "%s matched %s in %s" % (myre,re.search(myre,teststring).group(1),teststring)
 else:
    print "%s does not match %s" % (myre,teststring)
for teststring in arrstr:
 m = re.search(myre1,teststring)
 if m:
    print "%s matched %s in %s" % (myre1,re.search(myre1,teststring).group(1),teststring)
 else:
    print "%s does not match %s" % (myre1,teststring)
