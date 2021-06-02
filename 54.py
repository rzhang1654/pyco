#!/usr/bin/env python
# matching \b in raw or not raw 
import re

m = re.match('\bblow','blow')
if m: print m.group()
m = re.match('\\bblow','blow')
if m: print m.group()
m = re.match(r'\bblow','blow')
if m: print m.group()
