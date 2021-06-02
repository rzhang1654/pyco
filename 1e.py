#!/usr/bin/env python
class Prefix:
  def __init__(self):
     self.public = 10
     self._private = 12

test = Prefix()
print(test.public)
print(test._private)
