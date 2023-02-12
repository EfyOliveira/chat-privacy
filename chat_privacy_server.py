import socket

# Endereço IP e porta do servidor
HOST = '127.0.0.1'
PORT = 12345

# Cria o socket do servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liga o socket ao endereço IP e porta especificados
server.bind((HOST, PORT))

# Escuta por conexões
server.listen()

# Aceita uma conexão e retorna um novo socket e o endereço do cliente
conn, addr = server.accept()

while True:
    # Recebe uma mensagem do cliente
    message = conn.recv(1024).decode()

    # Verifica se a mensagem é "exit" para encerrar a conexão
    if message == 'exit':
        break

    # Imprime a mensagem
    print(f'Mensagem recebida do cliente: {message}')

    # Envia uma resposta para o cliente
    conn.sendall(b'Mensagem recebida com sucesso!')

# Fecha a conexão
conn.close()
