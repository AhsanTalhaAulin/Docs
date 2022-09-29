import requests


# payload = {
#     'username': 'test',
#     'password': 'test'
# }

# r =  requests.get('https://httpbin.org/basic-auth/test/test', auth=('test', 'test'), timeout=3)
response = requests.get('http://localhost:8069/customerSyncAPI')

# with open ('xkcd.png', 'wb') as f:
#     f.write(r.content)
#     print('Downloaded xkcd image')


# r_dict = r.json()


print(response.text)