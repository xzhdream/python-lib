import socket

HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('server fileno:',s.fileno()) # server fileno: 6
    with conn:
        print('Connected by', addr,conn,conn.fileno())
        # Connected by ('127.0.0.1', 57683) <socket.socket fd=7, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 50007), raddr=('127.0.0.1', 57683)> 7
        while True:
            data = conn.recv(1024)
            if not data: break
            # conn.sendall(data)
            print(data)