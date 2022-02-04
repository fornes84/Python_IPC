# /usr/bin/python
#-*- coding: utf-8-*-
# cal-server-one2one-pissara.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket,os,signal,argparse,time
from subprocess import Popen, PIPE
# -------------------------------------
parser = argparse.ArgumentParser(description=\
        """ps-ax server""")

parser.add_argument("-p","--port", type=int, default=51000)

args=parser.parse_args()
# -------------------------------------
#llistaPeers=[]  # Definim la llista buida de les connexions
HOST = ''   # Definim com a HOST (localhost)
PORT = args.port    # Definim el PORT que l'agafarà per l'argument (parser)

def mysigusr1(signum,frame):    # Definim la funció del signal usr1 (kill -10)
  print("Signal handler called with signal:", signum)
  sys.exit(0)   # Pleguem
#  
def mysigusr2(signum,frame):    # Definim la funció del signal usr2 (kill -12)
  print("Signal handler called with signal:", signum)
  sys.exit(0)   # Pleguem
#
def mysigterm(signum,frame):    # Definim la funció del signal term (kill -15)
  print("Signal handler called with signal:", signum)
  sys.exit(0)   # Pleguem
# ---------------------------------------
pid=os.fork()

if pid != 0:    # Fem l'if en funció el PID al pare (ens dirà quin es el PID fill)
  print("Engegat el server ps:", pid)
  sys.exit(0)   # Programa 'pare' finalitzarà

# NOMÉS S'EXECUTARÀN AL PROGRAMA FILL JA QUE EL PROGRAMA PARE JA ES MORT!!!
signal.signal(signal.SIGUSR1,mysigusr1)
signal.signal(signal.SIGUSR2,mysigusr2)
signal.signal(signal.SIGTERM,mysigterm)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(1)

while True: # Bucle infinit (atendre connexions un darrera l'altre --> per cada connexió atén 1 client)
  conn, addr = s.accept()   # Guardem les variables conn i addr
  print("Connected by", addr)   # Printem
  nomFitxer = "/tmp/%s-%s-%s.log" % (addr[0], addr[1], time.strftime("%Y%m%d-%H%M%S"))  # Nombrem el fitxer --> addr[1] : núm port
  fitxer = open(nomFitxer,"w")  # L'obrim
  while True:   # Bucle infinit
    data = conn.recv(1024)  # Límit de dades a rebre (llegim el socket)
    if not data:    # Si no hi ha dades, sortim (quan el client "penja")
        break
    fitxer.write(str(data)) # Escribim al fitxer
  fitxer.close()    # Tanquem el fitxer
  conn.close()  # Tanquem la connexió
