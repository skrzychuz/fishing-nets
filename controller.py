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


def get_json():
    r = requests.get(url)
    print("Get Status Code:", r.status_code)
    return r.json()

def add_score(name, score):
    json_data = get_json()
    json_data["scores"].append({
        'name': name,
        'score': score,
    })
    put_json(json_data)


def get_sorted_scores():
    return (sorted(get_json()["scores"], reverse=True, key=lambda x: x["score"]))
