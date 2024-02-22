# Read version number from database and create a domain block on versions less than x.x.x

# WORK IN PROGRESS JUST IGNORE FOR NOW ;)

import requests
import json
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('Sqlite3.db')

# Creating a cursor object using the
# cursor() method
cursor = conn.cursor()

ver = conn.execute('SELECT Version FROM Instances')
for row in ver:
    a = ver.fetchone()
    st = a[0]
    print(st)
    num = float((st[:-2]))
    print(num)
    if num < 4.2:
        dn = conn.execute('SELECT Domain FROM Instances Where Version="%s" ' % (st))
        d = dn.fetchone()
        dm = d[0]
        print(d[0])
        url = "https://{'instance url'}/api/v1/admin/domain_blocks"
        payload = json.dumps({
        "domain": dm
        })
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        

conn.close()