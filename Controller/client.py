import socket

def client(host = '172.17.0.2', port=8080):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server
    server_address = (host, port)
    print ("Connecting to %s port %s" % server_address)
    sock.connect(server_address)
    # Send data
    try:
        # Send data
        message = "client1" 
       
        print ("Sending %s" % message)
       
        sock.sendall(message.encode('utf-8'))
        # Look for the response
        amount_received = 0 
        amount_expected = len(message)
        '''
        while True:
            data = sock.recv(16)
            amount_received += len(data)
            print ("Received: %s" % data)
        '''
    except socket.error as e:
        print ("Socket error: %s" %str(e))
    except Exception as e:
        print ("Other exception: %s" %str(e))
    finally:
        print ("Closing connection to the server")
        sock.close()

client()
