#!/usr/bin/env python
# 
import pymysql as MySQLdb

conn = MySQLdb.connect (host = "10.107.31.109",
                        user = "webuser",
                        passwd = "lotus123",
                        db = "webapp")
cursor = conn.cursor ()
cursor.execute ('CREATE TABLE t4(login VARCHAR(8), userid INT)')
cursor.close ()
conn.close ()
