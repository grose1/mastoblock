# Read version number from database and create a domain block on versions less than x.x.x 
# Then saves the id number returned for the domain block from the mastodon server to the database
# This is currently set to block any instance with a version number less than 4.2

# WORK IN PROGRESS JUST IGNORE FOR NOW ;)

import requests
import json
import sqlite3
from configparser import ConfigParser



# Read env file
config_object = ConfigParser()
config_object.read(".env")
serverenv = config_object['SERVER']
server = serverenv['server_url']
token = serverenv['api_token']

bearer = 'Bearer ' + token


# Connecting to sqlite
conn = sqlite3.connect('Sqlite3.db')

# Creating a cursor object using the
# cursor() method
cursor = conn.cursor()

ver = conn.execute('SELECT Version FROM Instances')
for row in ver:
    a = ver.fetchone()
    st = a[0]
    #print(st)
    num = float((st[:-2]))
    #print(num)
    if num < 4.2:
        dn = conn.execute('SELECT Domain FROM Instances Where Version="%s" ' % (st))
        d = dn.fetchone()
        dm = d[0]
        #print(d[0])
        url = "https://{}/api/v1/admin/domain_blocks".format(server)
        payload = json.dumps({
        "domain": dm ,
        "severity": "suspend" ,
        "public_comment": "Software out of Date" ,
        "reject_media": 'true' ,
        "reject_reports": 'true' ,
        "obfuscate": 'true' 
        })
        headers = {
        'Content-Type': 'application/json',
        'Authorization': bearer
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        data = response.json()
        bl_id = data['id']
        print(bl_id)
        cursor.execute('UPDATE Instances set BL_ID = ? where Domain= ? ', (bl_id, dm))
        conn.commit()
        
        

conn.close()