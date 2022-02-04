# IPC - Rubén Rodríguez García M06-ASO
# Curs 2021-2022

ASIX M06-ASO Escola del treball de barcelona

#### Repàs Python / Argsparse / Objectes

 * [Python documentation](https://docs.python.org/3/library/argparse.html)
 * [Argparse tutorial](https://docs.python.org/3/howto/argparse.html)

**01-head.py [file]**
  
  Mostrar les deu primeres línies de file o stdin

**02-exemple-args.py**

  Exemple fet interactivament per mostrar el funcionament
  de argparser. Pyton documentation 15.4.

 *Argparser (Python documentation 14.5 / argparse tutorial):*
   * creació objecte. afegir arguments.
   * paràmetres posicionals i opcionals.
   * help, description, epíleg, prog, metavar.
   * destination, type.
   * fer el parse. diccionari de resultats.
   * fitxers de tipus file (inconvenients) o str.
   * validació automàtica i missatges d’error. Independència de l’ordre dels 
     arguments opcionals (no dels posicionals).
   * validació automàtica del tipus dels arguments.
   * Els *paràmetres posicionals* es defineixen per ordre i simplement amb el
      “nom”. Els *opcionals* poden anar en qualsevol ordre i cal definir “-n” i “--nom”.


**03-head-args.py [-n nlin] [-f filein]**

  Mostar les n primeres línies (o 10)  de filein (o stdin).

  Definir els dos paràmetres opcionals i les variables on
  desar-los. Usar un str default de “/dev/stdin” com a nom 
  de fitxer per defecte, simplifica el codi, tenim sempre
  un string.

**04-head-choices.py [-n 5|10|15]   -f filein**

  Mostar les n primeres 5 o 10 o 15 (def 10)  de filein.
  Usar choices de argparse per definir un conjunt de valors vàlids.

**05-head-multi.py [-n 5|10|15]   [-f filein]...**

  Mostar les n primeres 5 o 10 o 15 (def 10)  de filein.
  Processa múltiples files indicats per -f file, -f file, etc.
  Ampliació: [-v][--verbose] boleà que si hi és mostra una capçalera 
  de llistat amb el nom del fitxer a llistar.

**06-exemple-objectes.py**

  Exemple de creació de una classe simplificada UnixUser amb camps login, uid, gid. 
  Constructor donats els tres valors, mètode show() i mètode sumaun()  que fa la tonteria
  de sumar 1 al uid.
  Crea objectes user1 i user2 de tipus UnixUser, els mostra, els posa a una llista.

**07-list-users.py   [-f file]**

  Donat un file tipus /etc/passwd o stdin (amb aquest format) fer:
  * el constructor d'objectes *UnixUser* rep un strg amb la línia sencera 
    tipus /etc/passwd.
  * llegir línia a línia cada usuari assignant-lo a un objecte 
    UnixUser i afegir l’usuari a una llista d’usuaris UnixUser.
  * un cop completada la carrega de dades i amb la llista amb 
    tots els usuaris, llistar per pantalla els usuaris recorrent la llista.

**08-sort-users.py [-s login|gid] file**

  Carregar en una llista a memòria els usuaris provinents d'un fitxer
  tipus /etc/passwd, usant objectes *UnixUser*, i llistar-los.
  Ordenar el llistat (stdout) segons el criteri login o el criteri 
  gid (estable).

**09-sort-gname.py   [-s login|gid|gname]  -u fileusers -g fileGroup**

  Carregar en una llista a memòria els usuaris provinents d'un fitxer tipus
  /etc/passwd, usant objectes UnixUser, i llistar-los. Ordenar el llistat
  (stdout) segons el criteri login o el criteri gid o el gname.
 
   Requeriments: primer carregar a un diccionari totes les dades de tots
   els grups. Després carregar a una llista totes les dades dels usuaris.
   Finalment ordenar i llistar.

**10-count-by-group.py [-s gid | gname | nusers ] -u usuaris -g grups**

  LListar els grups del sistema ordenats pel criteri de gname, gid o de 
  número d'usuaris.
  *Atenció* cal gestionar apropiadament la duplicitat dels usuaris en un grup.
  Requeriment: desar a la llista d'usuaris del grup tots aquells usuaris
  que hi pertanyin, sense duplicitats, tant com a grup principal com a 
  grup secundari.
