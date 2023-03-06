class Http_request():
    
    def __init__(self, msg):
        self.structure_http = msg
        self.method = ''
        self.body = ''
        self.split_structure()
        self.router = ''
    
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
       

      
  