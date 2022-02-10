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
print("PID proces actual: ", os.getpid())

pid=os.fork()   # El programa és divideix i passen a haver-hi 2 programes
                # 'os.fork()' retorna 2 processos, el pare i el fill.

# A PARTIR D?AQUI TENIM 2 PROCESOS QUE CONTINUEN CAP ABALL. NO SABEM QUIN ANIRA MES RAPID
# quan mor el fill, el pare passa a tenir ?¿?
# I UN SEMPRE RETORNA pid=0 (fill) i l'altre (pare) retoran sempre pid=Pidfill

if pid != 0: # diferent de 0 es el pare..
  os.wait() # El procés pare espera a que finalitzi el fill per mostrar el seu PID.
  # quan mor el fill el pare es desbloqueja
  print("Programa Pare", os.getpid(), pid)  # És diferent a 0 perquè és el pare. 
else: # 0 es el fill
  print("Programa fill", os.getpid(), pid)  # 'os.getpid()' li dona valor al PID de fill.                                                              És 0 perquè el 'os.fork()' retorna 0.
  #while True:   # Si fem 'pgreep python', el fill segueix executant-se (bucle infinit) en bg com a dimoni
      #pass

print("Hasta lugo lucas!")

sys.exit(0)
