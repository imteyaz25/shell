<html>
<head><title>Yahoo first bottle application</title></head>
<body>
<p>Username : {{username}}</p>
<ul>
%for thing in things:
   <li> {{thing}}</li>
%end
</ul>
<p>
<form action="/favorite_fruit" method="POST">
What is your favorite fruit:
<input type="text" name="fruit" size="40" value="" /><br/>
<input type="submit" value="Submit" />
</form>
</p>
</body>
</html>
