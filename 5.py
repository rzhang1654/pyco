#!/usr/bin/env python
import re

def main():
  filename = "t3.txt"
  file = open(filename, "r")
  for line in file:
     sppair = line.split()
     print (re.match(sppair[0],sppair[1]).span())
     print (re.match(sppair[0],sppair[1]).group())
  file.close()

if __name__ == '__main__':
  main()
