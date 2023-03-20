import file
import random
from datetime import datetime, timedelta
import variables as var


PRICE_PER_KWH = 0.35

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
    users = file.read(var.PATH_USERS)
   
    for i in range(len(users)):
        if(user_name == users[i].get("name")):
            return users[i].get("med")


def register_client(_name, _password):
    data = file.read(var.PATH_USERS)
    num_med = create_id_measurer()
    user = {'name':_name, "password":_password, "med":num_med, "last_measurement": "05/02/2023", "register_moth": []}
    data.append(user)
    file.write(data, var.PATH_USERS)


def create_id_measurer():
    data = file.read(var.PATH_DATA_MEASURE)
    num = str(random.randrange(0,10000))

    while(num in data):
        num = str(random.randrange(0,10000))
    add_measurer(num)
    return num


def add_measurer(num):
   data = file.read(var.PATH_DATA_MEASURE) 
   data[num] = []
   file.write(data, var.PATH_DATA_MEASURE)
   

'''
Realiza o calculo da fatura desde a útima leitura até o tempo corrente.
'''
def calculate_invoice(str_http): 
    closure = "10" 
    data_meas = file.read(var.PATH_DATA_MEASURE)
    data_users = file.read(var.PATH_USERS)
    name_client = str_http.get_user_name()
    l_measurement = ""
    current = datetime.now()
    total_kwh = 0
    
    for i in range(len(data_users)):
        if(name_client == data_users[i].get("name")):
            l_measurement = datetime.strptime(data_users[i].get("last_measurement"), '%d/%m/%Y')
            break

    list_data_meas = data_meas.get(get_num_measurer(name_client))

    for i in range(len(list_data_meas)):
        format_dt = datetime.strptime(list_data_meas[i].get("date_hour"), '%d/%m/%Y %H:%M')
        if(format_dt > l_measurement and format_dt < current):
            total_kwh += list_data_meas[i].get("consumption")

    price_total = total_kwh * PRICE_PER_KWH
    invoice_moth()


'''Calcula automaticamente a fatura do mês'''
def invoice_moth():
    data_meas = file.read(var.PATH_DATA_MEASURE)
    data_users = file.read(var.PATH_USERS)
    current = datetime.now()
    previus_day = datetime.strptime(file.read(var.PATH_READING_DAY).get("day_reading"), '%d/%m/%Y')
   
    if((current - previus_day).days >= 1):
        for i in range(len(data_users)):
            l_measurement = datetime.strptime(data_users[i].get("last_measurement"), '%d/%m/%Y')
            if((current - l_measurement).days == 30):
                print("é trinta")

    #terminar depois


def warning(str_http): 
    print("warning: ")
    data_meas = file.read(var.PATH_DATA_MEASURE)
    data_users = file.read(var.PATH_USERS)
    name_client = str_http.get_user_name()
    num_meas = ''
    for i in range(len(data_users)):
        if(data_users[i].get("name") == name_client):
            num_meas = data_users[i].get("med")
            break
    
    list_data_meas = file.read(var.PATH_DATA_MEASURE).get(num_meas)
    for i in range(7):
        

   




'''
def create_date():
    t = 10
    date_ = datetime.now()
    new_date = date_.replace(day=t,hour=0,minute=0,second=0)
    print(new_date)
'''