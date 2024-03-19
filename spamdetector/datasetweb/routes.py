from bottle import route, template, static_file
from .data import get_message, set_label, dump_all, dump_path


@route('/')
def index():
    return template('index.html')


@route('/getmessage')
def api_getmessage():
    msg = get_message()
    return {'message': msg['message'], 'id': msg['id']}


@route('/setlabel/<id:int>/<label:int>')
def api_setlabel(id = None, label = None):
    api_getmessage.operations_counter += 1
    if api_getmessage.operations_counter > 100:
        dump_all()
        api_getmessage.operations_counter = 0
    set_label(id, label)


@route('/dump')
def api_dump():
    dump_all()
    return static_file(dump_path.name, dump_path.parent.absolute(), download='dump.csv')


api_getmessage.operations_counter = 0
    
