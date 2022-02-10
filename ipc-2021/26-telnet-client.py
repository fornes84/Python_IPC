# /usr/bin/python
#-*- coding: utf-8-*-
#
# 26-telnet-client.py -p port -s server
#
#while True: (Bucle per fer ordres)
#   input (ordre)
#   si ordre = exit:    # El client tanca la connexió
#       break
#   send(ordre)
#   while True:
#       reciv
#       print
#       sortim quan les dades diguin ja està (end of transmission (ascii 004)
#tanquem connexió
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
#
# Genera un diàleg amb el servidor, on el client li indica una consulta a 
# realitzar i aquest li retorna el resultat, quan el client envia un Enter
# el servidor tanca la connexió.
# -------------------------------------
import argparse, sys, socket
from subprocess import Popen, PIPE
# -------------------------------------------------
# Validem els arguments
parser = argparse.ArgumentParser(description='Consulta el calendari ai un servidor')

parser.add_argument("-p", help='Port on realitzar la consulta',type=int,\
     dest="port", required=False, default="51000")

parser.add_argument("-s", type=str, help="Servidor on realitzar la consulta",\
     dest="server", required=False, default="localhost")

args = parser.parse_args()
# -------------------------------------------------
# Crea el SOCKET TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Es connecta al HOST i al PORT, és l'antònim del accept
s.connect((args.server, args.port))
# -------------------------------------------------
# Fins que no li pengin el telèfon
while True:
	# Envia l'ordre a executar, si és un enter, tanca la connexió
	cmd = input("telnet2>")
	if cmd == '':
		s.close()
		break
	else:
		cmd = cmd.encode()
		s.send(cmd)
	while True:
		# Val les dades o val 'None'
		data = s.recv(2)
		# Mostra les dades
		print (str(data))
		# Si rep la senyal de final, surt (man ascii -> 004)
		if data[-1:] == b'\x04':
			break
print ("Exit")

sys.exit(0)
