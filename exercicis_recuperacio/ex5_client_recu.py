# /usr/bin/python
#-*- coding: utf-8-*-
#
# 26-telnet-client.py -p port -s server
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# Genera un diàleg amb el servidor, on el client li indica una consulta a 
# realitzar i aquest li retorna el resultat, quan el client envia un Enter
# el servidor tanca la connexió.
# -------------------------------------
import argparse, sys, socket
from subprocess import Popen, PIPE
# -------------------------------------
# Validem els arguments
parser = argparse.ArgumentParser(description='Consulta el status d\'un servei')

parser.add_argument("-p", help='Port on realitzar la consulta',type=int,\
     dest="port", required=True)

parser.add_argument("server", type=str, help="Servidor on realitzar la consulta")

args = parser.parse_args()
# -------------------------------------
HOST = args.server
PORT = args.port

# Crea el SOCKET TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Es connecta al HOST i al PORT, és l'antònim del accept
s.connect((HOST, PORT))
# -------------------------------------
# Fins que no li pengin el telèfon
while True:
  cmd = input("indica_servei>")
  if cmd == '':
    s.close()
    break
  else:
    cmd = cmd.encode()
    s.send(cmd)
    while True:
        data = s.recv(1024)
        data = data.decode()
        print(data)
        if data[-1:] == b'\x04':
          s.close()
          break
print("Exit")

sys.exit(0)
