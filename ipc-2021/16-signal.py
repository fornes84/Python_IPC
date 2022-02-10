# /usr/bin/python3
#-*- coding: utf-8-*-
#
# 16-signal.py segons
# Passat 'n' segons plegar amb SIGALARM
# No és pot utiltizar el CTRL + C
# ALARM --> Quan acabi mostra quants cops han hagut UPs i quants cops han hagut DOWNs
# USR1 --> Augmenta 1 minut (UP)
# USR2 --> Disminueix 1 minut (DOWN)
# HUP --> Reiniciar el comptador
# TER --> Mostrar quants segons falten
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------

import sys, os, signal, argparse  

parser = argparse.ArgumentParser(description=\
        """Exemple signals""")

parser.add_argument("segons",type=int,\
        help="introduïr segons")

args=parser.parse_args()
# ----------------------------------------------
global comptador_up  # Variable global (vàlides dins de totes les funcions)
global comptador_down   # Variable global (vàlides dins de totes les funcions)
comptador_up = 0
comptador_down = 0

def myusr1(signum,frame):  # No podem modificar la funció perquè ja està definida per el sistema!
  global comptador_up   # Cridem la variable global.
  print("Signal handler called with signal:", signum)
  segs_actuals = signal.alarm(0)    # 0 ens retorna el valor actual d'aquesta funció (es un comptador de segons) --> valor a temps real
  signal.alarm(segs_actuals + 60)   # El mateix que valía (a dalt) + 60
  comptador_up += 1
#
def myusr2(signum,frame):
  global comptador_down
  print("Signal handler called with signal:", signum)
  segs_actuals = signal.alarm(0)
  if segs_actuals - 60 < 0: # Li restem 60 (sempre que hi hagi 60) a l'alarma
      print("Adeu, t'ignoro %d" % (segs_actuals))
      signal.alarm(segs_actuals)
  else:
      signal.alarm(segs_actuals - 60)
  comptador_down += 1
#
def myhup(signum,frame):
  print("Signal handler called with signal:", signum)
  print("Restoring value: ", args.segons)
  signal.alarm(args.segons) # Reinicïa al valor introduït per l'usuari
#
def myterm(signum,frame):
  print("Signal handler called with signal:", signum)
  segs_falta = signal.alarm(0) # Valor a temps real
  signal.alarm(segs_falta)  # Fiquem els segons introduïts anteriorment (a dalt)
  print("Falten actualment %d segons" % (segs_falta))
#
def myalarm(signum,frame):
  global comptador_up, comptador_down
  print("Signal handler called with signal:", signum)
  print("Finalitzant.... nº UPs:%d  nº DOWNs:%d" % (comptador_up, comptador_down))
  sys.exit(1)
#
signal.signal(signal.SIGALRM,myalarm) 
signal.signal(signal.SIGUSR2,myusr2) 
signal.signal(signal.SIGUSR1,myusr1)    
signal.signal(signal.SIGHUP,myhup)
signal.signal(signal.SIGTERM,myterm)
signal.signal(signal.SIGINT,signal.SIG_IGN) # Ignorem CTRL + C
signal.alarm(args.segons)
print(os.getpid())
#
while True:
  pass
signal.alarm(0) # Envía un signal d'alarma

sys.exit(0)

# Proves
#kill -15 <PID_PROGRAMA>
#kill -10 <PID_PROGRAMA>
#kill -12 <PID_PROGRAMA>
#kill -11 <PID_PROGRAMA>
