#!/usr/bin/env python
# 
import pymysql as MySQLdb

conn = MySQLdb.connect (host = "10.107.31.109",
                        user = "root",
                        passwd = "minus361",
                        db = "test")
cursor = conn.cursor ()
cursor.execute ("SELECT VERSION()")
row = cursor.fetchone ()
print "server version:", row[0]
cursor.close ()
conn.close ()
