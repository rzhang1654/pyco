#!/usr/bin/env python
# urllib
import urllib
url_file = urllib.urlopen("https://docs.python.org/3/library/urllib.request.html")
urllib_docs = url_file.read()
url_file.close()
#print urllib_docs
print len(urllib_docs)

