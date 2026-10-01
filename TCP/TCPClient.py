from socket import *

serverName = "localhost"
serverPort = 10219
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
mensagem_resposta = input('coloque qualquer coisa: ')
clientSocket.send(mensagem_resposta.encode())
modifiedSentence = clientSocket.recv(1040)
print("do servidor : ", modifiedSentence.decode())
clientSocket.close()

