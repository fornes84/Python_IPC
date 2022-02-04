# /usr/bin/pyhton3
#-*-coding: utf-8-*-
#
# 13-sql-injectat.py
#
# usage: python3 13-sql-injectat.py "select * from oficinas"
# ------------------------------------------------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# ------------------------------------------------------------------------------
import sys,argparse
from subprocess import Popen, PIPE

parser = argparse.ArgumentParser(description=\
        """Consulta a la base de dades entrada per argument al prigrama.""")

parser.add_argument("cons",type=str,\
        help="consulta a la base de dades training")

args=parser.parse_args()
# ------------------------------------------------------------------------------
command = [f"psql -qtA -F',' -h 172.17.0.2 -U postgres training -c \"{args.cons}\""]    # On està la variable, pot fer més coses que una sentència, per exempel, DROP DATABASE ... CONCLUSIÓ: ERROR DE SEGURETAT BRUTAL!
pipeData = Popen(command, stdout=PIPE, shell=True)

for line in pipeData.stdout:
    print(line.decode("utf-8")[:-1])

exit(0)
