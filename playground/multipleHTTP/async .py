# import asyncio
# import names
# import random
# import string
# import requests
# import json
# import time
# import aiohttp

# url = 'https://httpbin.org/uuid'
# count = 10
# res_list = []

# async def fetch(session, url):
#     async with session.get(url) as response:
#         json_response = await response.json()
#         res_list.append(json_response['uuid'])


# async def call():
#     for _ in range(count):
#         with aiohttp.ClientSession as session:
#             tasks = [fetch(session, url) for _ in range (count)]
#             await asyncio.gather(*tasks)

# start = time.time()
# asyncio.run(call())
# end = time.time()

# print(end - start)

# print(res_list)

import asyncio

async def main():
    print("asdf")
    task = asyncio.create_task(foo("text"))

    await task
    print("finish")

async def foo(text):
    print(text)
    await asyncio.sleep(1)
    await asyncio.sleep(1)
 
# print(main())
asyncio.run(main())