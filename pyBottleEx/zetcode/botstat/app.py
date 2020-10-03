from bottle import route, run, static_file

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./public/')

run(host='localhost', port=8000, debug=True)
