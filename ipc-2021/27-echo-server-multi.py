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
conns=[s]
while True:
    actius,x,y = select.select(conns,[],[])
    for actual in actius:
        if actual == s:
            conn, addr = s.accept()
            print('Connected by', addr)
            conns.append(conn)
        else:
            data = actual.recv(1024)
            if not data:
                sys.stdout.write("Client finalitzat: %s \n" % (actual))
                actual.close()
                conns.remove(actual)
            else:
                actual.sendall(data)
                #actual.sendall(chr(4),socket.MSG_DONTWAIT)
s.close()
sys.exit(0)


