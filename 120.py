#!/usr/bin/env python
# 
import psycopg2

try:
   conn = psycopg2.connect(dbname='testdb',host='admin-omf-20v', user='exlirep', password='exlirep')
except:
    print "I am unable to connect to the database"

cur = conn.cursor()

cur.execute("""SELECT * from demo""")
rows = cur.fetchall()
print "\nShow me the demos:\n"

print rows
