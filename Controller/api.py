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

'''
Classe API que contém métodos de retorno de requisições do usuário
'''
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
        
        if(router == "/adm/registers"):
            self.str_http.teste()
            return self.create_arq_http("Os usuários cadastrados")
        
        if(router == "/invoice"):
            return self.create_arq_http(calculate_req.calculate_invoice_partial(self.str_http))
         
        if(router == "/warning"):
            return self.create_arq_http(calculate_req.warning(self.str_http))
            
    
    
    def response(self):
        if(self.str_http.check_user_exist() and self.str_http.router !="/register-client" or self.str_http.router != "/adm/registers"):
            return self.all_requests_get(self.str_http.router) if "GET" == self.str_http.method else self.all_request_post(self.str_http.router)
        else:
            return self.create_arq_http("Você não está cadastrado")

    def all_request_post(self, router):
       
        if(router == "/register-client"):
            calculate_req.register_client(self.str_http)
            return self.create_arq_http("Cadastrado com sucesso!")
