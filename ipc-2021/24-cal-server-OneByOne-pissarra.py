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
        """CAL server""")

parser.add_argument("-a","--any", type=int, default=2022)

parser.add_argument("-p","--port", type=int, default=50001)

args=parser.parse_args()
# -------------------------------------
llistaPeers=[]  # Definim la llista buida de les connexions
HOST = ''   # Definim com a HOST (localhost)
PORT = args.port    # Definim el PORT que l'agafarà per l'argument (parser)
ANY = args.any  # Definim ANY que a l'igual que PORT, ho agafarà per (parser)

def mysigusr1(signum,frame):    # Definim la funció del signal usr1 (kill -10)
  print("Signal handler called with signal:", signum)
  print(llistaPeers)    # Llistem la llista de connexions actuals
  sys.exit(0)   # Pleguem
#  
def mysigusr2(signum,frame):    # Definim la funció del signal usr2 (kill -12)
  print("Signal handler called with signal:", signum)
  print(len(llistaPeers))   # Printem el len (quantitat) de la llista de connexions
  sys.exit(0)   # Pleguem
#
def mysigterm(signum,frame):    # Definim la funció del signal term (kill -15)
  print("Signal handler called with signal:", signum)
  print(llistaPeers, len(llistaPeers))  # Mostrem una llista amb les connexions i el len() de totes les connexions que han hagut
  sys.exit(0)   # Pleguem
# ---------------------------------------
pid=os.fork()  # creem un procés fill amb PID=0 que herada tot lo del pare, i aquí tenim para amb PID=XXX i fill amb PID=0

# pq fem això ?? pq el procés fill es converteix en un diomoni que treballa en 2n pla i que espera signals u ordre per fer coses !!

if pid != 0:    # El procés pare es qui entra aquí
  print("Engegat el server CAL:", pid) # pid retornarà XXXXXX
  sys.exit(0)   # el procés 'pare' finalitza/mor, i el PID del fill passa a ser el del pare + 1

# NOMÉS S'EXECUTARÀN AL PROGRAMA FILL JA QUE EL PROGRAMA PARE JA ES MORT!!!

signal.signal(signal.SIGUSR1,mysigusr1) # Vinculem a les senyals a les funcions que han de cridar !
signal.signal(signal.SIGUSR2,mysigusr2)
signal.signal(signal.SIGTERM,mysigterm)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(1) #ESPEREM TRUCADES

while True: # Bucle infinit (atendre connexions un darrera l'altre)
  conn, addr = s.accept()   # Guardem les variables conn i addr si entra una petició de conexió d'un client !
  print("Connected by", addr)   # Printem
  llistaPeers.append(addr)  # Afegim l'adreça la llista de connexions
  command = "cal %d" %(ANY)    # Especifiquem la commanda que s'executarà (%d (integer), %s (string)--> any pasat per argument)
  pipeData = Popen(command,shell=True,stdout=PIPE)  # Popen (shell=True --> es perquè funcioni l'ordre UNIX)
  for line in pipeData.stdout: # Per cada línea
    conn.send(line)
  conn.close()

# -------------------------------------
# PROVES:
# python3 24-cal-server-OneByOne-pissarra.py (SERVER)
# telnet localhost 50001 (client)
