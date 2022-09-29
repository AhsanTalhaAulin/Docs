import names
import random
import string
import requests
import json
import time

from multiprocessing.pool import Pool

url = 'https://httpbin.org/uuid'


def fetch(session, url):
    with session.get(url) as response:
        print(response.json())

start = time.time()

res_list = []
with Pool() as pool:
    pool.starmap(fetch, [(requests.Session(), url) for _ in range(10)] )


# for _ in range(10):
#     fetch(requests.Session(), url)

end = time.time()



print(end - start)

# print(type(res_list) )
# print(res_list)