#!/usr/bin/env python
# *kargs for variable number of keyword arguments 
def myFun(**kwargs):
  for key, value in kwargs.items():
     print ("%s  => %s" %(key, value))

myFun(first='geek',second='for',third='hipy')
