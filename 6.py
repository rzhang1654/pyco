#!/usr/bin/env python
import re

def main():
  filename = "t4.txt"
  file = open(filename, "r")
  for line in file:
     sppair = line.split()
     print re.search(sppair[0],sppair[1]).groups
  file.close()

if __name__ == '__main__':
  main()
