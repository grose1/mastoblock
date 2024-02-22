# Read version number from database and create a domain block on versions less than x.x.x

# WORK IN PROGRESS JUST IGNORE FOR NOW ;)

import requests
import json
import sqlite3
import re

# Connecting to sqlite
conn = sqlite3.connect('Sqlite3.db')

# Creating a cursor object using the
# cursor() method
cursor = conn.cursor()

ver = conn.execute('SELECT Version FROM Instances')
for row in ver:
    a = ver.fetchone()
    c = str(a)
    d = c[2:7]
    #e = float(d)
    print(d)
    if d != '4.2.0':
        print('yes')
conn.close()