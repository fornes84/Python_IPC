# /usr/bin/python
#-*- coding: utf-8-*-
#
# sort-users [-s login|gid]  file
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys, argparse
from functools import cmp_to_key

parser = argparse.ArgumentParser(description=\
        """Llistar els usuaris de file o stdin (format /etc/passwd""",\
        epilog="thats all folks")

parser.add_argument("-s","--sort",type=str,\
        help="sort criteria: login | gid", metavar="criteria",\
        choices=["login","gid"],dest="criteria",default="login")

parser.add_argument("fitxer",type=str,\
        help="user file (/etc/passwd style)", metavar="file")
args=parser.parse_args()
# -------------------------------------------------------
class UnixUser():
  """Classe UnixUser: prototipus de /etc/passwd
  login:passwd:uid:gid:gecos:home:shell""" 
  #
  def __init__(self,userLine):
    "Constructor objectes UnixUser"
    userField=userLine.split(":")
    self.login=userField[0]
    self.passwd=userField[1]
    self.uid=int(userField[2])
    self.gid=int(userField[3])
    self.gecos=userField[4]
    self.home=userField[5]
    self.shell=userField[6][:-1]
  #
  def show(self):
    "Mostra les dades de l'usuari"
    print(f"login: {self.login} uid: {self.uid} gid: {self.gid} gecos: {self.gecos} home: {self.home} shell: {self.shell}")
  #
  def __str__(self):
    "Funció to_string"
    return "%s %s %d %d %s %s %s" %(self.login, self.passwd, self.uid, self.gid, self.gecos, self.home, self.shell)
# -------------------------------------------------------
def sort_login(user):       # Compararem els logins i retornarem els logins ordenats amb la sortida de                                'userList' que tenim a sota utilitzant la key.
  '''Comparador d'usuaris segons el login'''
  return user.login
  
def sort_gid(user):         # Compararem els gids i si aquest són iguals compararem per login i                                       retirbaren aquests ordenats amb la sortida de 'userList' que tenim a sota                               utilitzant la 'key'.
  '''Comparador d'usuaris segons el gid'''
  return (user.gid, user.login)
# -------------------------------------------------------
fileIn=open(args.fitxer,"r")        # Obrim el fitxer / fitxer stdin
userList=[]     # Creem una llista buida

for line in fileIn:             # Per cada linea del fitxer...
  oneUser=UnixUser(line)        # Afegim cada línea a una variable nova creada 'oneUser0
  userList.append(oneUser)      # Afegim cada user a la llista creada perviament.
fileIn.close()      # Tanquem el fitxer
# -----------------------------------------------------
if args.criteria=="login":  # Si l'argument escollit per ordenar es login...
  userList.sort(key=sort_login)     # key --> específiquem el criteri per el qual ordenarem                                                   Ordenem per login i passem resultat a la funció 'sort_login'
else:
  userList.sort(key=sort_gid)       # Si no és login, ordenem per gid i passem resultat a la funció                                           'sort_gid'
# -----------------------------------------------------
for user in userList:       # Per cada usuari en la llista d'usuaris:
 print(user)            # Mostrem

exit(0)     # Sortim
