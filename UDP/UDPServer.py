from socket import *
from contagem_vogais import *

serverPort = 10219
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort)) #vincula o numero da porta ao servidor, cliente envia um pacote e vai chegar nessa porta 
print("O servidor está preparado para receber pacotes")

while True: #permite que o servidor receba e processe o pacote recebido
    message, clientAddress = serverSocket.recvfrom(2048)
    texto = message.decode()
    contagem = contagem_vogais(texto)
    mensagem_resposta = resposta(contagem)
    serverSocket.sendto(mensagem_resposta.encode(), clientAddress) #envia o pacote resultante ao servidor socket para que a internet mande o resultado ao endereço do client
