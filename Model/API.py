
import os
import sys

dir_abs = os.path.dirname(os.path.realpath(__file__))
new = dir_abs[:-5]
new = new + "Controller"
sys.path.insert(0, new)

#from Database import *

#Criar um classe para a resposta
def create_arq_http(body):
    return "HTTP/1.0 200 OK\n\n{}".format(body)


def all_requests_get(router):
    if(router == "/consumption"):
       print('entrou aq')
       return create_arq_http("Seu consumo atual é: %s" % 111)

    elif(router == "/fatura"):
        return create_arq_http("Sua fatura atual é de R$50,00")

    elif(router == "/warning/excessive/energy"):
        return create_arq_http("Você tem um alerta de consumo excessivo.")
    
    elif(router == "/warning/variation/energy"):
        return create_arq_http("Houve uma variação de energia capturado na sua residência.")
    

def all_request_post(router, content):
    if(router == "/"):
        print("")