#!/usr/bin/env python
# time stamp server for python 2 

from socket import *
from time import ctime
import sys

#HOST = '127.0.0.1'
HOST = '10.107.33.76'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)

while True:
  data = raw_input('> ')
  if not data:
    break
  udpCliSock.sendto(data, ADDR)
  data, ADDR = udpCliSock.recvfrom(BUFSIZ)
  if not data:
    break
  print data
udpCliSock.close()
