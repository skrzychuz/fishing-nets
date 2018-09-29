import json

import requests

url = 'https://api.myjson.com/bins/z3kww'
filename = 'data.json'

with open(filename) as f:
    data = json.load(f)

def put_json(data):
    headers = {'Content-Type': 'application/json'}
    req = requests.put(url, json=data, headers=headers)
    print("Put Status Code: ", req.status_code)
    res = req.text


def get_json():
    r = requests.get(url)
    print("Get Status Code:", r.status_code)
    return r.json()


# put_json(data)
#
# print(get_json())

