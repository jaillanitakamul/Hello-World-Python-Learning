'''
In Python, a list is a built-in dynamic sized array (automatically grows and shrinks). 
We can store all types of items (including another list) in a list. 
A list may contain mixed type of items, this is possible because a list mainly stores references at contiguous locations 
and actual items maybe stored at different locations.

List can contain duplicate items.
List in Python are Mutable. Hence, we can modify, replace or delete the items.
List are ordered. It maintain the order of elements based on how they are added.
Accessing items in List can be done directly using their position (index), starting from 0.

'''

import os 
os.system('cls')

friendsList =["Enayatullah","Samim","Farid","Sherzad"]
print(friendsList)

print (friendsList[1])

friendsList[1]="Samsor Sir Jee"
print(friendsList)

varList = [1,2,3.0,"Jaillani","Prince Willam", True]
print(varList)

print(type(varList[0]))
print(type(varList[1]))
print(type(varList[2]))
print(type(varList[3]))
print(type(varList[4]))
print(type(varList[5]))

# Using list() Constructor
aList = list((1,2,3.0,"Jaillani",True))
print(aList)

bList = (1,2,3.0,"Jaillani", True)
print(bList)

print(type(aList))
print(type(bList))

# Creating List with Repeated Elements
a=[2]*10
print(a)

b=["-"]*5
print(b)

# Accessing List Elements
aData = [10,20,30,40,50,60,70,80,90,100]
print(aData[0])
print(type(aData))

print(aData[len(aData)-1])
print(aData[-2])






