# /usr/bin/python
#-*- coding: utf-8-*-
#
# exemple-execv.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,os
# ------------------------------------------------
print("Hola, començament del programa principal")
print("PID pare: ", os.getpid())

pid=os.fork()
if pid !=0:
  print("Programa Pare", os.getpid(), pid)
  sys.exit(0)

#-------------------------------------------------
print("Programa fill", os.getpid(), pid)
os.execv("/usr/bin/python3", ["/usr/bin/python3", "16-signal.py", "60"])    # Li passem els següents paràmetres perquè executi el programa 16 amb 60 segons.
#-------------------------------------------------
print("Hasta lugo lucas!")   # Mai és veurà!!!!!
sys.exit(0)
