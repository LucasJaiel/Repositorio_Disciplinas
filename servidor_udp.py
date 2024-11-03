#!/usr/bin/python3

import socket

def start_udp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("0.0.0.0", 5001))
    print(f'[UDP] Servidor escutando na porta 5001.')
    
    while True:
        mensagem, addr = server.recvfrom(1024)
        print(f"[UDP] Mensagem recebida de {addr}: {mensagem.decode('utf-8')}")
        resposta = f"UDP: {mensagem.decode('utf-8')}"
        server.sendto(resposta.encode('utf-8'), addr)

if __name__ == "__main__":
    start_udp_server()
