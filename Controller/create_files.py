import json
import file
import os

def create_files(data, name_file):
    _path = "./Database/{}.json".format(name_file)
    if not os.path.exists(_path):        
        with open(_path, "w") as arquivo:    
            json.dump(data, arquivo, indent=4)
    

data = {}
create_files(data,"DB_consumption")
data = []
create_files(data,"DB_users")