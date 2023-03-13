class Http_request():
    
    def __init__(self, msg):
        self.structure_http = msg.replace("\r", "")
        self.method = ''
        self.body = ''
        self.split_structure()
        self.router = ''
        self.extract_router()
    
    def split_structure(self):
        temp = ''

        pos =  self.structure_http.find("Content-Length")
        if(pos > -1):
            for i in range(pos, len(self.structure_http)):
                temp = temp + self.structure_http[i]
           
            for i in range(temp.find('\n'), len(temp)):
                self.body = self.body + temp[i]

            self.to_json()
       
        split_structure = self.structure_http.split("\n")
        self.method = split_structure[0].split(" ")[0]
       

    def get_info_date(self):
        list_date = ['date_i', 'date_f']
        date = []

        for i in range(0,len(list_date)):
            temp = self.get_str(list_date[i], self.structure_http)
            data_temp = self.get_str(":", temp)
            data_temp = data_temp.replace(":", "")
            data_temp = data_temp.replace(" ", "")
            
        #data inicial e data final
        date.append(data_temp)
        

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
        
    def extract_router(self):
        self.router = self.structure_http.split()[1]

            