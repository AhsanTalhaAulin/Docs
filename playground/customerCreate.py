from operator import index
import names
import random
import string
import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor


baseUrl = "https://training.harriswebworks.com/"
url = baseUrl+ "rest/all/V1/customers"

email_list = []

def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

def createCustomer(index):
    payload = json.dumps({
      "customer": {
        "email": random_char(7)+"@gmail.com",
        "firstname": names.get_first_name(),
        "lastname": names.get_last_name(),
        "addresses": [
          {
            "defaultShipping": True,
            "defaultBilling": True,
            "firstname": names.get_first_name(),
            "lastname": names.get_last_name(),
            # "addresses":[
            #     {
            #         "telephone": "01886296563"
            #     }
            # ]
          }
        ]
      },
      "password": "Password1"
    })
    headers = {
      'Content-Type': 'application/json'
    }
    time1 = time.time()
    response = requests.request("POST", url, headers=headers, data=payload)
    time2 = time.time()
    print(json.loads(response.text)["email"])
    print(time2-time1)
    email_list.append(json.loads(response.text)["email"])


count = 10
index = 1
start = time.time()
with ThreadPoolExecutor() as executor:
    executor.map(createCustomer, [index]*count, )
    executor.shutdown(wait=True)
end = time.time()


print(end - start)

# print(email_list)


# print(end - start)
# from random_address import real_random_address

# print(real_random_address())