#This file explains usage of underscore in python.

###Underscore usage

Underscore `_` character can be used for following :
1. In interactive mode, it can be used to get last output value.
2. It can be used to ignore the values  
	Ex.
	1. `x,_,y = (1, 2, 3)` will result into x = 1, y = 3, while ignoring 2.  
	2. `x, *_, y = (1, 2, .., 10)` will result into x = 1, y = 10, while ignoring rest of the values.  
	3. `for _ in range(10): do_something()` will ignore the index  
	4. `for _, val in list: do_something()` will ignore a value of specific location  
3. It can be used to give special meanings to name of variables and functions. (convention)  
`_single_leading_underscore` 			- for private variables, functions, methods and classes in module.  
`single_trailing_underscore_` 			- for avoiding conflict with python keywords and built-ins.  
`__double_leading_underscore` 			- for unknown use.  
`__double_leading_and_trailing_underscore__` 	- for special variables or methods such as `__init__`, `__len__`, `__file__`, `__eq__`.  
4. Seperate digits of number literal values just for increased readability. Ex - `a = 1_000_000`  

This is all about Underscore usage.

`End-of-document`

**See ya!**
