#!/usr/bin/env python
# time stamp server for python 2 

from socket import *
from time import ctime

# empty mean choose any aviabale IP address
#HOST = ''
HOST = '10.107.33.76'

PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
   print 'waiting for message...'
   data, addr = udpSerSock.recvfrom(BUFSIZ)
   udpSerSock.sendto('[%s] %s' % (ctime(),data), addr)
   print '...received from and returned to:', addr
udpSerSock.close()
