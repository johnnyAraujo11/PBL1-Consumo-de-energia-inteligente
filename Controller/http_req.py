import re

class http_request():
    
    def __init__(self, msg):
        self.structure_http = msg
        self.method = ''
        self.body = ''
        self.split_structure()
    
    def split_structure(self):
        print("request")

        t = re.sub('\r','', self.structure_http)
        
        print(t.split("\n"))
        #print(t)
        split_structure = self.structure_http.split("\n")
        self.method = split_structure[0].split(" ")[0]
        '''
        print("\n")
        print(split_structure)
        print("\n")
        ''' 
        data = ''
        j = False
        for row in split_structure:
            if("Content-Length" in row):
                j = True
            if(j and row != ""):
                print("linha")

