# Projeto Cliente/Servidor com Sockets TCP e UDP

Este projeto implementa uma aplicação cliente/servidor em Python que utiliza sockets TCP e UDP para comunicação. O objetivo é compreender as diferenças entre os dois protocolos de transporte.

## Estrutura do Projeto

O projeto consiste nos seguintes arquivos:

- `servidor.py`: Contém a implementação do servidor que escuta por conexões TCP e UDP.
- `cliente.py`: Contém a implementação do cliente que se comunica com o servidor.

## Funcionalidades

### Servidor

- Escuta na porta 5000 para conexões TCP.
- Escuta na porta 5001 para conexões UDP.
- Para cada conexão TCP, cria uma nova thread para atender ao cliente, devolvendo a mensagem recebida com o prefixo "TCP:".
- Para conexões UDP, processa as mensagens e responde com o prefixo "UDP:".

### Cliente

- Permite ao usuário escolher entre os protocolos TCP ou UDP.
- Solicita uma mensagem do usuário para enviar ao servidor.
- Exibe a resposta recebida do servidor.

## Requisitos

- Python 3.x instalado.
- Bibliotecas padrão de Python (não é necessário instalar bibliotecas adicionais).

## Instruções de Uso

### 1. Executando o Servidor

Para iniciar o servidor, siga estas etapas:

1. Abra um terminal e navegue até o diretório onde os arquivos estão localizados.
2. Execute o seguinte comando:

   ```bash
   python3 servidor.py