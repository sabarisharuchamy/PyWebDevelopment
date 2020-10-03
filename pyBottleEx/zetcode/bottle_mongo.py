from bottle import route, run, HTTPResponse
from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')

@route('/cars')
def getcars():

    db = client.testdb
    cars = list(db.cars.find({}, {'_id': 0}))

    if cars:

        return json.dumps(cars)
    else: 
        raise HTTPResponse(status=204)

run(host='localhost', port=8000, debug=True)
