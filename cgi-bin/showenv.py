#!/bin/env python
import os

print "Content-type: text/html\r\n\r\n";
#print "<font size=+1>Environment</font><br><br>";
print "<H2>Environment</H2><br><br>";
for param in os.environ.keys():
   print "<b>%20s</b>: %s<br>" % (param, os.environ[param])
