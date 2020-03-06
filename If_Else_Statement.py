#Boolean Expression

print(20 > 10)
print(20 == 10)
print(20 < 10)
print(bool("Hellow World"))
print(bool(20))


python Contitions

Equals 						-> x == y
Not Equals					-> x != y					
Less than					-> x < y
less than or equal to 		-> x <= y
Greater than				-> x > y
Greater than or equal to	-> x >= y
Boolean OR 					-> x or y , x | y
Boolean AND					-> x and y , x & y
Boolean Not 				-> not y

x = 70
>>> y = 60
>>> if x > y:
...     print("x is greater than y")
... else:
...     print("x is not greater than y")
...
x is greater than y

if x < y:
...     print("x is greater than y")
... else:
...     print("x is not greater than y")
...
x is not greater than y

x is not greater than y
>>> if x > y :
...  print ("x is greater than y")
... elif x >= y:
...     print ("x is greater than or equal to y")
... elif y < x:
...     print ("y is smaller than x")
... else:
...     print("x is nothing")
...
x is greater than y

 if x == y:
...     print("Answer 1")
... elif x < y:
...     print ("Answer 2")
... elif x <= y:
...     print ("Answer 3")
... else:
...     print("default")
...
default

>>> x = 50
>>> y = 150
>>> if x > y: print("x is greater than y")
... elif x == y: print ("x and y are equal")
... else: print("x is less than y")
...
x is less than y

>>> x = 50
>>> y = 40
>>> z = 100
>>> if x > y or z < y:
...     print ("one of the conditions is True")
... elif x > y and z > y:
...     print ("All conditions are True")
... else:
...     print ("nothing else")
...
one of the conditions is True

 if x > y and z > y and z > x:
...     print("Answer 1")
... elif x == y or z == y or z > y and x > y:
...     pritnt("Answer 2")
... elif z > y and y < x or z > y:
...     print("Answer 3")
... else:
...     print("Default")
...
Answer 1

x = 50 

if x > 10:
	print("x is ten")
	if x > 28:
		print("x is greater than 20")
	else:
		print("No,x is not greater than 20")
if x > 10 and x != 10 or x > 20:

	print("x is greater than 10 and 20")
else:
	print("x is not greater than 10 & 20")