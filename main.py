import requests
import json
import sqlite3
# Connecting to sqlite
conn = sqlite3.connect('Sqlite3.db')

# Creating a cursor object using the
# cursor() method
cursor = conn.cursor()

url = "https://{your_instance_url}/api/v1/instance/peers"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()
with open('data.json', 'w') as f:
    json.dump(data, f)
with open('data.json') as data_file:
    data = json.load(data_file)
    for item in data:
        inst = "https://" + item + "/api/v2/instance"
        try:
            response2 = requests.request("GET", inst, headers=headers, data=payload)
            #print(response2.json())
            data2 = response2.json()
            domain = data2['domain']
            title = data2['title']
            version = data2['version']
            cursor.execute('INSERT INTO Instances (Domain, Title, Version) values (?, ?, ?)', (domain, title, version))
            conn.commit()
            print(domain, title, version)
        except:
            pass


