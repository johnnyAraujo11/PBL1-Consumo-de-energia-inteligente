import file
from datetime import datetime

def consumption(str_http):
    date = str_http.get_info_date()
    date_i = date[0]
    date_f = date[1]
    print(date_f + " " + date_i)
    if(date_i != None and date_f != None):
       print("Calculando comsumo")


