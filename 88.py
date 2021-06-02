#!/usr/bin/env python
# twisted server
from twisted.internet import protocol, reactor

PORT = 21567
HOST = 'localhost'

class TSClntProtocol(protocol.Protocol):
  # this our own method
  def sendData(self):
    data = raw_input('> ')
    if data:
      print '...sending %s...' % data
      self.transport.write(data)
    else:
      self.transport.loseConnection()
  #over ride the default
  def connectionMade(self):
    self.sendData()
  #over ride the default
  def dataReceived(self, data):
    print data
    self.sendData()

class TSClntFactory(protocol.ClientFactory):
  protocol = TSClntProtocol
  clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()
