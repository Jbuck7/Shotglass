import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # alklows server socket to reuse local address immedietly after socket is closed

SERVER_PORT = 8080
SERVER_HOST ="0.0.0.0"
server_socket.bind((SERVER_HOST,SERVER_PORT))

server_socket.listen(5) # server socket is listening for incoming connections with a backlog of 

print(f"Server is listening on {SERVER_HOST}:{SERVER_PORT}")


while True:
    client_socket, client_address = server_socket.accept() # server socket accepts incoming connection
    request = client_socket.recv(1024).decode() # server socket receives data from client
    print(request)
