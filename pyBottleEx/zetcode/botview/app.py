from bottle import route, run, template, HTTPResponse
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

@route('/cars')
def getcars():

    db = client.testdb
    data = db.cars.find({}, {'_id': 0})

    if data:

        return template('show_cars', cars=data)
    else: 
        return HTTPResponse(status=204)


run(host='localhost', port=8000, debug=True)
