import names
import random
import string
import requests
import json
import time

url = 'https://httpbin.org/uuid'
count = 10
res_list = []

def fetch(session, url):
    with session.get(url) as response:
        res_list.append(response.json())

start = time.time()
for _ in range(count):
    fetch(requests.Session(), url)

end = time.time()

print(end - start)

print(res_list)