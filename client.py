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
    Words_LINE = LINE.split(" ")
    Register = Words_LINE[0]
    SIP_dir = Words_LINE[1]
    Expires = int(Words_LINE[2])
    if Register ==  "register":
       
        body_msg1 = "REGISTER " + "sip: " + SIP_dir + " " + " SIP/2.0\r\n" +  "Expires: " + str(Expires) +"\r\n"
        LINE = body_msg1
        print(LINE) 
        my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
        data = my_socket.recv(1024)
        print('Recibido -- ', data.decode('utf-8'))
print("Socket terminado.")
