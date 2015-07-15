from pymongo import MongoClient
import sys

#connection to Mongo DB
try:
   connection = MongoClient()
except:
   print sys.exc_info()[0]

#database select 
db = connection.students
#select a collection "grades"
collection = db.grades

query = {'type':'homework'}
selection = {'student_id':1, 'score':1}
cursor =  collection.find(query, selection).sort([('student_id',1),('score',1)])

std=-1
inc=0
for grade in cursor:
    if(grade['student_id']==std):
        inc = inc+1
        print "Double"
    else:
       std=grade['student_id']
       print std 
       collection.remove({'student_id':grade['student_id'], 'score':grade['score']})
