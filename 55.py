#!/usr/bin/env python
#split who output by at least 2 spaces
import re
import subprocess

def run_who():
  p = subprocess.Popen("who",shell=True,stdout=subprocess.PIPE)
  return p.stdout

if __name__ == "__main__":
  f = run_who()
  for line in f:
    print re.split(r'\s\s+',line)
  f.close()  

