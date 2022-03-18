#!/usr/bin/env python3

class Dog:
	# Class attributes. These values are the same for all class instances
	species = "Canis familiaris"

	def __init__(self, name, age): # This means the initial state of the "Dog" instance
		# These are instance attributes. Specify to a particular instance of the class. All "Dog" objects
		# have a name and an age, but the values for the 'name' and 'age' attributes will vary depending on 
		# the "Dog" instance
		self.name = name
		self.age = age

	# This is a dunder method. 
	def __str__(self): #
		return f"{self.name} is {self.age} years old"

	# Instance method. Defined inside a class and can only be called from an 
	# instance of that class. Just like .__init__(), an instance method's first parameter
	# is always self
	def speak(self,sound):
		return f"{self.name} barks: {sound}"

## These are child classes which inherit the parent class "Dog"
class JackRussellTerrier(Dog):
	def speak(self, sound="Arf"): # Remember that child functions can overwrite parent functions
		return f"{self.name} says {sound}"

class Dachshund(Dog):
	pass

class Bulldog(Dog):
	pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(miles.speak())
print(miles.speak("Grrr")) # You can still use parent classes when needed

print(jim.speak("Woof"))

# All objects created from a child class are instances of the parent class, although they
# may not be instances of other child classes
print(isinstance(miles,Dog))
print(isinstance(miles,Bulldog))
print(isinstance(jack,Dachshund))