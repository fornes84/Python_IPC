# /usr/bin/python
#-*- coding: utf-8-*-
#
# daytime-server-one2one.py  
# -------------------------------------
# @ edt ASIX M06 Curs 2021-2022
# Gener 2022
# -------------------------------------
import sys,socket,argparse,os,signal
from subprocess import Popen, PIPE
# -------------------------------------
parser = argparse.ArgumentParser(description=\
        """Server One by One""")

parser.add_argument("-p","--port", type=int, help="port al qual ens connectem",\
     default=50001, dest="port")

args=parser.parse_args()
# -------------------------------------
HOST = ''
PORT = args.port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(1)

while True:
  conn, addr = s.accept()
  print("Connected by", addr)
  command = ["date"]
  pipeData = Popen(command,stdout=PIPE)
  for line in pipeData.stdout:
    conn.send(line)
  conn.close()
