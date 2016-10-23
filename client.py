#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

# Constantes. Dirección IP del servidor y contenido a enviar

SERVER = sys.argv[1]
PORT = int(sys.argv[2])
LINE = ' '.join(sys.argv[3:])

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    print("Enviando:", LINE)
    if LINE[0:8] ==  "register":
        SIP_dir = LINE[8:]
        body_msg = "RESGISTER " + "sip:" + SIP_dir  #+ " SIP/2.0" 
        #No se como imprimir el \r\n\r porq lo ingora
        LINE = body_msg
        #print(LINE)
        #my_socket.send(bytes(body_msg)
        my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
        data = my_socket.recv(1024)
        print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
