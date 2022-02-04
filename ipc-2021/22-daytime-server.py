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
s.bind((HOST,PORT))
s.listen(1) # Escolta
conn, addr = s.accept() # Accepta la connexió
print("Connected by", addr) # Rep la connexió
command = ["date"]  # Li especifiquem el command que utiltizarem
pipeData = Popen(command,stdout=PIPE)   # Executem el popen

for line in pipeData.stdout:    # Retornem les línees
  conn.send(line)   # Enviem la líena
conn.close()    # Tanquem la connexió

sys.exit(0)
