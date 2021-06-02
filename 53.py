#!/usr/bin/env python
# conditional re: xx yy is not allower, xy yx allowed
import re

print bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xy'))
print bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'yx'))
print bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xx'))
print bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'yy'))

print re.search(r'(?:(x)|y)(?(1)y|x)', 'xy').group()
print re.search(r'(?:(x)|y)(?(1)y|x)', 'xy').groups()
print re.search(r'(?:(x)|y)(?(1)y|x)', 'yx').group()
print re.search(r'(?:(x)|y)(?(1)y|x)', 'yx').groups()
print re.search(r'(?:(x)|y)(?(1)y|x)', 'xx').groups()
print re.search(r'(?:(x)|y)(?(1)y|x)', 'yy').groups()
