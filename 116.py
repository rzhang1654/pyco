#!/usr/bin/env python
# 
import pymysql as MySQLdb

conn = MySQLdb.connect (host = "10.107.31.109",
                        user = "webuser",
                        passwd = "lotus123",
                        db = "webapp")
cursor = conn.cursor ()

cursor.execute("UPDATE t4 SET userid=7100 WHERE userid=7001")

cursor.execute("SELECT * FROM t4")
for data in cursor.fetchall():
  print '%s\t%s' % data

cursor.close ()
conn.close ()
