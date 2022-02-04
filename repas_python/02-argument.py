# /usr/bin/python
#-*- coding: utf-8-*-
#
# Programa per processar arguments
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import argparse

# Creem un objecte (parser) constructor (ArgumentParser):
parser=argparse.ArgumentParser(description=\
  "programa exemple de processar arguments",prog="02-arguments.py",epilog="hasta luegu lucas!")
parser.add_argument("-e","--edat", type=int, dest="useredat", help="edat a processar")
parser.add_argument("-n","--nom", type=str, help="nom d'usuari") # dest = variable per defecte
parser.add_argument("fit", type=str, help="fitxer")
args=parser.parse_args()    # La funció parser_args() analitza els arguments que li hem passat segons la
                            # construcció feta abans, ho ficarà a una variable de nom "args"
print(parser)
print(args)
print(args.useredat, args.nom)
exit(0)
