import socket
import threading

clients = []
nicknames = []

def broadcast(message, sender=None):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove_client(client)

def remove_client(client):
    if client in clients:
        index = clients.index(client)
        nickname = nicknames[index]
        clients.remove(client)
        client.close()
        nicknames.remove(nickname)
        broadcast(f"{nickname} покинул чат!".encode('utf-8'))

def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            broadcast(message, sender=client)
        except:
            remove_client(client)
            break

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))
    server.listen()
    print("Сервер чата запущен и ожидает подключений...")

    while True:
        client, address = server.accept()
        print(f"Подключение от {str(address)}")

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        
        nicknames.append(nickname)
        clients.append(client)

        print(f"Никнейм клиента: {nickname}")
        broadcast(f"{nickname} присоединился к чату!", sender=client)
        client.send("Подключение к серверу успешно!".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    run_server()