#!/usr/bin/env python3

"""
Challenge description

There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine
how many pairs of socks with matching colors there are.

Example
n = 7
ar = [1,2,1,2,1,3,2]

There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color.
The number of pairs is 2

"""

def sockMerchant(n, ar):
	"""
	@param int n : the number of socks in the pile
	@param in ar[n] : the colors of each sock
	@return the number of pairs
	"""
	checkedSocks = []
	numberOfPairs = 0

	# Enumerate over all socks
	for sock in ar:

		# If we have already determined the number
		# of this sock, continue to next sock
		if (sock in checkedSocks):
			continue

		# Determine the number of occurences of this sock
		x = [i for i in ar if i == sock]
		numberOfSpecificSock = len(x)

		# Calculate the number of pairs you can make from
		# this specific sock
		numberOfPairs += int(numberOfSpecificSock / 2)

		# Append the type of sock to checkedSocks
		checkedSocks.append(sock)

	return numberOfPairs

if __name__ == "__main__":
	socks = [10,20,20,10,10,30,50,10,20]

	print(sockMerchant(len(socks),socks))


# paired = [1,4,2,3,5,8]
# numberofPairs = 3
# unpaired = [7,9]