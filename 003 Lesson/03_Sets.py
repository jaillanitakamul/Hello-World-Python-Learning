'''
C. Set
Definition: A set in Python is an unordered collection of unique elements.
Created using { } or set() function.

Key Properties:
Unordered  does not maintain order.
Mutable  can add or remove elements.
No duplicates allowed.
Supports set operations (union, intersection, difference).
'''

import os 
os.system('cls')

fruitName = {"apple","orange","cherry"}
print(fruitName)

numList = [1,2,3,4]
numSet = set(numList)
print(numSet)
print(type(numSet))

#Empty
empty_Set = {} 
empty_Set2 = set()

print(empty_Set)
print(empty_Set2)

numberSet={1,2,3,4,5,6,7,8,9}
print(numberSet)