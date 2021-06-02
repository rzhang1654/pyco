#!/usr/bin/env python
# 
import psycopg2
conn = psycopg2.connect(dbname='testdb',host='admin-omf-20v', user='exlirep', password='exlirep')
print conn
