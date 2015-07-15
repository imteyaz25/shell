use school;
var id;
var types= ['exam', 'homework', 'quiz'];
for(var id =0; id<100;id++)
{
	for(type=0;type<3;type++)
	{
		var r = {'student_id':id,'type':types[type],'score':id};
                printjson(r);
		db.scores.insert(r);
	}

}
