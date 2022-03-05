#!/usr/bin/env python3

import time
from functools import reduce

# The goal here is to return just an iterable and not a string of my name. 
# I following this -> https://stackabuse.com/map-filter-and-reduce-in-python-with-examples/

# My name in decimal
decimal_name = [109,97,120,105,109,105,108,108,105,97,110]

"""
Below are all of my attemps at optimizing code
"""
# First generation uses basic for-loops
s = []
print("First Generation:")
string_name = ''
start = time.time()
for d in decimal_name:
	s.append(chr(d))
end = time.time()
print(f"\tFirst generation time: {end - start}")

# Second generation uses list comprehenions
print("Second Generation:")
string_name = ''
start = time.time()
string_name = "".join([chr(d) for d in decimal_name])
end = time.time()
print(f"\tSecond generation time: {end - start}")

# Third generation uses convinience functions
print("Third Generation:")
string_name = ''
start = time.time()
string_name = "".join(map(chr,decimal_name))
end = time.time()
print(f"\tThird generation time: {end - start}")

# Fourth generation using convinience functions with for-loop
print("Fourth Generation")
string_name = ''
start = time.time()
for c in map(chr, decimal_name):
	string_name = string_name + c
end = time.time()
print(f"\tFourth generation time: {end - start}")


"""
Below is how the article performed this task. Put a quick lesson on anonymous functions
"""
# The article uses "anonymous functions" or "lambda functions" which are functions that are not initialized in the regular manner.
# lambda funcitons syntax is:
#	lambda arguments: expression
# 
# Think of lambdas as one-line methods without a name (hence "anonymous")
# For example, the typical function:
# def add(x,y):
# 	return x + y
# 
# Can be used as
# lambda x, y: x + y
#
# So  what makes lambda relevant to map(), filter(), and reduce()?
# All three of these methods expect a function object as the first argument. This function object can be a pre-defined method with a name.
# Though, more often than not, functions passed to map(), filter(), and reduce() are the ones you'd use only once, so theres' often no point in defining a
# referenceable function
#
# The map() Fuction
# The man function iterates thorugh all items in the gien iterable and executes the function we passwed as na argument on each of them.
# map(function, iterable(s))
#
# The filter() Function
# As the name suggests, filter() forms anew list that contains only elements that satisfy a certain condition, i.e. the function we passwd returns True
# 	evens = list(filter(lambda x: x % 2 == 0, decimal_name))
# 	print(evens)
