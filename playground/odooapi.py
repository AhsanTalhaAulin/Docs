import requests
import json

url = "http://localhost:8069/hello_api/"

payload = json.dumps({
  "params": {
    "fname": "ahsan",
    "lname": "hoque",
    "email": "asd@ads.asdf"

  }
})
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'session_id=87fc8293f9823519fd216d51f3043778645b9811'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
