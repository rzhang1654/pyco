#!/usr/bin/env python
# 
from atexit import register
from random import randrange
from re import compile
from threading import Thread, currentThread, Lock
from time import sleep, ctime
 
lock = Lock()

class CleanOutputSet(set):
  def __str__(self):
    return ', '.join(x for x in self)

loops = (randrange(2,5) for x in xrange(randrange(3,7)))
remaining = CleanOutputSet()

def loop(nsec):
  myname = currentThread().name
  lock.acquire()
  remaining.add(myname)
  print '[%s] started %s' % (ctime(),myname)
  #print '[{0}] started {1}'.format(ctime(),myname) # 2.6+
  #print('[{0}] started {1}'.format(ctime(),myname)) # 3+
  lock.release()
  sleep(nsec)
  lock.acquire()
  remaining.remove(myname)
  print '[%s] completed %s (%d secs)' % (ctime(),myname,nsec)
  print '       (remaining: %s)' % (remaining or 'NONE')
  lock.release()

def _main():
  for pause in loops:
    Thread(target=loop, args=(pause,)).start()

@register
def _atexit():
  print 'all DONE at:', ctime()

if __name__ == '__main__':
  _main()