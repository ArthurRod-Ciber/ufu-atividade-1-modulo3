from socket import *
from inverter_texto import *
serverPort = 10219
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print("O servidor esta pronto para receber pacotes")
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1040).decode()
    mensagem_resposta = resposta(sentence)
    connectionSocket.send(mensagem_resposta.encode())
    connectionSocket.close()