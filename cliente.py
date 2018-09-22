import sys
import socket
import struct
import time

HOST    = sys.argv[1]
PORT    = int(sys.argv[2])
palavra = sys.argv[3]
tamanho = len(palavra)
rotacao = int(sys.argv[4])
tcp     = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (HOST, PORT)

mensagem_codificada = []

for c in palavra:
    rotacao %= 25
    tmp = (ord(c) - 97 + rotacao) % 26 + 97
    mensagem_codificada += chr(tmp if 97 <= tmp <= 122 else 96 + tmp % 122)

mensagem = ''.join(mensagem_codificada)
tcp.connect(destino)
tcp.send(struct.pack('!i', tamanho))
tcp.send(mensagem.encode('ASCII', 'ignore'))
tcp.send(struct.pack('!i', rotacao))

palavra_decodificada = tcp.recv(tamanho)
print(palavra_decodificada.decode())
tcp.close()
