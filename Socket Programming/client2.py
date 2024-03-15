import socket

host = socket.gethostname()
port = 6969

s=socket.socket()
s.connect((host,port))
while True:
    msg = s.recv(1024)
    print("\n msg:",msg.decode())
    if msg!="bye":
        msg = input("Enter the message to send to server:")
        s.send(msg.encode())
        if msg=="bye":
            break
    else:
        break