#!/usr/bin/env python
#positive look ahead - only look for first name with last name of van Rossum
import re

print re.findall(r'\w+(?= van Rossum)',
'''
Tim Peters
Alex Martelli
Just van Rossum
Raymond Hettinger
Ellen van Rossum
''')
