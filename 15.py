#!/usr/bin/env python
import sys

def validate(data):
  if 'username' in data and data['username'].startswith('_'):
    raise ValueError("Username must not begin with an underscore.")

if __name__ == '__main__':
  username = sys.argv[1]
  try:
    #only validate AttributeError in validate()
    validate({'username':username})
  except (TypeError,ValueError),e:
  # except TypeError,ValueError as e: in python 3
    print e
