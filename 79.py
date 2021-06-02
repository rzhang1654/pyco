#!/usr/bin/env python
# time stamp server for python 2 

from socket import *
from time import ctime
import sys

HOST = '::1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET6,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
  data = raw_input('> ' )
  if not data:
    break
  tcpCliSock.send(data)
  data = tcpCliSock.recv(BUFSIZ)
  if not data:
    break
  print data
tcpCliSock.close()
   
