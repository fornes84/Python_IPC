# /usr/bin/python
#-*- coding: utf-8-*-
'''
Enunciat del problema
Volem crear un servidor de ftp trivial. Haurem de crear, també, un client per comprovar que el
servidor funciona correctament.
Requeriments per al servidor:

● Se li passa com a argument (​ p n) el número de port que ha d'escoltar.
● Admet un sol client a l'hora.
● Accepta les següents ordres del client:
○ ls [path]. Retorna al client el llistat de fitxers del directori actiu.
○ get [path]nom_fitxer. Retorna al client el contingut de nom_fitxer.

● Quan el client acaba, el servidor es queda esperant una altra connexió.
● Acaba ordenadament quan rep un SIGTERM.
Requeriments per al client (mode interactiu):
● Se li passen com a arguments opcionals el host (​ H a.b.c.d) i el port (​ p n) amb qui s'ha de
connectar. Si es donen els dos arguments fa la connexió immediatament.
● Admet ordres de l'usuari per l'stdin:
○ connect host:port. Permès només si encara no ha fet la connexió.
○ ls [path]. Li envia l'ordre al servidor i espera un llistat de fitxers que mostra per
stdout.
○ get [path]nom_fitxer. Li envia l'ordre al servidor i espera una seqüència de bytes que
grava en el directori actiu amb el nom indicat.
○ quit. Tanca la connexió amb el servidor i acaba.
● Cada vegada que el programa espera alguna cosa de l'usuari li escriu un prompt
(client_ftp_trivial>)
'''
# -------------------------------------
#
# Gener 2022
# -------------------------------------
import sys,socket,os,signal,argparse,time
from subprocess import Popen, PIPE
# -------------------------------------
parser = argparse.ArgumentParser(description=\
        """ps-ax server""")
parser.add_argument("-p","--port", type=int, default=51000)
parser.add_argument("-H","--server", type=str, default="localhost")
parser.add_argument("-f","--fitxer", type=str, default="carta.txt")

args=parser.parse_args()
PORT = args.port
HOST=args.server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


data = Popen(command,shell=True,stdout=PIPE)
s.send(data)
sys.exit(0)
