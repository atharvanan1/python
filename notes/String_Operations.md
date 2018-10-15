# This file explains string operations till string manipulations.

### String Operations p1

Strings can be enclosed in following ways:  
`'..'`		single quotes
`".."`		double quotes

Use \ to escape quotes.  
Ex.  
	`"\'Hello, world\'"` will output as 'Hello, world'  
	`"\"Hello, world\""` will output as "Hello, world"  
	`'\'Hello, world\''` will output as 'Hello, world'  
	`'\"Hello, world\"'` will output as "Hello, world"  
	`''Hello, world''` will output as syntax error  
	`""Hello, world""` will output as syntax error  
	`'"Hello, world"'` will output as "Hello, world"  
	`"'Hello, world'"` will output as 'Hello, world'

`\n` 		new line character  
`r`		raw string Ex. `print(r"\n")` will print \n  
`'''...'''`	multiline output  
`'"""..."""`	multiline output  
`*`		repeat
`+`		concatenate
`'..''..'`	side-by-side concatenate, only for literals  
`word[n]`	gives out nth element of the string, counting starts from zero  
`word[-n]`	gives out nth element from behind, counting last as 1  
`word[x:y]`	slices the string from x to y, where yth element isn't included  
`word[x:]`	slices the string from x to the end  
`word[:y]`	slices the string from beginning to y, where yth element isn't included  
`word[-2:]`	slices the string from -2 to the end  
Python handles out of range arguments in slicing very well. It would give output till the end, while out of range part will be given as null.  
`word[2:42]`	assuming string length is 5, this would be equivalent to `word[2:]`  
`word[43:]`	assuming string length is 5, this would give null string as output  
`len(string_name)`	gives string length  

`End-of-document`

**See ya!**
