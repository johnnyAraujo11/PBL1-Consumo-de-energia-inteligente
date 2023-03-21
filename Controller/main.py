import server
import create_files as create
import calculate_req
import threading

create.create_files

start_server = server.Server()
start_server.connect()
threading.Thread(target=calculate_req.invoice_moth).start()