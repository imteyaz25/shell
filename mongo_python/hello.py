import bottle
import pymongo

#This is the handler for the default path of the web server

@bottle.route('/')
def index():

    #connect to MongoDB
    connection = pymongo.MongoClient('localhost', 27017)
    #attach to the test database
    db = connection.test

    #get handle for name collection
    name = db['name']
    
    #find a single document
    item = name.find_one()

    return '<b>Hello %s!</b>' % item['name']

bottle.run(host='localhost', port=8082)
