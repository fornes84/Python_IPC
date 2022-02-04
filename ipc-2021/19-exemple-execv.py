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
#os.execv("/usr/bin/ls",["/usr/bin/ls","-ls","/"])  # 'v' ACCEPTA llistes i tuples
#os.execl("/usr/bin/ls","/usr/bin/ls","-ls","/") # 'l' NO ACCEPTA llistes i tuples, només li podem passar paràmetres fixes.
#os.execlp("ls","ls","-ls","/") # 'l' hem de passar-li els arguments literals, 'p' buscarà ell el PATH fins l'executable (no ens cal posar-li la ruta absoluta (/usr/bin/ls))
#os.execvp("uname",["uname", "-a"])  # Amb 'p' buscarà l'executable 'uname' i executarà l'ordre '-a'
#os.execv("/bin/bash",["/bin/bash", "show.sh"]) # executem el programa 'show.sh'
os.execle("/bin/bash", "/bin/bash", "show.sh", {"nom":"joan", "edat":"25"})   # 'e' li passem variables d'entorn (com a diccionari)
#-------------------------------------------------
print("Hasta lugo lucas!")   # Mai és veurà!!!!!
sys.exit(0)
