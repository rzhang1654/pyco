#!/usr/bin/env python
# time stamp server for python 3

from socket import *
from time import ctime

# empty mean choose any aviabale IP address
#HOST = ''
HOST = '10.107.33.76'

PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
# 5 connections until turn customer away
tcpSerSock.listen(5)

while True:
  print('waiting for connection...')
  tcpCliSock, addr = tcpSerSock.accept()
  print('...connected from:', addr)

  while True:
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
       break
    #socket sent in python 3 have to be bytes instead of str
    tcpCliSock.send('[%s] %s' % (bytes(ctime().encode('utf-8')),data))
  tcpCliSock,close()
tcpSerSock.close()   
