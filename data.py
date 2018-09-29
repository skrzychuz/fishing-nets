import json
import controller as api


# filename = 'data.json'
# with open(filename) as f:
#     json_data = json.load(f)
#     # Print the 2010 population for each country.
# # json_data[{}] = "jacek"
# # json_data[0]['srame'] = "jacek"
#
# json_data["scores"].append({
#     'name': 'dupa',
#     'score': 654,
#
# })


def add_score(name, score):
    # with open(api.get_json()) as f:
    json_data = api.get_json()
    json_data["scores"].append({
        'name': name,
        'score': score,
    })
    api.put_json(json_data)


# add_score("Cezary", 6565)

def get_score():
    return api.get_json()


def get_best_ten():
    print(sorted(get_score()["scores"], reverse=True, key=lambda x: x["score"]), )


get_best_ten()

# data["list"].append({'b':'2'})
#
#
# iter(json_data).next()['name'] = "marian"


# print(json_data)

# for item in json_data['scores']:
#     name = item['name']
#     score = item['score']
#     print(name + ": " + str(score))

# print(json.dumps(json_data['scores'], sort_keys=True, indent=4))

# print(json_data.sort(key='score', reverse=True))


# print(sorted(json_data["scores"], key=lambda x: x["score"]))
#
#
# d = {
#     1: 'Marian',
#     3: 'Bob',
#     2: 'Adam'
# }
#
#
# co_to = (sorted(d.items(), key=lambda x: x[0]))
