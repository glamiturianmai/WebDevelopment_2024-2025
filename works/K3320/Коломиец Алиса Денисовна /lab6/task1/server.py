import socket

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_address = ('localhost', 12345)
    print(f"Запуск сервера на {server_address[0]}:{server_address[1]}")
    server_socket.bind(server_address)
    
    server_socket.listen(1)
    
    while True:
        print("Ожидание соединения...")
        connection, client_address = server_socket.accept()
        
        try:
            print(f"Подключен клиент: {client_address}")
            
            data = connection.recv(1024)
            print(f"Получено от клиента: {data.decode('utf-8')}")
            
            response = "Hello, client"
            connection.sendall(response.encode('utf-8'))
            print(f"Отправлено клиенту: {response}")
            
        finally:
            connection.close()
            print("Соединение с клиентом закрыто")

if __name__ == "__main__":
    run_server()