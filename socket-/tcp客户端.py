import socket

HOST = '192.168.212.171'    # The remote host
PORT = 55555             # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print('client fileno:',s.fileno())
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))