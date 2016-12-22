from bottle import route, run, template
import modeli

@route('/')
def index():
    return 'Pozdravljeni'

@route('/pomoc/')
def pomoc():
    return 'Pojdi na stran...'

run()
