#!/usr/bin/env python
# python 2 and 3 compatible
import csv
from distutils.log import warn as printf

u = open ('stock.txt', 'r')
reader = csv.reader(u)
for tick,price,chg,pct in reader:
  print tick.ljust(7),('%.2f' % round(float(price),2)).rjust(6), \
    chg.rjust(6), pct.rstrip().rjust(6)
u.close()

