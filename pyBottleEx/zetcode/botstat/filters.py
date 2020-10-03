from bottle import route, run

@route('/app/<myid:int>/')
def provide(myid):
    return "Object with id {} returned".format(myid)

@route('/app/<name:re:[a-z]+>/')
def provide(name):
    return "Name {} given".format(name)    

run(host='localhost', port=8000, debug=True)
