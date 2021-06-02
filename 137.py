#!/usr/bin/env python
import urllib2
LOGIN = 'wesley'
PASSWD = 'wesley'
#URL = 'http://linuxbuild-omf-20.exelonds.com/restricted/license.html'
URL = 'http://linuxbuild-omf-20.exelonds.com'
REALM = 'Secure Archive'

def handler_version(url):
  from urlparse import urlparse
  hdlr = urllib2.HTTPBasicAuthHandler()
  o =  urlparse(url)
  #c = o.netloc + o.path
  c = o.netloc
  hdlr.add_password(REALM, c, LOGIN, PASSWD)
  opener = urllib2.build_opener(hdlr)
  urllib2.install_opener(opener)
  return url

def request_version(url):
  from base64 import encodestring
  req = urllib2.Request(url)
  b64str = encodestring('%s:%s' % (LOGIN, PASSWD))[:-1]
  print b64str
  req.add_header("Authorization", "Basic %s" % b64str)
  return req

for funcType in ('handler', 'request'):
  print '*** Using %s:' % funcType.upper()
  url = eval('%s_version' % funcType)(URL)
  print url
  f = urllib2.urlopen(url)
  print f.readline()
  f.close()
