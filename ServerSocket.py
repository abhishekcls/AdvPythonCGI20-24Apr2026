import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen(1)

print("Server listening...")

conn, addr = server.accept()
print("Connected by", addr)

data = conn.recv(1024)
print("Client says:", data.decode())

conn.sendall(b"Hello from server")
conn.close()

# import socket
# import threading

# def handle_client(conn):
#     print("Client connected")
#     data = conn.recv(1024)
#     conn.sendall(b"OK")
#     conn.close()

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(("127.0.0.1", 5000))
# server.listen()

# while True:
#     conn, addr = server.accept()
#     threading.Thread(target=handle_client, args=(conn,)).start()