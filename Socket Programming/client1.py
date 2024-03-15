import socket


host = socket.gethostname()
port = 3333


s =socket.socket()

s.connect((host,port))
msg = s.recv(1024)
print(msg.decode())
msg ="haa moj"
s.send(msg.encode())
