#! /usr/bin/python
#-*- coding: utf-8 -*-
# @ edt Desembre 2014
# ASIX-M06
# -----------------------------------------------
import os,sys

newProc="/usr/bin/ls"
pid=os.fork()
if pid!=0:
    print "programa pare, (%s,%s)" % (os.getpid(),pid)
    sys.exit(0)

print "...",os.getpid()
os.execv(newProc,[""])
sys.exit(0)

