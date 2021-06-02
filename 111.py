#!/usr/bin/env python
# 
from concurrent.futures import ThreadPoolExecutor
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
  #with uopen('{0}{1}'.format(EXELON,title)) as page:
  #  return str(REGEX.findall(page.read())[0], 'utf-8')

def _main():
  print 'At', ctime(), 'on Exelon ...'
  with ThreadPoolExecutor(3) as executor:
    for page,script in zip(PAGEs, executor.map(getScript,PAGEs)):
      print('- %s is %s' % (PAGEs[page],script))
  print('all DONE at:', ctime())

if __name__ == '__main__':
  _main()
