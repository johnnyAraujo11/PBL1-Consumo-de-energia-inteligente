class http_msg():
    
    def __init__(self, method, status = None,host = None, content = None):
       self.method
       self.status
       self.host
       self.content


    def response(num_status,status, body):
        print("reponse")
        return "HTTP/1.0 {} {}\n\n{}".format(num_status, status, body)


    def request():
        print("request")