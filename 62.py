#!/usr/bin/env python
# working for RHEL for both python 2 and 3
import os
from distutils.log import warn as printf
import re

with os.popen('who','r') as f:
  for line in f:
    #() need to be escaped
    m = re.split('\040\040+|\011|\040\050|\051',line.rstrip())
    #by default pop out the last item or pos from 1 to n-1
    # to get the value of popped out x = m.pop()
    m.pop()
    printf(m)
# with with fclose is not needed
