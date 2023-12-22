import socket, threading


connected_clients = []

def receive_image(client_socket):
    global connected_clients
    image_size = int(client_socket.recv(1024).decode())

    client_socket.sendall('ACK'.encode())

    received_data = b''
    while len(received_data) < image_size:
        data = client_socket.recv(1024)
        if not data:
            break
        received_data += data

    for client in connected_clients:
        try:
            client.sendall(f"image:{image_size}".encode('utf-8'))

            chunk_size = 1024
            for i in range(0, len(received_data), chunk_size):
                client.sendall(received_data[i:i + chunk_size])

        except Exception as e:
            print(f"Error sending message to client: {e}")


def handle_client(client_socket):
    global connected_clients
    connected_clients.append(client_socket)

    try:
        receive_image(client_socket)

    except ConnectionResetError:
        print("Client disconnected unexpectedly.")

    except Exception as e:
        print(f"Error: {e}")

    finally:

        connected_clients.remove(client_socket)
        client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostname = socket.gethostname()
server_address = (hostname, 5556)
server_socket.bind(server_address)

server_socket.listen(1)
print("Server is listening for connections...")

while True:
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()

