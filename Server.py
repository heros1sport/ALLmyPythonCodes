import socket
import ast
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',4455))
s.listen(10)
client1, adr1 = s.accept()
print("Client 1 : " + str(adr1))

f = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
f.bind(('127.0.0.1',4456))
f.listen(10)
client2, adr2 = f.accept()
print("Client 2 : " + str(adr2))
recv1 = 0
recv2 = 0
while True:
    recv1 = client1.recv(1024)
    recv2 = client2.recv(1024)
    print(str(recv1.decode("utf-8")) + str(recv2.decode("utf-8")))
    client2.send(recv1)
    client1.send(recv2)
        
    
