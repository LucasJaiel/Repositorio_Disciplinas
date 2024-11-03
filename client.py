#!/usr/bin/python3

import socket

def tcp_client(mensagem):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 5000))
    client.send(mensagem.encode('utf-8'))
    resposta = client.recv(1024).decode('utf-8')
    client.close()
    print(f"Resposta do servidor: {resposta}")

def udp_client(mensagem):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(mensagem.encode('utf-8'), ("127.0.0.1", 5001))
    resposta, _ = client.recvfrom(1024)
    print(f"Resposta do servidor: {resposta.decode('utf-8')}")

if __name__ == "__main__":
    protocolo = input("Escolha o protocolo (TCP/UDP): ").strip().upper()
    mensagem = input("Digite a mensagem para o servidor: ").strip()

    if protocolo == "TCP":
        tcp_client(mensagem)
    elif protocolo == "UDP":
        udp_client(mensagem)

    else:
        print("Protocolo inválido. Escolha entre TCP ou UDP.")

