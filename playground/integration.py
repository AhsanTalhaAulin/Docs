import requests

url = "http://testmage.hww/rest/V1/products/types"

payload={}
headers = {
  'Authorization': 'Bearer u7q6luz2dueccyq40slvlxe2tqkicwau',
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response)
