# IPC (Inter Process Comunication)

* **Shared memory** --> És una zona habilitada perquè diversos processos es comuniquin entre ells.
* **Pipes** --> Un procés executa un altre procés i es comuniquen entre ells a través d'un pipe.
* **Signals** --> Per dir-li a un programa que pari utiltizem 'kill' i li diem el número del sistema 'kill -9'. Els processos es poden comunicar entre ells amb programes.
* **Sockets** --> Establir sockets perquè es comuniquin entre ells.

## Processos (ordres de repàs):
isx48062351@i24:/tmp/m01$ sleep 99999 & --> Creem processos en background

[1] 9951

isx48062351@i24:/tmp/m01$ sleep 99999 &

isx48062351@i24:/tmp/m01$ sleep 99999 &

isx48062351@i24:/tmp/m01$ pgrep sleep --> Veiem els processos 'sleep' que s'estan executant.

9951

9952

9953

isx48062351@i24:/tmp/m01$ jobs	--> Llistem els jobs

[1]   Running                 sleep 99999 &

[2]-  Running                 sleep 99999 &

[3]+  Running                 sleep 99999 &

isx48062351@i24:/tmp/m01$ fg %1	--> Possem en foreground el priemr 'job'

sleep 99999

^Z

[1]+  Stopped		      sleep 99999 &

isx48062351@i24:/tmp/m01$ killall sleep	--> Matem tots els processos

[1]-  Terminated	      sleep 99999

[2]-  Terminated              sleep 99999

[3]+  Terminated              sleep 99999

isx48062351@i24:/tmp/m01$ lsof --> Llista els fitxers que tenim oberts

TOT PROCÉS QUE EXECUTA EL SHELL HEREDA LES VARIABLES D'ENTORN.

### Pipes:
* ordre1 | ordre2 --> El contingut de la ordre 1 passa a l'ordre 2
**EX:** grep "10" /etc/passwd | wc -l

/proc --> Representació virtual dels processos del sistema

cat | sort | wc -l > cara.txt

isx48062351@i24:/tmp/m01$ ls -la /proc/11730/fd

total 0

dr-x------ 2 isx48062351 hisx2  0 Jan 18 11:23 .

dr-xr-xr-x 9 isx48062351 hisx2  0 Jan 18 11:23 ..

lrwx------ 1 isx48062351 hisx2 64 Jan 18 11:23 0 -> /dev/pts/1 --> entrada estàndard (stdin)

l-wx------ 1 isx48062351 hisx2 64 Jan 18 11:23 1 -> 'pipe:[234590]' --> stdout

lrwx------ 1 isx48062351 hisx2 64 Jan 18 11:23 2 -> /dev/pts/1 --> sortida estàndard (stderr)

isx48062351@i24:/tmp/m01$ ls -la /proc/11731/fd

total 0

dr-x------ 2 isx48062351 hisx2  0 Jan 18 11:24 .

dr-xr-xr-x 9 isx48062351 hisx2  0 Jan 18 11:23 ..

lr-x------ 1 isx48062351 hisx2 64 Jan 18 11:24 0 -> 'pipe:[234590]'

l-wx------ 1 isx48062351 hisx2 64 Jan 18 11:24 1 -> 'pipe:[234592]'

lrwx------ 1 isx48062351 hisx2 64 Jan 18 11:24 2 -> /dev/pts/1

isx48062351@i24:/tmp/m01$ ls -la /proc/11732/fd

total 0

dr-x------ 2 isx48062351 hisx2  0 Jan 18 11:24 .

dr-xr-xr-x 9 isx48062351 hisx2  0 Jan 18 11:23 ..

lr-x------ 1 isx48062351 hisx2 64 Jan 18 11:24 0 -> 'pipe:[234592]'

l-wx------ 1 isx48062351 hisx2 64 Jan 18 11:24 1 -> /tmp/m01/carta.txt

lrwx------ 1 isx48062351 hisx2 64 Jan 18 11:24 2 -> /dev/pts/1

A partir del número 3, són personalitzats

mkfifo --> creem estructures de dispositius
**EX:** mkfifo /tmp/dades

Per esborrar les estructures de dispositius:
**EX:** rm /tmp/dades

isx48062351@i24:/tmp/m01$ ls -la /tmp/dades 

prw-r--r-- 1 isx48062351 hisx2 0 Jan 18 11:26 /tmp/dades --> Tipus 'pipe' (named pipe)

isx48062351@i24:/tmp/m01$ tail -f /tmp/dades --> '-f' de follow (cada cop que executem una ordre dins d'aquest directori, el follow ens ho anirà mostrant

* **Documentació popen:** https://docs.python.org/3.8/library/subprocess.html

### Signals:
**EXS:** kill -<num> $(pgrep <programa>)
	 kill -<num> <PID>
         jobs --> per veure el jobs actius

**pgrep <programa>** Per veure el seu PID (Proccess ID)

**pstree -pl** <PID> (p --> process, l --> + info)

**CTRL + Q** --> Atura el procés en execució (**EX:** tree /)

**CTRL + S** --> Continua el procés aturat (**EX:** tree /)

* **Senyals:** (Per mirar aquests: **kill -l**)
* 1 - SIGHUP (Senyal que reinicia el procés)
* 2 - SIGINT (Senyal que plega el programa --> equivalent a CTRL + C)
* 9 - SIGKILL (Senyal que mata el procés)
* 10 - SIGUSR1 (Senyal sense funció assignada, està així perquè l'usuari el defineixi)
* 12 - SIGUSR2 (Senyals sense funció assignada, està així perquè l'usuari el defineixi)
* 14 - SIGALRM (Senyal que envia una alarma)
* 15 - SIGTERM (Senyal que li demana al programa que plegui)
* 18 - SIGCONT (Senyal que li demana al procés que continuï --> equivalent a CTRL + Q)
* 19 - SIGSTOP (Senyal que para el procés --> equivalent a CTRL + S / CTRL + Z)

### Forks:
**EX:** Programa base:

* codi
* codi
* fork() --> RÈPLICA EXACTA DEL PID, LI DIREM FILL, RETORNA UN NÚMERO QUÈ ÉS UN PID
	     RETORNA 0 EN EL FILL (PER SABER QUE ÉS EL FILL, PER AIXÒ 0) I EL Nº PID DEL FILL HO RETORNA	     EN EL PARE.
* codi
* codi

**execv:** El procés que s'està executant passa a convertir-se en el programa que se li ha passat (li passem el path del programa, i després li passem una llista amb el path del programa ([0]), l'ordre ([1]) i on s'executarà aquesta ordre ([2])), MAI executarà el que hi hagi sota seu.

**Ordres exec: (+ info --> https://docs.python.org/3/library/os.html)**
* os.execl(path, arg0, arg1, ...)
* os.execle(path, arg0, arg1, ..., env)
* os.execlp(file, arg0, arg1, ...)
* os.execlpe(file, arg0, arg1, ..., env)
* os.execv(path, args)
* os.execve(path, args, env)
* os.execvp(file, args)
* os.execvpe(file, args, env)

### Sockets:
Necesitem protocols.

\-------	  \-------

|      |          |      |

|      | Connexió |      |

|      |          |      |

|      |          |      |

\-------          \-------

 Client           Servidor

Port dinàmic -- Connexió -- Port (Well-Known) (0 - 1023) / Port definit per l'acplicació.

Sabem que una communicació és única per la communicació 'IP orígen:Port orígen --> (Socket orígen) + IP destí:Port destí --> (Socket destí)'

* **Documentació 'python3 sockets' --> https://docs.python.org/3/library/socket.html** 

**vim /etc/xinetd.d/** --> Opcions de programes

**Editem els següents (possant 'disable = no'):**
* echo
* daytime
* chargen

**Reiniciem i comprobem:**
* systemctl stop xinetd + systemctl start xinetd + systemctl status xinetd
* nmap localhost (han de sortir 7, 13 i 19)

'telnet' --> ordre bàsica per connexions TCP

**EX:**
* telnet <hostname> [7 / 13 / 19] 
* CTRL + ALT GR + CLAUDATOR --> HO PAREM

\-------	  \-------

|      |          |      |

|      |   Hola   |      |

|      |          |      |

|      |          |      |

\-------          \-------

Client.py         Servidor
(stdout)        (echo-server)
