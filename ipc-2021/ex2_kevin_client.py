# /usr/bin/python3
# -------------------------------------
import sys,socket,argparse
from subprocess import Popen, PIPE
# -------------------------------------
parser = argparse.ArgumentParser(description="""Exàmen practica""")

parser.add_argument("-s",type=str, dest="server")

parser.add_argument("-p",type=int,  dest="port")

args=parser.parse_args()
# -------------------------------------
if args.server and args.port:	
	HOST = args.server
	PORT = args.port
else:
	print("Selieccionar host e ip")
	consola = input("client_ftp_trivial>")
	if 'connect' in consola:
		HOST = consola.split()[1].split(':')[1]
		PORT = consola.split()[1].split(':')[2]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
# ------------------------------------
while True:
    entrada = input("client_ftp_trivial>")
    if entrada == 'quit':
        s.close()        
        break
    if 'get' in entrada:
        fitxer = open(entrada.split()[1].split('/')[-1],'a')
        entrada = "cat " + entrada.split()[1] 
    line = entrada
    entrada = entrada.encode()
    s.send(entrada)
    while True:
        data = s.recv(1024)
        print(str(data))
        if 'cat' in line:
            fitxer.write(str(data))
        else:
            print (str(data))
        if data[-1:] == b'\x04':
            break

sys.exit(0)

