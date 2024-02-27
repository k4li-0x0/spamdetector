from bottle import route, template, abort

@route('/')
def index():
    return template('index.html')


@route('/getmessage')
def getmessage():
    abort(501)


@route('/setlabel/<id:int>')
def setlabel(id):
    abort(501)
