from bottle import route, run, template, request, response
import modeli

@route('/')
def domaca_stran():
    return template(
        'domaca_stran',
        igre = topDeset()
    )

@route('/pomoc/')
def pomoc():
    return 'Pojdi na stran...'

###iukaj dobimo up. ime trenutno prijavljenega uporabnika
##@route('/counter')
##def counter():
##    count = int( request.cookies.get('counter', '0') )
##    count += 1
##    response.set_cookie('counter', str(count))
##    return 'You visited this page %d times' % count


run()
