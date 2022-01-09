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


"""
TCP Client:

There have been countless times during penetration tests that I’ve needed to whip up a TCP client to
test for services, send garbage data, fuzz, or any number of other tasks. If you are working within the
confines of large enterprise environments, you won’t have the luxury of networking tools or
compilers, and sometimes you’ll even be missing the absolute basics like the ability to copy/paste or
an Internet connection. This is where being able to quickly create a TCP client comes in extremely
handy.
"""

