import socket
from threading import Thread

host = socket.gethostname()
port = 6969

s=socket.socket()
s.connect((host,port))

def send1():
    while True:
        msg =input()
        s.send(msg.encode())
def recv1():
    while True:
        msg = s.recv(1024)
        print(msg.decode())

t1 = Thread(target = send1)
t2 = Thread(target = recv1)

t1.start()
t2.start()