from socket import *

serverName = "localhost" #ou 10.0.99.150
serverPort = 10219
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('digite qualquer sentença:')
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()