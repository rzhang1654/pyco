#!/usr/bin/env python
#universal version works for both python 2 and 3
import re
import os
from distutils.log import warn as printf

with os.popen('who','r') as f:
  for line in f:
    printf(re.split(r'\s\s+|\t',line.rstrip()))
# with with fclose is not needed
