import json


def loading_json_file(file_name):
    with open(file_name, 'r') as json_file:
        json_data = json.load(json_file)
    return json_data


products = loading_json_file('products.json')['products']


