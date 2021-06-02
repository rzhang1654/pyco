#!/usr/bin/env python
from time import ctime
from wsgiref.simple_server import make_server

def simple_wsgi_app(environ, start_response):
  status = '200 OK'
  headers = [('Content-type', 'text/plain')]
  start_response(status, headers)
  return ['Hello world!']

class Ts_ci_wrapp(object):
  def __init__(self, app):
    self.orig_app = app

  def __call__(self, *stuff):
    return ('[%s] %s' % (ctime(), x) for x in self.orig_app(*stuff))

httpd = make_server('', 8000, Ts_ci_wrapp(simple_wsgi_app))
print "Started app serving on port 8000..."
httpd.serve_forever()
