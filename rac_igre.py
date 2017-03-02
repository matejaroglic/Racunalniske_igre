from bottle import route, run, template, request, response, post, redirect
from bottlesession import session
from modeli import *

sess = session()
sess.set("up_id", None)

@post('/')
def prijavarequest():
    if request.forms.gumb == 'registracija':
        dodaj_uporabnik(request.forms.up_ime, request.forms.geslo)
        redirect('/')
    if request.forms.gumb == 'vpis':
        up_ime = request.forms.up_ime
        geslo = request.forms.geslo
        up_id = prijava(up_ime, geslo)
        if up_id is None:
            redirect('/pomoc/')
        else:
            sess.set("up_id", up_id)
            redirect('/')
    if request.forms.gumb == 'odjava':
        sess.set("up_id", None)
        redirect('/')

@route('/pomoc/')
def pomoc():
    return 'Narobe ste vnesli geslo.'

@route('/dodaj_uporabnika/')
def dodajuporabnika():
    return template('dodaj_uporabnika')

@post('/dodaj_uporabnika/')
def dodajuporabnika():
    up = request.forms.up_ime
    pas = request.forms.geslo
    if not aliVBazi(up):
        dodaj_uporabnika(up,pas)
    return redirect('/dodaj_uporabnika/')
    

@route('/')
def domaca_stran():
    return template(
        'domaca_stran',
        igre = topDeset(),
        up_id = sess.read('up_id'),
        upor_ime = vrni_imeUp(sess.read("up_id"))
    )

@route('/vec/')
def pomoc():
    return 'Pojdi na stran...'


@route('/igra/<id_igre:int>/')
def vec_o_igri(id_igre):
    return template(
        'vec_o_igri',
        ocenil = aliOcenil(sess.read('up_id'),id_igre),
        up = sess.read('up_id'),
        id_igre = id_igre,
        podatki = podatkiOigri(id_igre),
        razvijalec = razvijalecIgra(id_igre),
        platforme=igraPlatforme(id_igre),
        zvrsti=igraZvrsti(id_igre),
        komentarji = komentarjiIgre(id_igre),
        povpOcena = povprecna_ocena(id_igre)
            )

@post('/igra/<id_igre:int>/')
def ocena_kom(id_igre):
    if request.forms.izbira != "" and sess.read('up_id') != None:
        dodaj_oceno(id_igre, sess.read('up_id'), request.forms.izbira)
    if request.forms.komentar != "" and sess.read('up_id') != None:
        dodaj_komentar(request.forms.komentar, sess.read('up_id'), id_igre)
    redirect('/igra/{}/'.format(id_igre))

@route('/dodaj_igro')
def dodaj_igro():
    return template(
        'dodaj_igro',
        zvrsti = seznam_zvrsti(),
        platforme = seznam_platform()
        )

@post('/dodaj_igro')
def dodaj_igro_post():
    ime = request.forms.ime_igre
    leto = request.forms.leto
    razvijalec = request.forms.razvijalec
    zaloznik = request.forms.zaloznik
    uporabnik = sess.read('up_id')
    platforme = request.forms.getall("platforme")
    zvrsti = request.forms.getall("zvrsti")
    if ime != None and uporabnik != None and leto != None:
        dodaj_igro_v_bazo(ime, leto, razvijalec, zaloznik, uporabnik, platforme, zvrsti) 



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
