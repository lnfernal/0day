#!/usr/bin/env python3

"""
Challenge Description

Two cats and a mouse are at various positions on a line. You will be given their
starting positions. Your task to to determine which cat will reach the mouse first, assuming
the mouse does not move and the cats travel at equal speed. If the cats arrive at the same 
time, the mouse will be allowed to move and it will escape wihle they fight.
- If can A catches the mouse first, print Cat A
- If cat B catches the mouse first, print Cat B
- If both cats reach the mouse at the same time, print Mouse C as the two cats fight and mouse escapes

Example
x = 2
y = 5
z = 4
The cats are at positions 2 (Cat A) and 5 (Cat B), and the mouse is at position 4. Cat B, at position 5 will arrive first
since it is only 1 unit away while the other is 2 units away. Return 'Cat B'
"""

def catAndMouse(x, y, z):
	"""
	@param int x: Cat A's position
	@param int y: Cat B's position
	@param int z: Mouse's C's position
	@return string: Either 'Cat A', 'Cat B', 'Mouse C'
	"""
	animal = ''

	# Killing cases
	if  (x == z and y == z):
		return 'Mouse C'
	elif (x == z):
		return 'Cat A'
	elif (y == z):
		return 'Cat B'

	if (x < z and y < z):
		animal = catAndMouse(x + 1, y + 1, z)
	elif (x > z and y > z):
		animal = catAndMouse(x - 1, y - 1, z)
	elif ((x < z) and (y > z)):
		animal = catAndMouse(x + 1, y - 1, z)
	elif ((x > z) and (y < z)):
		animal = catAndMouse(x - 1, y + 1, z)

	return animal

if __name__ == "__main__":
	x = 2
	y = 5
	z = 4
	print(catAndMouse(x, y, z))