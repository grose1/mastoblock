import requests
import json

# this gets a list of instances and software version from the fediverse.observer api 


url = "https://api.fediverse.observer/"

payload = json.dumps({
  "query": "{ nodes(softwarename: \"mastodon\") {domain shortversion}}"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

data = response.json()
with open('list.json', 'w') as f:
    json.dump(data, f)
