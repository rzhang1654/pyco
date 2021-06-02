#!/usr/bin/env python
# send one email with multiart and one with two image attchedments and one pdf ans one ppt and an html email body 
from email.mime.image import MIMEImage
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
from smtplib import SMTP
from email import encoders

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
def make_img_msg(fn,fn1,fn2,fn3):
  msgRoot = MIMEMultipart('mixed')
  f  = open(fn,'rb')
  f1  = open(fn1,'rb')
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

  ctype,encoding = mimetypes.guess_type(fn2)
  maintype,subtype = ctype.split('/',1)
  fp = open(fn2,'rb')
  msg = MIMEBase(maintype,subtype)
  msg.set_payload(fp.read())
  fp.close()
  encoders.encode_base64(msg)
  msg.add_header('Content-Disposition','attachment: filename="%s"' % fn2)
  msgRoot.attach(msg)

  ctype1,encoding1 = mimetypes.guess_type(fn3)
  maintype1,subtype1 = ctype1.split('/',1)
  fp1 = open(fn3,'rb')
  msg1 = MIMEBase(maintype1,subtype1)
  msg1.set_payload(fp1.read())
  fp1.close()
  encoders.encode_base64(msg1)
  msg1.add_header('Content-Disposition','attachment: filename="%s"' % fn3)
  msgRoot.attach(msg1)

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
  msg = make_img_msg('exbuild.jpg','songy.jpg','1.pdf','2.pptx')
  msg['From'] = SENDER
  msg['To'] = ', '.join(RECIPS)
  msg['Subject'] = 'image file test'
  sendMsg(SENDER,RECIPS,msg.as_string())
