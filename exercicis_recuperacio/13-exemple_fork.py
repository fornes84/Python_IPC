#! /usr/bin/python
#-*- coding: utf-8 -*-
# @ edt Desembre 2014
# ASIX-M06
# -----------------------------------------------
import os,sys

print "hola"
pid=os.fork()
if pid!=0:
    print "programa pare, (%s,%s)" % (os.getpid(),pid)
else:
    print "programa fill,",pid
print "bye!"
sys.exit(0)

