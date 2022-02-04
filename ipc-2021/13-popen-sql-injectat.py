# /usr/bin/python
#-*- coding: utf-8-*-
#
# popen-sql.py
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 20202
# -------------------------------------
# Utilitza el docker edtasixm06/postgres
# -----------------------------------------
#commandLocal = "psql -qtA -F ';' lab_clinic -c 'select * from pacients;'"
#commandRemote = "psql -qtA -h i11 -U postgres -F ';' lab_clinic -c 'select * from pacients;'"
# -------------------------------------------
import sys
from subprocess import Popen, PIPE
import argparse

parser = argparse.ArgumentParser(description='Consulta SQL interactiva')

parser.add_argument('sqlStatment', help='Sentència SQL a executar', metavar='sentènciaSQL')

args = parser.parse_args()
#----------------------------------------------------------
cmd = "psql -qtA -F',' -h 172.17.0.2 -U postgres training"
pipeData = Popen(cmd, shell = True, bufsize=0, universal_newlines=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)   # shell = True --> el shell que és fa servir és /bin/sh, bufsize=0 --> sense buffer (no posi en memoria res, tot en directe), universal_newlines=True --> retorna string (text), stdin=PIPE --> write, stdout i stderr=PIPE read.
pipeData.stdin.write("select * from oficinas;\n\q\n")   # El primer '\n' fa un enter per executar la sentència, '\q' surt del fitxer, i el segon '\n', confirma el '\q' per sortir.

for line in pipeData.stdout:
  print(line, end="")

exit(0)
