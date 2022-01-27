# bibliotecas são importadas
import socket
import threading
import time

# porta definida
PORT = 5050
# formato de mensagem
FORMATO = 'utf-8'
# ip do servidor
SERVER = "192.168.0.109"
# tupla do endereço
ADDR = (SERVER, PORT)

# cria socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# conexão com o servidor
client.connect(ADDR)

def handle_mensagens():
    while(True):
        # recebe mensagem
        msg = client.recv(1024).decode()
        # separa a mensagem
        mensagem_splitada = msg.split("=")
        # exibe remetente e conteúdo da mensagem
        print(mensagem_splitada[1] + ": " + mensagem_splitada[2])

def enviar(mensagem):
    # mensagem codificada é enviada ao servidor
    client.send(mensagem.encode(FORMATO))

def enviar_mensagem():
    # coleta mensagem do cliente
    mensagem = input()
    # envia dado
    enviar("msg=" + mensagem)

def enviar_nome():
    # coleta nome do cliente
    nome = input('Digite seu nome: ')
    # envia dado
    enviar("nome=" + nome)

def iniciar_envio():
    # envia nome
    enviar_nome()
    # envia mensagem do cliente
    enviar_mensagem()

def iniciar():
    # thread para receber mensagem
    thread1 = threading.Thread(target=handle_mensagens)
    # thread para enviar mensagem
    thread2 = threading.Thread(target=iniciar_envio)
    # inicar threads
    thread1.start()
    thread2.start()

iniciar()