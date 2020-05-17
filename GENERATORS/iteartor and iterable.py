Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[1,2,3,4]
>>> it=iter(x)
>>> it
<list_iterator object at 0x03D4B1D8>
>>> for i in it:
	ptint(i)

	
Traceback (most recent call last):
  File "<pyshell#5>", line 2, in <module>
    ptint(i)
NameError: name 'ptint' is not defined
>>> for i in it:
	print(i)

	
2
3
4
>>> for j in it:
	print(j)

	
>>> 
>>> x=[1,2,3,4]
>>> for i in x:
	print(i)
	for j in x:
		print(j)

		
1
1
2
3
4
2
1
2
3
4
3
1
2
3
4
4
1
2
3
4
>>> x=[1,2,3,4,5]
>>> xi=iter(x)
>>> for in xi:
	
SyntaxError: invalid syntax
>>> for i in xi:
	print(i)
	for j in xi:
		print(j)

		
1
2
3
4
5
>>> for iin xi:
	
SyntaxError: invalid syntax
>>> for i in xi:
	print(next(i))

	
>>> next(xi)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    next(xi)
StopIteration
>>> x=iter(1,2,3)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    x=iter(1,2,3)
TypeError: iter expected at most 2 arguments, got 3
>>> x=(1,2,3,4)
>>> xi=iter(x)
>>> next(xi)
1
>>> next(xi)
2
>>> for i in xi:
	print(i)

	
3
4
>>> 