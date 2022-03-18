#!/usr/bin/env python3

"""
Challenge Description

People want to determine the most expensive computer keyboard and USB drive that can be purchased with a given budget. Give price lists for keyboards and USB drives and a budget
find the cost to buy them. If it is not possible to buy both items, return -1

Example
b = 60
keyboards = [40,50,60]
drives = [5,8,12]

The person can buy a 40 keyboard + 12 USB drive = 52 or a 50 keyboard + 8 USB drive = 58. 
Choose the latter as the more expensive option and return 58.
"""

def getMoneySpent(keyboards, drives, budget):
	"""
	Determines the most expensive purchasing option given a
	list of keyboards and USB drives
	@param int keyboards[n] : List of prices for keyboards
	@param int drives[m] : List of prices for USB drives
	@param int budget : Total amount of money one can spend
	@return int : Returns cost of most expensive purchase. If no purchase can be made
				  return -1
	"""
	mostExpensive = 0

	# Brute force method
	for keyboard in keyboards:
		for drive in drives:
			# Calculate the total cost of every keyboard with every drive
			totalCost = keyboard + drive

			# If the total cost does not exceed the budget and is greater than
			# the most expensive option
			if (totalCost <= budget and totalCost > mostExpensive):
				mostExpensive = totalCost

	if (totalCost == 0):
		return -1

	return mostExpensive


if __name__ == "__main__":
	keyboards = [40,50,60]
	drives = [5,8,12]
	budget = 60
	print(getMoneySpent(keyboards, drives, budget))