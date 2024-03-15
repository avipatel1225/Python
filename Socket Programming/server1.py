import socket


host = socket.gethostname()
port = 3333


s = socket.socket()

s.bind((host,port))


s.listen(1)

a,c  = s.accept()
msg = "hello how are you"
a.send(msg.encode())
msg = a.recv(1024)
print(msg.decode())
'''

print(a,"\n",c)
'''