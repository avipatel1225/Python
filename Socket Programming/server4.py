import socket
from threading import Thread

host = socket.gethostname()
port = 6969

s=socket.socket()
s.bind((host,port))
s.listen(2)

user_list=[]
def users():
    while True:
        x,y=s.accept()
        user_list.append(x)
    
def send1():
    while True:
        msg = input()
        for i in user_list:
            i.send(msg.encode())
        if msg=="bye":
            break
            
def recv1():
    while True:
        '''
            msg = user_list[0].recv(1024).decode()
            print(msg)
            for i in user_list[1:]:
                i.send(msg.encode())       
            if msg=="bye":
                break
        '''
        print(user_list)
        for i in user_list:
            print("l")
            threadfun(i)
            
            
def threadfun(a):
    print("m")
    z = Thread(target = recv2,args=(a,))
    
    z.start()
    
def recv2(a):
    while True:
        print("a")
        msg = a.recv(1024)
        print(msg.decode())
    
            
t1 = Thread(target = users)            
t2 = Thread(target = send1)
t3 = Thread(target = recv1)

t1.start()
t2.start()
t3.start()