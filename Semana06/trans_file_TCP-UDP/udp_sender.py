# bibliotecas importadas
import socket
import time
import sys

# são definidos ip, portas de envio, tempo limite e tamanho do buffer
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
buf = 1024
# nome do arquivo recolhido
file_name = sys.argv[1]

# socket de internet é criado, junto aos parâmetros de rede, ip e protocolo udp
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# inicia conexão via ip e porta udp
sock.sendto(file_name, (UDP_IP, UDP_PORT))
print "Sending %s ..." % file_name

# arquivo aberto em modo de leitura
f = open(file_name, "r")
# o que há no arquivo é lido
data = f.read(buf)
while(data):
    # dado enviado para porta UDP
    if(sock.sendto(data, (UDP_IP, UDP_PORT))):
        data = f.read(buf)
        # "Dê ao receptor um pouco de tempo para economizar"
        time.sleep(0.02)

# socket e arquivos são fechados
sock.close()
f.close()