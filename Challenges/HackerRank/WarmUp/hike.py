#!/usr/bin/env python3

"""
Challenge Description

During the last hike that took exactly 'steps' steps, for every step it was noted if it was an uphill U, or a downhill, D.
Hikes always start and end at sea level. Each step represents a 1 unit of change in altitude.
- A mountain is a sequence of steps above sea level, starting with a step up from sea level and ending with a step down to sea level
- A valley is a sequence of steps below sea level, starting with a step down from sea level and ending with a step up to sea level
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through

Example
steps = 8 path = [DDUUUUDD]
The hiker first enters a valley 2 units deep. Then they climb out and up ounto a mountain 2 units high. Finally, the hiker 
returns to sea level and ends the hike.
"""

def countingValleys(steps, path):
	"""
	@param int steps : the number of steps on the hike
	@param string path: a string describing the path
	@return int numberOfValleys the number of valleys traversed
	"""

	# Initially start off at sea level
	elevation = 0
	numberOfValleys = 0
	path = list(path)

	# Start walkin'
	for step in path:

		# Take a step downward
		if (step == 'D'):
			
			# If at sea level and taking a step downward,
			# you've entered a valley. Increment valley
			if (elevation == 0): numberOfValleys += 1

			# Decrease elevation 
			elevation -= 1
		
		# Take step upwards
		elif (step == 'U'): elevation += 1

	return numberOfValleys

if __name__ == "__main__":
	path = 'UDDDUDUU'
	print(countingValleys(len(path), path))