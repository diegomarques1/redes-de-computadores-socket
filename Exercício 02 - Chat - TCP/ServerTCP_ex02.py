# Diego Souza Lima Marques - TIA: 32039921
# Lab - Socket - Ex. 02
# Servidor TCP

import socket #importa modulo socket
 
TCP_IP = '192.168.0.103' # endereço IP do servidor 
TCP_PORTA = 32039       # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024     # definição do tamanho do buffer
 
# Criação de socket TCP
# SOCK_STREAM, indica que será TCP.
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP e porta que o servidor deve aguardar a conexão
servidor.bind((TCP_IP, TCP_PORTA))

#Define o limite de conexões. 
servidor.listen()

# Aceita conexão 
conn, addr = servidor.accept()

while True:
    #dados retidados da mensagem recebida
    data = conn.recv(TAMANHO_BUFFER).decode('UTF-8')
    if data == 'QUIT':
        break
    else:
        print ("Mensagem recebida do cliente: ", data) 
        MENSAGEM = input("Digite uma mensagem para o cliente: ")
        if MENSAGEM == 'QUIT':
            conn.send(MENSAGEM.encode('UTF-8'))
            break
        print("Mensagem enviada para o cliente: ", MENSAGEM)
        conn.send(MENSAGEM.encode('UTF-8'))

conn.close()
servidor.close()
