# /usr/bin/python
#-*- coding: utf-8-*-
# prog [-d|--debug] [-p|--port]
#------------------------------
# ASIX M06 Curs 2021-2022 Examen 2019 processos python
# serverbasic.py
# Enunciat:

#---------------------------------

# EXERCICI 2

#---------------------------------
import sys,socket,os,signal,argparse
from subprocess import Popen, PIPE
#-------------------------------
parser = argparse.ArgumentParser(description="""Server01 Exàmen""")
# ULL L'ORDRE !! python3 -d examen.py SI,   pyton3 examen.py -d NO COLA !!!
parser.add_argument("-d","--debug",type=str, help="Descrivim tot el que està passant")
parser.add_argument("-p","--port",type=int,default=55555)
args=parser.parse_args()
#--------------------------------
llistaPeers=[]  # llista de conexions (per ara cap)
HOST = ''
PORT = args.port
def mysigusr1(signum,frame):  # 10) SIGUSR1 
  print("Signal handler called with signal:", signum)
  print(llistaPeers)
  sys.exit(0) # pleguem
def mysigusr2(signum,frame):  # 12) SIGUSR2
  print("Signal handler called with signal:", signum)
  print(len(llistaPeers))
  sys.exit(0) # pelguem
def mysigterm(signum,frame):  #15) SIGTERM
  print("Signal handler called with signal:", signum)
  print(llistaPeers, len(llistaPeers))
  sys.exit(0) # pelguem  
#------------------------------------------------------------
pid = os.fork()
if pid !=0:
    if args.debug:
        print("Server Engegat:", pid)
    sys.exit(0)  # mor el procés pare i ens quedem amb el fill que és un dimoni en 2n pla
signal.signal(signal.SIGUSR1,mysigusr1)
signal.signal(signal.SIGUSR2,mysigusr2)
signal.signal(signal.SIGTERM,mysigterm)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.bind((HOST, PORT))
s.listen(1)
print(os.getpid()) 

while True:         # One by One 
    conn, addr = s.accept() # rebem una petició de conexió
    llistaPeers.append(addr) # guardem IP a llistaPeers per printar després
    if args.debug: # si esta el debug, printem per pantalla
        print("Connectat el host:", addr)
        
    nomFitxer = "/tmp/%s-%s-%s.log" % (addr[0], addr[1], time.strftime("%Y%m%d-%H%M%S"))  # Nombrem el fitxer --> addr[1] : núm port
    fitxer = open(nomFitxer,"w")  # L'obrim
    
    while True: # el client por fer tantes consultes/transmissions com vulgui
        dades = conn.recv(1024)
        if dades == b'x04':  # si arriba el x04 ja s'ha acabat el que voliar dir
            break # no tanquem conexió pero atenem a altres clients	
           
    