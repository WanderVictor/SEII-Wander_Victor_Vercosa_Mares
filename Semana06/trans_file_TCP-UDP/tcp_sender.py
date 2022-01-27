# bibliotecas importadas
import socket
import sys

# são definidos ip, portas de envio e recepção, tempo limite e tamanho do buffer
TCP_IP = "127.0.0.1"
FILE_PORT = 5005
DATA_PORT = 5006
buf = 1024
# nome do arquivo recolhido
file_name = sys.argv[1]


try:
    # socket de internet é criado, junto aos parâmetros de rede, ip e protocolo tcp
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # inicia conexão via ip e porta de envio do arquivo
    sock.connect((TCP_IP, FILE_PORT))
    # nome do arquivo enviado
    sock.send(file_name)
    # conexão fechada
    sock.close()

    print "Sending %s ..." % file_name

    # arquivo aberto em modo de leitura
    f = open(file_name, "rb")
    # conexão aberta
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # inicia conexão via ip e porta de envio de dados
    sock.connect((TCP_IP, DATA_PORT))
    # o que há no arquivo é lido
    data = f.read()
    # conteúdo do arquivo é enviado
    sock.send(data)

finally:
    # conexão fechada junto com arquivo
    sock.close()
    f.close()