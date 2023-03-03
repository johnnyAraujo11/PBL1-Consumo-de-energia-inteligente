class http_request():
    
    def __init__(self, msg):
        self.structure_http = msg
        self.method
        self.body
    
    def split_structure(self):
        print("request")
        split_structure = self.structure_http.split("\n")
        self.method = split_structure[0].split(" ")[0]

        for row in split_structure:
            if(row == ""):
                print("achei a linha vazia")

