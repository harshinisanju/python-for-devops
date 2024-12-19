# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:18:59 2024

@author: harsh
"""

# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://technophileharsh.atlassian.net/rest/api/3/issue"

API_TOKEN="ATATT3xFfGF0TrZvUQu9aKDlcNJOXqxHN8WFkRDoin3br0thnyQH77Z9rXFiTFE3vYnKCPzjNKWCdGFyg8vsBktZNfgZYJxAE1M1_-4Mz-VOjN75CCYJYeiZBRitAbA4RlSafcIp3VUWbsajIt5Vtj7ivXVYGxQFQ0LElXYW90QX7rnidUoM-90=9787D2E7"

auth = HTTPBasicAuth("technophileharsh@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "SCRUM"
    },
    "issuetype": {
      "id": "10003"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))