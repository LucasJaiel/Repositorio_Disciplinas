#!/usr/bin/python3
#-*- coding: utf-8 -*-

import socket
import threading

# Definindo as portas para TCP e UDP
TCP_PORT = 5000
UDP_PORT = 5001
BUFFER_SIZE = 1024

def handle_tcp_connection(conn, addr):
    try:
        print(f"[TCP] Conexão estabelecida com {addr}")
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            response = f"TCP: {data.decode()}"
            conn.send(response.encode())
        print(f"[TCP] Conexão encerrada com {addr}")
    finally:
        conn.close()

def tcp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_sock:
        tcp_sock.bind(("", TCP_PORT))
        tcp_sock.listen()
        print(f"[TCP] Servidor escutando na porta {TCP_PORT}")
        while True:
            conn, addr = tcp_sock.accept()
            # Cria uma nova thread para cada conexão TCP
            thread = threading.Thread(target=handle_tcp_connection, args=(conn, addr))
            thread.start()

def udp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_sock:
        udp_sock.bind(("", UDP_PORT))
        print(f"[UDP] Servidor escutando na porta {UDP_PORT}")
        while True:
            data, addr = udp_sock.recvfrom(BUFFER_SIZE)
            print(f"[UDP] Mensagem recebida de {addr}: {data.decode()}")
            response = f"UDP: {data.decode()}"
            udp_sock.sendto(response.encode(), addr)

def main():
    tcp_thread = threading.Thread(target=tcp_server)
    udp_thread = threading.Thread(target=udp_server)
    
    
    tcp_thread.start()
    udp_thread.start()
    
    tcp_thread.join()
    udp_thread.join()

if __name__ == "__main__":
    main()
