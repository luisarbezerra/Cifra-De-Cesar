import socket
import sys
import struct
import threading

class ServidorThread(object):
    def __init__(self, HOST, PORT):
        self.host = HOST
        self.port = PORT
        self.tcp  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcp.bind((self.host, self.port))

    def listen(self):
        self.tcp.listen(5)
        while True:
            client, address = self.tcp.accept()
            client.settimeout(15)
            threading.Thread(target = self.cifraDeCesar,args = (client,address)).start()

    def cifraDeCesar(self, client, address):
        while True:
            try:
                tamanho = client.recv(4)
                tamanho = struct.unpack('!i', tamanho)[0]
                palavra = client.recv(tamanho)
                palavra = palavra.decode()
                rotacao = client.recv(4)
                rotacao = struct.unpack('!i', rotacao)[0]

                mensagem_decodificada = []

                for c in palavra:
                    rotacao %= 26
                    tmp = (ord(c) - 97 - rotacao) % 26 + 97
                    mensagem_decodificada += chr(tmp if 97 <= tmp <= 122 else 96 + tmp % 122)
                
                mensagem_final = ''.join(mensagem_decodificada)
                if palavra:
                    # Set the response to echo back the recieved data
                    print(mensagem_final)
                    response = mensagem_final
                    client.send(response.encode('ASCII', 'ignore'))
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False

if __name__ == '__main__':
    while True:
        port_num = sys.argv[1]
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    ServidorThread('127.0.0.1',port_num).listen()
