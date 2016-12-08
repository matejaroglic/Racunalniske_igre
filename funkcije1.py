import sqlite3
import random

con = sqlite3.connect('racunalniske_igre.db')

def seznam_podjetij():
    sql = '''
    SELECT id
    FROM podjetja  
          '''
    imena = []
    for (ime,) in con.execute(sql):
        imena.append(ime)
    return imena
#print(seznam_podjetij())

def seznam_uporabnikov():
    sql = '''
    SELECT id
    FROM uporabnik  
          '''
    uporabniki = []
    for (up_ime,) in con.execute(sql):
        uporabniki.append(up_ime)
    return uporabniki
#print(seznam_uporabnikov())
def sez_iger():
    sql= '''
    SELECT id
    FROM igra
    '''
    imena = []
    for (ime,)in con.execute(sql):
        imena.append(ime)
    return imena

print(sez_iger())

def sez_imen_let(vhodna):
    dat = open(vhodna)
    seznam = []
    for vrstica in dat:
        vrst = vrstica.strip()
        pod = vrst.split(',')
        pod[1] = int(pod[1])
        seznam.append(pod)
    return seznam

def vnesi_igra():
    ime_leto = sez_imen_let('igraLeto.txt')
    uporabniki = seznam_uporabnikov()
    podjetja = seznam_podjetij()
    sql = '''INSERT INTO igra (ime, leto, uporabnik, zaloznik, razvijalec)
             VALUES (?,?,?,?,?)'''
    for ime,leto in ime_leto:
        uporabnik = random.choice(uporabniki)
        zaloznik = random.choice(podjetja)
        razvijalec = random.choice(podjetja)
        values = (ime, leto, uporabnik, zaloznik, razvijalec)
        print(values)
        con.execute(sql, values)
    con.commit()
#vnesi_igra()


    
    




        
        
        
        
    
