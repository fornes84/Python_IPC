# /usr/bin/python3
#-*- coding: utf-8-*-
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
# Exemple de programació Objectes POO
# -------------------------------------
class UnixUser():
  """Classe UnixUser: prototipus de 
  /etc/passwd
  login:passwd:uid:gid:gecos:home:shell"""

  def __init__(self, line):      # Mètode Constructor	
    "Constructor objectes UnixUser"
    camp=line.split(":")
    self.login=camp[0]
    self.passwd=camp[1]
    self.uid=int(camp[2])
    self.gid=int(camp[3])
    self.gecos=camp[4]
    self.home=camp[5]
    self.shell=camp[6]

  def show(self):   # Utilitza les dades de si mateix (self)
    "Mostrar les dades de l'usuari"
    """
    print(self.login)
    print(self.passwd)
    print(self.uid)
    print(self.gid)
    print(self.gecos)
    print(self.home)
    print(self.shell)
    """
    print(f"login: {self.login} uid: {self.uid} gid: {self.gid} gecos: {self.gecos} home: {self.home} shell: {self.shell}")

  def __str__(self):
    "Funció per retornar un string del objecte"
    return "%s %d %d" % (self.login, self.uid, self.gid)

print ("Programa")
user1=UnixUser("pere:x:1000:100:Postgres:/home/pere:/bin/bash")
user1.show()   # cridem a la funció show de la classe "user1" 
#print(user1)
exit(0)
