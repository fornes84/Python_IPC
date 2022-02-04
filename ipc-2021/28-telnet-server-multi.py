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
print(os.getpid())
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
            command = actual.recv(1024)
            if not command:
                sys.stdout.write("Client finalitzat: %s \n" % (actual))
                actual.close()
                conns.remove(actual)
            else:
                command = command.decode()
                pipeData = Popen(command,shell=True,stdout=PIPE,stderr=PIPE)
                for line in pipeData.stdout:
                    actual.sendall(line)
                for line in pipeData.stderr:
                    actual.sendall(line)
                actual.sendall(chr(4).encode())

s.close()

sys.exit(0)

