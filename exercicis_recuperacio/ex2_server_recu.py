# /usr/bin/python
#-*- coding: utf-8-*-
# ps-server.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket,os,signal,argparse,time
from subprocess import Popen, PIPE
# -------------------------------------
parser = argparse.ArgumentParser(description=\
        """nmap server""")

parser.add_argument("-p","--port", type=int, default=50001)

args=parser.parse_args()
# -------------------------------------
HOST = ''   # Definim com a HOST (localhost)
PORT = args.port    # Definim el PORT que l'agafarà per l'argument (parser)

# ---------------------------------------
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(1)

while True: # Bucle infinit (atendre connexions un darrera l'altre --> per cada connexió atén 1 client)
  conn, addr = s.accept()   # Guardem les variables conn i addr
  print("Connected by", addr)   # Printem
  nomFitxer = "/tmp/%s.log" % (addr[0])  # Nombrem el fitxer --> addr[1] : núm port
  fitxer = open(nomFitxer,"a")  # L'obrim
  while True:   # Bucle infinit
    data = conn.recv(1024)  # Límit de dades a rebre (llegim el socket)
    if not data:    # Si no hi ha dades, sortim (quan el client "penja")
        break
    fitxer.write(str(data)) # Escribim al fitxer
  fitxer.close()    # Tanquem el fitxer
  conn.close()  # Tanquem la connexió
