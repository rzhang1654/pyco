#!/usr/bin/env python
# 
from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR = 'relay.exelonds.com'

who = 'run.zhang@exeloncorp.com'
body = '''\
From: %(who)s
To: %(who)s
Subject: test msg

Hello World!
''' % {'who' : who}
sendSvr = SMTP(SMTPSVR)
errs = sendSvr.sendmail(who,[who],body)
sendSvr.quit()
