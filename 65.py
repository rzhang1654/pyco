#!/usr/bin/env python
import re
data  = 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8 Mon Mar 21 11:43:59 2000::wewew@exelonds.com::12345678-9-0'
patt = '^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'
m = re.match(patt,data)
if m:
  print "#### match ####"
  print m.group()
  print m.group(1)
  print m.groups() 
m = re.search(patt,data)
if m:
  print "#### search ###"
  print m.group()
  print m.group(1)
  print m.groups() 
m = re.findall(patt,data)
if m:
  print "#### findall ####"
  print m
m = re.finditer(patt,data)
for im in m:
  print "#### finditer ####"
  print im.group()
  print im.group(1)
  print im.groups()
