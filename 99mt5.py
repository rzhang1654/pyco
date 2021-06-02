#!/usr/bin/env python
# threading - passing class not function
from time import sleep, ctime
import threading

loops = (4,2)

class MyThread(threading.Thread):
  def __init__(self,func,args,name=''):
    threading.Thread.__init__(self)
    self.name = name
    self.func = func
    self.args = args

  def getResult(self):
    return self.res

  def run(self):
    print 'starting', self.name, 'at:', ctime()
    self.res = self.func(*self.args)
    print self.name, 'finished at:',ctime()
 
def loop(nloop,nsec):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()

def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))
   
    for i in nloops:  #creatre all threads
      t = MyThread(loop,(i,loops[i]),loop.__name__)
      threads.append(t)

    for i in nloops: #start all threads
      threads[i].start()

    for i in nloops: #wait for completion
      threads[i].join()

    print 'all Done at:', ctime()

if __name__ == '__main__':
  main()
