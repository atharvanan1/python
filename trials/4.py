#!/usr/bin/env python3

# This file comprises of all the code regarding Data Structure module in Python documentation.

# LIST METHODS | ...

a = [1, 2, 3, 4, 5]
print(a)
print("-"*40)

# list append
print("List appends.")
a.append(6)
print(a)
print("-"*40)

# list extend
b = ['my', 'name', 'is', 'x']
print(b)
print("Extending the list")
a.extend(b)
print(a)
print("-"*40)

# list insert
print("Inserting things")
a.insert(5, 'insert')
a.insert(0, 'insert')
a.insert(len(a), 'insert')
print(a)
del b
print("-"*40)

# list remove
print("Removing things")
print(a)
a.remove(5)
print(a)
print("-"*40)

# list pop
print("poping stuff")
a.pop()
a.pop(5)
print(a)
print("-"*40)

# list clear
b = [1, 2, 3, 4, 5]
print(b)
print("Clearing list")
b.clear()
print(b)
print("-"*40)

# list index
b = [1, 2, 3, 4, 5, 6]
print(b)
print("Index searching")
print(b.index(3))
print(b.index(3, 1, 4))
print("-"*40)

# list count
print("Counting things")
print(a.count(2))
print(b.count(3))
print("-"*40)

# list sort
b.sort()
print("Sorting lists")
print(b)
print("-"*40)

# list reverse
a.reverse()
print("Reversing list")
print(a)
print("-"*40)

# list copy
c = a.copy()
print("Shadow copy of list")
print(c)

# LISTS AS STACK | pop, push

# LISTS AS QUEUES | add, remove

# LIST COMPREHENSION | This is long and complicated and useful

# Nested List Comprehension | more and more comprehension

# DEL STATEMENT | del del

# TUPLES AND SEQUENCES | I am immutable!

# SETS | I am mathematical, a little!

# DICTIONARIES | We come in couples

# LOOPING TECHNIQUES | loop()()

# CONDITIONS | if...else

# COMPARING SEQUENCES | I am bigger!
