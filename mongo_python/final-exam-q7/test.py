from pymongo import MongoClient
import sys
import collections

#connection to Mongo DB
try:
   connection = MongoClient()
except:
   print sys.exc_info()[0]

#database select
db = connection.blog
#select a collection "students"

query = {}
selection = {'_id':1, 'images':1}
all_albums =  db.albums.find(query,selection)

q={}
s={'_id':1}
all_images = db.images.find(q,s)
i=0

def in_album(img):
   flag =0
   for alb in all_albums:
       if img in alb['images']:
          flag=alb['_id']
   return flag

for image in all_images:
     image_id = image['_id']
     flg = in_album(image_id)
     print flg
     print image_id
     #if flg == 1:
     #   print "Not in array"
     #   continue

#flg = in_album(1)
#print flg
