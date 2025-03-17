import socket

def start_client(host='127.0.0.1', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    while True:
        message = input("Client: ")
        client_socket.sendall(message.encode())

        if message.lower() == 'exit':
            print("Closing connection.")
            break

        response = client_socket.recv(1024).decode()
        print(f"Server: {response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
