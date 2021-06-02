#!/usr/bin/env python
# 
import mysql.connector    
cnx = mysql.connector.connect(user='webuser', 
                              password='lotus123',
                              host='admin-omf-17v',
                              database='webapp',
                              port=3306)
try:
   cursor = cnx.cursor()
   cursor.execute("select * from t1")
   result = cursor.fetchall()
   print(result)
finally:
    cnx.close()
