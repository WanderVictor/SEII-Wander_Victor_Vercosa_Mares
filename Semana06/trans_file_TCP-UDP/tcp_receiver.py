# bibliotecas importadas
import socket

# são definidos ip, portas de envio e recepção, tempo limite e tamanho do buffer
TCP_IP = "127.0.0.1"
FILE_PORT = 5005
DATA_PORT = 5006
timeout = 3
buf = 1024

# socket de internet é criado, junto aos parâmetros de rede, ip e protocolo tcp
sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ip passa a ser vinculado a porta na qual o arquivo será recebido
sock_f.bind((TCP_IP, FILE_PORT))
# somente um arquivo por vez
sock_f.listen(1)

# socket de internet é criado, junto aos parâmetros de rede, ip e protocolo tcp
sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ip passa a ser vinculado a porta na qual o dado será recebido
sock_d.bind((TCP_IP, DATA_PORT))
# somente um dados por vez
sock_d.listen(1)


while True:
    # em caso de conexão aceita
    # retorna o socket e endereço vinculado
    conn, addr = sock_f.accept()
    # recebe o buffer e armazena o mesmo em data
    data = conn.recv(buf)
    # em caso de existir algo, print no nome do arquivo
    if data:
        print "File name:", data
        # retira espaços no inicio e fim
        file_name = data.strip()
    
    # arquivo em aberto em modo de escrita
    f = open(file_name, 'wb')

    # em caso de conexão aceita
    # retorna o socker e endereço vinculado
    conn, addr = sock_d.accept()
    while True:
        # dados recebidos são escritos em um arquivo
        data = conn.recv(buf)
        if not data:
            break
        f.write(data)

    # escrita finalizada e arquivo fechado
    print "%s Finish!" % file_name
    f.close()