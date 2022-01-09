import socket

#Define Here Target Host Port.
target_host = "ww.example123.com"
target_port = 80

#Making Socket Object Here AF_INET it's Mean We Are Make TCP Connection.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Makeing Connection To Target.
client.connect((target_host,target_port))

#Create Variable Data And Write Data. Data Can Be Anything IP,Web Adress.  
data = "GET / HTTP/1.1\r\nHost: example123.com\r\n\r\n"

#Sending Data To Taregt.
client.send(data.encode('utf-8'))

#Getting Response From Target.
response = client.recv(4096)

print(response)