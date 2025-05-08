import socket
from datetime import datetime

def load_html_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "<h1>404 Not Found</h1><p>Файл не найден</p>"

def create_http_response(html_content):
    response = f"""HTTP/1.1 200 OK
Server: Python HTTP Server
Date: {datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT')}
Content-Type: text/html; charset=utf-8
Content-Length: {len(html_content)}
Connection: close

{html_content}"""
    return response.encode('utf-8')

def run_http_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('localhost', 8080)
    
    print(f"Запуск HTTP-сервера на http://{server_address[0]}:{server_address[1]}")
    server_socket.bind(server_address)
    server_socket.listen(1)
    
    while True:
        print("\nОжидание подключения...")
        connection, client_address = server_socket.accept()
        
        try:
            print(f"Подключен клиент: {client_address}")
            
            request = connection.recv(1024).decode('utf-8')
            print(f"Получен запрос:\n{request[:200]}...")
            
            html_content = load_html_file('index.html')
            
            http_response = create_http_response(html_content)
            connection.sendall(http_response)
            print("HTML-страница отправлена клиенту")
            
        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            connection.close()
            print("Соединение закрыто")

if __name__ == "__main__":
    run_http_server()