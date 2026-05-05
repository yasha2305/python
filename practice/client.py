import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

username = input("Enter your username: ")

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "USERNAME":
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        msg = input("")
        message = f"{username}: {msg}"
        client.send(message.encode('utf-8'))

threading.Thread(target=receive).start()
threading.Thread(target=write).start()