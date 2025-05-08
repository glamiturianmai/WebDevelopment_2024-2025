import socket

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    
    print("Подключение к серверу...")
    client_socket.connect(server_address)
    
    try:
        print("Введите длины катетов через запятую:")
        a, b = input().split(',')
        message = f"{a},{b}"
        
        client_socket.sendall(message.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        
        print("Результат от сервера:", response)
        
    except ValueError:
        print("Ошибка: введите два числа через запятую!")
    finally:
        client_socket.close()

if __name__ == "__main__":
    run_client()