# /usr/bin/python3
#-*- coding: utf-8-*-
#
# exemple-fork.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,os, signal

#----------------------------------------------------
def mysigusr1(signum,frame):
  print("Signal handler called with signal:", signum)
  print("Hola radiola")
#
def mysigusr2(signum,frame):
  print("Signal handler called with signal:", signum)
  print("Adeu andreu!")
  sys.exit(0)
    
#----------------------------------------------------
print("Hola, començament del programa principal")
print("PID pare: ", os.getpid())

pid = os.fork()
if pid != 0:    # Quan el PID es diferent a 0, el pare s'executa i finalitza
  print("Programa Pare", os.getpid(), pid)
  print("Hasta lugo lucas!")
  sys.exit(0)
  
print("Programa fill", os.getpid(), pid)    # El fill és queda executant-se.
signal.signal(signal.SIGUSR1,mysigusr1) # Li passem el signal 10 per mostrar 'Hola radiola'
signal.signal(signal.SIGUSR2,mysigusr2) # Li passem el signal 12 per mostrar 'Adeu andreu' i finalitzar
#----------------------------------------------------
while True:
  pass
