#!/usr/bin/env python
import re
re_string = "{{(.*?)}}"
some_string = "this is a string with {{words}} embedded in\
{{curly brackets}} to show an {{example}} of {{regular expressions}}"
for match in re.findall(re_string,some_string):
 print "MATCH->",match
re_string = "{{(.*)}}"
for match in re.findall(re_string,some_string):
 print "MATCH->",match
re_string = "{{(.*?)}}"
some_string = "this is a string with {{}} embedded in\
{{curly brackets}} to show an {{example}} of {{regular expressions}}"
for match in re.findall(re_string,some_string):
 print "MATCH->",match
