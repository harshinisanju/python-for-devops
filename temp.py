# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://technophileharsh.atlassian.net/rest/api/3/project"

API_TOKEN="ATATT3xFfGF0TrZvUQu9aKDlcNJOXqxHN8WFkRDoin3br0thnyQH77Z9rXFiTFE3vYnKCPzjNKWCdGFyg8vsBktZNfgZYJxAE1M1_-4Mz-VOjN75CCYJYeiZBRitAbA4RlSafcIp3VUWbsajIt5Vtj7ivXVYGxQFQ0LElXYW90QX7rnidUoM-90=9787D2E7"

auth = HTTPBasicAuth("technophileharsh@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)
