from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
connectionSocket, addr = serverSocket.accept()
print("Connection established")

while True:
    sentence = connectionSocket.recv(1024).decode()
    print("From Client:", sentence)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    if sentence == "q":
        break
connectionSocket.close()
