# bibliotecas são importadas
import socket
import threading
import time

SERVER_IP = socket.gethostbyname(socket.gethostname())
# porta definida
PORT = 5050
# tupla do endereço
ADDR = (SERVER_IP, PORT)
# formato da mensagem
FORMATO = 'utf-8'

# cria socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# vincula com endereço
server.bind(ADDR)

# listas para coonexões e mensagens
conexoes = []
mensagens = []

def enviar_mensagem_individual(conexao):
    print(f"[ENVIANDO] Enviando mensagens para {conexao['addr']}")
    # enviar mensagem desde a ultima recebida até a quantidade total
    for i in range(conexao['last'], len(mensagens)):
        # concatena mensagem com inicio "msg="
        mensagem_de_envio = "msg=" + mensagens[i]
        # envia mensagem para conexão
        conexao['conn'].send(mensagem_de_envio.encode())
        # atualiza a ultima mensagem enviada
        conexao['last'] = i + 1
        # tempo antes de enviar a proxima mensagem
        time.sleep(0.2)

def enviar_mensagem_todos():
    global conexoes
    for conexao in conexoes:
        # envia mensagem individual para cada conexão
        enviar_mensagem_individual(conexao)

"""
1 vez que o cliente entrar, vai mandar o nome:
nome=.....
E as mensagens vem:
msg=
"""

def handle_clientes(conn, addr):
    # nova conexão criada
    print(f"[NOVA CONEXAO] Um novo usuario se conectou pelo endereço {addr}")
    # variaveis globais
    global conexoes
    global mensagens
    nome = False

    while(True):
        # mensagem recebida é decodificada e armazenada
        msg = conn.recv(1024).decode(FORMATO)
        if(msg):
            # se começa com "nome=", armazena o nome
            if(msg.startswith("nome=")):
                # mensagem é separada
                mensagem_separada = msg.split("=")
                # nome armazenado para conexão
                nome = mensagem_separada[1]
                # mapa com informações do cliente
                mapa_da_conexao = {
                    "conn": conn,
                    "addr": addr,
                    "nome": nome,
                    "last": 0
                }
                # mapa do novo cliente adicionado
                conexoes.append(mapa_da_conexao)
                # recebe mnesagens antigas
                enviar_mensagem_individual(mapa_da_conexao)
            # se a mensagem começa com "msg=", há uma nova mensagem    
            elif(msg.startswith("msg=")):
                # mensagem é separada
                mensagem_separada = msg.split("=")
                # armazena a mensagem
                mensagem = nome + "=" + mensagem_separada[1]
                # adiciona mensagens
                mensagens.append(mensagem)
                # envia mensagens para todos
                enviar_mensagem_todos()



def start():
    # inicia socket
    print("[INICIANDO] Iniciando Socket")
    # socket inicia a ouvir
    server.listen()
    while(True):
        # enquanto houver conexão, socker e endereço são armazenados
        conn, addr = server.accept()
        # thread criada para conexão
        thread = threading.Thread(target=handle_clientes, args=(conn, addr))
        thread.start()

start()