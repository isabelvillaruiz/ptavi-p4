#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import json
import time 
 
''' NOTAS '''  
'''
# self.wfile.write(b"SIP/2.0 200 OK") #SIRVE PARA ESCRIBIR UN MENSAJE EN EL CLIENTE 
Hay que conseguir que en caso de que sea 0 y este guardada esa direccion que nos la borre 
separators=('' , ': ')     
'''



class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    dicc = {}
 

    def register2json (self):
        json_file = open("registered.json","w")
        json.dump(self.dicc,json_file, indent = 4)
        json_file.close()

    def json2registered(self):

        try:
            print("Estamos probando")
            with open("registered.json") as JsonFile:
                self.dicc = json.load(JsonFile)
        except: 
                pass

    def handle(self):
        self.wfile.write(b"Hemos recibido tu peticion")
        self.json2registered()
        print(self.client_address)
        

        texto = self.rfile.read()
        print("El cliente nos manda ", texto.decode('utf-8'))
        LINE_S = texto.decode('utf-8')
        print(LINE_S)
        Words_LINES_S = LINE_S.split() 
             
        dir_sip = Words_LINES_S[2]
        Expires = int(Words_LINES_S[5])
        
        actual_time = time.time()
        expire_time = actual_time + Expires
        str_actual_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(actual_time))
        str_expire_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(expire_time))
        
        
        if (Expires) != 0:
            
            self.dicc[dir_sip] = [self.client_address[0], str_expire_time]
           
            
            
            
                #print(self.client_address)
                #print(self.client_address[0])
                #print(self.client_address[1])
                #Prueba de que son lo que son [Logico]
            print(self.dicc) #prueba de que guarda bien en el diccionario
            print()
            print("SIP/2.0 200 OK")

        

        elif (Expires) == 0 :
            if dir_sip in self.dicc:
                del self.dicc[dir_sip]
         
            self.register2json()
            print(self.dicc) #prueba de que guarda bien en el diccionario
            print()
            print("SIP/2.0 200 OK") 
            
        

    
if __name__ == "__main__":
    serv = socketserver.UDPServer(('', int(sys.argv[1])), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
