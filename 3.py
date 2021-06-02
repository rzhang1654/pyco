#!/usr/bin/env python
import re
import sys

def main():
  filename = sys.argv[1]
  file = open(filename, "r")
  for line in file:
     sppair = line.split()
     if re.search(sppair[0],sppair[1]):
       print "%s matched %s" % (sppair[0],sppair[1])
     else: 
       print "%s does not matched %s" % (sppair[0],sppair[1])
  file.close()

if __name__ == '__main__':
  main()

