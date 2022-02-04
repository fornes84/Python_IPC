# /usr/bin/python3
#-*- coding: utf-8-*-
#
# exemple-fork.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,os

print("Hola, començament del programa principal")
print("PID pare: ", os.getpid())

pid=os.fork()   # El programa és divideix i passen a haver-hi 2 programes
                # 'os.fork()' retorna 2 processos, el pare i el fill.
if pid != 0:
  os.wait() # El procés pare espera a que finalitzi el fill per mostrar el seu PID.
  print("Programa Pare", os.getpid(), pid)  # És diferent a 0 perquè és el pare. 
else:
  print("Programa fill", os.getpid(), pid)  # 'os.getpid()' li dona valor al PID de fill.                                                              És 0 perquè el 'os.fork()' retorna 0.
  #while True:   # Si fem 'pgreep python', el fill segueix executant-se (bucle infinit) en bg com a dimoni
      #pass

print("Hasta lugo lucas!")

sys.exit(0)
