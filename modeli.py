import sqlite3

con = sqlite3.connect('racunalniske_igre.db')
con.row_factory = sqlite3.Row

def seznam_podjetij():
    sql = '''
    SELECT id, ime
    FROM podjetja order by id
    '''
    return list(con.execute(sql))

##a = seznam_podjetij()
##print(a[0]["ime"])
##print(dict(a[0]))

def seznam_uporabnikov():
    sql = '''
    SELECT id, up_ime, geslo
    FROM uporabnik  
          '''
    return list(con.execute(sql))

b = seznam_uporabnikov()
#print(b[]
##print(dict(b[0]))

def sez_iger():
    sql= '''
    SELECT id, ime, leto, uporabnik, zaloznik, razvijalec
    FROM igra
    '''
    return list(con.execute(sql))

##c=sez_iger()
##print(dict(c[0]))

def seznam_platform():
    sql = '''SELECT id, katera FROM platforma '''
    return list(con.execute(sql))

d=seznam_platform()
##print(dict(d))
##print(dict(d[0]))

def seznam_zvrsti():
    sql = '''SELECT id, ime FROM zvrst'''
    return list(con.execute(sql))

##e =seznam_zvrsti()
##print(dict(e[0]))

def povprecna_ocena(igra):
    sql = '''SELECT AVG(koliko) AS povp FROM ocena WHERE igra = ?'''
    return con.execute(sql, [igra]).fetchone()["povp"]

def topDeset():
    sql = '''SELECT igra.ime,
               avg(ocena.koliko) AS ocena
          FROM igra
               JOIN
               ocena ON igra.id = ocena.igra
         GROUP BY igra.ime
         ORDER BY ocena DESC
         LIMIT 10'''
    top = []
    for (igra, ocena) in con.execute(sql):
        top.append((igra, ocena))
    return top

#print(topDeset())
    
def igreZBesedo(beseda):
    '''vrne vse igre, ki v imenu vsebujejo besedo'''
    sql = '''SELECT ime
          FROM igra
          WHERE ime LIKE "%{}%"'''.format(beseda)
    return list(con.execute(sql))

##print(igreZBesedo("As"))
##b= igreZBesedo("As")
##print(dict(b[0]))

def komentarjiIgre(igra):
    '''za igro vrne vse dodane komentarje, kdo je komentiral
    in datum komentarja'''
    sql = '''SELECT uporabnik.up_ime AS dodal,
               komentar.vsebina AS komentar,
               komentar.datum AS datum
          FROM komentar
               JOIN
               igra ON komentar.igra = igra.id
               JOIN
               uporabnik ON komentar.uporabnik = uporabnik.id
         WHERE igra.ime = ?'''
    return list(con.execute(sql, [igra]))

##a = komentarjiIgre("Fallout")
##print(a[0]["komentar"])
##print(dict(a[0]))


