#!/usr/bin/env python
from wsgiref.simple_server import make_server, demo_app
httpd = make_server('', 8000, demo_app)
print "Started app serving on port 8000..."
httpd.serve_forever()
