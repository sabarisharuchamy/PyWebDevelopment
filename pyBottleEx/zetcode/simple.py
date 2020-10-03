from bottle import route, run, request, get

@route('/')
def hello():
    return "This is my starting page"  

@route('/message')
def hello():
    return "Today is a rainy day"

@route('/cars')
def getcars():

    cars = [ {'name': 'Audi', 'price': 52642},
        {'name': 'Mercedes', 'price': 57127},
        {'name': 'Skoda', 'price': 9000},
        {'name': 'Volvo', 'price': 29000},
        {'name': 'Bentley', 'price': 350000},
        {'name': 'Citroen', 'price': 21000},
        {'name': 'Hummer', 'price': 41400},
        {'name': 'Volkswagen', 'price': 21600} ]

    return dict(data=cars)

@get('/msg')
def message():

    name = request.query.name
    age = request.query.age

    return "{0} is {1} years old".format(name, age)

run(host='localhost', port=8000, debug=True,reloader=True)
