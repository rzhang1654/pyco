#!/usr/bin/env python
# send one email with multiart and one with one image attchedment 
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
def make_img_msg(fn):
  f  = open(fn,'r')
  data = f.read()
  f.close()
  email = MIMEImage(data,name=fn)
  email.add_header('Content-Disposition', 'attachment: filename="%s"' % fn)
  return email

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
  msg = make_img_msg('songy.jpg')
  msg['From'] = SENDER
  msg['To'] = ', '.join(RECIPS)
  msg['Subject'] = 'image file test'
  sendMsg(SENDER,RECIPS,msg.as_string())
