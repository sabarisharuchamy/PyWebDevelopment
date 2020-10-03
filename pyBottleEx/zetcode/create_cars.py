from pymongo import MongoClient

cars = [ {'name': 'Audi', 'price': 52642},
    {'name': 'Mercedes', 'price': 57127},
    {'name': 'Skoda', 'price': 9000},
    {'name': 'Volvo', 'price': 29000},
    {'name': 'Bentley', 'price': 350000},
    {'name': 'Citroen', 'price': 21000},
    {'name': 'Hummer', 'price': 41400},
    {'name': 'Volkswagen', 'price': 21600} ]

client = MongoClient('mongodb://localhost:27017/')

with client:
    #db = client.testdb
    #db.cars.insert_many(cars)
    #print(client.list_database_names())
    mydb = client["testdb"]
    mycol = mydb["customers"]
    #print(mydb.list_collection_names())
    #mydict = { "name": "John", "address": "Highway 37" }
    #mycol.insert_one(mydict)
    #print(mydb.list_collection_names())
##    mylist = [{ "_id": 1, "name": "John", "address": "Highway 37"},
##              { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
##              { "_id": 3, "name": "Amy", "address": "Apple st 652"},
##              { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
##              { "_id": 5, "name": "Michael", "address": "Valley 345"},
##              { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
##              { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
##              { "_id": 8, "name": "Richard", "address": "Sky st 331"},
##              { "_id": 9, "name": "Susan", "address": "One way 98"},
##              { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
##              { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
##              { "_id": 12, "name": "William", "address": "Central st 954"},
##              { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
##              { "_id": 14, "name": "Viola", "address": "Sideway 1633"}]
##    mycol.insert_many(mylist)
##    for x in mycol.find({},{ "address": 0 }):
##      print(x)
    myquery = { "address": { "$gt": "S" } }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)  
