# /usr/bin/python
#-*- coding: utf-8-*-
#
# 26-telnetServer.py [-p port] [-d debug]
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# Genera un diàleg amb el client, on aquest l'indica una consulta a 
# realitzar i el servidor li retorna el resultat, quan el client envia un Enter
# el servidor tanca la connexió. El servidor escoltant a altres clients.
# Implementar un servidor i un client telnet. Client i server fan un diàleg.
# Cal un senyal de "finalitzat" Usem chr(4).
# Si s’indica debug el server genera per stdout la traça de cada connexió.
# -------------------------------------
import sys, socket, os, argparse
from subprocess import Popen, PIPE
# ---------------------------------
# Validem els arguments
parser = argparse.ArgumentParser(description='Enviar l\'status d\'un servei')

parser.add_argument("-p", type=int, help="Port on escoltar",\
     default=50001, dest="port")

parser.add_argument("-d","--debug",action='store_true',default=False)

args = parser.parse_args()
# ---------------------------------
# Especifiquem tots els hosts, el port per argument i el debug per argument
HOST = ''
PORT = args.port
DEBUG = args.debug
# Connexió tipus TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Reutilitza l'adreça encara que estigui bloquejada per alguna acció anterior
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Lliga la IP del meu host i el port
s.bind((HOST, PORT))
# Indica que s'ha de posar a escoltar, però continua
s.listen(1)
# ---------------------------------
# Per cada client
while True:
  conn, addr = s.accept()
  if DEBUG:
    print ("Connected by: %s" % (addr[0]))
  while True:
    data = conn.recv(1024)
    '''if DEBUG:
      print("La connexió amb %s ha tancat" % (addr[0]))
      conn.close()
      break'''
    data = data.decode()
    cmd = "systemctl show " + data
    pipeData = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    for line in pipeData.stdout:
      print(pipeData.stdout)
      if DEBUG:
        print ("Enviant... %s" % (line))
      conn.send(line)
    for line in pipeData.stderr:
      if DEBUG:
        print ("Enviant... %s" % (line))
      conn.send(line)
    conn.send(b'\x04')

sys.exit(0)
