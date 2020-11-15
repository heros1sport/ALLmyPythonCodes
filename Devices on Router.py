import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(3)
for i in range(255):
    try:
        
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(3)
        ip = socket.gethostbyname(socket.gethostname()).split(".")[0] +"."+ socket.gethostbyname(socket.gethostname()).split(".")[1] +"."+ socket.gethostbyname(socket.gethostname()).split(".")[2]+"."+ str(i)
        s.connect((ip,9999))
        
    except ConnectionRefusedError:
        print(ip,"is connected to Router")
    except socket.timeout:
        print(ip,"is open")
    s.close()
