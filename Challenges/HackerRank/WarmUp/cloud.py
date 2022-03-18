#!/usr/bin/env python3

"""
Challenge Description

Some clouds you can jump to are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal 
to the number of the current cloud plus 1 or 2. The player must avoid the thunderheads. Determine the minimum number of jumps it will take to 
jump from the starting position to the last cloud. It is always possible to win the game.

Example
c = [0,1,0,0,0,1,0]
Index the array from 0...6. The number on each cloud is its index in the list so the player must avoid the clouds at indices 1 and 5.
They ccould follow these two paths: 0->2->4->6 or 0->2->3->4->6.
"""

def jumpingOnClouds(c):
	"""
	@param int c[n] : an aray of binary integers
	@return int : the minimum number of jumps required
	"""
	hops = 0
	position = 0

	# Soar through the clouds
	while True:
		# Killing condition. If the end has been reached
		# kill the loop
		if (position == len(c)):
			return hops
		
		print(f"Position: {position} ; Total Hops: {hops}")
		# I hate indexing out-of-range. If this is the case
		# just hop once, until getting to the end
		twoHops = position + 2
		if (twoHops > len(c)):
			position += 1
			hops += 1
			continue

		# If there is a 0 two positions away, make the jump
		if (c[twoHops] == 0):
			position += 2
			hops += 1

		# Otherwise, move one position
		else:
			position += 1
			hops += 1



if __name__ == "__main__":
	c = [0,1,0,0,0,1,0]
	print(jumpingOnClouds(c))