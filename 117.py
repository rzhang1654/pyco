#!/usr/bin/env python
# 
import pymysql as MySQLdb

conn = MySQLdb.connect (host = "10.107.31.109",
                        user = "webuser",
                        passwd = "lotus123",
                        db = "webapp")
cursor = conn.cursor ()

cursor.execute("DELETE FROM t4 WHERE login='bob'")

cursor.execute("DROP TABLE t4")

cursor.close ()
conn.close ()
