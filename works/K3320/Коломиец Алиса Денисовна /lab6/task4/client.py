import socket
import threading

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "NICK":
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Ошибка соединения!")
            client.close()
            break

def send_messages():
    while True:
        message = f"{nickname}: {input()}"
        client.send(message.encode('utf-8'))

nickname = input("Выберите никнейм: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()