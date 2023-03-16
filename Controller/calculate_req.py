import file
import random
from datetime import datetime

def consumption(str_http):
    date = str_http.get_info_date()

    
    date_i = datetime.strptime(date[0], '%d/%m/%Y %H:%M')
    date_f = datetime.strptime(date[1], '%d/%m/%Y %H:%M')
    num_meas = get_num_measurer(str_http.get_user_name())
    data = file.read("./Database/DB_consumption.json")

    if(len(data) != 0):
        data_obj = data.get(num_meas)
        total_consu = 0
        for i in range(len(data_obj)):
            transf_date = datetime.strptime(data_obj[i].get("date_hour"), '%d/%m/%Y %H:%M') 
            if(date_i < transf_date and date_f > transf_date):
                total_consu +=  data_obj[i].get("consumption")
        return str(total_consu)
    



def get_num_measurer(user_name):
    users = file.read("./Database/DB_users.json")
   
    for i in range(len(users)):
        if(user_name == users[i].get("name")):
            return users[i].get("med")


def register_client(_name, _password):
    data = file.read("./Database/DB_users.json")
    num_med = create_id_measurer()
    user = {'name':_name, "password":_password, "med":num_med}
    data.append(user)
    file.write(data, "./Database/DB_users.json")


def create_id_measurer():
    data = file.read("./Database/DB_consumption.json")
    num = str(random.randrange(0,10000))

    while(num in data):
        num = str(random.randrange(0,10000))
    add_measurer(num)
    return num


def add_measurer(num):
   data = file.read("./Database/DB_consumption.json") 
   data[num] = []
   file.write(data, "./Database/DB_consumption.json")
   