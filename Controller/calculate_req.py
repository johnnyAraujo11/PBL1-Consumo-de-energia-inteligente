import file
import random
from datetime import datetime, timedelta
import variables as var
from time import sleep
import json
PRICE_PER_KWH = 0.35


'''
Realizar o cadastro de um cliente
'''
def register_client(str_http):
    obj_json = json.loads(str_http.body)
    data = file.read(var.PATH_USERS)
    num_med = create_id_measurer()
    user = {'name':obj_json.get("name"), "password":obj_json.get("password"), "med":num_med, "last_measurement": "05/02/2023", "register_moth": []}
    data.append(user)
    file.write(data, var.PATH_USERS)


'''
Realiza o cálculo do consumo em um intevalo especificado
'''
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



'''
Cria um número aleatório adicionar como identificador de um medidor.
'''
def create_id_measurer():
    data = file.read(var.PATH_DATA_MEASURE)
    num = str(random.randrange(0,10000))

    while(num in data):
        num = str(random.randrange(0,10000))
    add_measurer(num)
    return num

'''
Adicionar o número gerado de um medido em um arquivo json.
'''
def add_measurer(num):
   data = file.read(var.PATH_DATA_MEASURE) 
   data[num] = []
   file.write(data, var.PATH_DATA_MEASURE)
   

'''
Realiza o cálculo da fatura desde a útima leitura até o tempo corrente.
@str_http recebe a classe que representa a string http da requisção, podendo ser extraídas algumas informações 
para realizar a execução da função, como nesse caso, obter o nome do cliente logado.
'''
def calculate_invoice_partial(str_http): 
    data_meas = file.read(var.PATH_DATA_MEASURE)
    data_users = file.read(var.PATH_USERS)
    name_client = str_http.get_user_name()
    l_measurement = ""
    current = datetime.now()
    total_kwh = 0
    
    for i in range(len(data_users)):
        if(name_client == data_users[i].get("name")):
            l_measurement = datetime.strptime(data_users[i].get("last_measurement"), '%d/%m/%Y %H:%M')
            break

    list_data_meas = data_meas.get(get_num_measurer(name_client))

    for i in range(len(list_data_meas)):
        format_dt = datetime.strptime(list_data_meas[i].get("date_hour"), '%d/%m/%Y %H:%M')
        if(format_dt > l_measurement and format_dt < current):
            total_kwh += list_data_meas[i].get("consumption")

    price_total = total_kwh * PRICE_PER_KWH
    return str_invoice(price_total, name_client,  total_kwh)


def str_invoice(price, name, t_kwh):
    return "======= Fatura parcial =======\nNome: {}\nPreço: {}\nTotal cosumido: {}kwh".format(name, price, t_kwh)


'''Calcula automaticamente a fatura do mês'''
def invoice_moth():
    data_users = file.read(var.PATH_USERS)
    current = datetime.now()
    previus_day = datetime.strptime(file.read(var.PATH_READING_DAY).get("day_reading"), '%d/%m/%Y %H:%M')
    while(True):
        print("Esperando para executar...")
        sleep(3600)
        if((current - previus_day).days >= 1): 
            for i in range(len(data_users)):
                l_measurement = datetime.strptime(data_users[i].get("last_measurement"), '%d/%m/%Y %H:%M')
                temp_date = current.replace(hour=l_measurement.hour, minute=l_measurement.minute, second=0) 
                #Verifica se há 30 dias corridos desde a última medição
                if(abs((l_measurement- temp_date).days) == 30):
                    list_data_meas = file.read(var.PATH_DATA_MEASURE).get(data_users[i].get("med"))
                    total = 0
                    for j in range(len(list_data_meas)):
                        date_meas = datetime.strptime(list_data_meas[j].get("date_hour"), '%d/%m/%Y %H:%M')
                        if(date_meas >= l_measurement and date_meas <= temp_date):
                            total += list_data_meas[j].get("consumption")    
                    create_obj_invoice(data_users[i], data_users[i].get("name"), total, l_measurement, temp_date)
                    total = 0

        file.write(data_users, var.PATH_USERS)

'''Cria um obj no formato json e adicionar as informações da fatura ao cliente.'''
def create_obj_invoice(data_users, name, total, data_l_measurement, date_final):
    obj_json = {"nome":name,
                "Preco": round(total * PRICE_PER_KWH, 2),
                "ultima leitura":datetime.strftime(data_l_measurement, '%d/%m/%Y'),
                "Leitura autal": datetime.strftime(date_final,'%d/%m/%Y')}
    data_users.get("register_moth").append(obj_json)
   

'''
Realiza  média dos n últimos dias, verificando se no dia corrente o consumo de energia do cliente está em excesso.
'''
def warning(str_http): 
    n = 7
    data_users = file.read(var.PATH_USERS)
    name_client = str_http.get_user_name()
    seven_d_ago = (datetime.now() - timedelta(n)).replace(hour=0 , minute=0, second=0)
    previuos_day = (datetime.now() - timedelta(1)).replace(hour=0 , minute=0, second=0)
    num_meas = ''
    total_kwh = 0
    total_kwh_today = 0
    current = datetime.now()
    temp_current = datetime.now().replace(hour=0, minute=0, second=0)


    for i in range(len(data_users)):
        if(data_users[i].get("name") == name_client):
            num_meas = data_users[i].get("med")
            break
    
    list_data_meas = file.read(var.PATH_DATA_MEASURE).get(num_meas)
    for i in range(len(list_data_meas)):
        d_h = datetime.strptime(list_data_meas[i].get("date_hour"), '%d/%m/%Y %H:%M')
        if(d_h >= seven_d_ago and d_h <= previuos_day):
            total_kwh += list_data_meas[i].get("consumption")
        if(d_h >= temp_current and d_h <=current):
            total_kwh_today += list_data_meas[i].get("consumption")

    if(total_kwh_today != 0 and calculare_average(total_kwh, n) / total_kwh_today * 100 < 20):
            return "Alerta de alto consumo em relação ao últimos {} dias\nConsumo de hoje: {}kwh.".format(n, total_kwh_today)
    else:
        return "Não há consumo excessivo registrado."

'''
Faz o cálculo da média de n dias
'''
def calculare_average(total, n):
    return (total / n) 

'''
Retorna todos os clientes cadastrados
'''
def get_clients():
    return file.read(var.PATH_USERS)
    

    