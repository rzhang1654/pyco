#!/usr/bin/env python
from wsgiref.simple_server import make_server

def simple_wsgi_app(environ, start_response):
  status = '200 OK'
  headers = [('Content-type', 'text/plain')]
  start_response(status, headers)
  return ['Hello world!']

def main():
  httpd = make_server('', 8000, simple_wsgi_app)
  print "Started app serving on port 8000..."
  httpd.serve_forever()

if __name__ == "__main__":
  main()
