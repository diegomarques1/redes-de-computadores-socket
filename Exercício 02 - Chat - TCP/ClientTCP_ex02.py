# Diego Souza Lima Marques - TIA: 32039921
# Lab - Socket - Ex. 02
# Cliente TCP

import socket #importa modulo socket

TCP_IP = '192.168.0.103' # endereço IP do servidor 
TCP_PORTA = 32039      # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024

MENSAGEM  = input("Digite sua mensagem para o servidor: ")
    
# Criação de socket TCP do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conecta ao servidor em IP e porta especifica 
cliente.connect((TCP_IP, TCP_PORTA))

# envia mensagem para servidor 
cliente.send(MENSAGEM.encode('UTF-8'))

while True:
    data = cliente.recv(1024).decode('UTF-8')
    if data == 'QUIT':
        break
    else:
        print("Mensagem recebida do servidor: ", data)
        MENSAGEM = input("Digite uma mensagem para o servidor: ")
        if MENSAGEM == 'QUIT':
            cliente.send(MENSAGEM.encode('UTF-8'))
            break
        print("Mensagem enviada para o servidor: ", MENSAGEM)
        cliente.send(MENSAGEM.encode('UTF-8'))
        
# fecha conexão com servidor
cliente.close()
