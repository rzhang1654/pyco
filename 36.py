#!/usr/bin/env python
# character class
import re

pattern = '\w+@(\w+\.)?\w+.com'

m = re.match(pattern,'nobody@exeloncorp.com')
if m is not None:
 print m.group()

pattern = '\w+@(\w+\.)*\w+.com'

m = re.match(pattern,'nobody@unix.exeloncorp.com')
if m is not None:
 print m.group()

