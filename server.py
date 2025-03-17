import socket

def start_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data or data.lower() == 'exit':
            print("Connection closed by client.")
            break
        print(f"Client: {data}")

        response = input("Server: ")
        conn.sendall(response.encode())

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
