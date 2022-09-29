import names
import random
import string
import requests
import json
import time

from concurrent.futures import ThreadPoolExecutor

url = 'https://httpbin.org/uuid'
res_list = []
count = 9

def fetch(session, url):
    with session.get(url) as response:
        res_list.append(response.json()['uuid'])

start = time.time()

with ThreadPoolExecutor() as executor:
    executor.map(fetch, [requests.Session()]*count, [url]*count )
    executor.shutdown(wait=True)


# for _ in range(10):
#     fetch(requests.Sessio n(), url)

end = time.time()



print(end - start)
# print(res_list)