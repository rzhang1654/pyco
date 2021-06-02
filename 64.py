#!/usr/bin/env python
from sys import maxint
from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxint
from time import ctime
tlds = ('com','edu','net','org','gov')
# (5,11) generate 5 to 10
for i in xrange(randrange(5,11)):
  #maxint does not work
  #dtint = randrange(maxint)  # pick date
  dtint = randrange(32768)  # pick date
  dtstr = ctime(dtint)  # date string
  #between 4 to 7
  llen = randrange(4,8) # login is shorter
  login = ''.join(choice(lc) for j in range(llen))
  dlen = randrange(llen,13) # domain is longer
  dom = ''.join(choice(lc) for j in range(dlen))
  print '%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen)
