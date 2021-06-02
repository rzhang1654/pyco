#!/usr/bin/env python
from HTMLParser import HTMLParser
from cStringIO import StringIO
from urllib2 import urlopen
from urlparse import urljoin

from BeautifulSoup import BeautifulSoup, SoupStrainer
from html5lib import parse, treebuilders
import html5lib

URLs = (
    'http://python.org',
    'http://google.com',
)

def output(x):
  print '\n'.join(sorted(set(x)))

def html5libparse(url, f):
  'html5libparse() - use html5lib to parse anchor tags'
  #output(urljoin(url, x.attributes['href']) \
  #for x in parse(f) if isinstance(x,treebuilders.simpletree.Element) and \
  #x.name == 'a')
  #for x in parse(f):
  #  print x,type(x)
  output(urljoin(url, x.attributes['href']) for x in parse(f,treebuilder="lxml") if isinstance(x,html5lib.Element) and x.name == 'a')

def process(url, data):
  print '\n*** HTML5lib'
  html5libparse(url, data)

def main():
  for url in URLs:
    f = urlopen(url)
    data = StringIO(f.read())
    f.close()
    process(url, data)

if __name__ == '__main__':
  main()
