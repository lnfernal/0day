#!/usr/bin/env python3
import time

from collections import deque
import itertools

def without_function_libraries():
	"""
	For-loop which appends the uppercase letter in 's' to the array U.
	"""
	s = 'pendo'
	U = []
	start = time.time()
	for c in s:
		U.append(c.upper())
	end = time.time()
	print(f"\tTime spent in function: {end - start}")

def with_function_libraries():
	"""
	Perform the same actions as 'without_function_libraries' except the builit-in 'map' function is used.
	"""
	s = 'pendo'
	start = time.time()
	U = map(str.upper, s)
	end = time.time()
	print(f"\tTime spent in function: {end - start}")

def avoid_loops_and_list_comprehension():
	"""
	Initilization of list without using loops and list comprensions
	"""
	L1 = [-7, 2, 9, 22, -3, 0]
	L2 = [0] * len(L1)

def using_collections():
	"""
	Illustrates importing list-like container with fast appends and pops on
	either end.
	"""
	s = 'pendo'
	# Make a new deque
	d = deque(s)

	# add a new entry to the right side
	d.append('y')

	# add a new entry to the left side
	d.appendleft('h')

	d.pop() # return and remove the rightmost item

	d.popleft() # return and remove the leftmost item

	# print list deque in reverse
	#print(list(reversed(d)))

def using_itertools():
	"""
	Another built-in python library for permutations
	"""
	L = [1,2,3]
	iter = itertools.permutations(L)
	#print(list(iter))

def key_sort():
	L = [1, -3, 6, 11, 5]
	L.sort()
	#print(L)

	s = 'pendo'
	# use sorted() if you don't want to sort in place
	s = sorted(s)
	#print(s)

def string_concatenation_n_squared():
	"""
	Slow way of performing string concatenation
	"""
	s = 'hellogeeks'
	slist = ''
	start = time.time()
	for i in s:
		slist = slist + i
	end = time.time()
	print(f"\tTime spent in function: {end - start}")

def string_conatenation_n():
	"""
	Fast way of performing string concatenation
	"""
	st = 'hellogeeks'
	start = time.time()
	slist = ''.join([i for i in st])
	end = time.time()
	print(f"\tTime spent in function: {end - start}")

def slow_range_iteration():
	"""
	Slow way to iterate a range
	"""
	i = 0
	evens = []
	start = time.time()
	while i < 10:
		if i % 2 == 0:
			evens.append(i)
		i += 1
	end = time.time()
	print(f"\tTime spent in function: {end - start}")

def fast_range_iteration():
	"""
	Fast way to iterate range
	"""
	start = time.time()
	evens = [i for i in range(10) if i % 2 == 0 ]
	end = time.time()
	print(f"\tTime spent in function: {end - start}")

"""
Builtin functions like map() are implemented in C code. So the interpreter doesn't have to execute the loop, this gives 
a speedup. The map() funciton applies a function to every member of iterable and returns the result.

Avoid for-loops and list comprehensions where possible
"""
print("Without Function Libraries")
without_function_libraries()
print("With Function Libraries")
with_function_libraries()

"""
If you were to crate an array with just one initialization value, instead of using inefficient for-loops and list comprehension, you could
perform the following:
"""
avoid_loops_and_list_comprehension()

"""
If we are doing string operations, consider using an existing module 'collections'
"""
using_collections()
using_itertools()

# Use keys for sorts. In Python, we should use the key argument to the builkt-in sort instead, which is faster way to sort
key_sort()

"""
Optimizing loops. Write idiomatic code. This may sound counter-intuitive but writing idiomatic code will make your code faster in most
cases. This is because Python was designed to have only one obvious / correct way to do a task. 
"""
print("")
# Slow O(n^2) - for string concatentation
print("Slow string concatenation - O(n^2)")
string_concatenation_n_squared()
print("Fast string concatenation - O(n)")
string_conatenation_n()
print("")
print("Slow way to iterate a range")
slow_range_iteration()
print("Fast way to iterate a rangee")
fast_range_iteration()


"""
Always use built-in functions. These are written in C which is much faster than python. Functions such as sum(), map(), reduce(), max(), etc. rather than
carrying out those computations yourself. Its also less code to write. 
"""
print("")
# set consisting of all absolute values
print("Using map to create all absolute values")
abs_set = [1,-78,23,56,-45,-12,-87,22,36,45,-45]

start = time.time()
s = map(abs, abs_set)
end = time.time()
print(f"\tTotal time: {end - start}")

print("Not using map to create all absolute values")
s2 = []
start = time.time()
for number in abs_set:
	s2.append(abs(number))
end = time.time()
print(f"\tTotal time: {end - start}")

"""
If you're working with textual data, for string concatentation, instead of +=
"""
# Slow way of performing string concatenation
print("")
print("Slow way to concatenate")
sentence_list = ['This ','is ','a ','sentence']
sentence = ''
start = time.time()
for i in sentence_list:
	sentence += i
end = time.time()
print(f"\tTotal time: {end - start}")

print("Fast way to perform string concatenation")
start = time.time()
sentence = ''.join(sentence_list)
end = time.time()
print(f"\tTotal time: {end - start}")

# Instead of using
head = "<head></head>"
body = "<body></body>"
out = "<html>" + head + body + "</html>"

# Use
out = "<html>%s%s</html>" % (head, body)
