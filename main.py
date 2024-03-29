import requests
import json
import sqlite3
from configparser import ConfigParser



# Read env file
config_object = ConfigParser()
config_object.read(".env")
serverenv = config_object['SERVER']
server = serverenv['server_url']


# Connecting to sqlite
conn = sqlite3.connect('Sqlite3.db')

# Creating a cursor object using the
# cursor() method
cursor = conn.cursor()

url = "https://{}/api/v1/instance/peers".format(server)

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()
with open('data.json', 'w') as f:
    json.dump(data, f)
with open('data.json') as data_file:
    data = json.load(data_file)
    total_count = len(data)
    for count, item in enumerate(data, start=1):

        # already in database?
        res = conn.execute('SELECT domain FROM Instances WHERE domain="%s"' % (item))
        if res.fetchone():
            continue # already in system
        if 'activitypub-troll.cf' in item: # skipping activitypub-troll.cf from being included from lookup as its already blocked from my instance and takes up a large about of the json file
            continue

        print('[%d / %d] Looking up %s ...' % (count, total_count, item))
        inst = "https://" + item + "/api/v2/instance"
        try:
            response2 = requests.request("GET", inst, headers=headers, data=payload, timeout=10) # 10 sec
            #print(response2.json())
            data2 = response2.json()
            domain = data2['domain']
            title = data2['title']
            version = data2['version']
            version2 = version[:5] # removes trailing info after version number
            if 'compatible' in version: # Skips over Pleroma, Friendica and other software that responds to the Mastodon API
                continue
            if 'pixelfed' in domain: # Skips over Pixelfed responses in domain name
                continue
            if 'Pixelfed' in title: # Skips over Pixelfed responses in title
                continue
            else:
                cursor.execute('INSERT INTO Instances (Domain, Title, Version) values (?, ?, ?)', (domain, title, version2))
                conn.commit()
                print(domain, title, version2)
        except:
            pass
conn.close()


