# /usr/bin/python
#-*- coding: utf-8-*-
#
# head [file]
#  10 lines, file o stdin
# Si no le passem fitxer processa entrada estàndard
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys

MAXLIN=10
fileIn=sys.stdin

if len(sys.argv)==2:    # [python3(0) file_programa(1) file(2)]
  fileIn=open(sys.argv[1],"r")

counter=0
for line in fileIn:
  counter+=1
  print (line, end="") # end="": Serveix per quan acabi una línea no faci el salt de línea que fa per 
                       #         defecte el print. end = valor que declarem en aquell instant.
  if counter==MAXLIN: 
      break

fileIn.close()
exit(0)
