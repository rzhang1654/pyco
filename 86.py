#!/usr/bin/env python
# SocketServer was remaned as socketserve in python 3
from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime
HOST = ''
#HOST = '10.107.33.76'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):
    def handle(self):
        self.data = self.rfile.readline().strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data
        #self.wfile.write(self.data.upper())
        self.wfile.write('[%s] %s' % (ctime(),self.data))

tcpServ = TCP(ADDR,MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()
