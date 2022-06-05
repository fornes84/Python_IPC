# /usr/bin/python
#-*- coding: utf-8-*-
#
# 26-telnetServer.py [-p port] [-d debug]
#
#accepta la connexió
#while True:
#   recv * (s'hauria de fer un bucle recv)
#   Popen 
#   for line in Popen.stdout:
#       read (Popen)
#       send Popen
#   send (chr4) --> ascii 004
#   tanquem connexió
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# Genera un diàleg amb el client, on aquest l'indica una consulta a 
# realitzar i el servidor li retorna el resultat, quan el client envia un Enter
# el servidor tanca la connexió. El servidor escoltant a altres clients.
# Implementar un servidor i un client telnet. Client i server fan un diàleg.
# Cal un senyal de “yatà” Usem chr(4).
# Si s’indica debug el server generarà per stdout la traça de cada connexió.
# -------------------------------------
import sys, socket, os, argparse
from subprocess import Popen, PIPE
# -----------------------
# Validem els arguments
parser = argparse.ArgumentParser(description='Guarda ps ax a un fitxer')

parser.add_argument("-p", type=int, help="Port on escoltar",\
    default=51000, dest="port")

parser.add_argument("-d","--debug",action='store_true',default=False)

args = parser.parse_args()
# -----------------------
# Per totes les IP del meu host
HOST = ''
# Connexió tipus TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Reutilitza l'adreça encara que estigui bloquejada per alguna acció anterior
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Lliga la IP del meu host i el port
s.bind((HOST,args.port))
# Indica que s'ha de posar a escoltar, però continua
s.listen(1)
# Per cada client
while True:
	# Es posa a escoltar fins que es produeixi una connexió
	conn, addr = s.accept()	
	if args.debug:
		print ("Connected by: %s" %(addr[0]))
	while True: 
		# Rep la comanda que passa l'usuari
		cmd = conn.recv(1024)		
		if args.debug:
			print ("Comanda: %s" % (cmd))
		if not cmd:  # Si no rep més dades/comandes, li han penjat el telèfon, per tant tanca la connexió
			if args.debug:
				print ("La connexió amb %s ha tancat" % (addr[0]))
			conn.close()
			break		
		# Executa la comanda
		pipeData = Popen(cmd,shell=True, stdout=PIPE, stderr=PIPE) # EXECUTA AQUI (A SERVIDOR LA COMANDA)
		# Per cada resultat del PIPE.stdout, l'envia
		for line in pipeData.stdout:
			if args.debug:
				print ("Enviant: %s" %(line))
				conn.send(line)		
        # Per cada resultat del PIPE.stderr, l'envia
		for line in pipeData.stderr:
			if args.debug:
				print ("Enviant: %s" %(line))
			conn.send(line)		
		# Envia la senyal de final de comanda (man ascii -> 004)
		conn.send(b'\x04')		

sys.exit(0)  # AQUI NO ARRIBA MAI, DIRIA !!
