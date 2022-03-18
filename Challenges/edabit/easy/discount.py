#!/usr/bin/env python3

"""
Challenge Description

Create a function that takes two arguments: the original price and the discount percentage as 
integers and returns the final price after the discount.
"""

def dis(price, discount):
	discount = discount / 100
	calculatedPrice = price - (price * discount)
	calculatedPrice = round(calculatedPrice,2)
	return calculatedPrice

if __name__ == "__main__":
	print(dis(1500, 50))
	print(dis(89, 20))
	print(dis(100, 75))