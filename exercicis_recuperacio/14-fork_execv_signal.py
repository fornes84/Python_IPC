#! /usr/bin/python
#-*- coding: utf-8 -*-
# @ edt Desembre 2014
# ASIX-M06
# -----------------------------------------------
import os,sys

print "hola"
pid=os.fork()
if pid==0:
    print "daemon en execució..."
    os.execv("./11-signal.py",[""])
print "(%s,%s)" % (os.getpid(),pid)
os.wait()
sys.exit(0)

