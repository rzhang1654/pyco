#!/usr/bin/env python
import re

def main():
  filename = "t2.txt"
  file = open(filename, "r")
  for line in file:
     sppair = line.split()
     if re.search(sppair[0],sppair[1]):
       result1 = re.search(sppair[0],sppair[1])
       r1string = result1.group(0)
       r2string = result1.group(1)
       r3string = result1.groups()[0]
       print "%s matched %s" % (sppair[0],sppair[1])
       print "the subgroup 0 is: %s" % r1string
       print "the subgroup 1 is: %s" % r2string
       print "the subgroup 2 is: %s" % r3string
     else: 
       print "%s does not matched %s" % (sppair[0],sppair[1])
  file.close()

if __name__ == '__main__':
  main()
