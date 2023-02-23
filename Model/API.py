
import os
import sys

dir_abs = os.path.dirname(os.path.realpath(__file__))
new = dir_abs[:-5]
new = new + "Controller"
sys.path.insert(0, new)

from Database import *


def create_arq_http(body):
    return "HTTP/1.0 200 OK\n\n{}".format(body)


def all_requests_get(router):
    if(router == "/consumo"):
       return create_arq_http("Seu consumo atual é: %s" % 111)

    if(router == "/fatura"):
        return create_arq_http("Sua fatura atual é de R$50,00")

    if(router == "/warning/excessive/energy"):
        return create_arq_http("Você tem um alerta de consumo excessivo.")
    
    if(router == "/warning/variation/energy"):
        return create_arq_http("Houve uma variação de energia capturado na sua residência.")
    

def all_request_post(router, content):
    if(router == "/"):
        print("")