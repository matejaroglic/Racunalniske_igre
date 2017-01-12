from bottle import route, run, template, request, response, post
from bottlesession import session
from modeli import *

sess = session()
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

@route('/pomoc/')
def pomoc():
    return 'Narobe ste vnesli geslo.'

@route('/dodaj_uporabnika/')
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


@route('/')
def domaca_stran():
    return template(
        'domaca_stran',
        igre = topDeset()
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
###iukaj dobimo up. ime trenutno prijavljenega uporabnika
##@route('/counter')
##def counter():
##    count = int( request.cookies.get('counter', '0') )
##    count += 1
##    response.set_cookie('counter', str(count))
##    return 'You visited this page %d times' % count


run(debug=True)
