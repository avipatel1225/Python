import socket
from threading import Thread

host = "192.168.29.138"
port = 6969

s=socket.socket()
s.bind((host,port))
s.listen(2)

a,c=s.accept()
b,d=s.accept()

def send1():
    while True:
        msg = input()
        a.send(msg.encode())
        b.send(msg.encode())
        if msg=="bye":
            break
def recv1():
    while True:
        msg1 = a.recv(1024).decode()
        print(msg1)
        b.send(msg1.encode())
        
def recv2():
    while True:
        msg1 = b.recv(1024).decode()
        print(msg1)
        a.send(msg1.encode())
        
t1 = Thread(target = send1)
t2 = Thread(target = recv1)
t3 = Thread(target = recv2)

t1.start()
t2.start()
t3.start()