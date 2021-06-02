#!/usr/bin/env python
# send one email with multiart and one with two image attchedments and an html email body 
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

#multipart alternative: text and html
def make_mpa_msg():
  #both text and html part are attached, the email client will decide which to show
  email = MIMEMultipart('alternative')
  text = MIMEText('Hello World!\r\n', 'plain')
  email.attach(text)
  html = MIMEText(
         '<html><body><h4>Hello world!</h4>'
         '</body></html>', 'html')
  email.attach(html)
  return email

# multipart: images
def make_img_msg(fn,fn1):
  msgRoot = MIMEMultipart('mixed')
  f  = open(fn,'r')
  f1  = open(fn1,'r')
  data = f.read()
  data1 = f1.read()
  f.close()
  f1.close()
  
  html = MIMEText(
         '<html><body><h4>Hello world!</h4>'
         '</body></html>', 'html')

  msgImage1 = MIMEImage(data,name=fn)
  msgImage2 = MIMEImage(data1,name=fn1)
  msgImage1.add_header('Content-Disposition', 'attachment: filename="%s"' % fn)
  msgImage2.add_header('Content-Disposition', 'attachment: filename="%s"' % fn1)
  msgRoot.attach(html)
  msgRoot.attach(msgImage1)
  msgRoot.attach(msgImage2)
  return msgRoot

def sendMsg(fr,to,msg):
  s  = SMTP('relay.exelonds.com')
  errs = s.sendmail(fr,to,msg)
  s.quit()

if __name__ == "__main__":
  SENDER = 'run.zhang@exeloncorp.com'
  RECIPS = ['run.zhang@exeloncorp.com','rzhang725@yahoo.com']
  print 'Sending multipart alternative msg...'
  msg = make_mpa_msg()
  msg['From'] = SENDER
  msg['To'] = ', '.join(RECIPS)
  msg['subject'] = 'multipart alternative test'
  sendMsg(SENDER,RECIPS,msg.as_string()) 

  print 'Sending image msg...'
  msg = make_img_msg('songy.jpg','exbuild.jpg')
  msg['From'] = SENDER
  msg['To'] = ', '.join(RECIPS)
  msg['Subject'] = 'image file test'
  sendMsg(SENDER,RECIPS,msg.as_string())
