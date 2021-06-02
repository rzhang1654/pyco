#!/usr/bin/env python
from time import ctime
from wsgiref.simple_server import make_server

def simple_wsgi_app(environ, start_response):
  status = '200 OK'
  headers = [('Content-type', 'text/plain')]
  start_response(status, headers)
  return ['Hello world!']


def ts_simple_wsgi_app(environ, start_response):
  return ('[%s] %s' % (ctime(), x) for x in simple_wsgi_app(environ, start_response))

httpd = make_server('', 8000, ts_simple_wsgi_app)
print "Started app serving on port 8000..."
httpd.serve_forever()
