#!/usr/bin/env python
from socket import *
import sys

HOST = '10.107.33.76'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
  data = input('> ')
  if not data:
    break
  tcpCliSock.send(bytes(data.encode('utf-8')))
  data = tcpCliSock.recv(BUFSIZ)
  if not data:
    break
  #print(data.encode('utf-8'))
  print(data.decode('utf-8'))
  #print(data)
tcpCliSock.close()
