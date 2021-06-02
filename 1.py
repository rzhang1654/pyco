#!/usr/bin/env python
import re

def main():
  filename = "t1.txt"
  file = open(filename, "r")
  pattern = "9[0-9]%"
  outline = (line.split() for line in file)
  print outline
  #      flag = (" ".join(row) for row in outline if re.search(pattern,row[-1]))
  #      for line in flag: print "%s CRITICAL" % line
  for line in outline: 
    print  line

if __name__ == '__main__':
  main()
