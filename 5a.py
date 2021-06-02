#!/usr/bin/env python
import sys

if ((3,0) <= sys.version_info <= (3,9)):
  from urllib.parse import urlparse
elif ((2,0) <= sys.version_info <= (2,9)):
  from urlparse import urlparse

parseresult = urlparse('http://abc.com/client/cgi.cgi?runz#accinfo')
print (parseresult)
