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

parser.add_argument("-d","--database", help="base de dades a usar",\
     default="training")

parser.add_argument('-c', "--client", help='client', type=str,\
     action="append", dest="clieList", required="True")

args = parser.parse_args()
#----------------------------------------------------------
cmd = "psql -qtA -F',' -h 172.17.0.2 -U postgres " + args.database
pipeData = Popen(cmd, shell = True, bufsize=0, universal_newlines=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)   # shell = True --> el shell que és fa servir és /bin/sh, bufsize=0 --> sense buffer (no posi en memoria res, tot en directe), universal_newlines=True --> retorna string (text), stdin=PIPE --> write, stdout i stderr=PIPE read.

for num_clie in args.clieList:  # Recorrem els clients i comparem si estàn dins de la BBDD
   sentencia = "select * from clientes where num_clie = %s;" % (num_clie)     # Li donem el valor de la sentència
   pipeData.stdin.write(sentencia+"\n")     # Prenem enter per executar la sentència
   print(pipeData.stdout.readline(), end="")        # Llegim 1 línea ja que la sentència retorna només 1 línea i mostrem.

pipeData.stdin.write("\q\n")    # Sortim del postgres (és necessari ja que no sabem si l'usuari posarà algun que no existeixi o algun que hi hagin N clients que ens ha de retornar!!!!!)
exit(0)
