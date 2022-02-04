# /usr/bin/python3
#-*- coding: utf-8-*-
#
# exemple-popen.py ruta
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys, argparse
from subprocess import Popen, PIPE

parser = argparse.ArgumentParser(description=\
        """Exemple popen""")

parser.add_argument("ruta",type=str,\
        help="directori a llistar")

args=parser.parse_args()
#---------------------------------------------
command= " psql -qtA -F',' -h 172.17.0.2 -U postgres training -c \"select * from clientes; \""
pipeData = Popen(command,shell=True,stdout=PIPE)

for line in pipeData.stdout:
    print(line.decode("utf-8"),end="")

exit(0)
