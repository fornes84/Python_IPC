# /usr/bin/python
#-*- coding: utf-8-*-
'''EXAMEN 02: Processos: Volem fer un servidor que rebi fitxers enviats des d'un
programa client i els guardi en el disc. El servidor acceptarà la connexió d'un sol
client al mateix temps, després d'atendre'l acceptarà la connexió d'un altre i així
succesivament fins que rebi un senyal per a finalitzar.Per simplificar només es
transmetran fitxers de text. Servidor: prog_servidor Client: prog_cliente -H
adreça_servidor -p port_servidor -f fitxer1 -f fitxer2 ...
'''
# -------------------------------------
#
# Gener 2022
# -------------------------------------
import sys,socket,os,signal,argparse,time
from subprocess import Popen, PIPE
# -------------------------------------

PORT = 51000
HOST = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(1)

def mysigusr1(signum,frame):    # Definim la funció del signal term (kill -15)
  print("Signal handler called with signal:", signum)
  # aqui hem penso que hauriem d'anar plegant la conexió
  sys.exit(0)   # Pleguem
# ---------------------------------------
pid=os.fork()

if pid != 0:    # Fem l'if en funció el PID al pare (ens dirà quin es el PID fill)
  print("Engegat el server :", pid)
  sys.exit(0)   # Programa 'pare' finalitzarà

# NOMÉS S'EXECUTARÀN AL PROGRAMA FILL JA QUE EL PROGRAMA PARE JA ES MORT!!!
signal.signal(signal.SIGUSR1,mysigusr1)

while True:

    conn, addr = s.accept()   # Guardem les variables conn i addr
    print("Connected by", addr)   # Printem


sys.exit(0)
