import file
from datetime import datetime

def consumption(str_http):
    date = str_http.get_info_date()

    date_i = datetime.strptime(date[0], '%d/%m/%Y %H:%M')
    date_f = datetime.strptime(date[1], '%d/%m/%Y %H:%M')
    num_meas = get_num_measurer(str_http.get_user_name())

    if(date_i != None and date_f != None):
        data = file.read("./Controller/DB_consumption.json")
        data_obj = data.get(num_meas)
        total_consu = 0
        for i in range(len(data_obj)):
            transf_date = datetime.strptime(data_obj[i].get("date_hour"), '%d/%m/%Y %H:%M') 
            if(date_i < transf_date and date_f > transf_date):
                total_consu +=  data_obj[i].get("consumption")
        return str(total_consu)
    else: 
        print("não foi especificado um intevalo de datas")


def get_num_measurer(user_name):
    users = file.read("./Controller/DB.json")
   
    for i in range(len(users)):
        if(user_name == users[i].get("name")):
            return users[i].get("med")
            