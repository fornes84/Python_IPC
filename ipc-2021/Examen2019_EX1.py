# /usr/bin/python
#-*- coding: utf-8-*-
# prog [-d|--debug] [-p|--port]
#------------------------------
# ASIX M06 Curs 2021-2022 Examen 2019 processos python
# serverbasic.py
# Enunciat:

#---------------------------------

# EXERCICI 1

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
    command = "ps -ax"
    pipeData = Popen(command,shell=True,stdout=PIPE,stderr=PIPE)
    
    for line in pipeData.stderr:
        conn.send(line)
    for line in pipeData.stdout:  # L'enunciat no especifica si cal enviar els errors..
        conn.send(line)
    #conn.send(b'\x04')	# pendent veure si es necesari tenint telnet com a client --> no cal
    conn.close() # hem dit que el client només pot fer 1 petició i DEU !
   