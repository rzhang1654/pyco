#!/usr/bin/env python
import re
import sys

def main():
  filename = sys.argv[1]
  file = open(filename, "r")
  for line in file:
     sppair = line.split()
     pattern1 = sppair.pop(0) 
     string1 = " ".join(sppair)
     if re.search(pattern1,string1):
       print "%s matched %s" % (pattern1,string1)
     else: 
       print "%s does not matched %s" % (pattern1,string1)
  file.close()

if __name__ == '__main__':
  main()

