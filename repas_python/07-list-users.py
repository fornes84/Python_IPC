# /usr/bin/python
#-*- coding: utf-8-*-
#
# list-users [-f file]
# 10 lines, file o stdin
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys, argparse

parser = argparse.ArgumentParser(description=\
        """Llistar els usuaris de file o stdin (format /etc/passwd""",\
        epilog="thats all folks")

parser.add_argument("-f","--fit",type=str,\
        help="user file or stdin (/etc/passwd style)", metavar="file",\
        default="/dev/stdin",dest="fitxer")

args=parser.parse_args()
# -------------------------------------------------------
class UnixUser():
  """Classe UnixUser: prototipus de /etc/passwd
  login:passwd:uid:gid:gecos:home:shell"""
  #
  def __init__(self,userLine):
    "Constructor objectes UnixUser"
    camp=userLine.split(":")
    self.login=camp[0]
    self.passwd=camp[1]
    self.uid=int(camp[2])
    self.gid=int(camp[3])
    self.gecos=camp[4]
    self.home=camp[5]
    self.shell=camp[6][:-1]
  #
  def show(self):
    "Mostra les dades de l'usuari"
    print(f"login: {self.login} uid: {self.uid} gid: {self.gid} gecos: {self.gecos} home: {self.home} shell: {self.shell}")
  #
  def __str__(self):
    "Funció que pasa a string"
    return "%s %s %d %d %s %s %s" %(self.login, self.passwd, self.uid, self.gid, self.gecos, self.home, self.shell)
# -------------------------------------------------------
fileIn=open(args.fitxer,"r")    # Obrim el fitxer o fitxer stdin
userList=[]     # Inicialitzem una llista buida

for line in fileIn:     # Per cada línea del fitxer o fitxer stdin ...
  oneUser=UnixUser(line)    # De la classe UnixUser li passem com a paràmetre cada línea del fitxer i                                 guardem cada usuari a una variable nova (oneUser)
  userList.append(oneUser)      # Afegim cada usuari a la llista creada anteriorment (buida)
fileIn.close()  # Tanquem el fitxer

for user in userList:   # Verifiquem que els usuaris afegits són correcte (recorrem la llista)
 print(user)    # Els mostrem

exit(0) # Sortim
