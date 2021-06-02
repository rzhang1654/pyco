#!/usr/bin/env python
#create db.table,insert,select and delete using cursor
from distutils.log import warn as printf
import mysql.connector
import mysql.connector.errors as DB_EXC
import os
from random import randrange as rand
