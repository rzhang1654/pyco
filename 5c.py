#!/usr/bin/env python
from urlparse import urlparse

url = 'http://runzhang:mypin@www.gurlge.com:80/path/file.html;params?a=1#fragment'
o = urlparse(url)
print o.scheme
print o.netloc
print o.hostname
print o.port
print o.path
print o.params
print o.query
print o.fragment
print o.username
print o.password
