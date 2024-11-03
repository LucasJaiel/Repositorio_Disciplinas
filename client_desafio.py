#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket

def tcp_client(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_sock:
        tcp_sock.connect(("localhost", 5000))
        tcp_sock.sendall(message.encode())
        response = tcp_sock.recv(1024).decode()
        print(f"Resposta do servidor (TCP): {response}")

def udp_client(message):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_sock:
        udp_sock.sendto(message.encode(), ("localhost", 5001))
        response, _ = udp_sock.recvfrom(1024)
        print(f"Resposta do servidor (UDP): {response.decode()}")

def main():
    while True:
        protocol = input("Escolha o protocolo (TCP/UDP ou 'sair' para encerrar): ").strip().lower()
        if protocol == 'sair':
            break
        
        message = input("Digite a mensagem a ser enviada: ")
        
        if protocol == 'tcp':
            tcp_client(message)
        elif protocol == 'udp':
            udp_client(message)
        else:
            print("Protocolo inválido! Escolha TCP ou UDP.")

if __name__ == "__main__":
    main()
