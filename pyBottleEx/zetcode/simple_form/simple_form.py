from bottle import route, run, post, request, static_file, error

@route('/')
def server_static(filepath="index.html"):
    return static_file(filepath, root='./public/')

@post('/doform')
def process():

    name = request.forms.get('name')
    occupation = request.forms.get('occupation')
    return "Your name is {0} and you are a(n) {1}".format(name, occupation)

@error(404)
def error404(error):
    return '404 - the page u requested doesnt exit naturally'

run(host='localhost', reloader=True, port=8000, debug=True)
