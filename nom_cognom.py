# /usr/bin/python
#-*- coding: utf-8-*-
# XXXXX-server.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Juny 2022
# -------------------------------------
import sys,socket,os,signal,argparse,time
from subprocess import Popen, PIPE
# ------------------------------------
parser = argparse.ArgumentParser(description=\
        """CAL server""")
parser.add_argument("-s","--server", type=str, default='')
parser.add_argument("-p","--port", type=int, default=XXX)
args=parser.parse_args()
#------------------------------------------------------
HOST = ''
PORT = XXX
#HOST = args.server
#PORT = args.port


