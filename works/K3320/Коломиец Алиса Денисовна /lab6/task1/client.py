import socket

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_address = ('localhost', 12345)
    print(f"Подключение к серверу {server_address[0]}:{server_address[1]}")
    client_socket.connect(server_address)
    
    try:
        message = "Hello, server"
        client_socket.sendall(message.encode('utf-8'))
        print(f"Отправлено серверу: {message}")
        
        data = client_socket.recv(1024)
        print(f"Получено от сервера: {data.decode('utf-8')}")
        
    finally:
        client_socket.close()
        print("Соединение с сервером закрыто")

if __name__ == "__main__":
    run_client()