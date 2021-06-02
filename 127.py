#!/usr/bin/env python
#create db.table,insert,select and delete using cursor
import sqlite3
conn=sqlite3.connect('user.db')
print "Opened database successfully";

cur=conn.cursor()
cur.execute('CREATE TABLE users(login VARCHAR(8),userid INTEGER)')
cur.execute('INSERT INTO users VALUES("john", 100)')
cur.execute('INSERT INTO users VALUES("jane", 110)')
cur.execute('SELECT * FROM users')
for eachUser in cur.fetchall():
  print eachUser
cur.execute('DROP TABLE users')
cur.close()
conn.commit()
conn.close()
