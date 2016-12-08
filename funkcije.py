import sqlite3
import random

con = sqlite3.connect('racunalniske_igre.db')

def seznam_podjetij():
    sql = '''
    SELECT ime
    FROM podjetja  
          '''
    imena = []
    for (ime,) in con.execute(sql):
        imena.append(ime)
    return imena

#print(seznam_podjetij())

def seznam_uporabnikov():
    sql = '''
    SELECT up_ime
    FROM uporabnik  
          '''
    uporabniki = []
    for (up_ime,) in con.execute(sql):
        uporabniki.append(up_ime)
    return uporabniki

def sez_imen_let(vhodna):
    dat = open(vhodna)
    seznam = []
    for vrstica in dat:
        pod = vrstica.split(',')
        seznam.append(pod)
    return seznam
    
print(sez_imen_let('igraLeto.txt'))

##def vstaviVigro(vhodna,izhodna):
##    izpis = "INSERT INTO igra (ime,leto, uporabnik, zaloznik, razvijalec) VALUES ("
##    podatki = []
##    f = open(izhodna,'w')
##    uporabniki = seznam_uporabnikov()
##    podjetja = seznam_podjetij()
##    for vrstica in open(vhodna):
##        pod = vrstica.split(',')
##        ime = pod[0]
##        leto = pod[1]
##        uporabnik = random.choice(uporabniki)
##        zaloznik = random.choice(podjetja)
##        razvijalec = random.choice(podjetja)
##        izpis += ime + "," + leto + "," + uporabnik + "," + zaloznik + "," + razvijalec+ ")"
##        print(izpis, file=f)
##
##vstaviVigro('igraLeto.txt', 'igra.txt')
        
        
        
        
    
