# /usr/bin/python3
#-*- coding: utf-8-*-
#
# signal-exemple.py
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys, os, signal

def myhandler(signum,frame):  # Rebrà un objecte que representa una senyal i farà una serie d'accions (li passo una cosa i li diem que vol que faci)
  print("Signal handler called with signal:", signum)
  print("hasta luego lucas!")
  sys.exit(1)   # Plega
#
def mydeath(signum,frame):  # Quan passi X senyal, s'executarà aquesta funció
  print("Signal handler called with signal:", signum)
  print("no em dona la gana de morir!")
#
signal.signal(signal.SIGALRM,myhandler) # 14 (Quan rebi el senyal SIGALARM, executarà la funció myhandler, si passan 60 segons, enviarà l'alarm amb el 'sig' 14)
signal.signal(signal.SIGUSR2,myhandler) # 12 (Idem a l'anterior però quan li passem SIGUSR2)
signal.signal(signal.SIGUSR1,mydeath)   # 10 (Quan rebi el senyal SIGUSR1, executarà la funció mydeath.
signal.signal(signal.SIGTERM,signal.SIG_IGN) # (Quan el programa rebi el senyal SIGTERM (ignorarà))
signal.signal(signal.SIGINT,signal.SIG_IGN) # (Quan el programa rebi SIGINT (CTRL + C), (ignorarà))
signal.alarm(60)
print(os.getpid())
#
while True:
  pass
signal.alarm(0) # Envía un signal d'alarma

sys.exit(0)

# Proves
#kill -2 <PID_PROGRAMA>
#kill -10 <PID_PROGRAMA>
#kill -12 <PID_PROGRAMA>
