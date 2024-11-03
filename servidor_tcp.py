#!/usr/bin/python3
import socket
from threading import Thread

def manusear_client(conn,addr):
    print(f'[TCP] Conexão com {addr} estabelecida.')
    mensagem = conn.recv(1024).decode('utf-8')
    print(f'[TCP] Mensagem recebida de {addr}: {mensagem}')
    resposta = f'TCP: {mensagem}'
    conn.send(resposta.encode('utf-8'))
    conn.close
    print(f'[TCP] Conexão com {addr} encerrada.')
    
def start_tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5000))
    server.listen(5)
    print(f'[TCP] Servidor escutando na porta 5000.')
    
    while True:
        conn,addr = server.accept()
        thread = Thread(target=manusear_client, args=(conn, addr))
        thread.start()
if __name__ == "__main__":
    start_tcp_server()

