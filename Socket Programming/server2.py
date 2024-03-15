import socket

host = socket.gethostname()
port = 6969

s=socket.socket()

s.bind((host,port))
s.listen(1)

a,c = s.accept() 
while True:
    msg = input("Enter the message to send to client:")
    a.send(msg.encode())
    if msg!="bye":
        msg = a.recv(1024)
        print("\n msg:",msg.decode())
        if msg.decode()=="bye":
            break
    else:
        break