# bibliotecas importadas
import socket
import select

# são definidos ip, portas de envio e tempo limite
UDP_IP = "127.0.0.1"
IN_PORT = 5005
timeout = 3

# socket de internet é criado, junto aos parâmetros de rede, ip e protocolo udp
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# ip e porta de recebimento vinculados
sock.bind((UDP_IP, IN_PORT))

while True:
    # dados de 1024 bits são recebidos, dado e endereço de origem são retornados
    data, addr = sock.recvfrom(1024)
    if data:
        # nome do arquivo é printado
        print "File name:", data
        # espaços são retirados do inicio e do fim
        file_name = data.strip()

    # arquivo é aberto em modo de escrita
    f = open(file_name, 'wb')

    while True:
        # aguarda para leitura
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            # em caso de existir, recebe a quantidade de dados e escreve no arquivo
            data, addr = sock.recvfrom(1024)
            f.write(data)
        else:
            # em caso de não existir, finaliza
            print "%s Finish!" % file_name
            f.close()
            break