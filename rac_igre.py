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

@route('/dodajKomentar')
def dodajKomentar():
    return template(
        'dodajKomentar'
    )
###iukaj dobimo up. ime trenutno prijavljenega uporabnika
##@route('/counter')
##def counter():
##    count = int( request.cookies.get('counter', '0') )
##    count += 1
##    response.set_cookie('counter', str(count))
##    return 'You visited this page %d times' % count


run(debug=True)
