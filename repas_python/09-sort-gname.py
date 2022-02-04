# /usr/bin/python
#-*- coding: utf-8-*-
#
# gname-users [-s login|gid|gname] -u users -g groups
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys, argparse

parser = argparse.ArgumentParser(description=\
        """Llistar els usuaris de file o stdin (format /etc/passwd""",\
        epilog="thats all folks")

parser.add_argument("-s","--sort",type=str,\
        help="sort criteria: login | gid | gname", metavar="criteria",\
        choices=["login","gid", "gname"],dest="criteria")

parser.add_argument("-u","--userFile",type=str,\
        help="user file (/etc/passwd style)", metavar="userFile",required=True)

parser.add_argument("-g","--groupFile",type=str,\
        help="user file (/etc/passwd style)", metavar="groupFile",required=True)

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
    self.gname=""       # Definim 'gname' com a cadena buida
    if self.gid in groupDict:       # Assignem un 'gname' donat un gid (estarà guardat al diccionari), si no està al diccionari, llavors no agafa el valor.
      self.gname=groupDict[self.gid].gname
    self.gecos=userField[4]
    self.home=userField[5]
    self.shell=userField[6]
  #
  def show(self):
    "Mostra les dades de l'usuari"
    print(f"login: {self.login} uid: {self.uid} gid: {self.gid} gecos: {self.gecos} home: {self.home} shell: {self.shell}")
  #
  def __str__(self):
    "Funció to_string"
    return "%s %s %d %d %s %s %s %s" %(self.login, self.passwd, self.uid, self.gid, self.gname, self.gecos, self.home, self.shell)
# -------------------------------------------------------
class UnixGroup():
    """Classe UnixGroyp: prototipus de /etc/group
    gname:passwd:gid:userList"""
    #
    def __init__(self,groupLine):
        "Constructor objectes UnixGroup"
        groupField=groupLine.split(":")
        self.gname=groupField[0]
        self.passwd=groupField[1]
        self.gid=int(groupField[2])
        self.userListStr=groupField[3][:-1]     # Treiem el salt de línea amb [:-1] (\n)
        self.userList=[]
        if self.userListStr:     # Si la llista de strings conté coses, llavors fem coses.
          self.userList = self.userListStr[:-1].split(",")
    #
    def __str__(self):
        "Funció to_string"
        return "%s %s %d %s" %(self.gname, int(self.gid), self.userList)
# -------------------------------------------------------
def sort_login(user):       # Compararem els logins i retornarem els logins ordenats amb la sortida de 'userList' que tenim a sota utilitzant la key.
  '''Comparador d'usuaris segons el login'''
  return user.login
  
def sort_gid(user):         # Compararem els gids i si aquest són iguals compararem per login i ordenarem aquests amb la sortida de 'userList' que tenim a sota utilitzant la key.
  '''Comparador d'usuaris segons el gid'''
  return (user.gid, user.login)

def sort_gname(user):        # Compararem els gnames i retornarem aquests ordenats amb la sortida de 'gnameList' que tenim a sota utilitzant la key.
    '''Comparador de gnames segons el gname'''
    return (user.gname, user.login)
# -------------------------------------------------------
groupDict={}
groupFile=open(args.groupFile,"r")

for line in groupFile:    # Per cada línea en el fitxer...
  group=UnixGroup(line)   # Adegim cada línea a una variable que creem ('group')
  groupDict[group.gid]=group    # Li donem el valor del grup al diccionari.

groupFile.close()   # Tanquem el fitxer
# -------------------------------------------------------
userFile=open(args.userFile,"r")    # Obrim el fitxer o fitxer stdin
userList=[]     # Creem una llista buida

for line in userFile:     # Per cada línea en el fitxer d'usuaris...
  user=UnixUser(line)     # La variable nova 'user', pasarà a tenir el valor d'aquest usuari (agafa el valor)
  userList.append(user)   # Afegim l'usuari a la llista

userFile.close()    # Tanquem el fitxer
# -------------------------------------------------------
if args.criteria=="login":      # Si s'ha decidit ordenar per login...
  userList.sort(key=sort_login)     # Amb 'key' especifiquem el valor pel qual s'ordenarà (login en aquest cas)
elif args.criteria=="gid":      # Si s'ha decidit ordenar per gid...
  userList.sort(key=sort_gid)       # Amb 'key' especifiquem el valor pel qual s'ordenarà (gid en aquest cas)
else:
  userList.sort(key=sort_gname)     # Amb 'key' especifiquem el valor pel qual s'ordenarà (gname en aquest cas)

for user in userList:   # Per cada usuari en la llista d'usuaris...
 print(user, end=" ")   # Printem

exit(0)   # Sortim
