import json




def save_json(msg):
    with open("./Controller/DB.json", encoding='utf-8') as r_json:
        registered = json.load(r_json)