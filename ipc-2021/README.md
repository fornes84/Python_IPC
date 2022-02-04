ASIX M06-ASO Escola del treball de barcelona

#### IPC: Pipes / Subprocess / Popen

**11-exemple-popen.py dir**

  Crear un programa que executa un ls de un argument rebut i 
  mostra per stdout el que rep del popen. Utilitza subprocess.Popen.

**12-popen-sql.py** 

  Es pot fer una primera versió tot hardcoded sense diàleg amb: 
  psql -qtA -F';' training  -c “select * from oficinas;”.
  Executa la consulta “select * from oficinas;” usant psq.  
  Atenció: posar al popen shell=True.
  Podem usar un container Docker amb la bd training de postgres
  fent:

```
Hi ha un docker a dockerhub:
$ docker run --rm --name psql -h psql -it edtasixm06/postgres /bin/bash

A la adreça de github [asixm06-docker](https://github.com/edtasixm06/asixm06-docker/tree/master/postgres:base) hi la les ordres per engegar el postgres.

Cal fer-les per posar en marxa el servei i inicialitzar la base de dades.
$ su -l postgres
$ /usr/bin/pg_ctl -D /var/lib/pgsql/data -l logfile start

Verificar el funcionament des de dins del container:
$ psql -qtA -F',' training -c "select * from clientes;"


Des del host executar consultes, cal indicar la adreça ip del container al que connectem, i l’usuari (role) que és edtasixm06:
$  psql -qtA -F',' -h 172.17.0.2 -U edtasixm06 training -c "select * from clientes;"

Si volem que el container faci map a un dels ports del host:
$ docker run --rm --name psql -h psql -p 5432:5432  -it edtasixm06/postgres /bin/bash
$inicialitzar des de dins del docker
$ psql -qtA -F','  -h d02  -U edtasixm06 training -c "select * from oficinas;"
```
**13-popen-sql-injectat.py  consulta**

  Fer que la sentència sql a fer sigui un argument tot entre cometes 
  que es passa com a argument.
  sql injectat: perills d’injectar codi d’usuari en els programes.

**14-popen-sql-multi.py  -d database   -c numclie[...]**

  Atacar la database indicada, llistar cada un dels registres del codi indicat.
  Explicació dels diàlegs, un read o readlines es queda encallat at infinitum 
  quan el subprocess no finalitza. Cal llegir exactament les n línies de resposta
  (dues si ok, una si error), pero no infinites.
  Exemple amb wc < file i wc de stdin.
  *Atenció:* no programar el cas desfaborable de posar num_clie que no existeixen,
  això implica buscar un mecanisme de diàleg tipus “canvi!”... com amb els walki-talki.

  Hem après a:
   * posar el /n al final per que faci la acció.
   * si el popen finalitza és com si hi ha el ^d al final de fi de fluxe i podem llegir les n línies que retorni.
   * si el popen és interactiu i no finalitza cal saber a priori quantes línies llegir o es quedarà ‘enganxat’.
 

#### IPC: Signals

**15-exemple-signal.py**

  Programa d'exemple del funcionament de signal. 
  Defineix handlers i els assigna als senyals 
  sigalarm i sigterm. Finalitza automàticament
  en passar els n segons de l'alarma definida.

**16-signal.py segons**

  Deifineix alarma(n segons). siguser1 incrementa 1 minut, 
  siguser2 decrementa 1 minut, sighub reinicia el compte (valor argument inicial), 
  sigterm mostra quants segons falten de l'alarma, 
  no és interrumpible amb control c. 
  Sigalarm  mostra el valor de upper (quants hem incrementat)
  i down (quants decrementat) i acaba.
  *Ateció* per usar els comptadors upper i down caldrà usar
  variables globals

#### IPC: Fork / Execv

**17-exemple-fork.py**

  Exemple bàsic fork amb programa pare que llança programa fill (un while infinit). 
  Observar els PID i la lògica del fluxe de funcionament.

**18-fork-signal.py**

  Usant el programa d'exemple fork fer que el procés fill (un while infinit) es
  governi amb senyals. Amb siguser1 mostra "hola radiola" i amb sigusr2 mostra
  "adeu andreu" i finalitza. El programa pare genera el procés fill i finalitza.

**19-exemple-execv.py**

  Ídem anterior però ara el programa fill execula un “ls -la /”. Executa un nou 
  procés carregat amb execv. Aprofitar per veure les diferents variants de *exec*.
  Provar cada un dels casos.

**20-execv-signal.py**

  Usant l'exemple execv programar un procés pare que llança un fill i finalitza.
  El procés fill executa amb execv el programa python *16-signal.py* al que li 
  passa un valor hardcoded de segons.

#### IPC: Sockets

-----------------------------------------------------------------------------
Sockets:
  * *Simple*: Exemples simples de construir un client/servidor. 

    - Simple indica que el servidor engega, escolta fins que rep una
    connexió, la atén i finalitza. Francament un servidor que processa un sol
    client en la seva vida útil és massa simple!.

    - Simple també indica que el contingut que es transmet del client al servidor i de retorn 
    al client és hardcoded i de mida limitada.


      * 21-exemple-echo-client-simple.py / 21-exemple-echo-server-simple.py


 * *Buffer*: El client (o el servidor) no té preestablert quanta informació es rebrà, per tant
   no n'hi ha prou de fer un sol reciv (escola un sol cop) sinó que cal fer un bucle per anar
   rebent informació mentre n'hi hagi. usualment és una estructura *"while not data"*.

      * 22-daytime-client.py / 22-daytime-server.py 


 * *One2one*: No té sentint que un servidor atengui un client i finalitzi. Una millora 
   (elemental) és anar atenent els clients un a un. Es connecta un client, se l'atén, es tanca
   la conexió amb aquest client i es passa a escoltar per rebre una nova conexió.
   En aquest cas el server fa un bucle ininit, va atenent clients infinitament un darrera l'altre
   (o si més no s'espera a entendre'ls). És per això que cal governar el servidor, per exemple
   amb senyals.

      * 23-daytime-server-one2one.py
      * 24-calendar-slient-one2one.py / 24-calendar-server-one2one.py


 * *ClientPopen*: En els exemples anteriors el servidor era qui executava un procés i retornava
   la informació al client, però això no té perquè ser així. Un client pot per exemple recopilar
   la informació dels processos que s'executen en el seu host i enviar-ho com un informe 
   al servidor (que per exemple ho desa a disc).

     * 25-psClientOne2one 25-psserverOne2oner.py


 * *Diàleg interactiu*:  Finalment farem un exemple en que client i servidor dialògin 
   realment, intercanviant-se vàris missatges. Per exemple implementant un *telnet*.

     * 26-telnetClient 26-telnetServer.py


 * *Multi connexió*: El servidor accepta múltiples clients connectats simultàniament
   i els atén també simultàniament.

    * 27-echoServerMulti.py
    * 28-telnetServerMulti.py
-----------------------------------------------------------------------------

**21-exemple-echo-client-simple.py**

**21-exemple-echo-server-simple.py**

  Fer els exemples de echo server/ echo client. 
  En l’exemple el client es hardcoded que escolta una resposta de mida fixa.
  Sockets: echo server/client bàsic on el client envia un text i el server el retorna. 
  Text acotat usant reciv encara no correctes del tot (encara no fem que tot 
  siguin bucles ni el caràcter de fi de diàleg).
  Fer primer el server i deixar-lo en marxa. Qualsevol client com ncat es pot comunicar amb el server.
  Observar el server amb netstat en mode listen i en mode established.

**22-daytime-client.py**

**22-daytime-server.py**
 
  Crear un daytime client/server amb un popen de date. El server plega un cop respost. 
  En aquest cas el client pot ser qualsevol eina client que simplement es connecta i 
  escolta la resposta del servidor.
  El client es connecta al servidor  i aquest li retorna la data i tanca la conexió. El
  client mostra l adata rebuda i en veure que s'ha tancat la connexió també finalitza.
  El servidor engega i espera a rebre una conexió, quan l'accepta executa un Popen per
  fer un *date* del sistema operatiu, retorna la informació i tanca la conexió. També
  finalitza (és un servidor molt poc treballador!!).

**23-daytime-server-one2one.py**

  Ídem exercici anterior, generar un daytime-server que accepta múltiples clients
  correlatius, és a dir, un un cop finalitzat l'anteior: *One2one*.

**24-calendar-client-one2one.py [-s server] [-p port]**

**24-calendar-server-one2one.py [-p port] [-a any]**

  Calendar server amb un popen, el client es connecta i rep el calendari. El server 
  tanca la connexió amb el client un cop contestat però continua escoltant noves connexions.

  El server ha de governar-se amb senyals que fan:
   - sigusr1: llista de peers i plega.
   - sigusr2: count de listpeer i plega.
   - sigterm: llista de peers, count i plega.

  El server és un daemon que es queda en execució després de fer un fork del seu
  pare (que mor) i es governa amb senyals.

  Que sigui el servidor qui rep l'any com a argument és una tonteria, seria més lògic
  fer-ho en el client, però el diàleg client servidor queda per a una pràctica
  posterior. Aquí es vol practicar usar un arg en el popen.

**25-ps-client-one2one.py [-p port] server**

**25-ps-server-one2one.py [-p port]**
  
  Els clients es connecten a un servidor, envien un informe consistent en fer
  *"ps ax"* i finalitzen la connexió. El servidor rep l'informe del client i 
  el desa a disc. Cada informe es desa amb el format: ip-port-timestamt.log, on 
  timestamp té el format AADDMM-HHMMSS.

  Usar un servidor com el de l'exercici anterior, un daemon governat per senyals.


**26-telnet-client.py -p port -s server**

**26-telnetServer.py [-p port] [-d debug]**

  Implementar un servidor i un client telnet. Client i server fan un diàleg. 
  Cal un senyal de “yatà” Usem chr(4).
  Si s’indica debug el server genera per stdout la traça de cada connexió.


**27-echoServerMulti.py**

  Exemple de servidor amb connexions concurrents, accepta múltiples connexions
  simultàniament. Utilitzem el echo-server.

**28-telnetServerMulti.py**

  Implementar un servidor telnet amb connexions concurrents.


--------------------------------------------------------------------------

#### Test Remot

Per practicar aquests exercicis remotament (clients/servidor) a part de 
fer-ho a l'aula s'ha manat obrir un compte a AWS EC2 Amazon Elastic Cloud
Computing EC2. Des d'allà s'engegen els servidors i es prova l'accés remot

Implica l'aprenentatge de:

  * Crear compte a AWS EC2. 
  * Crear instàncies linux (Fedora Cloud Base 27 / London)
  * Cloaus d'accés via SSH
  * Obrir ports d'accés al servidor.

Podeu consultar a [Howto-ASIX-Amazon-AWS-EC2-AMI-Cloud.pdf](https://gitlab.com/edtasixm06/ipc-2018-19/blob/master/HowTo-ASIX-Amazon-AWS-EC2-AMI-Cloud.pdf) documentació al respecte.
