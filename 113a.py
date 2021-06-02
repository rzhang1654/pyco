#!/usr/bin/env python
# 
import mysql.connector    
cnx = mysql.connector.Connect(**{'user':'root', 
                              'password':'minus361',
                              'host':'10.107.31.109',
                              'database':'test',})
print(cnx)
