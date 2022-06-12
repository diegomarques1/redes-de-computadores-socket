# Diego Souza Lima Marques - TIA: 32039921
# Lab - Socket - Desafio - Ex. 03
# Servidor TCP

import socket #importa modulo socket
 
TCP_IP = '192.168.0.103' # endereço IP do servidor 
TCP_PORTA = 32039        # porta disponibilizada pelo servidor
# TAMANHO_BUFFER = 1024     # definição do tamanho do buffer
 
# Criação de socket TCP
# SOCK_STREAM, indica que será TCP.
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP e porta que o servidor deve aguardar a conexão
servidor.bind((TCP_IP, TCP_PORTA))

#Define o limite de conexões. 
servidor.listen(1)

flag_escrita = False
final_arquivo = False

while True:
    # Aceita conexão a cada 1024 bytes lidos
    conn, addr = servidor.accept()
    nome_arquivo = conn.recv(1024).decode('utf-8')
    arq_recebido = open(nome_arquivo, 'wb')
    while flag_escrita == False:
        parte_arq = conn.recv(1024) # recebe cada parte de 1024 bytes do arquivo
        while parte_arq:
            arq_recebido.write(parte_arq) # escreve no arquivo
            parte_arq = conn.recv(1024) # lê a próxima parte

        flag_escrita = True

    arq_recebido.close()
    break

print("Arquivo recebido com sucesso! Imprimindo seu conteúdo:\n")

arq_final = open(nome_arquivo, 'r', encoding='utf-8')
while not final_arquivo:
    linha = arq_final.readline()
    if linha == '': # string vazia
        final_arquivo = True
    else:
        conteudo = linha.rstrip() # tirar o caractere de controle
        print(conteudo)

arq_final.close()

conn.close()
servidor.close()

