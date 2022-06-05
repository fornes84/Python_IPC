# /usr/bin/python
#-*- coding: utf-8-*-
#
# daytime-client.py  
# Fem una connexió amb el servidor, i ell quan vegi una connexió ens vomitarà informació.
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys,socket
# -------------------------------------
HOST = ''
PORT = 50001
#PORT = 13
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # contruim objetce socket TCP en local
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # permet reutilitzar IPs
s.connect((HOST, PORT))

while True: # Bucle perquè no sabem quan acabarà la transm de dades que enviarà el servidor
  data = s.recv(1024)   # en paquets de fins a 1024
  if not data: # SI SERVER HA FINALITZAT ..
      break # para d'escoltar/rebre, sortint del while
  print('Data:', repr(data)) #vomita per pantalla fins a 1024 chars per linea (repr es pq es representi en humà)
s.close()

sys.exit(0)
