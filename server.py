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
            if line.decode('utf-8')[0:8] == 'REGISTER':
                dicc = { self.client_address[0] : self.client_address[1] }                 
                #print(self.client_address)
                #print(self.client_address[0])
                #print(self.client_address[1])
                #Prueba de que son lo que son
                print(dicc) #prueba de que guarda bien en el diccionario
                #self.wfile.write(b"Lo que sea") SIRVE PARA ESCRIBIR UN MENSAJE EN EL CLIENTE
                
                '''
                LO QUE HAY QUE HACER A CONTINUACION ES QUE EL CLIENTE VA A ENVIAR UNA PETICION CON
                UNA DIRECCION DE "CORREO" TENEMOS QUE GUARDAR EN NUESTRO DICCIONARIO LA DIRECCION JUNTO
                A LA IP NO CON EL PUERTO ESO HAY QUE QUITARLO DE MANERA QUE CUANDO LO GUARDE EN EL CLIENTE LE LLEGUE
                EL 200 OK QUE HEMOS APRENDIDO A IMPRIMIR
                '''

					
				
if __name__ == "__main__":
    serv = socketserver.UDPServer(('', int(sys.argv[1])), SIPRegisterHandler)
    
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
