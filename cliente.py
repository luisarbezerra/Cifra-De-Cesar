import sys
import socket

HOST     = sys.argv[1]
PORT     = int(sys.argv[2])
palavra  = sys.argv[3]
chave    = sys.argv[4]
tcp      = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino  = (HOST, PORT)

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

tcp.connect(destino)
print('Para sair use CTRL+X\n')
msg = input()

while msg != '\x18':
    tcp.send(msg.encode('latin1'))
    msg = tcp.recv(1024).decode('latin1')
    print(msg)
    msg = input()

tcp.close()
