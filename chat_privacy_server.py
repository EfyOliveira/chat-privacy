import socket

def iniciar_servidor():
    host = 'localhost'
    port = 12345
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, port))
    servidor.listen(1)
    print("Servidor iniciado.")
    print("Aguardando conexão...")
    conn, addr = servidor.accept()
    print("Conexão estabelecida com:", addr)
    return conn

def iniciar_cliente():
    host = 'localhost'
    port = 12345
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, port))
    print("Conectado ao servidor.")
    return cliente

def enviar_mensagem(conn):
    while True:
        mensagem = input()
        if mensagem == "sair":
            conn.send(mensagem.encode())
            conn.close()
            break
        conn.send(mensagem.encode())

def receber_mensagem(conn):
    while True:
        mensagem = conn.recv(1024).decode()
        if mensagem == "sair":
            conn.close()
            break
        print("Outro usuário:", mensagem)

def bate_papo():
    modo = input("Você deseja ser o servidor ou o cliente? (s/c)")
    if modo == 's':
        conn = iniciar_servidor()
        enviar_mensagem(conn)
        receber_mensagem(conn)
    elif modo == 'c':
        conn = iniciar_cliente()
        receber_mensagem(conn)
        enviar_mensagem(conn)

bate_papo()
