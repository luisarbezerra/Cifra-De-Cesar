import socket

HOST   = '' # Endereco IP do Servidor
PORT   = 5000 # Porta que o Servidor esta
tcp    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
origem = (HOST, PORT)

tcp.bind(origem)
tcp.listen(1)
print('\nServidor TCP iniciado no IP', HOST, 'na porta', PORT)

conexao, cliente = tcp.accept()
print('Conectado por', cliente)

while True:
    mensagem = conexao.recv(1024)
    if not mensagem: 
        break
    msg = mensagem.decode()
    print(cliente, msg)
print('Finalizando conexao do cliente', cliente)
conexao.close()
