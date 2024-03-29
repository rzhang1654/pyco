#!/usr/bin/env python
# single vs multiple threads
from myThread import MyThread
from time import ctime,sleep

def fib(x):
  sleep(0.005)
  if x<2: return 1
  return (fib(x-2) + fib(x-1))

def fac(x):
  sleep(0.01)
  if x<2: return 1
  return (x * fib(x-1))

def sum(x):
  sleep(0.1)
  if x<2: return 1
  return (x + sum(x-1))

funcs = [fib,fac,sum]
n = 12

def main():
  nfuncs = range(len(funcs))
  print '*** SINGLE THREAD'
  for i in nfuncs:
    print 'starting',funcs[i].__name__,'at:',ctime()
    print funcs[i](n)
    print funcs[i].__name__,'finished at:',ctime()
 
  print '*** MULTIPLE THREADS'
  threads = []
  for i in nfuncs:
    t = MyThread(funcs[i],(n,),funcs[i].__name__)
    threads.append(t)

  for i  in nfuncs:
    threads[i].start()

  for i in nfuncs:
     threads[i].join()
     print threads[i].getResult()

  print 'all DONE'

if __name__ == '__main__':
  main()
