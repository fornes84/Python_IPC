# /usr/bin/python3
#-*- coding: utf-8-*-
#
# exemple-echoServer.py  
#
# Primer de tot, haurem de tenir el servidor engegat, a continuació...
# 1 - El server haurà d'escolatar connexions
# 2 - El client ha de fer un 'connect' --> 'Trucar' i preguntar si és pot connectar
# 3 - El servidor ha d'acceptar la connexió ('accept')
# 4 - El client envia dades --> bucle infinit, rebre, enviar
# 5 - El client finalitza.
# 6 - Tancar... (if not data)
# -------------------------------------
# @ edt ASIX M06 Curs 2019-2020
# Gener 2020
# -------------------------------------
import sys,socket
#-------------------------------------
HOST = ''
PORT = 50001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Constructor...
s.bind((HOST,PORT)) # lliga el servei amb una connexió concreta (IP:port)
s.listen(1) # S'ha de possar per força
conn, addr = s.accept() # El servidor és queda clavat aquí fins que s'accepti una connexió --> Retorna una tupla (primer valor (objecte de tipus connection --> 'conn'), segon valor (adreça --> 'addr')
print("Connected by", addr) # Printem quan és faci la connexió

while True: # Bucle infinit (per quan hi hagi dades)
  data = conn.recv(1024)    # El client envia les dades, el servidor les rep i les torna
  if not data:  # if not data = s'ha tancat la connexió, el servidor finalitzarà (SERVIDOR!)
      break
  conn.send(data)   # Tornem les dades
conn.close()    # Client tanca la connexió (CLIENT!)

sys.exit(0) # Finalitzem programa

# ----------------------------------------
# PROVES (SURT EL CLIENT):
# ----------------------------------------
# CONSOLA SERVIDOR:
# python3 21-exemple-echo-server-simple.py
# ----------------------------------------
# CONSOLA CLIENT:
# python3 21-exemple-echo-client-simple.py / telnet localhost 50001 (cada cop que escribim alguna cosa, ho rebota) / nc localhost 50001 

# telnet i nc (netcat) són ordres clients de qualsevol transmissió (TCP, UDP)
# nc -lk --> 'l' --> listen | 'k' --> Quan acaba una connexió, passa a la següent
