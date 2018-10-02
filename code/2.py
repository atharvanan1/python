#!/usr/bin/env python3
#This is a python code to practice mathematical operators and limited string operations.
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

