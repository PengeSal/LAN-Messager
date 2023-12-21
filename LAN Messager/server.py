import socket
import threading

connected_clients = []

def handle_client(client_socket):
    global connected_clients
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        for client in connected_clients:
            if client != client_socket: 
                try:
                    client.send(message.encode('utf-8'))
                except Exception as e:
                    print(f"Error sending message to client: {e}")
                    connected_clients.remove(client)
                    client.close()

        print(f"{message}")

hostname = socket.gethostname()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((hostname, 5555))
server_socket.listen(5)

print(f"Server is listening for connections on {hostname}...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} has been established!")

    connected_clients.append(client_socket)

    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start())
