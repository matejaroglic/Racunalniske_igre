<<<<<<< HEAD
from bottle import route, run, template, request, response, post, redirect
=======
from bottle import route, run, template, request, response, post
>>>>>>> 7d0c47359bd1996773e69c95fef7a6f63440c20a
from bottlesession import session
from modeli import *

sess = session()
<<<<<<< HEAD
sess.set("up_id", None)

@post('/')
def prijavarequest():
    if request.forms.gumb == 'registracija':
        pass#dodajuporabnika!
    else:
        up_ime = request.forms.up_ime
        geslo = request.forms.geslo
        print(up_ime, geslo)
        up_id = prijava(up_ime, geslo)
        if up_id is None:
            redirect('/pomoc/')
        else:
            sess.set("up_id", up_id)
            redirect('/')

=======
sess.set("uporabnik", "")

@post('/')
def prijavare():
    upIme = request.forms.up_ime
    geslo = request.forms.geslo
    aliPravo = prijava(up_ime,geslo)
    #print(upIme,geslo,aliPravo)
##    if aliPravo is not None:
##        (sektor,stSek) = modeli.poisciSektor(upIme) ##vrnemo sektor in st vseh sektorjev za zanko,
##                                            ##ce se v prihodnosti odločimo, da dodamo še kak sektor
##        sess.set('upIme', upIme)
##        sess.set('sektor', sektor)
##        return redirect('/{0}/'.format(sektor))
##    else:
##        return redirect('/pomoc/')
>>>>>>> 7d0c47359bd1996773e69c95fef7a6f63440c20a

@route('/pomoc/')
def pomoc():
    return 'Narobe ste vnesli geslo.'

@route('/dodaj_uporabnika/')
<<<<<<< HEAD
def dodajuporabnika():
    return template('dodaj_uporabnika')

@post('/dodaj_uporabnika/')
def dodajuporabnika():
    up = request.forms.up_ime
    pas = request.forms.geslo
    if not aliVBazi(up):
        dodaj_uporabnika(up,pas)
        
            
    return redirect('/dodaj_uporabnika/')
    
##@route('/prijava/')
##def prijava():
##    return template('prijava')
=======
def dodaj_uporabnika():
    return template('dodaj_uporabnika')

@post('/dodaj_uporabnika/')
def dodaj_uporabnika():
    up = request.forms.uporabnik
    pas = request.forms.geslo
    if up and pas:
        dodaj_uporabnika(up,pas)
            
    return redirect('/dodaj_uporabnika/')
    
@route('/prijava/')
def prijava():
    return template('prijava')
>>>>>>> 7d0c47359bd1996773e69c95fef7a6f63440c20a


@route('/')
def domaca_stran():
    return template(
        'domaca_stran',
        igre = topDeset(),
        up_id = sess.read('up_id')
    )

@route('/vec/')
def pomoc():
    return 'Pojdi na stran...'

@route('/igra/<id_igre:int>/')
def vec_o_igri(id_igre):
    return template(
        'vec_o_igri',
        podatki =podatkiOigri(id_igre),
        razvijalec = razvijalecIgra(id_igre),
        platforme=igraPlatforme(id_igre),
        zvrsti=igraZvrsti(id_igre),
        komentarji = komentarjiIgre(id_igre)#dodal, komentar, datum

    )

@route('/dodajKomentar')
def dodajKomentar():
    return template(
        'dodajKomentar'
        )

#@post('dodajKomentar')
#def ...
#    modeli.dodajKomentar(idIgre, vsebina, sess.read('up_id'))

@route('/iskanje/')
def rezultati_iskanja():
    return template(
        'rezultati_iskanja',
        rezultati = seznamPoizvedba(request.query.iskanje)
        
    )

@route('/vse_igre')
def vse_igre():
    return template(
        'vse_igre',
        igre = sez_iger()
        
    )

run(debug=True)
