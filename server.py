#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
          

class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        self.wfile.write(b"Hemos recibido tu peticion")
        print(self.client_address)
        dicc = {}
        for line in self.rfile:
            print("El cliente nos manda ", line.decode('utf-8'))
            #if line.decode('utf-8')[0:8] == 'REGISTER ':
            dir_sip = line.decode('utf-8')[15:]
            print (dir_sip)
            dicc = { self.client_address[0] : dir_sip }    
                #print(self.client_address)
                #print(self.client_address[0])
                #print(self.client_address[1])
                #Prueba de que son lo que son
            print(dicc) #prueba de que guarda bien en el diccionario
            print("SIP/2.0 200 OK")
            #self.wfile.write(b"SIP/2.0 200 OK") #SIRVE PARA ESCRIBIR UN MENSAJE EN EL CLIENTE
                
if __name__ == "__main__":
    serv = socketserver.UDPServer(('', int(sys.argv[1])), SIPRegisterHandler)
    
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
