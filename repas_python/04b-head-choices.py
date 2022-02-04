# /usr/bin/python3
#-*- coding: utf-8-*-
#
# head [-n 5|10|15] file
#  10 lines, file
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2020
# -------------------------------------
import sys, argparse

parser = argparse.ArgumentParser(description=\
        """Mostrar les N primereslínies """,\
        epilog="thats all folks")

parser.add_argument("-n","--nlin",type=int,\
        help="Número de línies 5|10|15, def 10",\
        dest="nlin",\
        metavar="numLines",default=10,\
        choices=[5,10,15])

parser.add_argument("-f","--file",type=str, required=True,\
        help="fitxer a processar", metavar="file", dest="fitxer") # optional parameter que ha de ser-hi                                                                     per collons

args=parser.parse_args()
print(args)
# -------------------------------------------------------
MAXLIN=args.nlin
fileIn=open(args.fitxer,"r")

counter=0
for line in fileIn:
  counter+=1
  print (line, end='')
  if counter==MAXLIN: break

fileIn.close()
exit(0)
