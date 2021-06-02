#!/usr/bin/env python
# twisted server
from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
  # override with this when client connect
  def connectionMade(self):
    clnt = self.clnt = self.transport.getPeer().host
    print '...connected from: ', clnt
  # override this when client send data .. the protocol return thru it
  def dataReceived(self, data):
    self.transport.write('[%s] %s' % (ctime(), data))

factory = protocol.Factory()
factory.protocol =  TSServProtocol
print 'waiting for connection...'
reactor.listenTCP(PORT, factory)
reactor.run()
