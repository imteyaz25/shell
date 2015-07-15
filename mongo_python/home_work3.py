from pymongo import MongoClient
import sys
import collections

#connection to Mongo DB
try:
   connection = MongoClient()
except:
   print sys.exc_info()[0]

#database select 
db = connection.school
#select a collection "students"
collection = db.students

query = {}
selection = {'_id':1,'scores':1}
cursor =  collection.find(query,selection).sort([('scores.score',1)])
i=0
for items in cursor:
    if(items['scores'][2]> items['scores'][3]):
        print items['scores'][2], items['scores'][3]
        collection.update({'_id':items['_id']},{'$set':{'scores':[items['scores'][0], items['scores'][1], items['scores'][2]]}})
    elif(items['scores'][2]< items['scores'][3]):
        print items['scores'][3], items['scores'][2]
        collection.update({'_id':items['_id']},{'$set':{'scores':[items['scores'][0], items['scores'][1], items['scores'][3]]}})
       
    #collection.update({'_id':items['_id']},{'$set':{'scores':[items['scores'][0], items['scores'][1], items['scores'][3]]}}) 
#         for score in sorted(items['scores']):
#             if(score['type']=='homework'):
#                 homesc = score['score']
#             if(score['type']=='exam'):
#                 xyg = score['score']
#             if(score['type']=='quiz'):
#                 quizsc = score['score']
#             #if(i==0):
#                 print xyg
#                 print quizsc, homesc 
                 #collection.update({'_id':items['_id']},{'$set':{'scores':[{'score':homesc,'type':'homework'}]}})
                 #print items['_id']
                 #print sct
             #i=i+1
#        i=0
#        print "******"
