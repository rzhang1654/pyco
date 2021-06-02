#!/usr/bin/env python
import SimpleXMLRPCServer
import csv
import operator
import time

server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", 8888))
server.register_introspection_functions()

FUNCs = ('add', 'sub', 'mul', 'div', 'mod')
for f in FUNCs:
  server.register_function(getattr(operator, f))
  server.register_function(pow)

class SpecialServices(object):
  def now_int(self):
    return time.time()

  def now_str(self):
    return time.ctime()

  def timestamp(self, s):
    return '[%s] %s' % (time.ctime(), s)

server.register_instance(SpecialServices())

try:
  print 'Welcome to PotpourriServ v0.1\n(Use ^C to exit)'
  server.serve_forever()
except KeyboardInterrupt:
  print 'Exiting'
