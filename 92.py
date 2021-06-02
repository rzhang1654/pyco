#!/usr/bin/env python
# 
import ftplib
import os
import socket
usern = 'user0'
passw = 'user0'

HOST = 'linuxbuild-omf-20.exelonds.com'
DIRN = 'd1'
FILE = 'f1'

def main():
  try:
    f = ftplib.FTP(HOST)
  except (socket.error, socket.gaierror) as e:
    print 'ERROR: cannot reach "%s"' % HOST
    return
  print '*** Connected to host "%s"' % HOST

  try:
    f.login(usern,passw)
  except ftplib.error_perm:
    print 'ERROR: cannot login anonymously'
    f.quit()
    return
  print '*** LOgged in as "anonymous"'

  try:
    f.cwd(DIRN)
  except ftplib.error_perm:
    print 'ERROR: cannot CD to "%s"' % DIRN
    f.quit()
    return
  print '*** Changed to "%s" folder' % DIRN
  
  try:
    f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)
  except ftplib.error_perm:
    print 'ERROR: cannot read file "%s"' % FILE
    os.unlink(FILE)
  print  '*** Downloaded "%s" to CWD' % FILE

  f.quit()

if __name__ == '__main__':
  main()
