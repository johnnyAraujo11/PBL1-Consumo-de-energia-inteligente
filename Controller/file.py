import json

def read(_path):

    with open(_path, encoding='utf-8') as r_json:
        data = json.load(r_json)
        return data
      
def write(data, _path):
    with open(_path, 'w') as json_file:
        json.dump(data, json_file, indent=5)
        print("escrevendo")


