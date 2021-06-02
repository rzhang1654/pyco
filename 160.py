#!/usr/bin/env python
from math import pi
import xmlrpclib

server = xmlrpclib.ServerProxy('http://localhost:8888')
print 'Current time in seconds after epoch:', server.now_int()
print 'Current time as a string:', server.now_str()
print 'Area of circle of radius 5:', server.mul(pi, server.pow(5, 2))
