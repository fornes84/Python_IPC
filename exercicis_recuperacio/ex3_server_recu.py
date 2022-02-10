#!/usr/bin/python
#-*- coding: utf-8-*-
# ------------------------------------------------------
# Escola del treball de Barcelona
# ASIX2 M06-ASO UF2 NF1-Scripts
# @edt Curs 2021-2022
# Gener 2022
# Telnet server multiple-connexions
# ------------------------------------------------------
import socket, sys, select, os, argparse
from subprocess import Popen, PIPE
# ------------------------------------------------------
parser = argparse.ArgumentParser(description="""Telnet server""")

parser.add_argument("-p","--port",type=int, default=50001)

parser.add_argument("-d","--debug",type=str, default="")

args=parser.parse_args()
# -----------------------------------------------------
HOST = ''
PORT = args.port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)
conns=[s]
# -----------------------------------------------------
while True:
    actius,x,y = select.select(conns,[],[])
    for actual in actius:
        if actual == s:
            conn, addr = s.accept()
            print('Connected by', addr)
            conns.append(conn)
        else:
            msg = actual.recv(1024)
            if not msg:
                sys.stdout.write("Client finalitzat: %s \n" % (actual))
                actual.close()
                conns.remove(actual)
            else:
                msg = msg.decode()
#                pipeData = Popen(msg,shell=True,stdout=PIPE,stderr=PIPE)
                print("Out", addr[0], msg)
#                for line in pipeData.stdout:
 #                   print("Out", addr[0], actual.sendall(line))

s.close()

sys.exit(0)
