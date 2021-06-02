#!/usr/bin/env python
# 
import pymysql as MySQLdb

conn = MySQLdb.connect (host = "10.107.31.109",
                        user = "webuser",
                        passwd = "lotus123",
                        db = "webapp")
cursor = conn.cursor ()

cursor.execute("INSERT INTO t4 VALUES('john', 7000)")
cursor.execute("INSERT INTO t4 VALUES('Jay', 7001)")
cursor.execute("INSERT INTO t4 VALUES('Bob', 7002)")

cursor.execute("SELECT * FROM t4 WHERE login LIKE 'j%'")
for data in cursor.fetchall():
  print '%s\t%s' % data

cursor.close ()
conn.close ()
