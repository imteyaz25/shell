db.products.aggregate([{$group:{_id:"$manufactorer",num_products:{$sum:1}}}])


db.products.aggregate([{$group:{_id:"$category",num_products:{$sum:1}}}])

Aggregation Pipelien
Unix : du -s *|sorting
Compund Group:
_id:{
     "manufacture":"$manufacture"
     "category": "$category"
}

sum_prices:{$sum:"$prices"}

db.zips.aggregate([{$group:{_id:"$state",population:{$sum:"$pop"}}}])


Sum:db.zips.aggregate([{$group:{_id:"$state",population:{$sum:"$pop"}}}])

Avg:db.zips.aggregate([{$group:{_id:"$state",average_pop:{$avg:"$pop"}}}])

Max: db.zips.aggregate([{$group:{_id:"$state",pop:{$max:"$pop"}}}])
Add to set :db.zips.aggregate([
{$group:
       {_id:{
	    "maker":"$manufacturer"
	    },
	    categories:{$addToSet:"$category"}
	}
}])



db.zips.aggregate([{$group: {_id:"$city",postal_codes:{$addToSet:"$_id"}}}])

push:
db.zips.aggregate([{$group: {_id:"$city",postal_codes:{$addToSet:"$_id"}}}])


use agg
db.grades.aggregate([
{'$group':{_id:{class_id:"$class_id",student_id:"$student_id"},'average':{"$avg":"$score"}}},
{'$group':{_id:"$id_class_id",'average':{"$avg":"$average"}}}
])


$project:
remove keys
add new keys
reshape keys
use some simple functions
    $toupper
    $tolower
    $add
    $multiply

use agg
db.products.aggregate([
   {$project:
     {
        _id:0,
        'maker': {$tolower:"$manufacturer"},
        'detail': {'category':"$category",
                   'price': {"$multiply":["$price",10]}
                  },
        'item': '$name'
     }
   }
])

use agg
db.zips.aggregate([
   {$project:
       {
           _id:0,
           loc:0,
           'city':{$tolower:"$city"},
           'pop':"$pop",
           'state':"$state",
           'zip':"$_id"
       }
   }
])

db.zips.aggregate([{$project:{_id:0,loc:0,'city':{$tolower:"$city"},'pop':"$pop",'state':"$state",'zip':"$_id"}}])

db.zips.aggregate([{$match:{state:"NY"}}])

db.zips.aggregate([
     {$match:
             {
                  state:"NY"
             }
     },
     {$group:
       {     _id:"$city",
            population:{$sum:"$pop"},
            zip_codes:{$addToSet:"$_id"}
       }
     }
     {$project:
       {
         _id:0,
         city:"$_id",
         population: "$population",
         zip_codes:1
       }
     }
])

db.zips.aggregate([{$sort:{"state":1,"city":1}}])

unwind: unjoin and rejoin

