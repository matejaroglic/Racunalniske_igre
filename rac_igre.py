from bottle import route, run, template, request, response
from modeli import*

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
