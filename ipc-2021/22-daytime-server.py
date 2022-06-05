# /usr/bin/python
#-*- coding: utf-8-*-
#
# daytime-server.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket
from subprocess import Popen, PIPE
# ------------------------------------
HOST = ''
PORT = 50001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT)) # lliga ip/port
s.listen(1) # Escolta pel socket creat
conn, addr = s.accept() # Si entra una petició de conexió, guarda l'objecte conn i la IP
print("Connected by", addr) # Printa qui s'ha conectat
command = ["cat","prova.txt"]  # especifiquem el command que utiltizarem
pipeData = Popen(command,stdout=PIPE)   # Creem l'objecte popen amb l'ordre i diem que la sortida serà un pipe 
for line in pipeData.stdout:    # Per cada linea que retorni l'ordre del pipe..
  conn.send(line)   # envia-la
conn.close()    # Tanquem la connexió al acabr tot el que vomiti l'ordre

sys.exit(0)
