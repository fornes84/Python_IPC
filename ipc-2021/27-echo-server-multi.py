#!/usr/bin/python
#-*- coding: utf-8-*-
'''
# -----------------------------------------------------------------
# Escola del treball de Barcelona
# ASIX Hisi2 M06-ASO UF2NF1-Scripts
# @edt Curs 2021-2022
# Gener 2022
# Echo server multiple-connexions
# -----------------------------------------------------------------
'''
import socket, sys, select, os
HOST = ''                 
PORT = 50007             
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print(os.getpid())
conns=[s] # afegim sempre el socket que escolta, el 1er
while True: # forevver
    actius,x,y = select.select(conns,[],[]) # nomes interesa actius (es una llista)
    for actual in actius: # cada cop que entra una conexió aquesta val s
        if actual == s:   # CLAU:
            conn, addr = s.accept() # TIPIC D?ACEPTAR UNA CONX ENTRANT
            print('Connected by', addr)
            conns.append(conn) # la conexió actual l'afegim a conns
        else: # SI LA CONEX JA EXISTEIX, ESCOLTA DADES
            data = actual.recv(1024)
            if not data:
                sys.stdout.write("Client finalitzat: %s \n" % (actual))
                actual.close()
                conns.remove(actual)
            else:
                actual.sendall(data) #  
                #actual.sendall(b'chr(4)',socket.MSG_DONTWAIT)

s.close()# TANCA SOCKET
sys.exit(0) #FI PROGRAMA


