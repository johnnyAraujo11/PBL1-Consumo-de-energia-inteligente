class http_msg():
    
    def __init__(self, method = None, status = None,host = None, content = None, num_status = None, body = None):
       self.method = method
       self.status = status
       self.host = host
       self.content = content
       self.num_status = num_status
       self.body = body


    def request():
        print("request")

    def get_method(self):
        return self.method
    
    def get_status(self):
        return self.status
    
    def get_host(self):
        return self.host
    
    def get_content(self):
        return self.content
    

    def response(self):
        print("reponse")
        return "HTTP/1.0 {} {}\n\n{}".format(self.num_status, self.status, self.body)
    
    def request():
        print("request")