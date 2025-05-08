import socket
import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    print(f"Сервер запущен на {server_address}")
    server_socket.bind(server_address)
    server_socket.listen(1)
    
    while True:
        print("Ожидание подключения клиента...")
        connection, client_address = server_socket.accept()
        
        try:
            print(f"Подключен клиент: {client_address}")
            data = connection.recv(1024).decode('utf-8')
            print(f"Получены данные: {data}")
            
            try:
                a, b = map(float, data.split(','))
                result = calculate_hypotenuse(a, b)
                response = f"Гипотенуза треугольника с катетами {a} и {b} равна {result:.2f}"
            except ValueError:
                response = "Ошибка: неверный формат данных. Введите два числа через запятую."
            
            connection.sendall(response.encode('utf-8'))
            
        finally:
            connection.close()
            print("Соединение закрыто")

if __name__ == "__main__":
    run_server()