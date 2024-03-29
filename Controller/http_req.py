import base64
import file
import variables as var


'''
Classe responável por extrair informações da requisição HTTP.
'''
class Http_request():
    
    def __init__(self, msg):
        self.structure_http = msg.replace("\r", "")
        self.method = ''
        self.body = ''
        self.router = ''
        self.cript_user = ''
        self.extract_user_cript()
        self.split_structure()
        self.extract_router()
    
    '''
    Função que executa quando o objeto é instanciado, extraindo o método HTTP. 
    '''
    def split_structure(self):
        temp = ''

        pos =  self.structure_http.find("Content-Length")
        if(pos > -1):
            for i in range(pos, len(self.structure_http)):
                temp = temp + self.structure_http[i]
           
            for i in range(temp.find('\n'), len(temp)):
                self.body = self.body + temp[i]

            #self.to_json()
       
        split_structure = self.structure_http.split("\n")
        self.method = split_structure[0].split(" ")[0]
       

    '''
    Extraí a data especificada para realizar a filtragem dos dados a serem respondidos.
    '''
    def get_info_date(self):
        list_date = ['date_i', 'date_f']
        date = []
        for i in range(0,len(list_date)):
            temp = self.get_str(list_date[i], self.structure_http)
            data_temp = self.get_str(":", temp)
            data_temp = data_temp.replace(":", "",1)
            data_temp = data_temp.replace(" ", "",1)
            date.append(data_temp)
        return date
        


    def get_str(self, _string, msg):
        temp = ""
        pos = msg.find(_string)
        if(pos > -1):
            for i in range(pos, len(msg)):
                if(self.structure_http[i] != '\n'):
                    temp = temp + msg[i]
                else:
                    break
        return temp                
        
    '''
    Extrai a rota que foi informada.
    '''
    def extract_router(self):
        self.router = self.structure_http.split()[1]

    '''
    Extrai o login do usuário com a seu usuário e senha criptografados
    '''
    def extract_user_cript(self):
        temp = self.get_str("Authorization", self.structure_http)
        temp = temp.split(" ")
        self.cript_user = temp[2]
        
    '''
    Decodifica o usuário e senha criptografados.
    '''
    def decode_user(self):
        user = base64.b64decode(self.cript_user).decode('utf-8')
        list_l = user.split(":")
        return list_l
    
    '''
    Retorna o nome do usuário logado
    '''
    def get_user_name(self):
        return self.decode_user()[0]
    
    '''
    Verifica se o usuário existe ou se a lista de usuários está vazia.
    '''
    def check_user_exist(self):
        users = file.read(var.PATH_USERS)
        data_user = self.decode_user()
        if(users != 0):
            for json_obj in users:
                return True if json_obj.get("name") == data_user[0] and json_obj.get("password") == data_user[1] else False 
        else:
            return False       
    
   