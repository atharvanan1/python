#!/usr/bin/env python3
#This is a python code to practice mathematical operators, spring operations, and lists.
#Mathematical operations
a = 5
b = 10
print(a + b)        #prints addition of two variables
print(a - b)        #prints subtraction of two variables
print(a * b)        #prints multiplicaiton of two variables
c = a / b           #experimenting
print(c*2)          #prints division of two variables
#note: This division will always be a floating point number.
print(a // b)       #truncates the fractional part
print(a % b)        #outputs remainder
print(a ** 2)       #a squared or a power 2

#String operations
print('Hello, world')           #single quoted string
print("Hello, world")           #double quoted string
print("'Hello', world")         #just a trial
print('\'Hello\', world')       #trial with escape operator
print("\"Hello, world\"")       #trial with escape operator
print("Hello, world")           #Using "".."" produces a syntax error.
print("Hello, \n world")        #newline character
print(r"I\n\i\'\''anything")    #raw string
a = input("Say something        ")      #asking for input from user
b = input("Say something more   ")      #asking for more input from user
print(a + b)                    #concatenate
print(a + "ok?")                #concatenate variable and literal
print(b + 'ok')                 #concatenate v & l again
print(a * 3 + 'hello')          #with repetition
print(b + 'hello' * 3)          #more repetition
print('''
Hi, my name is Azzentys.
I come fr\'om Earth.
You might wan\'t to try this.\n
-h [can be displayed like this]
''')                            #multiline stuff- very accurately represented.
print("""
        This is my and ""safjaslfjaslf""
        aslfj'as'd
        a;lsjfas;
        """)                    #more multiline stuff
#Slicing and manipulation operations
rando = 'Python'
print(rando[0])             #Will print 'P'
print(rando[-1])            #Will print 'n'
print(rando[0:2])           #Will slice and print 'Py'
print(rando[:2])            #slice from beginning
print(rando[2:])            #slice till the end
print(rando[-2:])            #negative count and slicing
print(rando[4:42])          #out of range
print(rando[42:])           #more out of range - prints null

#List operations
X = [1, 2, 3, 4, 5]
print(X[1])                 #same operations like strings
print(X[:])                 #prints whole list
X.append(4)                 #adding new element to the list
print(X[:])                     
len(X)                      #gives length of a sequence
a = [1, 3, 5, 6]
z = [a, X]                  #Nested lists
print(z)
