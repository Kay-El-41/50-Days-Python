import json


def save_json(adict: dict):
    with open('data.json', 'w') as file:
        json.dump(adict, file, indent=4)


def read_json():
    with open('data.json', 'r') as file2:
        data = json.load(file2)
    return data


names = {'name': 'Carol', 'sex': 'female', 'age': 55}
save_json(names)
print(read_json())
