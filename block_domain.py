import requests
import json

url = "https://{'your_instance'}/api/v1/admin/domain_blocks"

payload = json.dumps({
  "domain": "test.social"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer '
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)