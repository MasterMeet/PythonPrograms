import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname()
port = 444

serversocket.bind((host,port))

serversocket.listen()

while True:
    clientsocket, address = serversocket.accept()
    print(f"Data Received from {str(address)}")
    message = "Connection Established!"
    clientsocket.send(message)
    clientsocket.close()