# /usr/bin/python3
#-*- coding: utf-8-*-
# ps-client.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket,argparse
from subprocess import Popen,PIPE
# -------------------------------------
parser = argparse.ArgumentParser(description=\
        """ps-ax client""")

parser.add_argument("-p","--port", type=int, default=51000)

parser.add_argument("server", type=str, default='')

args=parser.parse_args()
# -------------------------------------
HOST = args.server
PORT = args.port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

command = "ps -ax"    # Especifiquem la commanda que s'executarà (%d (integer), %s (string)--> any passat per argument)
pipeData = Popen(command,shell=True,stdout=PIPE)  # Popen (shell=True --> es perquè funcioni)

for line in pipeData.stdout: # Per cada línea
    s.send(line)    # Enviem per el socket les linees
s.close()   # Tanquem el socket (connexió)

sys.exit(0)
