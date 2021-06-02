#!/usr/bin/env python
# 
from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib import urlopen as uopen
 
REGEX = compile(r'<script type="(.+?)">')
EXELON = 'https://www.exeloncorp.com/leadership-and-governance'
PAGEs = {
     'ethics-and-conduct': 'ethics and conduct',
     'executive-profiles': 'executive profiles',
     'governance-overview': 'governance overview',
}

def getScript(title):
  page = uopen('%s%s' % (EXELON,title))
  data = page.read()
  page.close()
  return REGEX.findall(data)[0]


def _showScript(title):
  print '- %s is %s' % (PAGEs[title], getScript(title))

def _main():
  print 'At', ctime(), 'on Exelon ...'
  for title in PAGEs:
     Thread(target=_showScript, args=(title,)).start()

@register
def _atexit():
  print 'all DONE at:', ctime()

if __name__ == '__main__':
  _main()
