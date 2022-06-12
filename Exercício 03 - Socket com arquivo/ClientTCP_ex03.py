# Diego Souza Lima Marques - TIA: 32039921
# Lab - Socket - Desafio - Ex. 03
# Cliente TCP

import socket #importa modulo socket

TCP_IP = '192.168.0.103' # endereço IP do servidor 
TCP_PORTA = 32039      # porta disponibilizada pelo servidor
# TAMANHO_BUFFER = 1024     # definição do tamanho do buffer

# Criação de socket TCP do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conecta ao servidor em IP e porta especifica 
cliente.connect((TCP_IP, TCP_PORTA))

nome_arquivo = input("Digite o nome do arquivo .txt a ser lido: ")

cliente.send(nome_arquivo.encode('UTF-8'))

arq = open(nome_arquivo, 'rb') # leitura de arquivo binário

parte_arq = arq.read(1024) # lê 1024 bytes do arquivo

while parte_arq: # enquanto ainda houver conteúdo para ler
    cliente.send(parte_arq) # envia o conteúdo do cliente para o servidor
    parte_arq = arq.read(1024) # lê os próximos 1024 bytes do arquivo

arq.close()

# fecha conexão com servidor
cliente.close()
