import requests
import json

url = "http://testmage.hww/rest/all/V1/customers"

payload = json.dumps({
  "customer": {
    "email": "a.4sdfg4shoque@harriswebworks.com",
    "firstname": "Jane",
    "lastname": "Doe"
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJraWQiOiIxIiwiYWxnIjoiSFMyNTYifQ.eyJ1aWQiOjIsInV0eXBpZCI6MiwiaWF0IjoxNjU4NzM5OTc3LCJleHAiOjE2NTg3NDM1Nzd9.oLVxTgVKDJLY3gOQFW2Dpc-8EnykF7v6YXj8nrzI91c',
  'Cookie': 'PHPSESSID=m8olu9qhrpvjb17sjd4lvq7vtc; mage-messages=%5B%7B%22type%22%3A%22error%22%2C%22text%22%3A%22Invalid%20Form%20Key.%20Please%20refresh%20the%20page.%22%7D%2C%7B%22type%22%3A%22error%22%2C%22text%22%3A%22Invalid%20Form%20Key.%20Please%20refresh%20the%20page.%22%7D%2C%7B%22type%22%3A%22error%22%2C%22text%22%3A%22Invalid%20Form%20Key.%20Please%20refresh%20the%20page.%22%7D%2C%7B%22type%22%3A%22error%22%2C%22text%22%3A%22Invalid%20Form%20Key.%20Please%20refresh%20the%20page.%22%7D%2C%7B%22type%22%3A%22error%22%2C%22text%22%3A%22Invalid%20Form%20Key.%20Please%20refresh%20the%20page.%22%7D%2C%7B%22type%22%3A%22error%22%2C%22text%22%3A%22Invalid%20Form%20Key.%20Please%20refresh%20the%20page.%22%7D%2C%7B%22type%22%3A%22error%22%2C%22text%22%3A%22Invalid%20Form%20Key.%20Please%20refresh%20the%20page.%22%7D%5D; private_content_version=86e0db9b12a1ef18d5989c132e1a4100'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
