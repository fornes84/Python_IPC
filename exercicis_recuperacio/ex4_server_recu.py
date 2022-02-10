# /usr/bin/python
#-*- coding: utf-8-*-
# cal-server-one2one-pissara.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket,os,signal,argparse
from subprocess import Popen, PIPE
# -------------------------------------
parser = argparse.ArgumentParser(description=\
        """Server""")

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

while True: # Bucle infinit (atendre connexions un darrera l'altre)
  conn, addr = s.accept()   # Guardem les variables conn i addr
  print("Connected by", addr)   # Printem
  command = "ls"
  pipeData = Popen(command,stdout=PIPE)
  for line in pipeData.stdout: # Per cada línea
      conn.send(line)
  conn.close()
