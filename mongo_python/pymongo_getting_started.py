import pymongo

from pymongo import MongoClient

#connect to database
connection = MongoClient('localhost', 27017)

db = connection.test

#handles to name collections
name = db['name']

item = name.find_one()

print item['name']
