
#!/usr/bin/python3 # This is client.py file
import socket
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
port = 9999
print(host)
# connection to hostname on the port.
s.connect((host, port))
# Receive no more than 1024 bytes

x = 0
while (x==0):
    i = input(" enter the country name  : ")
    s.send(i.encode('ascii'))

    msg = s.recv(1024)
    print ("========> ", msg.decode('ascii'))
    msg_str = msg.decode('ascii')
    if(msg_str == "STOPPED"):
        break



s.close()


