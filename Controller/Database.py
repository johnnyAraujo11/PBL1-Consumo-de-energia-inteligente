import json


with open("./Controller/DB.json", encoding='utf-8') as r_json:
    registered = json.load(r_json)


def is_register(name):
    for regis in registered:
        if(name == regis['name']):
            print("cadastrado")
            return regis['name']
    
