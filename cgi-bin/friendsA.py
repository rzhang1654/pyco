#!/usr/bin/env python
import cgi
from urllib import unquote_plus
#from urllib import unquote
#import cgitb
#cgitb.enable()
#url = "%2B"
# Python 2
#url = unquote(url).decode('utf8')
#print url

reshtml = '''Content-Type: text/html\n
<HTML><HEAD><TITLE>
Friends CGI Demo (dynamic screen)
</TITLE></HEAD>
<BODY><H3>Friends list for: <I>%s</I></H3>
Your name is: <B>%s</B><P>
You have <B>%s</B> friends.
</BODY></HTML>'''

form = cgi.FieldStorage()
who = form['person'].value.replace(' ','+')
#who = str(form['person'].value.decode("utf-8"))

#print who
howmany = form['howmany'].value
print reshtml % (who, who, howmany)
