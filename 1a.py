#!/usr/bin/env python
import re
aa ={'sqlite': 'sqlite:///:memory:', 'mysql': 'mysql://root@10.107.31.109/test'}
if 'mysql' not in aa:
   print "not"
else:
  print "in"
