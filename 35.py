#!/usr/bin/env python
# character class
import re


m = re.match('[cr][23][dp][o2]','c2d2')
if m is not None:
 print m.group()

m = re.match('[cr][23][dp][o2]','r3d2')
if m is not None:
 print m.group()

m = re.match('r2d2|r3do','r3d2')
if m is not None:
 print m.group()
