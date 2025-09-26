import socket
s = socket.socket()
s.connect(('localhost', 9000))
while True:
    ip = input("Enter mac address: ")
    s.send(ip.encode())
    print("Logical address", s.recv(1024).decode())
