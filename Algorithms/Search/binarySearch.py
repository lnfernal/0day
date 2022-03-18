#!/usr/bin/env python3

def binarySearch(dataSet, targetValue):
    minimum = 0
    maximum = len(dataSet) - 1

    while maximum > minimum:
        guess = maximum + minimum) // 2

        if (dataSet[guess] == targetValue):
            return guess
        elif (dataSet[guess] < targetValue):
            minimum = guess + 1
        elif (dataSet[guess] > targetValue):
            maximum = guess - 1

    return -1

if __name__ == "__main__":
    primes = [3,5,7,11,13,17,19,23,27,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    usrInput = int(input("What number are you looking for: "))
    
    index = binarySearch(primes, usrInput)

    if (index == -1):
        print("Could not find specified number")
    else:
        print(f"Specified number found at index: {index}")
