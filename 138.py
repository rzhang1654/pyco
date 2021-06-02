#!/usr/bin/env python
import urllib.request, urllib.error, urllib.parse
LOGIN = 'wesley'
PASSWD = 'wesley'
#URL = 'http://linuxbuild-omf-20.exelonds.com/restricted/license.html'
URL = 'http://linuxbuild-omf-20.exelonds.com'
REALM = 'Secure Archive'

def handler_version(url):
  from urllib.parse import urlparse
  hdlr = urllib.request.HTTPBasicAuthHandler()
  o =  urlparse(url)
  #c = o.netloc + o.path
  c = o.netloc
  hdlr.add_password(REALM, c, LOGIN, PASSWD)
  opener = urllib.request.build_opener(hdlr)
  urllib.request.install_opener(opener)
  return url

def request_version(url):
  from base64 import encodestring
  req = urllib.request.Request(url)
  b64str = encodestring(bytes('%s:%s' % (LOGIN, PASSWD), 'utf-8'))[:-1]
  print(b64str)
  req.add_header("Authorization", "Basic %s" % b64str)
  return req

for funcType in ('handler', 'request'):
  print('*** Using %s:' % funcType.upper())
  url = eval('%s_version' % funcType)(URL)
  print(url)
  f = urllib.request.urlopen(url)
  print(f.readline())
  f.close()
