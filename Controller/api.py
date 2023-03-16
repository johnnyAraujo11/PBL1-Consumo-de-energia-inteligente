import os
import sys
import json
import http_req
import calculate_req
from datetime import datetime

dir_abs = os.path.dirname(os.path.realpath(__file__))
new = dir_abs[:-5]
new = new + "Controller"
sys.path.insert(0, new)

#from Database import *
from http_req import *


class API():

    def __init__(self, msg_http) -> None:
        self.str_http = http_req.Http_request(msg_http)


    def create_arq_http(self, body):
        return "HTTP/1.0 200 OK\n\n{}".format(body)


    def all_requests_get(self, router):
        if(router == "/consumption"):
            total_cons = calculate_req.consumption(self.str_http)
            _date = self.str_http.get_info_date()
            return self.create_arq_http("O consumo total entre as datas {} e {} foi de {}".format(_date[0], _date[1], total_cons))
       
        if(router == "/register-client"):
            client = self.str_http.decode_user()
            calculate_req.register_client(client[0], client[1])

            return self.create_arq_http("Cadastrado com sucesso!")
        
        if(router == "/adm/registers"):
            return self.create_arq_http("Os usuários cadastrados")
        
        if(router == "/fatura"):
            return self.create_arq_http("Sua fatura atual é de R$50,00")

        if(router == "/warning/excessive/energy"):
            return self.create_arq_http("Você tem um alerta de consumo excessivo.")
        
        if(router == "/warning/variation/energy"):
            return self.create_arq_http("Houve uma variação de energia capturado na sua residência.")
     

    def response(self):
        if(self.str_http.check_user_exist() and self.str_http.router !="/register-client" or self.str_http.router != "/adm/registers"):
            return self.all_requests_get(self.str_http.router) if "GET" == self.str_http.method else self.all_request_post(self.str_http.router)
        else:
            return self.create_arq_http("Você não está cadastrado")

    def all_request_post(self, router, content):
        if(router == "/"):
            print("")


    def openFile():
        file = open('DB.json',)
        data = json.load(file)
        file.close()
        return data


#str_http.get_info_date()
#str_http.extract_router()
            