#!/usr/bin/env python
import sys
import re

rx_sequence=re.compile(r"^(.+?)\n\n((?:[A-Z]+\n)+)")
rx_blanks=re.compile(r"\W+") # to remove blanks and newlines
text="""Some varying text1

AAABBBBBBCCCCCCDDDDDDD
EEEEEEEFFFFFFFFGGGGGGG
HHHHHHIIIIIJJJJJJJKKKK

Some varying text 2

LLLLLMMMMMMNNNNNNNOOOO
PPPPPPPQQQQQQRRRRRRSSS
TTTTTUUUUUVVVVVVWWWWWW
"""
for match in rx_sequence.finditer(text):
  title, sequence = match.groups()
  title = title.strip()
  sequence = rx_blanks.sub("",sequence)
  print "Title:",title
  print "Sequence:",sequence
  print
