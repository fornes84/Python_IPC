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

  def __init__(self, l, i, g):      # Mètode Constructor	
    "Constructor objectes UnixUser"
    self.login=l
    self.uid=i
    self.gid=g

  def show(self):   # Utilitza les dades de si mateix (self)
    "Mostrar les dades de l'usuari"
    print(self.login)
    print(self.uid)
    print(self.gid)

  def __str__(self):
    "Funció per retornar un string del objecte"
    return "%s %d %d" % (self.login, self.uid, self.gid)

print ("Programa")
user1=UnixUser("pere", 1000, 100)
user1.show()   # cridem a la funció show de la classe "user1" 
print(user1)
exit(0)
