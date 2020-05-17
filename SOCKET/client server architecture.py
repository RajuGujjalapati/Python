import socket
# create a socket object
print(" I am server I am starting a new stream for any queries :")
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
port = 9999
# bind to the port
serversocket.bind((host, port))#ip,port bind it
# queue up to 5 requests
serversocket.listen(5)
clientsocket,addr = serversocket.accept()#store the ip and adrr and accept the request
print("=======> ", clientsocket,addr)
print("Got a connection from %s" % str(addr))

while True:
    

    q = clientsocket.recv(2048)#receive from the client ques
    #print(" ***************> " , q , type(q))
    qs = q.decode('ascii')#decoding
    print ("========> ", qs, type(qs) )

    if(('USA' in  qs) or ('IND' in qs) or ('UK' in qs)):
        msg = "Welcome to " + str(qs) 
        clientsocket.send(msg.encode('ascii'))#encoding
    elif(qs == "STOP"):
        msg = "STOPPED" 
        clientsocket.send(msg.encode('ascii'))
        break
    else:
        msg = "Not supporting the country " + qs 
        clientsocket.send(msg.encode('ascii'))

clientsocket.close()



print(" Ended herte ")

