import sqlite3
import hashlib

con = sqlite3.connect('racunalniske_igre.db')
con.row_factory = sqlite3.Row

def najdi_podjetje(ime):
    sql = '''
    SELECT id
    FROM podjetja
    WHERE ime = ?
    '''
    print(ime)
    id = con.execute(sql, [ime]).fetchone()
    if id is None:
        sql = '''insert into podjetja (ime) values (?)'''
        id = con.execute(sql, [ime]).lastrowid
        con.commit()
        return id
    return id[0]

def seznam_uporabnikov():
    sql = '''
    SELECT id, up_ime, geslo
    FROM uporabnik  
          '''
    return list(con.execute(sql))

def vrni_imeUp(idUp):
    '''vrne ime uporabnika, ki ima id enak idUp'''
    sql = '''select up_ime from uporabnik where id = ?'''
    if idUp is not None:
        return con.execute(sql, [idUp]).fetchone()["up_ime"]

print(vrni_imeUp(104))

def sez_iger():
    sql= '''
    SELECT id, ime, leto, uporabnik, zaloznik, razvijalec
    FROM igra
    '''
    return list(con.execute(sql))

def seznam_platform():
    sql = '''SELECT id, katera FROM platforma '''
    return list(con.execute(sql))

def seznam_zvrsti():
    sql = '''SELECT id, ime FROM zvrst'''
    return list(con.execute(sql))

def topDeset():
    '''vrne prvih 10 iger z najboljšo povprečno oceno'''
    sql = '''SELECT igra.id, igra.ime,
               avg(ocena.koliko) AS ocena
          FROM igra
               JOIN
               ocena ON igra.id = ocena.igra
         GROUP BY igra.ime
         ORDER BY ocena DESC
         LIMIT 10'''
    return list(con.execute(sql))

    
def IsciZBesedo(beseda):
    '''vrne vse igre, ki v imenu vsebujejo besedo'''
    vzorec = '%{}%'.format(beseda)
    sql = '''SELECT igra.ime as ime
          FROM igra
          WHERE ime LIKE ?"'''
    return list(con.execute(sql, [vzorec]))

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
         WHERE igra.id = ?'''
    return list(con.execute(sql, [igra]))


def seznamPoizvedba(beseda):
    '''za iskanje iger, ki imajo v imenu ali drugih komponentah niz beseda''' 
    vzorec = '%{}%'.format(beseda)
    sql ='''SELECT DISTINCT igra.ime AS ime, igra.id AS id
  FROM igra
       JOIN
       platforma_igra ON igra.id = platforma_igra.igra
       JOIN
       platforma ON platforma_igra.platformA = platforma.id
       JOIN
       podjetja AS zalozniki ON zalozniki.id = igra.zaloznik
       JOIN
       podjetja AS razvijalci ON razvijalci.id = igra.razvijalec
       JOIN
       uporabnik ON uporabnik.id = igra.uporabnik
       JOIN
       zvrst_igra ON igra.id = zvrst_igra.igra
       JOIN
       zvrst ON zvrst_igra.zvrst = zvrst.id
 WHERE (igra.ime LIKE ?) OR 
       (platforma.katera LIKE ?) OR 
       (razvijalci.ime LIKE ?) OR 
       (zalozniki.ime LIKE ?) OR 
       (uporabnik.up_ime LIKE ?) OR 
       (zvrst.ime LIKE ?);'''
    return list(con.execute(sql,[vzorec, vzorec, vzorec, vzorec, vzorec, vzorec]))

def zvrstiIgra(zvrst):
    '''vrne igre zvrsti zvrst'''
    sql = '''SELECT igra.ime AS igra
          FROM igra
               JOIN
               zvrst_igra ON igra.id = zvrst_igra.igra
               JOIN
               zvrst ON zvrst_igra.zvrst = zvrst.id
         WHERE zvrst.ime = ?'''
    return list(con.execute(sql))
    
def igraPlatforme(igra):
    '''vrne platforme igre igra'''
    sql = '''SELECT platforma.katera AS platforma
          FROM platforma
               JOIN
               platforma_igra ON platforma.id = platforma_igra.platforma
               JOIN
               igra ON platforma_igra.igra = igra.id
         WHERE igra.id = ?'''
    return list(con.execute(sql, [igra]))

#execute vrne iterator
def igraZvrsti(igra):
    sql = '''SELECT zvrst.ime AS zvrst
          FROM zvrst
               JOIN
               zvrst_igra ON zvrst.id = zvrst_igra.zvrst
               JOIN
               igra ON zvrst_igra.igra = igra.id
         WHERE igra.id = ?'''
    return list(con.execute(sql, [igra]))


def podatkiOigri(igra):
    '''vrne ime, leto, založnika, uporabnika igre'''
    sql = '''SELECT igra.ime AS ime,
       igra.leto AS leto,
       podjetja.ime AS zaloznik,
       uporabnik.up_ime AS uporabnik
  FROM igra
       JOIN
       podjetja ON igra.zaloznik = podjetja.id
       JOIN
       uporabnik ON igra.uporabnik = uporabnik.id
 WHERE igra.id = ?'''
    return con.execute(sql, [igra]).fetchone()

def razvijalecIgra(igra):
    '''vrne  razvijalca igre'''
    sql = '''SELECT podjetja.ime AS razvijalec
  FROM podjetja
       JOIN
       igra ON igra.razvijalec = podjetja.id
 WHERE igra.id = ?'''
    return con.execute(sql, [igra]).fetchone()


def povprecna_ocena(igra):
    sql = '''SELECT AVG(koliko) AS povp FROM ocena WHERE igra = ?'''
    if con.execute(sql, [igra]).fetchone()["povp"] is not None:
        return round(con.execute(sql, [igra]).fetchone()["povp"],2)
    else:
        return "Igra še nima ocene."


##Od tu naprej
def kodirajGeslo(geslo):
    '''vrne zakodirano geslo'''
    return hashlib.md5(geslo.encode()).hexdigest()

def prijava(up_ime,geslo):
    sql = '''
        select id
        from uporabnik
        where up_ime = ?
          and geslo = ?;
          '''
    oseba = con.execute(sql, [up_ime, kodirajGeslo(geslo)]).fetchone()
    if oseba:
        return oseba['id']
    
def aliVBazi(up_ime):
    sql = '''select up_ime from uporabnik
    where up_ime == ?'''
    if con.execute(sql, [up_ime]).fetchone():
        return True
    return False

def aliOcenil(upId, igraId):
    '''vrne 1, če je uporabnik že ocenil igro in 0, če je ni'''
    sql = '''SELECT count(*)
          FROM ocena
          WHERE uporabnik = ? AND 
          igra = ?'''
    return con.execute(sql,[upId,igraId]).fetchone()[0]
    
print(aliOcenil(14, 63))

###Dodajanje v bazo

def dodaj_uporabnik(up_ime,geslo):
    if not aliVBazi(up_ime):
        sql =   '''
                 insert into uporabnik
                 (up_ime,geslo)
                 values (?,?)
                '''
        con.execute(sql,[up_ime,kodirajGeslo(geslo)])
        con.commit()

def dodaj_komentar(vsebina, uporabnik, igra):
    sql = '''INSERT INTO komentar (vsebina, uporabnik, igra, datum)
           VALUES (?,?,?, DATE('now'))'''
    con.execute(sql, [vsebina, uporabnik, igra])
    con.commit()
    
def dodaj_oceno(igra, uporabnik, koliko):
    sql = '''INSERT INTO ocena (igra, uporabnik, koliko)
           VALUES (?,?,?)'''
    con.execute(sql, [igra, uporabnik, koliko])
    con.commit()

    
def dodaj_igro_v_bazo(ime, leto, razvijalec, zaloznik, uporabnik, platforme, zvrsti):
    zid = najdi_podjetje(zaloznik)
    rid = najdi_podjetje(razvijalec) 
    
    sql ='''INSERT INTO igra (ime, leto, razvijalec, zaloznik, uporabnik)
       VALUES (?,?,?,?,?)'''
    
    cur = con.execute(sql, [ime, leto, rid, zid, uporabnik])
    id = cur.lastrowid
    sql2 = '''insert into platforma_igra (igra, platforma) VALUES (?, ?)'''
    for pl in platforme:
        con.execute(sql2, [id, pl])
    sql3 = '''insert into zvrst_igra (igra, zvrst) VALUES (?, ?)'''
    for zv in zvrsti:
        con.execute(sql3, [id, zv])
    con.commit()

