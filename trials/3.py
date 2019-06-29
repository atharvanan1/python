#!/usr/bin/env python3

# This files has code for few of the control structures.

# IF STATEMENTS | if_else

x = 5 

if (x % 2 == 0):
    print("The number is even.")
elif (x % 2 != 0):
    print("The number is odd.")
else:
    print("Invalid input")
    raise Exception ("Invalid input babez")
print("-" * 72)

#-----------------------------------------------------------------------

# FOR LOOPS | loop()()

for i in range(10):
    print(i)
print("-" * 72)

#-----------------------------------------------------------------------

# RANGE FUNCTION | iterate!

# Printing output of range with end arg
range(10)

# Printing output of range with start and end arg
range(5, 10)

# Printing output of range with start, end, and step arg
range(5, 10, 2)

# A bit of a play with negatives
range(-1, -10, -1)

# Since, range is just iterator and not a list
__l = list(range(5))
print(__l)
print("-" * 72)

#-----------------------------------------------------------------------

# BREAK, CONTINUE, AND ELSE CLAUSE FOR LOOP | stop, run, dump me!

# break - use it for getting out of loop

for i in range(10):
    for j in range(10):
        print("*")
        if (j == 5):
            break

# continue - use it to step to next iteration

for i in range(6):
    if(i % 2 == 0):
        print("Even")
        continue
    print("Odd")

# else for loops

for i in range(3):
    print(i)
else:
    print("Use else to do something after the loop ends")
print("-" * 72)

#-----------------------------------------------------------------------

# PASS STATEMENT | Meh

# use it to do nothing!

def pass_example():
    pass
print("-" * 72)

#----------------------------------------------------------------------- 

# FUNCTIONS! | Use me more than once

def function_name(arg):
    print(arg)

function_name("Example function output 1")
f = function_name
f("Function assignment")
print("-" * 72)

#-----------------------------------------------------------------------

# FUNCTION ARGUMENTS - DEFAULTS | arg=X

def func1(a = "find"):
    print(a)

# calling function with default args
func1()

# calling funciton with normal args
func1("search")
print("-" * 72)

# FUNCTION ARGUMENTS - KEYWORDS | arg_arg=X

def func2(a = "find", write = "write_me", more_keywords = "kwkwkwkk"):
    print(a)
    print(write + more_keywords)

# calling with default args
func2()

# calling with non-keyword args
func2(2, 5, 8)

# calling with keyword args
func2(3, write = "love", more_keywords = "no love")

# non-usable cases are used in documentation

# some quirks | *arg, **kw

def func3(x, *arguments, **keywords):
    print("Formatted arg:", x)
    for i in arguments:
        print("Args: ", i)
    for i in keywords:
        print("Keywords:", i)

func3(4, "myass", "yourass", cc = "full ass", dd = "half ass")

print("-" * 72)

# FUNCTION ARGUMENTS - ARBITARY LISTS | *arg

def func4(x, *args):
    print("Formatted:", x)
    print("Following are arguments other than formatted:")
    print(args)

func4(4, "myintheocean", "killmewithkindness", "dbz", 'dbaw')
print("-" * 72)

# FUNCTION ARGUMENTS - UNPACKING FROM LISTS | *d

a = [3, 6]
print(list(range(*a)))

def func5(x, y, z):
    print("Adding x, y, z")

asdf = {1, 3, 5}
func5(*asdf)
print("-" * 72)

#-----------------------------------------------------------------------  

# FUNCTIONS - LAMBDA | small anonymous functions

def increment(n):
    return lambda x: x + n
f = increment(1)
f(4)
print("-" * 72)

#-----------------------------------------------------------------------

# FUNCTIONS - DOCUMENTATION STRINGS | """"""

def func6():
    '''This is document string - Title

    This function does x, y, and z. Use it like this...blah blah
    '''
    pass
print(func6.__doc__)
print("-" * 72)

#----------------------------------------------------------------------- 

# FUNCTIONS - ANNOTATIONS | __ano__

def func7(x: int, y: int = 6):
    """Func7 - adds stuff

    This function adds two numbers passed to it.
    """
    return x + y
func7(4, 5)
func7(4)
print(func7.__annotations__)
print("-" * 72)

# -----End-----of-----Program-----
